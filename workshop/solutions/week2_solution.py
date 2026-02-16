"""
Week 2 Solution: Eye Color ML Model
Complete working code
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import pickle

EYE_COLOR_SNPS = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']

def encode_genotype(genotype):
    """Convert genotype to numeric"""
    encoding = {'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2, 'AT': 1, 'TT': 2}
    return encoding.get(genotype, -1)

def prepare_eye_color_data(snp_df, labels_df):
    """Convert SNP data to ML features"""
    features = []
    labels = []
    
    for idx, row in labels_df.iterrows():
        sample_snps = snp_df[snp_df['sample_id'] == row['sample_id']]
        feature_vector = []
        
        for snp in EYE_COLOR_SNPS:
            snp_row = sample_snps[sample_snps['rsid'] == snp]
            if not snp_row.empty:
                feature_vector.append(encode_genotype(snp_row.iloc[0]['genotype']))
            else:
                feature_vector.append(-1)
        
        features.append(feature_vector)
        labels.append(row['eye_color'])
    
    return np.array(features), np.array(labels)

def train_eye_color_model(X, y):
    """Train Random Forest classifier"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    train_acc = model.score(X_train, y_train)
    print(f"Training accuracy: {train_acc:.2%}")
    
    return model, X_test, y_test

def evaluate_model(model, X_test, y_test):
    """Calculate accuracy and show confusion matrix"""
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    print(f"\nTest Accuracy: {accuracy:.2%}")
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, predictions))
    print("\nClassification Report:")
    print(classification_report(y_test, predictions))

def save_model(model, filepath):
    """Save trained model to disk"""
    with open(filepath, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {filepath}")

def load_model(filepath):
    """Load saved model"""
    with open(filepath, 'rb') as f:
        return pickle.load(f)

def predict_eye_color(model, snp_data):
    """Predict eye color from SNPs"""
    feature_vector = [encode_genotype(snp_data.get(snp, 'AA')) for snp in EYE_COLOR_SNPS]
    prediction = model.predict([feature_vector])[0]
    probabilities = model.predict_proba([feature_vector])[0]
    confidence = max(probabilities)
    
    return prediction, confidence

if __name__ == "__main__":
    snp_df = pd.read_csv('../data/eye_color_training.csv')
    labels_df = pd.read_csv('../data/eye_color_labels.csv')
    
    X, y = prepare_eye_color_data(snp_df, labels_df)
    model, X_test, y_test = train_eye_color_model(X, y)
    evaluate_model(model, X_test, y_test)
    
    save_model(model, '../models/eye_color_model.pkl')
    
    test_snps = {
        'rs12913832': 'AG',
        'rs1800407': 'GG',
        'rs12896399': 'GG',
        'rs16891982': 'GG',
        'rs1393350': 'AA',
        'rs12203592': 'GG'
    }
    prediction, confidence = predict_eye_color(model, test_snps)
    print(f"\nPredicted eye color: {prediction} (confidence: {confidence:.2%})")
