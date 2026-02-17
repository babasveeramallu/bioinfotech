"""
Generate Sample SNP Datasets for Training
Creates realistic synthetic data based on known genetics
"""

import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)
random.seed(42)

def generate_sample_snps(n_samples=100):
    """Generate sample SNP data for Week 1"""
    chromosomes = list(range(1, 23)) + ['X', 'Y']
    genotypes = ['AA', 'AG', 'GG', 'AC', 'CC', 'AT', 'TT', 'CT']
    
    # Key SNPs for traits
    key_snps = [
        ('rs12913832', 15, 28365618),  # Eye color (HERC2)
        ('rs1800407', 15, 28230318),   # Eye color (OCA2)
        ('rs12896399', 14, 92773663),  # Eye color (SLC24A4)
        ('rs16891982', 5, 33951693),   # Eye color (SLC45A2)
        ('rs1393350', 11, 89011046),   # Eye color (TYR)
        ('rs12203592', 6, 396321),     # Eye color (IRF4)
        ('rs1805007', 16, 89986117),   # Hair color (MC1R)
        ('rs1805008', 16, 89985940),   # Hair color (MC1R)
        ('rs1805009', 16, 89986144),   # Hair color (MC1R)
        ('rs1042602', 11, 89017961),   # Hair color (TYR)
        ('rs2228479', 15, 28356859),   # Hair color (OCA2)
        ('rs1426654', 15, 48426484),   # Ancestry (SLC24A5)
        ('rs3827760', 2, 109513601),   # Ancestry (EDAR)
        ('rs2814778', 1, 159174683),   # Ancestry (DARC)
    ]
    
    data = []
    for rsid, chrom, pos in key_snps:
        for sample in range(n_samples):
            data.append({
                'sample_id': f'SAMPLE_{sample:03d}',
                'rsid': rsid,
                'chromosome': chrom,
                'position': pos,
                'genotype': random.choice(genotypes[:3])  # AA, AG, GG most common
            })
    
    # Add random SNPs
    for i in range(86):  # Total 100 unique SNPs
        rsid = f'rs{random.randint(1000000, 9999999)}'
        chrom = random.choice(chromosomes)
        pos = random.randint(1000000, 200000000)
        for sample in range(n_samples):
            data.append({
                'sample_id': f'SAMPLE_{sample:03d}',
                'rsid': rsid,
                'chromosome': chrom,
                'position': pos,
                'genotype': random.choice(genotypes)
            })
    
    df = pd.DataFrame(data)
    df.to_csv('../../data/sample_snps.csv', index=False)
    print(f"Generated sample_snps.csv with {len(df)} rows")

def generate_eye_color_training(n_samples=3000):
    """Generate eye color training data with correct genetics"""
    eye_snps = ['rs12913832', 'rs1800407', 'rs12896399', 'rs16891982', 'rs1393350', 'rs12203592']
    eye_colors = ['blue', 'green', 'hazel', 'brown']
    
    # Correct genetic rules
    def predict_eye_color(snps):
        score = 0
        
        # rs12913832 (HERC2) - STRONGEST predictor
        # GG = blue, AA = brown, AG = intermediate
        herc2 = snps['rs12913832']
        if herc2 == 'GG':
            score -= 5  # Strong blue
        elif herc2 == 'AA':
            score += 5  # Strong brown
        else:
            score += 1  # Intermediate
        
        # rs1800407 (OCA2) - AA = lighter, GG = darker
        if snps['rs1800407'] == 'AA':
            score -= 2
        elif snps['rs1800407'] == 'GG':
            score += 2
        
        # rs12203592 (IRF4) - TT = light, AA = dark
        if snps['rs12203592'] in ['TT', 'AT']:
            score -= 1
        elif snps['rs12203592'] == 'AA':
            score += 1
        
        # rs12896399 (SLC24A4) - TT = light
        if snps['rs12896399'] in ['TT', 'GT']:
            score -= 1
        
        # Determine color from score
        if score <= -4:
            return 'blue'
        elif score <= -1:
            return random.choice(['blue', 'green'])
        elif score <= 2:
            return random.choice(['green', 'hazel'])
        else:
            return 'brown'
    
    snp_data = []
    labels = []
    
    for i in range(n_samples):
        sample_id = f'TRAIN_{i:04d}'
        
        # Generate realistic genotype combinations
        snp_values = {}
        snp_values['rs12913832'] = random.choice(['AA', 'AG', 'GG'])  # HERC2
        snp_values['rs1800407'] = random.choice(['AA', 'AG', 'GG'])  # OCA2
        snp_values['rs12203592'] = random.choice(['AA', 'AT', 'TT'])  # IRF4
        snp_values['rs12896399'] = random.choice(['GG', 'GT', 'TT'])  # SLC24A4
        snp_values['rs16891982'] = random.choice(['AA', 'AG', 'GG'])  # SLC45A2
        snp_values['rs1393350'] = random.choice(['AA', 'AG', 'GG'])  # TYR
        
        eye_color = predict_eye_color(snp_values)
        
        for snp, genotype in snp_values.items():
            snp_data.append({
                'sample_id': sample_id,
                'rsid': snp,
                'genotype': genotype
            })
        
        labels.append({
            'sample_id': sample_id,
            'eye_color': eye_color
        })
    
    pd.DataFrame(snp_data).to_csv('../../data/eye_color_training.csv', index=False)
    pd.DataFrame(labels).to_csv('../../data/eye_color_labels.csv', index=False)
    print(f"Generated eye color training data: {n_samples} samples")

