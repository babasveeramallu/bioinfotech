"""
Week 3 Solution: Multi-Trait Models
Complete working code
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import pickle

HAIR_COLOR_SNPS = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
ANCESTRY_SNPS = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832']

def encode_genotype(genotype):
    """Convert genotype to numeric"""
    encoding = {'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2, 'AT': 1, 'TT': 2, 'CT': 1}
    return encoding.get(genotype, -1)

def train_hair_color_model(X, y):
    """Train hair color classifier"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print(f"Hair Color Model - Test Accuracy: {model.score(X_test, y_test):.2%}")
    return model

def train_ancestry_model(X, y):
    """Train ancestry predictor"""
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    print(f"Ancestry Model - Test Accuracy: {model.score(X_test, y_test):.2%}")
    return model

def predict_all_traits(eye_model, hair_model, ancestry_model, snp_data):
    """Run all three models on input data"""
    # Eye color prediction
    eye_features = [encode_genotype(snp_data.get(snp, 'AA')) for snp in 
                    ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']]
    eye_pred = eye_model.predict([eye_features])[0]
    eye_conf = max(eye_model.predict_proba([eye_features])[0])
    
    # Hair color prediction
    hair_features = [encode_genotype(snp_data.get(snp, 'AA')) for snp in HAIR_COLOR_SNPS]
    hair_pred = hair_model.predict([hair_features])[0]
    hair_conf = max(hair_model.predict_proba([hair_features])[0])
    
    # Ancestry prediction
    ancestry_features = [encode_genotype(snp_data.get(snp, 'AA')) for snp in ANCESTRY_SNPS]
    ancestry_probs = ancestry_model.predict_proba([ancestry_features])[0]
    ancestry_classes = ancestry_model.classes_
    
    results = {
        'eye_color': {
            'prediction': eye_pred,
            'confidence': eye_conf
        },
        'hair_color': {
            'prediction': hair_pred,
            'confidence': hair_conf
        },
        'ancestry': {ancestry_classes[i]: ancestry_probs[i] for i in range(len(ancestry_classes))}
    }
    
    return results

def visualize_ancestry(ancestry_probs):
    """Create bar chart of ancestry percentages"""
    plt.figure(figsize=(10, 6))
    colors = ['#3498db', '#e74c3c', '#f39c12', '#2ecc71', '#9b59b6']
    plt.barh(list(ancestry_probs.keys()), list(ancestry_probs.values()), color=colors)
    plt.xlabel('Probability')
    plt.title('Ancestry Prediction')
    plt.xlim(0, 1)
    for i, (ancestry, prob) in enumerate(ancestry_probs.items()):
        plt.text(prob + 0.02, i, f'{prob:.1%}', va='center')
    plt.tight_layout()
    plt.show()

def add_confidence_labels(results):
    """Add confidence level labels"""
    for trait in ['eye_color', 'hair_color']:
        conf = results[trait]['confidence']
        if conf > 0.8:
            results[trait]['confidence_level'] = 'High'
        elif conf > 0.6:
            results[trait]['confidence_level'] = 'Medium'
        else:
            results[trait]['confidence_level'] = 'Low'
    return results

if __name__ == "__main__":
    # Load models
    eye_model = pickle.load(open('../models/eye_color_model.pkl', 'rb'))
    hair_model = pickle.load(open('../models/hair_color_model.pkl', 'rb'))
    ancestry_model = pickle.load(open('../models/ancestry_model.pkl', 'rb'))
    
    test_snps = {
        'rs12913832': 'AG',
        'rs1800407': 'GG',
        'rs1805007': 'CC',
        'rs1426654': 'AA',
        'rs2814778': 'GG'
    }
    
    results = predict_all_traits(eye_model, hair_model, ancestry_model, test_snps)
    results = add_confidence_labels(results)
    
    print("Prediction Results:")
    print(f"Eye Color: {results['eye_color']['prediction']} ({results['eye_color']['confidence_level']} - {results['eye_color']['confidence']:.1%})")
    print(f"Hair Color: {results['hair_color']['prediction']} ({results['hair_color']['confidence_level']} - {results['hair_color']['confidence']:.1%})")
    print("\nAncestry:")
    for ancestry, prob in results['ancestry'].items():
        print(f"  {ancestry}: {prob:.1%}")
    
    visualize_ancestry(results['ancestry'])
