import os
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


def training_model():
    
    database_path = os.path.join('data', 'phishing_urls.csv')
    
    if not os.path.exists(database_path):
        print(f"Error: please place your dataset at {database_path} before running")
        
        return 
    print("Loading dataset..")
    df = pd.read_csv(database_path)
    
    
     X = df['url']
    y = df['label']

    #  Splits data into Training (80%) of the model and Testing (20%) of the model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Vectorizing text URLs into numerical data...")
    # TfidfVectorizer breaks URLs down into pieces (tokens) to find malicious patterns
    
    vectorizer = TfidfVectorizer(tokenizer=lambda x: x.split('/'))
    X_train_vectorized = vectorizer.fit_transform(X_train)
    X_test_vectorized = vectorizer.transform(X_test)

    print("Training the AI model (Logistic Regression)...")
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_vectorized, y_train)

    # Evaluate the model performance
    predictions = model.predict(X_test_vectorized)
    accuracy = accuracy_score(y_test, predictions)
    print(f"Training complete! Model Accuracy: {accuracy * 100:.2f}%")
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

    #Save the trained model and the vectorizer to disk
    print("Saving AI assets to disk...")
    with open('phishing_model.pkl', 'wb') as model_file:
        pickle.dump(model, model_file)
        
    with open('vectorizer.pkl', 'wb') as vec_file:
        pickle.dump(vectorizer, vec_file)
        
    print("Done! 'phishing_model.pkl' and 'vectorizer.pkl' are ready for your Flask app.")

if __name__ == "__main__":
    train_phishing_model()
