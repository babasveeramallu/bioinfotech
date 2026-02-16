# DNA Trait Predictor - Production Code
## Complete Implementation Following Scrum Plan

### Project Overview
AI-powered application that predicts **eye color**, **hair color**, and **ancestry** from DNA SNP data using machine learning.

**Duration**: 4 weeks (March 10 – April 7, 2026)  
**Total Story Points**: 46  
**Framework**: Scrum with 1-week sprints

---

## 📁 Project Structure

```
DNA Biotech/
├── src/
│   ├── sprint1/
│   │   └── data_pipeline.py          # US-01 to US-04 (12 pts)
│   ├── sprint2/
│   │   └── eye_color_model.py        # US-05 to US-09 (14 pts)
│   ├── sprint3/
│   │   └── multi_trait_models.py     # US-10 to US-13 (15 pts)
│   ├── sprint4/
│   │   └── gui_application.py        # US-14 to US-16 (6 pts)
│   └── main.py                       # Main application entry point
├── data/
│   ├── generate_datasets.py          # Generate training data
│   ├── sample_snps.csv
│   ├── eye_color_training.csv
│   ├── hair_color_training.csv
│   └── ancestry_training.csv
├── models/                            # Trained ML models (generated)
│   ├── eye_color_model.pkl
│   ├── hair_color_model.pkl
│   └── ancestry_model.pkl
└── requirements.txt
```

---

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install pandas scikit-learn numpy matplotlib
```

### 2. Generate Training Data
```bash
cd data
python generate_datasets.py
```

### 3. Train Models
```bash
cd src
python main.py --train
```

### 4. Launch GUI
```bash
python main.py --gui
```

---

## 📋 Sprint Breakdown

### Sprint 1: Data Pipeline (12 Story Points)
**Files**: `src/sprint1/data_pipeline.py`

| User Story | Description | Points |
|------------|-------------|--------|
| US-01 | Load SNP data from CSV | 3 |
| US-02 | Filter SNPs by chromosome/position | 3 |
| US-03 | Visualize SNP distributions | 2 |
| US-04 | Create training dataset for eye color | 4 |

**Key Classes**:
- `SNPDataLoader`: Load CSV files
- `SNPFilter`: Filter by chromosome/position
- `SNPVisualizer`: Plot distributions
- `TrainingDataCreator`: Prepare ML features

### Sprint 2: Eye Color ML Model (14 Story Points)
**Files**: `src/sprint2/eye_color_model.py`

| User Story | Description | Points |
|------------|-------------|--------|
| US-05 | Train Random Forest for eye color | 5 |
| US-06 | Split data into train/test sets | 2 |
| US-07 | Evaluate model with accuracy metrics | 3 |
| US-08 | Save trained model to disk | 2 |
| US-09 | Make predictions on new SNP data | 2 |

**Key Classes**:
- `EyeColorModel`: Train and evaluate
- `EyeColorPredictor`: High-level prediction interface

**Key SNPs**: rs12913832, rs1800407, rs12896399, rs16891982, rs1393350, rs12203592

### Sprint 3: Multi-Trait Models (15 Story Points)
**Files**: `src/sprint3/multi_trait_models.py`

| User Story | Description | Points |
|------------|-------------|--------|
| US-10 | Train hair color classifier | 4 |
| US-11 | Train ancestry predictor | 5 |
| US-12 | Create unified prediction pipeline | 3 |
| US-13 | Add confidence scores | 3 |

**Key Classes**:
- `HairColorModel`: Black/brown/blonde/red prediction
- `AncestryModel`: Continental ancestry percentages
- `UnifiedPipeline`: Integrate all models
- Helper predictors for each trait

### Sprint 4: GUI & Deployment (6 Story Points)
**Files**: `src/sprint4/gui_application.py`

| User Story | Description | Points |
|------------|-------------|--------|
| US-14 | tkinter GUI with SNP input fields | 4 |
| US-15 | Upload CSV through GUI | 2 |
| US-16 | Display results with confidence bars | (included) |

**Key Class**:
- `DNATraitPredictorGUI`: Complete GUI application

---

## 💻 Usage Examples

### Command Line Interface

```bash
# Train all models
python src/main.py --train

# Launch GUI (default)
python src/main.py --gui

# Run demo prediction
python src/main.py --demo

# Predict from CSV file
python src/main.py --predict data/sample_snps.csv
```

### Python API

```python
from src.main import DNATraitPredictor

# Initialize
app = DNATraitPredictor()

# Train models
app.train_all_models()

# Predict from file
results = app.predict_from_file('data/sample_snps.csv')

# Launch GUI
app.launch_gui()
```

### Individual Sprint Usage

```python
# Sprint 1: Load and filter data
from src.sprint1.data_pipeline import SNPDataLoader, SNPFilter

loader = SNPDataLoader()
df = loader.load_csv('data/sample_snps.csv')
chr15 = SNPFilter.filter_by_chromosome(df, 15)

