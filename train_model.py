import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
print("Loading dataset...")
df = pd.read_csv("your_dataset.csv")  # Update with actual dataset filename
print("Dataset loaded successfully!")

# Check dataset structure
print("Dataset Columns:", df.columns)
print("Label Distribution:\n", df['label'].value_counts())

# Use 'text_combined' or the correct column containing email text
if 'text_combined' in df.columns:
    X = df['text_combined']
else:
    raise ValueError("Error: 'text_combined' column not found!")

y = df['label']  # Ensure label column is correct

# Split data into training & testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data to numerical features
vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_transformed = vectorizer.fit_transform(X_train)
X_test_transformed = vectorizer.transform(X_test)

# Train model
print("Training model...")
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_transformed, y_train)
print("Model training complete!")

# Save model and vectorizer
joblib.dump(model, "phishing_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")
print("Model & vectorizer saved!")

# Evaluate model performance
y_pred = model.predict(X_test_transformed)

accuracy = accuracy_score(y_test, y_pred)
print("\n✅ Model Accuracy:", accuracy)

# Print detailed performance metrics
print("\n📊 Classification Report:\n", classification_report(y_test, y_pred))
