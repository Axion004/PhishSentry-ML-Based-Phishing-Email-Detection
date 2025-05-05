from flask import Flask, request, render_template, jsonify
import joblib
import requests
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask(__name__)
limiter = Limiter(get_remote_address, app=app, default_limits=["5 per minute"])

# Load Model & Vectorizer
model = joblib.load("phishing_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

API_KEYS = {"your_api_key_here"}  # Replace with actual API key

# PhishTank URL Check
def check_phishtank(url):
    API_KEY = "your_api_key_here"
    response = requests.post("https://phishtank.com/check/", data={"format": "json", "url": url, "app_key": API_KEY})
    result = response.json()
    return result.get("in_database", False)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    phishtank_result = None
    
    if request.method == "POST":
        email_text = request.form["email_text"]
        email_vector = vectorizer.transform([email_text])
        prediction = model.predict(email_vector)[0]
        result = "🚨 Phishing Email" if prediction == 1 else "✅ Legit Email"

        # Check URLs in PhishTank
        for word in email_text.split():
            if word.startswith("http") and check_phishtank(word):
                phishtank_result = f"⚠️ Phishing URL detected: {word}"
                break

    return render_template("index.html", result=result, phishtank_result=phishtank_result)

@app.route("/api/scan", methods=["POST"])
@limiter.limit("5 per minute")
def scan_email():
    data = request.get_json()
    api_key = request.headers.get("X-API-Key")
    if api_key not in API_KEYS:
        return jsonify({"error": "Unauthorized"}), 401

    email_text = data.get("email_text", "")
    email_vector = vectorizer.transform([email_text])
    prediction = model.predict(email_vector)[0]
    result = "Phishing Email" if prediction == 1 else "Legit Email"

    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
