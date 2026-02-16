"""
DNA Trait Predictor - Main Application
Integrates all 4 sprints following Scrum plan
Total Story Points: 46
"""

import sys
import os

# Add src directory to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from sprint1.data_pipeline import SNPDataLoader, SNPFilter, SNPVisualizer, TrainingDataCreator
from sprint2.eye_color_model import EyeColorModel, EyeColorPredictor
from sprint3.multi_trait_models import HairColorModel, AncestryModel, UnifiedPipeline
from sprint4.gui_application import DNATraitPredictorGUI

import tkinter as tk
import pandas as pd
import pickle

class DNATraitPredictor:
    """
    Complete DNA Trait Predictor Application
    
    Sprints:
    - Sprint 1 (12 pts): Data Pipeline
    - Sprint 2 (14 pts): Eye Color ML Model
    - Sprint 3 (15 pts): Multi-Trait Models
    - Sprint 4 (6 pts): GUI & Deployment
    """
    
    def __init__(self):
        self.data_loader = SNPDataLoader()
        self.filter = SNPFilter()
        self.visualizer = SNPVisualizer()
        self.training_creator = TrainingDataCreator()
        
        self.eye_model = None
        self.hair_model = None
        self.ancestry_model = None
    
    def train_all_models(self, data_dir='data'):
        """Train all three models"""
        print("="*60)
        print("Training All Models")
        print("="*60)
        
        # Train eye color model (Sprint 2)
        print("\n[Sprint 2] Training Eye Color Model...")
        eye_snp_df = pd.read_csv(f'{data_dir}/eye_color_training.csv')
        eye_labels_df = pd.read_csv(f'{data_dir}/eye_color_labels.csv')
        
        X_eye, y_eye = self.training_creator.prepare_eye_color_features(eye_snp_df, eye_labels_df)
        
        self.eye_model = EyeColorModel()
        self.eye_model.train(X_eye, y_eye)
        self.eye_model.evaluate()
        self.eye_model.save_model('models/eye_color_model.pkl')
        
        # Train hair color model (Sprint 3)
        print("\n[Sprint 3] Training Hair Color Model...")
        hair_snp_df = pd.read_csv(f'{data_dir}/hair_color_training.csv')
        hair_labels_df = pd.read_csv(f'{data_dir}/hair_color_labels.csv')
        
        hair_model = HairColorModel()
        X_hair, y_hair = hair_model.prepare_features(hair_snp_df, hair_labels_df)
        self.hair_model = hair_model.train(X_hair, y_hair)
        
        with open('models/hair_color_model.pkl', 'wb') as f:
            pickle.dump(self.hair_model, f)
        print("Hair color model saved!")
        
        # Train ancestry model (Sprint 3)
        print("\n[Sprint 3] Training Ancestry Model...")
        ancestry_snp_df = pd.read_csv(f'{data_dir}/ancestry_training.csv')
        ancestry_labels_df = pd.read_csv(f'{data_dir}/ancestry_labels.csv')
        
        ancestry_model = AncestryModel()
        X_ancestry, y_ancestry = ancestry_model.prepare_features(ancestry_snp_df, ancestry_labels_df)
        self.ancestry_model = ancestry_model.train(X_ancestry, y_ancestry)
        
        with open('models/ancestry_model.pkl', 'wb') as f:
            pickle.dump(self.ancestry_model, f)
        print("Ancestry model saved!")
        
        print("\n" + "="*60)
        print("All Models Trained Successfully!")
        print("="*60)
    
    def launch_gui(self):
        """Launch GUI application (Sprint 4)"""
        print("\n[Sprint 4] Launching GUI Application...")
        root = tk.Tk()
        app = DNATraitPredictorGUI(root)
        root.mainloop()
    
    def predict_from_file(self, filepath):
        """Predict traits from CSV file"""
        # Load data (Sprint 1)
        df = self.data_loader.load_csv(filepath)
        
        # Extract SNPs as dictionary
        snp_dict = {}
        for _, row in df.iterrows():
            snp_dict[row['rsid']] = row['genotype']
        
        # Predict using unified pipeline (Sprint 3)
        pipeline = UnifiedPipeline(
            'models/eye_color_model.pkl',
            'models/hair_color_model.pkl',
            'models/ancestry_model.pkl'
        )
        
        results = pipeline.predict_all_traits(snp_dict)
        results = pipeline.add_confidence_scores(results)
        
        return results
    
    def demo_prediction(self):
        """Demo prediction with sample data"""
        print("\n" + "="*60)
        print("Demo Prediction")
        print("="*60)
        
        sample_snps = {
            'rs12913832': 'AG',  # Eye color
            'rs1800407': 'GG',
            'rs12896399': 'GG',
            'rs16891982': 'GG',
            'rs1393350': 'AA',
            'rs12203592': 'GG',
            'rs1805007': 'CC',  # Hair color
            'rs1805008': 'CC',
            'rs1805009': 'GG',
            'rs1042602': 'AA',
            'rs2228479': 'GG',
            'rs3827760': 'AA',  # Ancestry
            'rs2814778': 'GG',
            'rs1426654': 'AA',
        }
        
        print("\nInput SNPs:")
        for snp, genotype in list(sample_snps.items())[:5]:
            print(f"  {snp}: {genotype}")
        print("  ...")
        
        # Predict
        pipeline = UnifiedPipeline(
            'models/eye_color_model.pkl',
            'models/hair_color_model.pkl',
            'models/ancestry_model.pkl'
        )
        
        results = pipeline.predict_all_traits(sample_snps)
        results = pipeline.add_confidence_scores(results)
        
        print("\nPredictions:")
        print(f"  👁️  Eye Color: {results['eye_color']['prediction']} "
              f"({results['eye_color']['confidence']:.1%} - {results['eye_color']['confidence_level']})")
        print(f"  💇 Hair Color: {results['hair_color']['prediction']} "
              f"({results['hair_color']['confidence']:.1%} - {results['hair_color']['confidence_level']})")
        print(f"  🌍 Ancestry:")
        for ancestry, prob in sorted(results['ancestry'].items(), key=lambda x: x[1], reverse=True):
            print(f"      {ancestry}: {prob:.1%}")
        
        print("="*60)

def main():
    """Main entry point"""
    import argparse
    
    parser = argparse.ArgumentParser(description='DNA Trait Predictor')
    parser.add_argument('--train', action='store_true', help='Train all models')
    parser.add_argument('--gui', action='store_true', help='Launch GUI')
    parser.add_argument('--demo', action='store_true', help='Run demo prediction')
    parser.add_argument('--predict', type=str, help='Predict from CSV file')
    
    args = parser.parse_args()
    
    app = DNATraitPredictor()
    
    if args.train:
        app.train_all_models()
    elif args.gui:
        app.launch_gui()
    elif args.demo:
        app.demo_prediction()
    elif args.predict:
        results = app.predict_from_file(args.predict)
        print(results)
    else:
        # Default: Launch GUI
        print("""
╔══════════════════════════════════════════════════════════╗
║                                                          ║
║           🧬 DNA TRAIT PREDICTOR 🧬                      ║
║                                                          ║
║     AI-Powered Eye Color, Hair Color & Ancestry         ║
║                                                          ║
╚══════════════════════════════════════════════════════════╝

Usage:
  python main.py --train    # Train all models
  python main.py --gui      # Launch GUI (default)
  python main.py --demo     # Run demo prediction
  python main.py --predict <file.csv>  # Predict from file

Launching GUI...
        """)
        app.launch_gui()

if __name__ == "__main__":
    main()
