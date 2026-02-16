"""
Sprint 3: Multi-Trait Models
User Stories: US-10, US-11, US-12, US-13
Story Points: 15
"""

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import matplotlib.pyplot as plt

class HairColorModel:
    """US-10: Train hair color classifier"""
    
    HAIR_COLOR_SNPS = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    @staticmethod
    def encode_genotype(genotype):
        """Convert genotype to numeric"""
        encoding = {
            'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2,
            'AT': 1, 'TT': 2, 'CT': 1, 'GT': 1
        }
        return encoding.get(genotype.upper(), 0)
    
    def prepare_features(self, snp_df, labels_df):
        """Extract hair color features"""
        features = []
        labels = []
        
        for idx, row in labels_df.iterrows():
            sample_snps = snp_df[snp_df['sample_id'] == row['sample_id']]
            feature_vector = []
            
            for snp in self.HAIR_COLOR_SNPS:
                snp_row = sample_snps[sample_snps['rsid'] == snp]
                if not snp_row.empty:
                    feature_vector.append(self.encode_genotype(snp_row.iloc[0]['genotype']))
                else:
                    feature_vector.append(-1)
            
            features.append(feature_vector)
            labels.append(row['hair_color'])
        
        return np.array(features), np.array(labels)
    
    def train(self, X, y):
        """Train hair color model"""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        
        train_acc = self.model.score(X_train, y_train)
        test_acc = self.model.score(X_test, y_test)
        
        print(f"Hair Color Model - Train: {train_acc:.2%}, Test: {test_acc:.2%}")
        return self.model
    
    def predict(self, snp_dict):
        """Predict hair color"""
        features = [self.encode_genotype(snp_dict.get(snp, 'AA')) for snp in self.HAIR_COLOR_SNPS]
        prediction = self.model.predict([features])[0]
        probabilities = self.model.predict_proba([features])[0]
        confidence = max(probabilities)
        
        return {
            'hair_color': prediction,
            'confidence': confidence
        }

class AncestryModel:
    """US-11: Train ancestry predictor"""
    
    ANCESTRY_SNPS = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832']
    
    def __init__(self):
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    @staticmethod
    def encode_genotype(genotype):
        """Convert genotype to numeric"""
        encoding = {
            'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2,
            'AT': 1, 'TT': 2, 'CT': 1, 'GT': 1
        }
        return encoding.get(genotype.upper(), 0)
    
    def prepare_features(self, snp_df, labels_df):
        """Extract ancestry features"""
        features = []
        labels = []
        
        for idx, row in labels_df.iterrows():
            sample_snps = snp_df[snp_df['sample_id'] == row['sample_id']]
            feature_vector = []
            
            for snp in self.ANCESTRY_SNPS:
                snp_row = sample_snps[sample_snps['rsid'] == snp]
                if not snp_row.empty:
                    feature_vector.append(self.encode_genotype(snp_row.iloc[0]['genotype']))
                else:
                    feature_vector.append(-1)
            
            features.append(feature_vector)
            labels.append(row['ancestry'])
        
        return np.array(features), np.array(labels)
    
    def train(self, X, y):
        """Train ancestry model"""
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        
        train_acc = self.model.score(X_train, y_train)
        test_acc = self.model.score(X_test, y_test)
        
        print(f"Ancestry Model - Train: {train_acc:.2%}, Test: {test_acc:.2%}")
        return self.model
    
    def predict(self, snp_dict):
        """Predict ancestry with probabilities"""
        features = [self.encode_genotype(snp_dict.get(snp, 'AA')) for snp in self.ANCESTRY_SNPS]
        probabilities = self.model.predict_proba([features])[0]
        classes = self.model.classes_
        
        ancestry_probs = {classes[i]: probabilities[i] for i in range(len(classes))}
        
        return ancestry_probs

