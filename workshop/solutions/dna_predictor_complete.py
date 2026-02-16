"""
Complete DNA Trait Predictor GUI Application
Full working solution
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import pickle
import pandas as pd
import numpy as np

class DNATraitPredictorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("DNA Trait Predictor")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f0f0')
        
        self.snp_entries = {}
        self.result_labels = {}
        
        self.load_models()
        self.create_widgets()
    
    def load_models(self):
        """Load all trained models"""
        try:
            self.eye_model = pickle.load(open('models/eye_color_model.pkl', 'rb'))
            self.hair_model = pickle.load(open('models/hair_color_model.pkl', 'rb'))
            self.ancestry_model = pickle.load(open('models/ancestry_model.pkl', 'rb'))
        except FileNotFoundError:
            messagebox.showerror("Error", "Model files not found. Please train models first.")
    
    def create_widgets(self):
        """Create all GUI elements"""
        # Title
        title = tk.Label(self.root, text="🧬 DNA Trait Predictor", 
                        font=("Arial", 24, "bold"), bg='#f0f0f0', fg='#2c3e50')
        title.pack(pady=20)
        
        # Input Frame
        input_frame = tk.LabelFrame(self.root, text="SNP Input", 
                                    font=("Arial", 12, "bold"), bg='#f0f0f0', padx=20, pady=10)
        input_frame.pack(padx=20, pady=10, fill='both')
        
        # Key SNPs
        key_snps = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 
                    'rs1393350', 'rs12203592', 'rs1805007', 'rs1426654']
        
        for i, snp in enumerate(key_snps):
            tk.Label(input_frame, text=f"{snp}:", font=("Arial", 10), 
                    bg='#f0f0f0').grid(row=i//2, column=(i%2)*2, sticky='e', padx=5, pady=5)
            entry = tk.Entry(input_frame, width=10, font=("Arial", 10))
            entry.grid(row=i//2, column=(i%2)*2+1, padx=5, pady=5)
            entry.insert(0, "AA")
            self.snp_entries[snp] = entry
        
        # Buttons Frame
        button_frame = tk.Frame(self.root, bg='#f0f0f0')
        button_frame.pack(pady=10)
        
        tk.Button(button_frame, text="📁 Upload CSV", command=self.upload_csv,
                 font=("Arial", 11), bg='#3498db', fg='white', padx=15, pady=5).pack(side='left', padx=5)
        tk.Button(button_frame, text="🔮 Predict", command=self.predict_traits,
                 font=("Arial", 11, "bold"), bg='#2ecc71', fg='white', padx=20, pady=5).pack(side='left', padx=5)
        tk.Button(button_frame, text="🗑️ Clear", command=self.clear_inputs,
                 font=("Arial", 11), bg='#e74c3c', fg='white', padx=15, pady=5).pack(side='left', padx=5)
        
        # Results Frame
        results_frame = tk.LabelFrame(self.root, text="Prediction Results", 
                                      font=("Arial", 12, "bold"), bg='#f0f0f0', padx=20, pady=10)
        results_frame.pack(padx=20, pady=10, fill='both', expand=True)
        
        # Eye Color Result
        tk.Label(results_frame, text="Eye Color:", font=("Arial", 11, "bold"), 
                bg='#f0f0f0').grid(row=0, column=0, sticky='w', pady=5)
        self.result_labels['eye_color'] = tk.Label(results_frame, text="---", 
                                                   font=("Arial", 11), bg='#f0f0f0')
        self.result_labels['eye_color'].grid(row=0, column=1, sticky='w', padx=10)
        
        # Hair Color Result
        tk.Label(results_frame, text="Hair Color:", font=("Arial", 11, "bold"), 
                bg='#f0f0f0').grid(row=1, column=0, sticky='w', pady=5)
        self.result_labels['hair_color'] = tk.Label(results_frame, text="---", 
                                                    font=("Arial", 11), bg='#f0f0f0')
        self.result_labels['hair_color'].grid(row=1, column=1, sticky='w', padx=10)
        
        # Ancestry Results
        tk.Label(results_frame, text="Ancestry:", font=("Arial", 11, "bold"), 
                bg='#f0f0f0').grid(row=2, column=0, sticky='nw', pady=5)
        self.result_labels['ancestry'] = tk.Text(results_frame, height=5, width=40, 
                                                 font=("Arial", 10), bg='white')
        self.result_labels['ancestry'].grid(row=2, column=1, sticky='w', padx=10, pady=5)
    
    def upload_csv(self):
        """Open file dialog and load SNP data"""
        filepath = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filepath:
            try:
                df = pd.read_csv(filepath)
                for snp in self.snp_entries.keys():
                    snp_row = df[df['rsid'] == snp]
                    if not snp_row.empty:
                        self.snp_entries[snp].delete(0, tk.END)
                        self.snp_entries[snp].insert(0, snp_row.iloc[0]['genotype'])
                messagebox.showinfo("Success", "SNP data loaded successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load CSV: {str(e)}")
    
    def encode_genotype(self, genotype):
        """Convert genotype to numeric"""
        encoding = {'AA': 0, 'AG': 1, 'GG': 2, 'AC': 1, 'CC': 2, 'AT': 1, 'TT': 2, 'CT': 1}
        return encoding.get(genotype.upper(), 0)
    
    def predict_traits(self):
        """Run predictions and display results"""
        try:
            snp_data = {snp: entry.get().upper() for snp, entry in self.snp_entries.items()}
            
            # Eye color
            eye_snps = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']
            eye_features = [self.encode_genotype(snp_data.get(snp, 'AA')) for snp in eye_snps]
            eye_pred = self.eye_model.predict([eye_features])[0]
            eye_conf = max(self.eye_model.predict_proba([eye_features])[0])
            
            # Hair color
            hair_snps = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
            hair_features = [self.encode_genotype(snp_data.get(snp, 'AA')) for snp in hair_snps]
            hair_pred = self.hair_model.predict([hair_features])[0]
            hair_conf = max(self.hair_model.predict_proba([hair_features])[0])
            
            # Ancestry
            ancestry_snps = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832']
            ancestry_features = [self.encode_genotype(snp_data.get(snp, 'AA')) for snp in ancestry_snps]
            ancestry_probs = self.ancestry_model.predict_proba([ancestry_features])[0]
            ancestry_classes = self.ancestry_model.classes_
            
            # Display results
            eye_color = 'green' if eye_conf > 0.8 else 'orange' if eye_conf > 0.6 else 'red'
            self.result_labels['eye_color'].config(
                text=f"{eye_pred} ({eye_conf:.1%} confidence)", 
                fg=eye_color, font=("Arial", 11, "bold"))
            
            hair_color = 'green' if hair_conf > 0.8 else 'orange' if hair_conf > 0.6 else 'red'
            self.result_labels['hair_color'].config(
                text=f"{hair_pred} ({hair_conf:.1%} confidence)", 
                fg=hair_color, font=("Arial", 11, "bold"))
            
            # Ancestry text
            self.result_labels['ancestry'].delete('1.0', tk.END)
            for i, ancestry in enumerate(ancestry_classes):
                self.result_labels['ancestry'].insert(tk.END, 
                    f"{ancestry}: {ancestry_probs[i]:.1%}\n")
            
        except Exception as e:
            messagebox.showerror("Error", f"Prediction failed: {str(e)}")
    
    def clear_inputs(self):
        """Clear all entry fields"""
        for entry in self.snp_entries.values():
            entry.delete(0, tk.END)
            entry.insert(0, "AA")
        
        self.result_labels['eye_color'].config(text="---", fg='black')
        self.result_labels['hair_color'].config(text="---", fg='black')
        self.result_labels['ancestry'].delete('1.0', tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = DNATraitPredictorGUI(root)
    root.mainloop()
