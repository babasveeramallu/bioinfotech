"""
Sprint 4: GUI & Deployment
User Stories: US-14, US-15, US-16
Story Points: 6
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pickle
import pandas as pd
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class DNATraitPredictorGUI:
    """US-14: tkinter GUI with input fields for SNPs"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("🧬 DNA Trait Predictor")
        self.root.geometry("800x700")
        self.root.configure(bg='#f0f0f0')
        
        # SNP input fields
        self.snp_entries = {}
        self.result_labels = {}
        
        # Load models
        self.load_models()
        
        # Create GUI
        self.create_widgets()
    
    def load_models(self):
        """Load trained ML models"""
        try:
            models_dir = os.path.join(os.path.dirname(__file__), '..', '..', 'models')
            self.eye_model = self._load_pickle(os.path.join(models_dir, 'eye_color_model.pkl'))
            self.hair_model = self._load_pickle(os.path.join(models_dir, 'hair_color_model.pkl'))
            self.ancestry_model = self._load_pickle(os.path.join(models_dir, 'ancestry_model.pkl'))
        except FileNotFoundError as e:
            messagebox.showwarning("Models Not Found", 
                                  "Some models are missing. Train models first.\n" + str(e))
    
    @staticmethod
    def _load_pickle(filepath):
        """Load pickled model"""
        if os.path.exists(filepath):
            with open(filepath, 'rb') as f:
                return pickle.load(f)
        return None
    
    def create_widgets(self):
        """Create all GUI elements"""
        # Title
        title_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        title_frame.pack(fill='x')
        title_frame.pack_propagate(False)
        
        title = tk.Label(title_frame, text="🧬 DNA Trait Predictor", 
                        font=("Arial", 26, "bold"), bg='#2c3e50', fg='white')
        title.pack(pady=20)
        
        subtitle = tk.Label(title_frame, text="AI-Powered Genetic Analysis", 
                           font=("Arial", 11), bg='#2c3e50', fg='#ecf0f1')
        subtitle.pack()
        
        # Main container
        main_frame = tk.Frame(self.root, bg='#f0f0f0')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Input Section
        self.create_input_section(main_frame)
        
        # Buttons Section
        self.create_buttons_section(main_frame)
        
        # Results Section
        self.create_results_section(main_frame)
    
    def create_input_section(self, parent):
        """US-14: Create input fields for SNPs"""
        input_frame = tk.LabelFrame(parent, text="📝 SNP Input", 
                                    font=("Arial", 13, "bold"), bg='#f0f0f0', 
                                    padx=15, pady=15)
        input_frame.pack(fill='x', pady=(0, 10))
        
        # Key SNPs for all traits
        key_snps = [
            ('rs12913832', 'Eye color (HERC2)'),
            ('rs1800407', 'Eye color (OCA2)'),
            ('rs12896399', 'Eye color (SLC24A4)'),
            ('rs16891982', 'Eye/Ancestry (SLC45A2)'),
            ('rs1393350', 'Eye color (TYR)'),
            ('rs12203592', 'Eye color (IRF4)'),
            ('rs1805007', 'Hair color (MC1R)'),
            ('rs1805008', 'Hair color (MC1R)'),
            ('rs1805009', 'Hair color (MC1R)'),
            ('rs1042602', 'Hair color (TYR)'),
            ('rs2228479', 'Hair color (OCA2)'),
            ('rs1426654', 'Ancestry (SLC24A5)'),
            ('rs3827760', 'Ancestry (EDAR)'),
            ('rs2814778', 'Ancestry (DARC)'),
        ]
        
        for i, (snp, description) in enumerate(key_snps):
            row = i // 2
            col = (i % 2) * 3
            
            tk.Label(input_frame, text=f"{snp}:", font=("Arial", 10, "bold"), 
                    bg='#f0f0f0', anchor='e', width=12).grid(row=row, column=col, 
                                                              sticky='e', padx=5, pady=5)
            
            entry = tk.Entry(input_frame, width=8, font=("Arial", 10), 
                           justify='center', relief='solid', borderwidth=1)
            entry.grid(row=row, column=col+1, padx=5, pady=5)
            entry.insert(0, "AA")
            self.snp_entries[snp] = entry
            
            tk.Label(input_frame, text=description, font=("Arial", 8), 
                    bg='#f0f0f0', fg='#7f8c8d', anchor='w').grid(row=row, column=col+2, 
                                                                  sticky='w', padx=5)
    
    def create_buttons_section(self, parent):
        """Create action buttons"""
        button_frame = tk.Frame(parent, bg='#f0f0f0')
        button_frame.pack(pady=15)
        
        # US-15: Upload CSV button
        upload_btn = tk.Button(button_frame, text="📁 Upload CSV", 
                              command=self.upload_csv,
                              font=("Arial", 11, "bold"), bg='#3498db', fg='white', 
                              padx=20, pady=10, relief='raised', borderwidth=2,
                              cursor='hand2')
        upload_btn.pack(side='left', padx=5)
        
        # Predict button
        predict_btn = tk.Button(button_frame, text="🔮 Predict Traits", 
                               command=self.predict_traits,
                               font=("Arial", 11, "bold"), bg='#2ecc71', fg='white', 
                               padx=20, pady=10, relief='raised', borderwidth=2,
                               cursor='hand2')
        predict_btn.pack(side='left', padx=5)
        
        # Clear button
        clear_btn = tk.Button(button_frame, text="🗑️ Clear", 
                             command=self.clear_inputs,
                             font=("Arial", 11, "bold"), bg='#e74c3c', fg='white', 
                             padx=20, pady=10, relief='raised', borderwidth=2,
                             cursor='hand2')
        clear_btn.pack(side='left', padx=5)
    
    def create_results_section(self, parent):
        """US-16: Display prediction results with confidence bars"""
        results_frame = tk.LabelFrame(parent, text="📊 Prediction Results", 
                                      font=("Arial", 13, "bold"), bg='#f0f0f0', 
                                      padx=15, pady=15)
        results_frame.pack(fill='both', expand=True)
        
        # Eye Color
        tk.Label(results_frame, text="👁️ Eye Color:", font=("Arial", 12, "bold"), 
                bg='#f0f0f0', anchor='w').grid(row=0, column=0, sticky='w', pady=8)
        self.result_labels['eye_color'] = tk.Label(results_frame, text="---", 
                                                   font=("Arial", 12), bg='#f0f0f0', 
                                                   anchor='w', width=30)
        self.result_labels['eye_color'].grid(row=0, column=1, sticky='w', padx=10)
        
        # Hair Color
        tk.Label(results_frame, text="💇 Hair Color:", font=("Arial", 12, "bold"), 
                bg='#f0f0f0', anchor='w').grid(row=1, column=0, sticky='w', pady=8)
        self.result_labels['hair_color'] = tk.Label(results_frame, text="---", 
                                                    font=("Arial", 12), bg='#f0f0f0', 
                                                    anchor='w', width=30)
        self.result_labels['hair_color'].grid(row=1, column=1, sticky='w', padx=10)
        
        # Ancestry
        tk.Label(results_frame, text="🌍 Ancestry:", font=("Arial", 12, "bold"), 
                bg='#f0f0f0', anchor='nw').grid(row=2, column=0, sticky='nw', pady=8)
        
        self.result_labels['ancestry'] = tk.Text(results_frame, height=6, width=40, 
                                                 font=("Courier", 10), bg='white', 
                                                 relief='solid', borderwidth=1)
        self.result_labels['ancestry'].grid(row=2, column=1, sticky='w', padx=10, pady=5)
    
    def upload_csv(self):
        """US-15: Upload CSV file and populate fields"""
        filepath = filedialog.askopenfilename(
            title="Select SNP Data File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filepath:
            try:
                df = pd.read_csv(filepath)
                
                # Populate SNP fields from CSV
                for snp in self.snp_entries.keys():
                    snp_row = df[df['rsid'] == snp]
                    if not snp_row.empty:
                        genotype = snp_row.iloc[0]['genotype']
                        self.snp_entries[snp].delete(0, tk.END)
                        self.snp_entries[snp].insert(0, genotype)
                
                messagebox.showinfo("Success", 
                                   f"✅ SNP data loaded successfully!\n{len(df)} SNPs found in file.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV:\n{str(e)}")
    
    def predict_traits(self):
        """Run all predictions and display results"""
        try:
            # Get SNP data from inputs
            snp_data = {snp: entry.get().upper().strip() for snp, entry in self.snp_entries.items()}
            
            # Validate inputs
            valid_genotypes = ['AA', 'AG', 'GG', 'AC', 'CC', 'AT', 'TT', 'CT', 'GT', 'GA', 'CA', 'TA', 'TC', 'CG', 'GC']
            for snp, genotype in snp_data.items():
                if genotype not in valid_genotypes:
                    messagebox.showwarning("Invalid Input", 
                        f"Invalid genotype '{genotype}' for {snp}.\nValid: {', '.join(valid_genotypes[:5])}...")
                    return
            
            # Check if models are loaded
            if not self.eye_model or not self.hair_model or not self.ancestry_model:
                messagebox.showerror("Models Not Loaded", 
                    "ML models are not loaded. Please train models first:\n\npython main.py --train")
                return
            
            # Predict eye color
            eye_result = self.predict_eye_color(snp_data)
            self.display_eye_result(eye_result)
            
            # Predict hair color
            hair_result = self.predict_hair_color(snp_data)
            self.display_hair_result(hair_result)
            
            # Predict ancestry
            ancestry_result = self.predict_ancestry(snp_data)
            self.display_ancestry_result(ancestry_result)
            
        except Exception as e:
            messagebox.showerror("Prediction Error", f"Failed to predict:\n{str(e)}")
    
    def predict_eye_color(self, snp_data):
        """Predict eye color"""
        snps = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']
        features = [self.encode_genotype(snp_data.get(snp, 'AA')) for snp in snps]
        
        prediction = self.eye_model.predict([features])[0]
        confidence = max(self.eye_model.predict_proba([features])[0])
        
        return {'prediction': prediction, 'confidence': confidence}
    
    def predict_hair_color(self, snp_data):
        """Predict hair color"""
        snps = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
        features = [self.encode_genotype(snp_data.get(snp, 'AA')) for snp in snps]
        
        prediction = self.hair_model.predict([features])[0]
        confidence = max(self.hair_model.predict_proba([features])[0])
        
        return {'prediction': prediction, 'confidence': confidence}
    
    def predict_ancestry(self, snp_data):
        """Predict ancestry"""
        snps = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832']
        features = [self.encode_genotype(snp_data.get(snp, 'AA')) for snp in snps]
        
        probabilities = self.ancestry_model.predict_proba([features])[0]
        classes = self.ancestry_model.classes_
        
        return {classes[i]: probabilities[i] for i in range(len(classes))}
    
    @staticmethod
    def encode_genotype(genotype):
        """Convert genotype to numeric"""
        encoding = {
            'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2,
            'AT': 1, 'TT': 2, 'CT': 1, 'GT': 1, 'GA': 1,
            'CA': 1, 'TA': 1, 'TC': 1, 'CG': 2, 'GC': 2
        }
        return encoding.get(genotype, 0)
    
    def display_eye_result(self, result):
        """Display eye color result with confidence"""
        pred = result['prediction']
        conf = result['confidence']
        
        color = '#2ecc71' if conf > 0.8 else '#f39c12' if conf > 0.6 else '#e74c3c'
        level = 'High' if conf > 0.8 else 'Medium' if conf > 0.6 else 'Low'
        
        self.result_labels['eye_color'].config(
            text=f"{pred.upper()} ({conf:.1%} confidence - {level})",
            fg=color, font=("Arial", 12, "bold")
        )
    
    def display_hair_result(self, result):
        """Display hair color result with confidence"""
        pred = result['prediction']
        conf = result['confidence']
        
        color = '#2ecc71' if conf > 0.8 else '#f39c12' if conf > 0.6 else '#e74c3c'
        level = 'High' if conf > 0.8 else 'Medium' if conf > 0.6 else 'Low'
        
        self.result_labels['hair_color'].config(
            text=f"{pred.upper()} ({conf:.1%} confidence - {level})",
            fg=color, font=("Arial", 12, "bold")
        )
    
    def display_ancestry_result(self, ancestry_probs):
        """US-16: Display ancestry with confidence bars"""
        self.result_labels['ancestry'].delete('1.0', tk.END)
        
        # Sort by probability
        sorted_ancestry = sorted(ancestry_probs.items(), key=lambda x: x[1], reverse=True)
        
        for ancestry, prob in sorted_ancestry:
            bar_length = int(prob * 30)
            bar = '█' * bar_length
            self.result_labels['ancestry'].insert(tk.END, 
                f"{ancestry:15s} {prob:5.1%} {bar}\n")
    
    def clear_inputs(self):
        """Clear all inputs and results"""
        for entry in self.snp_entries.values():
            entry.delete(0, tk.END)
            entry.insert(0, "AA")
        
        self.result_labels['eye_color'].config(text="---", fg='black', font=("Arial", 12))
        self.result_labels['hair_color'].config(text="---", fg='black', font=("Arial", 12))
        self.result_labels['ancestry'].delete('1.0', tk.END)

def main():
    """Launch the application"""
    root = tk.Tk()
    app = DNATraitPredictorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