class UnifiedPipeline:
    """US-12: Unified prediction pipeline for all traits"""
    
    def __init__(self, eye_model_path=None, hair_model_path=None, ancestry_model_path=None):
        self.eye_model = self._load_model(eye_model_path) if eye_model_path else None
        self.hair_model = self._load_model(hair_model_path) if hair_model_path else None
        self.ancestry_model = self._load_model(ancestry_model_path) if ancestry_model_path else None
    
    @staticmethod
    def _load_model(filepath):
        """Load pickled model"""
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    
    def predict_all_traits(self, snp_data):
        """US-12: Run all models on single dataset"""
        results = {}
        
        # Eye color
        if self.eye_model:
            eye_predictor = EyeColorPredictor(self.eye_model)
            eye_result = eye_predictor.predict_from_snps(snp_data)
            results['eye_color'] = eye_result
        
        # Hair color
        if self.hair_model:
            hair_predictor = HairColorPredictor(self.hair_model)
            hair_result = hair_predictor.predict_from_snps(snp_data)
            results['hair_color'] = hair_result
        
        # Ancestry
        if self.ancestry_model:
            ancestry_predictor = AncestryPredictor(self.ancestry_model)
            ancestry_result = ancestry_predictor.predict_from_snps(snp_data)
            results['ancestry'] = ancestry_result
        
        return results
    
    def add_confidence_scores(self, results):
        """US-13: Add confidence scores for each prediction"""
        for trait in ['eye_color', 'hair_color']:
            if trait in results:
                conf = results[trait]['confidence']
                if conf > 0.8:
                    results[trait]['confidence_level'] = 'High'
                elif conf > 0.6:
                    results[trait]['confidence_level'] = 'Medium'
                else:
                    results[trait]['confidence_level'] = 'Low'
        
        return results

class EyeColorPredictor:
    """Helper for eye color prediction"""
    EYE_COLOR_SNPS = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']
    
    def __init__(self, model):
        self.model = model
    
    @staticmethod
    def encode_genotype(genotype):
        encoding = {'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2, 'AT': 1, 'TT': 2, 'CT': 1, 'GT': 1}
        return encoding.get(genotype.upper(), 0)
    
    def predict_from_snps(self, snp_dict):
        features = [self.encode_genotype(snp_dict.get(snp, 'AA')) for snp in self.EYE_COLOR_SNPS]
        prediction = self.model.predict([features])[0]
        confidence = max(self.model.predict_proba([features])[0])
        return {'prediction': prediction, 'confidence': confidence}

class HairColorPredictor:
    """Helper for hair color prediction"""
    HAIR_COLOR_SNPS = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
    
    def __init__(self, model):
        self.model = model
    
    @staticmethod
    def encode_genotype(genotype):
        encoding = {'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2, 'AT': 1, 'TT': 2, 'CT': 1, 'GT': 1}
        return encoding.get(genotype.upper(), 0)
    
    def predict_from_snps(self, snp_dict):
        features = [self.encode_genotype(snp_dict.get(snp, 'AA')) for snp in self.HAIR_COLOR_SNPS]
        prediction = self.model.predict([features])[0]
        confidence = max(self.model.predict_proba([features])[0])
        return {'prediction': prediction, 'confidence': confidence}

class AncestryPredictor:
    """Helper for ancestry prediction"""
    ANCESTRY_SNPS = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832']
    
    def __init__(self, model):
        self.model = model
    
    @staticmethod
    def encode_genotype(genotype):
        encoding = {'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2, 'AT': 1, 'TT': 2, 'CT': 1, 'GT': 1}
        return encoding.get(genotype.upper(), 0)
    
    def predict_from_snps(self, snp_dict):
        features = [self.encode_genotype(snp_dict.get(snp, 'AA')) for snp in self.ANCESTRY_SNPS]
        probabilities = self.model.predict_proba([features])[0]
        classes = self.model.classes_
        return {classes[i]: probabilities[i] for i in range(len(classes))}

def visualize_ancestry(ancestry_probs):
    """Visualize ancestry percentages"""
    plt.figure(figsize=(10, 6))
    colors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71', '#9b59b6']
    plt.barh(list(ancestry_probs.keys()), list(ancestry_probs.values()), color=colors[:len(ancestry_probs)])
    plt.xlabel('Probability', fontsize=12)
    plt.title('Ancestry Prediction', fontsize=14, fontweight='bold')
    plt.xlim(0, 1)
    for i, (ancestry, prob) in enumerate(ancestry_probs.items()):
        plt.text(prob + 0.02, i, f'{prob:.1%}', va='center')
    plt.tight_layout()
    plt.show()

# Example usage
if __name__ == "__main__":
    print("Sprint 3: Multi-Trait Models")
    print("US-10: Hair Color Model")
    print("US-11: Ancestry Model")
    print("US-12: Unified Pipeline")
    print("US-13: Confidence Scores")
