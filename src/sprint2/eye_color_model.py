"""
Sprint 2: Eye Color ML Model
User Stories: US-05, US-06, US-07, US-08, US-09
Story Points: 14
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle
import os

class EyeColorModel:
    """US-05: Train Random Forest classifier for eye color"""
    
    def __init__(self, n_estimators=100, random_state=42):
        self.model = RandomForestClassifier(n_estimators=n_estimators, random_state=random_state)
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
    
    def split_data(self, X, y, test_size=0.2, random_state=42):
        """US-06: Split data into train/test sets"""
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X, y, test_size=test_size, random_state=random_state
        )
        return self.X_train, self.X_test, self.y_train, self.y_test
    
    def train(self, X=None, y=None):
        """Train the model"""
        if X is not None and y is not None:
            self.split_data(X, y)
        
        self.model.fit(self.X_train, self.y_train)
        train_acc = self.model.score(self.X_train, self.y_train)
        print(f"Training accuracy: {train_acc:.2%}")
        return self.model
    
    def evaluate(self):
        """US-07: Evaluate model with accuracy metrics"""
        if self.X_test is None or self.y_test is None:
            raise ValueError("No test data available. Run split_data() first.")
        
        predictions = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, predictions)
        
        print(f"\n{'='*50}")
        print(f"Eye Color Model Evaluation")
        print(f"{'='*50}")
        print(f"Test Accuracy: {accuracy:.2%}\n")
        
        print("Confusion Matrix:")
        print(confusion_matrix(self.y_test, predictions))
        print("\nClassification Report:")
        print(classification_report(self.y_test, predictions))
        
        return accuracy
    
    def save_model(self, filepath):
        """US-08: Save trained model to disk"""
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'wb') as f:
            pickle.dump(self.model, f)
        print(f"Model saved to {filepath}")
    
    @staticmethod
    def load_model(filepath):
        """Load saved model"""
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    
    def predict(self, snp_data):
        """US-09: Make predictions on new SNP data"""
        if isinstance(snp_data, dict):
            # Convert dict to feature array
            snp_data = [list(snp_data.values())]
        
        prediction = self.model.predict(snp_data)[0]
        probabilities = self.model.predict_proba(snp_data)[0]
        confidence = max(probabilities)
        
        # Get class probabilities
        classes = self.model.classes_
        prob_dict = {classes[i]: probabilities[i] for i in range(len(classes))}
        
        return {
            'prediction': prediction,
            'confidence': confidence,
            'probabilities': prob_dict
        }

class EyeColorPredictor:
    """High-level interface for eye color prediction"""
    
    EYE_COLOR_SNPS = ['rs12913832', 'rs1800407', 'rs12896399', 
                      'rs16891982', 'rs1393350', 'rs12203592']
    
    def __init__(self, model_path=None):
        if model_path and os.path.exists(model_path):
            self.model = EyeColorModel.load_model(model_path)
        else:
            self.model = None
    
    @staticmethod
    def encode_genotype(genotype):
        """Convert genotype to numeric"""
        encoding = {
            'AA': 0, 'AG': 1, 'GG': 2,
            'AC': 1, 'CC': 2, 'AT': 1, 
            'TT': 2, 'CT': 1, 'GT': 1
        }
        return encoding.get(genotype.upper(), 0)
    
    def predict_from_snps(self, snp_dict):
        """Predict eye color from SNP dictionary"""
        if self.model is None:
            raise ValueError("No model loaded. Train or load a model first.")
        
        # Extract features in correct order
        features = [self.encode_genotype(snp_dict.get(snp, 'AA')) 
                   for snp in self.EYE_COLOR_SNPS]
        
        prediction = self.model.predict([features])[0]
        probabilities = self.model.predict_proba([features])[0]
        confidence = max(probabilities)
        
        return {
            'eye_color': prediction,
            'confidence': confidence,
            'confidence_level': self._get_confidence_level(confidence)
        }
    
    @staticmethod
    def _get_confidence_level(confidence):
        """Convert confidence to level"""
        if confidence > 0.8:
            return 'High'
        elif confidence > 0.6:
            return 'Medium'
        else:
            return 'Low'

# Example usage
if __name__ == "__main__":
    # Load training data
    from sprint1.data_pipeline import TrainingDataCreator
    
    creator = TrainingDataCreator()
    snp_df = pd.read_csv('../data/eye_color_training.csv')
    labels_df = pd.read_csv('../data/eye_color_labels.csv')
    
    X, y = creator.prepare_eye_color_features(snp_df, labels_df)
    
    # US-05 & US-06: Train model with train/test split
    model = EyeColorModel()
    model.train(X, y)
    
    # US-07: Evaluate
    accuracy = model.evaluate()
    
    # US-08: Save model
    model.save_model('../models/eye_color_model.pkl')
    
    # US-09: Make prediction
    test_snps = {
        'rs12913832': 'AG',
        'rs1800407': 'GG',
        'rs12896399': 'GG',
        'rs16891982': 'GG',
        'rs1393350': 'AA',
        'rs12203592': 'GG'
    }
    
    predictor = EyeColorPredictor('../models/eye_color_model.pkl')
    result = predictor.predict_from_snps(test_snps)
    print(f"\nPrediction: {result['eye_color']}")
    print(f"Confidence: {result['confidence']:.1%} ({result['confidence_level']})")
