# 🧬 DNA Trait Predictor

AI-powered application that predicts **eye color**, **hair color**, and **ancestry** from DNA SNP data using machine learning.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0+-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-Educational-green.svg)](LICENSE)

## 🎯 Project Overview

Built following **Agile Scrum methodology** over 4 sprints (4 weeks), this project demonstrates the intersection of genetics and artificial intelligence.

- **Total Story Points**: 46
- **User Stories**: 16
- **ML Models**: 3 (Random Forest classifiers)
- **Accuracy**: 80-95% depending on trait

## ✨ Features

- 🔬 **Eye Color Prediction**: Blue, green, hazel, or brown (6 SNPs)
- 💇 **Hair Color Prediction**: Black, brown, blonde, or red (5 SNPs)
- 🌍 **Ancestry Estimation**: Continental ancestry percentages (5 SNPs)
- 🖥️ **GUI Application**: User-friendly tkinter interface
- 📊 **Confidence Scores**: High/Medium/Low reliability indicators
- 📁 **CSV Upload**: Bulk data analysis support

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/babasveeramallu/bioinfotech.git
cd bioinfotech

# Install dependencies
pip install pandas scikit-learn numpy matplotlib
```

### Generate Training Data

```bash
cd workshop/data
python generate_datasets.py
```

### Train Models

```bash
cd ../../src
python main.py --train
```

### Launch GUI

```bash
python main.py --gui
```

## 📁 Project Structure

```
bioinfotech/
├── src/                          # Production code (4 sprints)
│   ├── sprint1/                  # Data Pipeline (12 pts)
│   ├── sprint2/                  # Eye Color Model (14 pts)
│   ├── sprint3/                  # Multi-Trait Models (15 pts)
│   ├── sprint4/                  # GUI Application (6 pts)
│   └── main.py                   # Main entry point
├── workshop/                     # Teaching materials
│   ├── curriculum/               # Week-by-week lessons
│   ├── starter_code/             # Student templates
│   ├── solutions/                # Complete solutions
│   ├── data/                     # Training datasets
│   └── slides/                   # Presentation outlines
├── data/                         # Generated datasets
├── models/                       # Trained ML models
└── README.md
```

## 🧬 How It Works

### SNP Analysis
The application analyzes Single Nucleotide Polymorphisms (SNPs) - genetic variations that make us unique:

- **rs12913832** (HERC2 gene): Primary eye color determinant
- **rs1805007** (MC1R gene): Red hair variant
- **rs1426654** (SLC24A5 gene): European ancestry marker

### Machine Learning Pipeline
1. **Data Loading**: Parse CSV files with SNP data
2. **Feature Extraction**: Convert genotypes to numeric (AA=0, AG=1, GG=2)
3. **Model Training**: Random Forest with 100 trees
4. **Prediction**: Output trait with confidence score

## 📊 Model Performance

| Trait | Accuracy | Key SNPs |
|-------|----------|----------|
| Eye Color | 80-90% | 6 markers |
| Hair Color | 75-85% | 5 markers |
| Ancestry | 85-95% | 5 markers |

## 💻 Usage Examples

### Command Line

```bash
# Run demo prediction
python src/main.py --demo

# Predict from CSV file
python src/main.py --predict data/sample_snps.csv
```

### Python API

```python
from src.main import DNATraitPredictor

app = DNATraitPredictor()
app.train_all_models()

# Predict traits
results = app.predict_from_file('data/sample.csv')
print(results)
```

## 🎓 Workshop Materials

This project includes complete teaching materials for a 4-week workshop:

- **Week 1**: Data Pipeline & SNP Basics
- **Week 2**: Machine Learning Fundamentals
- **Week 3**: Multi-Trait Prediction
- **Week 4**: GUI Development

See `workshop/` directory for curriculum, starter code, and solutions.

## 🛠️ Tech Stack

- **Python 3.8+**: Core language
- **pandas**: Data processing
- **scikit-learn**: Machine learning (Random Forest)
- **numpy**: Numerical computing
- **tkinter**: GUI framework
- **matplotlib**: Visualization

## 📋 Scrum Plan

### Sprint 1: Data Pipeline (12 Story Points)
- US-01: Load SNP data from CSV (3 pts)
- US-02: Filter SNPs by chromosome/position (3 pts)
- US-03: Visualize SNP distributions (2 pts)
- US-04: Create training dataset (4 pts)

### Sprint 2: Eye Color ML Model (14 Story Points)
- US-05: Train Random Forest classifier (5 pts)
- US-06: Train/test split (2 pts)
- US-07: Evaluate with metrics (3 pts)
- US-08: Save model to disk (2 pts)
- US-09: Make predictions (2 pts)

### Sprint 3: Multi-Trait Models (15 Story Points)
- US-10: Hair color classifier (4 pts)
- US-11: Ancestry predictor (5 pts)
- US-12: Unified pipeline (3 pts)
- US-13: Confidence scores (3 pts)

### Sprint 4: GUI & Deployment (6 Story Points)
- US-14: tkinter GUI (4 pts)
- US-15: CSV upload (2 pts)
- US-16: Results display (included)

## 🔬 Scientific Background

### Data Sources
- [OpenSNP](https://opensnp.org/): Public genetic data
- [SNPedia](https://www.snpedia.com/): SNP database
- HIrisPlex research papers

### Key Research
- Walsh et al. (2013): HIrisPlex DNA-based prediction
- Branicki et al. (2011): Genetic determinants of hair color
- Kosoy et al. (2009): Ancestry-informative markers

## 🔒 Ethics & Privacy

⚠️ **Important Considerations**:
- Genetic data is sensitive and permanent
- Predictions are probabilistic, not deterministic
- Ancestry ≠ race (social construct)
- Not for medical diagnosis
- Respect genetic privacy

## 🤝 Contributing

This is an educational project. Contributions welcome:
- Report bugs
- Suggest improvements
- Add new traits
- Improve documentation

## 📄 License

Educational use only. Not for commercial purposes.

## 👨‍💻 Author

**Biotech Club Mini Missions - Spring 2026**

Created for teaching genetics + AI intersection to students.

## 🙏 Acknowledgments

- OpenSNP community
- scikit-learn developers
- Genetics research community



**🧬 Making genetics accessible through AI 🔬**
