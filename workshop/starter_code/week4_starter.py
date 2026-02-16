"""
Week 4 Starter Code: GUI Application
Students will complete the TODO sections
"""

import tkinter as tk
from tkinter import filedialog, messagebox
import pickle
import pandas as pd

class DNATraitPredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Trait Predictor")
        self.root.geometry("600x500")
        
        # Load models
        self.load_models()
        
        # Create GUI elements
        self.create_widgets()
    
    def load_models(self):
        """Load all trained models"""
        # TODO: Load eye, hair, and ancestry models
        # Hint: pickle.load()
        pass
    
    def create_widgets(self):
        """Create all GUI elements"""
        # Title
        title = tk.Label(self.root, text="DNA Trait Predictor", font=("Arial", 20, "bold"))
        title.pack(pady=10)
        
        # TODO: Create input frame for SNP entry
        # TODO: Add labels and entry fields for key SNPs
        # Example:
        # tk.Label(input_frame, text="rs12913832:").grid(row=0, column=0)
        # self.snp1_entry = tk.Entry(input_frame)
        # self.snp1_entry.grid(row=0, column=1)
        
        # TODO: Create "Upload CSV" button
        # Hint: tk.Button(command=self.upload_csv)
        
        # TODO: Create "Predict" button
        # Hint: tk.Button(command=self.predict_traits)
        
        # TODO: Create results frame to display predictions
        # Use tk.Label widgets to show results
        
        pass
    
    def upload_csv(self):
        """Open file dialog and load SNP data"""
        # TODO: Use filedialog.askopenfilename()
        # TODO: Parse CSV and populate entry fields
        pass
    
    def predict_traits(self):
        """Run predictions and display results"""
        # TODO: Get values from entry fields
        # TODO: Call predict_all_traits() from week 3
        # TODO: Update result labels
        # TODO: Show confidence bars
        pass
    
    def display_results(self, results):
        """Update GUI with prediction results"""
        # TODO: Update result labels with predictions
        # TODO: Color code by confidence (green=high, yellow=medium, red=low)
        pass
    
    def clear_inputs(self):
        """Clear all entry fields"""
        # TODO: Clear all entry widgets
        pass

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DNATraitPredictorGUI(root)
    root.mainloop()
