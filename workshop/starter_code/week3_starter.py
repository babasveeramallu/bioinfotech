"""
Week 3 Starter Code: Multi-Trait Models
Students will complete the TODO sections
"""

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Key SNPs for each trait
HAIR_COLOR_SNPS = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
ANCESTRY_SNPS = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832', 
                 'rs1800414', 'rs885479', 'rs1834640', 'rs2814778', 'rs1426654']

def train_hair_color_model(X, y):
    """
    Train hair color classifier
    
    Args:
        X: Features from HAIR_COLOR_SNPS
        y: Labels (black, brown, blonde, red)
    
    Returns:
        Trained model
    """
    # TODO: Same workflow as eye color model
    # TODO: Train RandomForestClassifier
    pass

def train_ancestry_model(X, y):
    """
    Train ancestry predictor
    
    Args:
        X: Features from ANCESTRY_SNPS
        y: Labels (European, African, East Asian, South Asian, Native American)
    
    Returns:
        Trained model
    """
    # TODO: Train classifier
    # Note: This model outputs probabilities for each ancestry
    pass

def predict_all_traits(eye_model, hair_model, ancestry_model, snp_data):
    """
    Run all three models on input data
    
    Args:
        eye_model: Trained eye color model
        hair_model: Trained hair color model
        ancestry_model: Trained ancestry model
        snp_data: Dictionary of all SNP values
    
    Returns:
        Dictionary with predictions and confidence scores
    """
    # TODO: Extract relevant SNPs for each model
    # TODO: Make predictions
    # TODO: Calculate confidence scores
    # TODO: Return structured results
    
    results = {
        'eye_color': {
            'prediction': None,
            'confidence': None
        },
        'hair_color': {
            'prediction': None,
            'confidence': None
        },
        'ancestry': {
            'European': None,
            'African': None,
            'East_Asian': None,
            'South_Asian': None,
            'Native_American': None
        }
    }
    # TODO: Fill in results
    return results

def visualize_ancestry(ancestry_probs):
    """
    Create bar chart of ancestry percentages
    
    Args:
        ancestry_probs: Dictionary of ancestry probabilities
    """
    # TODO: Create horizontal bar chart
    # TODO: Color code by ancestry group
    pass

def add_confidence_labels(results):
    """
    Add confidence level labels (High/Medium/Low)
    
    Args:
        results: Prediction results dictionary
    
    Returns:
        Results with confidence labels added
    """
    # TODO: Add 'confidence_level' field
    # High: >80%, Medium: 60-80%, Low: <60%
    pass

# Test your functions
if __name__ == "__main__":
    # Load all models
    import pickle
    eye_model = pickle.load(open('../models/eye_color_model.pkl', 'rb'))
    hair_model = pickle.load(open('../models/hair_color_model.pkl', 'rb'))
    ancestry_model = pickle.load(open('../models/ancestry_model.pkl', 'rb'))
    
    # Test SNP data
    test_snps = {
        'rs12913832': 'AG',
        'rs1800407': 'GG',
        'rs1805007': 'CC',
        'rs1426654': 'AA',
        # ... more SNPs
    }
    
    # Predict all traits
    results = predict_all_traits(eye_model, hair_model, ancestry_model, test_snps)
    results = add_confidence_labels(results)
    
    print("Prediction Results:")
    print(f"Eye Color: {results['eye_color']['prediction']} ({results['eye_color']['confidence_level']})")
    print(f"Hair Color: {results['hair_color']['prediction']} ({results['hair_color']['confidence_level']})")
    print("\nAncestry:")
    for ancestry, prob in results['ancestry'].items():
        print(f"  {ancestry}: {prob:.1%}")
    
    # Visualize
    visualize_ancestry(results['ancestry'])
