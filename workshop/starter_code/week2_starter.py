"""
Week 2 Starter Code: Eye Color ML Model
Students will complete the TODO sections
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
import pickle

# Key SNPs for eye color prediction
EYE_COLOR_SNPS = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']

def prepare_eye_color_data(snp_df, labels_df):
    """
    Convert SNP data to ML features
    
    Args:
        snp_df: DataFrame with SNP data
        labels_df: DataFrame with 'sample_id' and 'eye_color' columns
    
    Returns:
        X: Feature matrix (samples x SNPs)
        y: Labels (eye colors)
    """
    # TODO: Extract only the key SNPs
    # TODO: Convert genotypes to numeric (AA=0, AG=1, GG=2)
    # TODO: Merge with labels
    # Hint: Use pd.get_dummies() or manual encoding
    pass

def train_eye_color_model(X, y):
    """
    Train Random Forest classifier
    
    Args:
        X: Features
        y: Labels
    
    Returns:
        model: Trained classifier
        X_test: Test features
        y_test: Test labels
    """
    # TODO: Split data 80/20
    # Hint: train_test_split(X, y, test_size=0.2, random_state=42)
    
    # TODO: Create RandomForestClassifier
    # Hint: RandomForestClassifier(n_estimators=100, random_state=42)
    
    # TODO: Train model with .fit()
    
    # TODO: Return model and test data
    pass

def evaluate_model(model, X_test, y_test):
    """
    Calculate accuracy and show confusion matrix
    
    Args:
        model: Trained classifier
        X_test: Test features
        y_test: True labels
    """
    # TODO: Make predictions
    # Hint: model.predict(X_test)
    
    # TODO: Calculate accuracy
    # Hint: accuracy_score(y_test, predictions)
    
    # TODO: Print confusion matrix
    # Hint: confusion_matrix(y_test, predictions)
    pass

def save_model(model, filepath):
    """
    Save trained model to disk
    
    Args:
        model: Trained classifier
        filepath: Where to save
    """
    # TODO: Use pickle.dump()
    pass

def load_model(filepath):
    """
    Load saved model
    
    Args:
        filepath: Model file path
    
    Returns:
        Loaded model
    """
    # TODO: Use pickle.load()
    pass

def predict_eye_color(model, snp_data):
    """
    Predict eye color from SNPs
    
    Args:
        model: Trained classifier
        snp_data: Dictionary of SNP values
    
    Returns:
        prediction: Eye color
        confidence: Probability
    """
    # TODO: Convert snp_data to feature array
    # TODO: Get prediction and probability
    # Hint: model.predict_proba()
    pass

# Test your functions
if __name__ == "__main__":
    # Load training data
    snp_df = pd.read_csv('../data/eye_color_training.csv')
    labels_df = pd.read_csv('../data/eye_color_labels.csv')
    
    # Prepare data
    X, y = prepare_eye_color_data(snp_df, labels_df)
    
    # Train model
    model, X_test, y_test = train_eye_color_model(X, y)
    
    # Evaluate
    evaluate_model(model, X_test, y_test)
    
    # Save
    save_model(model, '../models/eye_color_model.pkl')
    
    # Test prediction
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