def generate_hair_color_training(n_samples=2500):
    """Generate hair color training data with correct MC1R genetics"""
    hair_snps = ['rs1805007', 'rs1805008', 'rs1805009', 'rs1042602', 'rs2228479']
    hair_colors = ['black', 'brown', 'blonde', 'red']
    
    def predict_hair_color(snps):
        mc1r_variants = 0
        
        # Count MC1R variants (TT or CT = variant)
        for snp in ['rs1805007', 'rs1805008', 'rs1805009']:
            if snps[snp] in ['TT', 'CT']:
                mc1r_variants += 1
        
        # MC1R variants strongly predict red/blonde
        if mc1r_variants >= 2:
            return random.choice(['red', 'red', 'blonde'])  # Red more likely
        elif mc1r_variants == 1:
            return random.choice(['blonde', 'brown', 'red'])
        else:
            # No MC1R variants
            if snps['rs1042602'] == 'AA':
                return random.choice(['brown', 'black'])
            else:
                return random.choice(['brown', 'blonde'])
    
    snp_data = []
    labels = []
    
    for i in range(n_samples):
        sample_id = f'HAIR_{i:04d}'
        snp_values = {}
        snp_values['rs1805007'] = random.choice(['CC', 'CT', 'TT'])  # MC1R
        snp_values['rs1805008'] = random.choice(['CC', 'CT', 'TT'])  # MC1R
        snp_values['rs1805009'] = random.choice(['GG', 'GT', 'TT'])  # MC1R
        snp_values['rs1042602'] = random.choice(['AA', 'AG', 'GG'])  # TYR
        snp_values['rs2228479'] = random.choice(['AA', 'AG', 'GG'])  # OCA2
        
        hair_color = predict_hair_color(snp_values)
        
        for snp, genotype in snp_values.items():
            snp_data.append({
                'sample_id': sample_id,
                'rsid': snp,
                'genotype': genotype
            })
        
        labels.append({
            'sample_id': sample_id,
            'hair_color': hair_color
        })
    
    pd.DataFrame(snp_data).to_csv('../../data/hair_color_training.csv', index=False)
    pd.DataFrame(labels).to_csv('../../data/hair_color_labels.csv', index=False)
    print(f"Generated hair color training data: {n_samples} samples")

def generate_ancestry_training(n_samples=3000):
    """Generate ancestry training data with correct markers"""
    ancestry_snps = ['rs3827760', 'rs2814778', 'rs16891982', 'rs1426654', 'rs12913832']
    ancestries = ['European', 'African', 'East_Asian', 'South_Asian', 'Native_American']
    
    snp_data = []
    labels = []
    
    for i in range(n_samples):
        sample_id = f'ANC_{i:04d}'
        ancestry = random.choice(ancestries)
        
        # Ancestry-specific genotype patterns (CORRECTED)
        if ancestry == 'European':
            snp_values = {
                'rs1426654': random.choice(['AA', 'AA', 'AG']),  # AA = European
                'rs3827760': random.choice(['GG', 'GG', 'AG']),  # GG = Non-East Asian
                'rs2814778': random.choice(['TT', 'TT', 'CT']),  # TT common in Europeans
                'rs16891982': random.choice(['GG', 'AG']),
                'rs12913832': random.choice(['GG', 'AG', 'AA'])
            }
        elif ancestry == 'African':
            snp_values = {
                'rs1426654': random.choice(['GG', 'GG', 'AG']),  # GG = African
                'rs3827760': random.choice(['GG', 'AG']),
                'rs2814778': random.choice(['CC', 'CC', 'CT']),  # CC = African
                'rs16891982': random.choice(['AA', 'AG']),
                'rs12913832': random.choice(['AA', 'AA', 'AG'])
            }
        elif ancestry == 'East_Asian':
            snp_values = {
                'rs1426654': random.choice(['AG', 'GG']),
                'rs3827760': random.choice(['AA', 'AA', 'AG']),  # AA = East Asian
                'rs2814778': random.choice(['TT', 'CT']),
                'rs16891982': random.choice(['AA', 'AG']),
                'rs12913832': random.choice(['AA', 'AG'])
            }
        else:
            snp_values = {snp: random.choice(['AA', 'AG', 'GG']) for snp in ancestry_snps}
        
        for snp, genotype in snp_values.items():
            snp_data.append({
                'sample_id': sample_id,
                'rsid': snp,
                'genotype': genotype
            })
        
        labels.append({
            'sample_id': sample_id,
            'ancestry': ancestry
        })
    
    pd.DataFrame(snp_data).to_csv('../../data/ancestry_training.csv', index=False)
    pd.DataFrame(labels).to_csv('../../data/ancestry_labels.csv', index=False)
    print(f"Generated ancestry training data: {n_samples} samples")

if __name__ == "__main__":
    print("Generating training datasets...")
    generate_sample_snps()
    generate_eye_color_training()
    generate_hair_color_training()
    generate_ancestry_training()
    print("\nAll datasets generated successfully!")
    print("Files created in data/ directory:")
    print("  - sample_snps.csv")
    print("  - eye_color_training.csv + eye_color_labels.csv")
    print("  - hair_color_training.csv + hair_color_labels.csv")
    print("  - ancestry_training.csv + ancestry_labels.csv")
