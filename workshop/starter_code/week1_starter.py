"""
Week 1 Starter Code: Data Pipeline & SNP Basics
Students will complete the TODO sections
"""

import pandas as pd
import matplotlib.pyplot as plt

def load_snp_data(filepath):
    """
    Load SNP data from CSV file
    
    Args:
        filepath: Path to CSV file
    
    Returns:
        DataFrame with columns: rsid, chromosome, position, genotype
    """
    # TODO: Use pandas to read CSV
    # Hint: pd.read_csv()
    pass

def filter_by_chromosome(df, chromosome):
    """
    Filter SNPs by chromosome number
    
    Args:
        df: SNP DataFrame
        chromosome: Chromosome number (1-22, X, Y)
    
    Returns:
        Filtered DataFrame
    """
    # TODO: Filter rows where chromosome column matches input
    # Hint: df[df['chromosome'] == chromosome]
    pass

def get_snp_by_id(df, rsid):
    """
    Find specific SNP by rsid
    
    Args:
        df: SNP DataFrame
        rsid: SNP identifier (e.g., 'rs12913832')
    
    Returns:
        Single row DataFrame or None
    """
    # TODO: Filter by rsid column
    pass

def plot_genotype_distribution(df):
    """
    Create bar chart of genotype counts
    
    Args:
        df: SNP DataFrame
    """
    # TODO: Count genotypes (AA, AG, GG, etc.)
    # Hint: df['genotype'].value_counts()
    # TODO: Create bar plot with matplotlib
    pass

def plot_chromosome_distribution(df):
    """
    Show how many SNPs per chromosome
    
    Args:
        df: SNP DataFrame
    """
    # TODO: Count SNPs per chromosome
    # TODO: Create bar plot
    pass

# Test your functions
if __name__ == "__main__":
    # Load sample data
    df = load_snp_data('../data/sample_snps.csv')
    
    # Print first 5 rows
    print("First 5 SNPs:")
    print(df.head())
    
    # Filter chromosome 15
    chr15 = filter_by_chromosome(df, 15)
    print(f"\nSNPs on chromosome 15: {len(chr15)}")
    
    # Find eye color SNP
    eye_snp = get_snp_by_id(df, 'rs12913832')
    print(f"\nEye color SNP: {eye_snp}")
    
    # Visualize
    plot_genotype_distribution(df)
    plot_chromosome_distribution(df)
