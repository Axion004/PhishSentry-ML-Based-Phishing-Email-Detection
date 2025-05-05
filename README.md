# PhishSentry-ML-Based-Phishing-Email-Detection
PhishSentry is an ML-powered phishing email detection tool using TF-IDF and Random Forest. It analyzes email text to classify messages as phishing or legitimate with high accuracy. Ideal for building email security solutions with reliable, text-based threat detection.
## 🚀 Features

- Detects phishing emails based on textual content
- Uses TF-IDF vectorization for feature extraction
- Trained with Random Forest classifier for high accuracy
- Saves the model and vectorizer for future inference

## 🔧 Technologies Used

- Python
- Pandas
- Scikit-learn
- Joblib
- TF-IDF (via `TfidfVectorizer`)
- Random Forest Classifier

## 📁 Project Structure

├── phishing_detector.py # Main training script
├── your_dataset.csv # CSV file with email text and labels
├── phishing_model.pkl # Trained model
├── vectorizer.pkl # Saved TF-IDF vectorizer
├── requirements.txt
└── README.md

## 📊 Model Performance

Model is evaluated using accuracy score and classification report metrics such as precision, recall, and F1-score.

## 📦 Installation

```bash
pip install -r requirements.txt `requirements.txt`

pandas
scikit-learn
joblib