# Sprint 2: Train eye color model
from src.sprint2.eye_color_model import EyeColorModel

model = EyeColorModel()
model.train(X, y)
model.evaluate()
model.save_model('models/eye_color_model.pkl')

# Sprint 3: Unified prediction
from src.sprint3.multi_trait_models import UnifiedPipeline

pipeline = UnifiedPipeline(
    'models/eye_color_model.pkl',
    'models/hair_color_model.pkl',
    'models/ancestry_model.pkl'
)
results = pipeline.predict_all_traits(snp_data)

# Sprint 4: Launch GUI
from src.sprint4.gui_application import main
main()
```

---

## 🧬 SNP Reference

### Eye Color SNPs (6 markers)
- **rs12913832** (HERC2): Most important - GG=brown, AA=blue, AG=mixed
- rs1800407 (OCA2): Modifies brown/blue
- rs12896399 (SLC24A4): Green vs blue
- rs16891982 (SLC45A2): Pigmentation intensity
- rs1393350 (TYR): Melanin production
- rs12203592 (IRF4): Blue/green modifier

### Hair Color SNPs (5 markers)
- **rs1805007** (MC1R): Red hair variant
- rs1805008 (MC1R): Red hair variant
- rs1805009 (MC1R): Red hair variant
- rs1042602 (TYR): Blonde hair
- rs2228479 (OCA2): Brown/black hair

### Ancestry SNPs (5 markers)
- **rs1426654** (SLC24A5): European ancestry
- rs3827760 (EDAR): East Asian ancestry
- rs2814778 (DARC): African ancestry
- rs16891982 (SLC45A2): European ancestry
- rs12913832 (HERC2): European ancestry

---

## 📊 Model Performance

### Expected Accuracy
- **Eye Color**: 80-90%
- **Hair Color**: 75-85%
- **Ancestry**: 85-95%

### Confidence Levels
- **High** (>80%): Strong genetic signal
- **Medium** (60-80%): Moderate signal
- **Low** (<60%): Weak signal

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python 3.8+ |
| Data Processing | pandas |
| Machine Learning | scikit-learn (Random Forest) |
| Numerical Computing | numpy |
| Visualization | matplotlib |
| GUI | tkinter (built-in) |
| Model Storage | pickle |

---

## 📝 Development Notes

### Genotype Encoding
```python
AA = 0  # Homozygous
AG = 1  # Heterozygous
GG = 2  # Homozygous
```

### Model Training
- Algorithm: Random Forest (100 trees)
- Train/Test Split: 80/20
- Random State: 42 (reproducibility)

### Data Format
CSV files with columns:
- `sample_id`: Unique identifier
- `rsid`: SNP identifier (e.g., rs12913832)
- `chromosome`: 1-22, X, Y
- `position`: Base pair position
- `genotype`: AA, AG, GG, etc.

---

## 🧪 Testing

Run individual sprint tests:
```bash
# Test Sprint 1
python src/sprint1/data_pipeline.py

# Test Sprint 2
python src/sprint2/eye_color_model.py

# Test Sprint 3
python src/sprint3/multi_trait_models.py

# Test Sprint 4
python src/sprint4/gui_application.py
```

---

## 🎯 Scrum Metrics

- **Total Story Points**: 46
- **Sprint Velocity**: 11.5 points/week
- **Sprint Duration**: 1 week each
- **Total Duration**: 4 weeks
- **User Stories**: 16
- **Sprints**: 4

---

## 📚 References

### Scientific Papers
- HIrisPlex: DNA-based eye and hair color prediction (Walsh et al., 2013)
- Genetic determinants of hair color (Branicki et al., 2011)
- Ancestry-informative markers (Kosoy et al., 2009)

### Data Sources
- OpenSNP.org: Public genetic data
- SNPedia: SNP database
- dbSNP: NCBI SNP database

---

## 🔒 Ethics & Privacy

- Genetic data is sensitive and permanent
- Predictions are probabilistic, not deterministic
- Ancestry ≠ race (social construct)
- Do not use for medical decisions without consulting a doctor
- Respect genetic privacy

---

## 🚧 Future Enhancements

- [ ] Add more traits (lactose intolerance, bitter taste)
- [ ] Implement deep learning models
- [ ] Create web version with Flask
- [ ] Add 23andMe data parser
- [ ] Implement cross-validation
- [ ] Add feature importance visualization
- [ ] Export results to PDF

---

## 📄 License

Educational use only. Not for commercial purposes.

---

## 👨‍💻 Author

Created for Biotech Club Mini Missions - Spring 2026

**Contact**: [Your Email]  
**GitHub**: [Your GitHub]

---

## 🙏 Acknowledgments

- OpenSNP community for public genetic data
- scikit-learn developers
- Genetics research community

---

**Ready to predict traits from DNA! 🧬🔬**
