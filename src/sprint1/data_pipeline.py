"""
Sprint 1: Data Pipeline
User Stories: US-01, US-02, US-03, US-04
Story Points: 12
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

class SNPDataLoader:
    """US-01: Load SNP data from CSV file"""
    
    def __init__(self):
        self.data = None
    
    def load_csv(self, filepath):
        """Load SNP data from CSV"""
        self.data = pd.read_csv(filepath)
        return self.data
    
    def get_data(self):
        """Return loaded data"""
        return self.data

class SNPFilter:
    """US-02: Filter SNPs by chromosome and position"""
    
    @staticmethod
    def filter_by_chromosome(df, chromosome):
        """Filter SNPs by chromosome number"""
        return df[df['chromosome'] == chromosome]
    
    @staticmethod
    def filter_by_position(df, chromosome, start_pos, end_pos):
        """Filter SNPs by chromosome and position range"""
        return df[(df['chromosome'] == chromosome) & 
                  (df['position'] >= start_pos) & 
                  (df['position'] <= end_pos)]
    
    @staticmethod
    def get_snp_by_id(df, rsid):
        """Get specific SNP by rsid"""
        result = df[df['rsid'] == rsid]
        return result if not result.empty else None

class SNPVisualizer:
    """US-03: Visualize SNP distributions"""
    
    @staticmethod
    def plot_genotype_distribution(df):
        """Plot genotype distribution"""
        counts = df['genotype'].value_counts()
        plt.figure(figsize=(10, 6))
        counts.plot(kind='bar', color='steelblue')
        plt.title('Genotype Distribution', fontsize=14, fontweight='bold')
        plt.xlabel('Genotype')
        plt.ylabel('Count')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    @staticmethod
    def plot_chromosome_distribution(df):
        """Plot SNPs per chromosome"""
        counts = df['chromosome'].value_counts().sort_index()
        plt.figure(figsize=(12, 6))
        counts.plot(kind='bar', color='coral')
        plt.title('SNPs per Chromosome', fontsize=14, fontweight='bold')
        plt.xlabel('Chromosome')
        plt.ylabel('Number of SNPs')
        plt.tight_layout()
        plt.show()

class TrainingDataCreator:
    """US-04: Create training dataset for eye color"""
    
    EYE_COLOR_SNPS = ['rs12913832', 'rs1800407', 'rs12896399', 
                      'rs16891982', 'rs1393350', 'rs12203592']
    
    @staticmethod
    def encode_genotype(genotype):
        """Convert genotype to numeric (AA=0, AG=1, GG=2)"""
        encoding = {
            'AA': 0, 'AG': 1, 'GG': 2,
            'AC': 1, 'CC': 2, 'AT': 1, 
            'TT': 2, 'CT': 1, 'GT': 1
        }
        return encoding.get(genotype, -1)
    
    def prepare_eye_color_features(self, snp_df, labels_df):
        """Extract features for eye color prediction"""
        features = []
        labels = []
        
        for idx, row in labels_df.iterrows():
            sample_snps = snp_df[snp_df['sample_id'] == row['sample_id']]
            feature_vector = []
            
            for snp in self.EYE_COLOR_SNPS:
                snp_row = sample_snps[sample_snps['rsid'] == snp]
                if not snp_row.empty:
                    feature_vector.append(self.encode_genotype(snp_row.iloc[0]['genotype']))
                else:
                    feature_vector.append(-1)
            
            features.append(feature_vector)
            labels.append(row['eye_color'])
        
        return np.array(features), np.array(labels)

# Example usage
if __name__ == "__main__":
    # US-01: Load data
    loader = SNPDataLoader()
    df = loader.load_csv('../data/sample_snps.csv')
    print(f"Loaded {len(df)} SNPs")
    
    # US-02: Filter data
    chr15 = SNPFilter.filter_by_chromosome(df, 15)
    print(f"SNPs on chromosome 15: {len(chr15)}")
    
    eye_snp = SNPFilter.get_snp_by_id(df, 'rs12913832')
    print(f"Eye color SNP found: {eye_snp is not None}")
    
    # US-03: Visualize
    SNPVisualizer.plot_genotype_distribution(df)
    SNPVisualizer.plot_chromosome_distribution(df)
    
    # US-04: Prepare training data
    creator = TrainingDataCreator()
    print(f"Eye color SNPs: {creator.EYE_COLOR_SNPS}")
