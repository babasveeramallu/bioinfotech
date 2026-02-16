"""
Week 1 Solution: Data Pipeline & SNP Basics
Complete working code
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_snp_data(filepath):
    """Load SNP data from CSV file"""
    return pd.read_csv(filepath)

def filter_by_chromosome(df, chromosome):
    """Filter SNPs by chromosome number"""
    return df[df['chromosome'] == chromosome]

def get_snp_by_id(df, rsid):
    """Find specific SNP by rsid"""
    result = df[df['rsid'] == rsid]
    return result if not result.empty else None

def plot_genotype_distribution(df):
    """Create bar chart of genotype counts"""
    counts = df['genotype'].value_counts()
    plt.figure(figsize=(10, 6))
    counts.plot(kind='bar', color='steelblue')
    plt.title('Genotype Distribution')
    plt.xlabel('Genotype')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_chromosome_distribution(df):
    """Show how many SNPs per chromosome"""
    counts = df['chromosome'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    counts.plot(kind='bar', color='coral')
    plt.title('SNPs per Chromosome')
    plt.xlabel('Chromosome')
    plt.ylabel('Number of SNPs')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    df = load_snp_data('../data/sample_snps.csv')
    print("First 5 SNPs:")
    print(df.head())
    
    chr15 = filter_by_chromosome(df, 15)
    print(f"\nSNPs on chromosome 15: {len(chr15)}")
    
    eye_snp = get_snp_by_id(df, 'rs12913832')
    print(f"\nEye color SNP:\n{eye_snp}")
    
    plot_genotype_distribution(df)
    plot_chromosome_distribution(df)
