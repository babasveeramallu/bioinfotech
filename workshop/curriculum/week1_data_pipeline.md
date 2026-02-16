# Week 1: Data Pipeline & SNP Basics
**Sprint Goal**: Load, filter, and visualize SNP data

## Session Outline (2 hours)

### Part 1: Introduction (20 min)
- What are SNPs? (Single Nucleotide Polymorphisms)
- How DNA determines traits
- Demo: Show final working app
- Dataset overview: CSV structure

### Part 2: Hands-On Coding (60 min)

#### Activity 1: Load SNP Data (15 min)
**Learning Goal**: Read CSV files with pandas
```python
# Students complete: load_snp_data()
# Input: CSV with columns [rsid, chromosome, position, genotype]
# Output: pandas DataFrame
```

#### Activity 2: Filter SNPs (20 min)
**Learning Goal**: Extract specific genetic markers
```python
# Students complete: filter_by_chromosome()
# Task: Get all SNPs on chromosome 15
# Task: Find specific SNP by rsid (e.g., rs12913832)
```

#### Activity 3: Visualize Data (25 min)
**Learning Goal**: Understand dataset distribution
```python
# Students complete: plot_snp_distribution()
# Create bar chart of genotypes (AA, AG, GG)
# Show chromosome distribution
```

### Part 3: Biology Deep Dive (30 min)
- Eye color genetics: HERC2 gene (rs12913832)
- Why some SNPs matter more than others
- Genotype notation: AA vs AG vs GG
- Q&A

### Part 4: Wrap-Up (10 min)
- Preview Week 2: Training first ML model
- Homework: Explore OpenSNP.org dataset

## Materials Needed
- `sample_snps.csv` (100 SNPs)
- `week1_starter.py` template
- Slides: SNP biology basics

## Success Criteria
✅ Students can load CSV data  
✅ Students can filter by chromosome/position  
✅ Students create basic visualizations  
✅ Students understand genotype notation
