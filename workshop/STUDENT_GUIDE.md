# Student Quick Start Guide
## DNA Trait Predictor Workshop

### Setup (Do This Before Week 1!)

#### Step 1: Install Python
- Download Python 3.8+ from [python.org](https://www.python.org/downloads/)
- **Important**: Check "Add Python to PATH" during installation

#### Step 2: Install Required Libraries
Open terminal/command prompt and run:
```bash
pip install pandas scikit-learn numpy matplotlib
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

#### Step 3: Verify Installation
Run this in Python:
```python
import pandas as pd
import sklearn
import numpy as np
import matplotlib.pyplot as plt
print("All libraries installed successfully!")
```

#### Step 4: Download Workshop Files
- Get files from instructor or GitHub
- Unzip to a folder like `Documents/dna_workshop/`

### Folder Structure
```
workshop/
├── curriculum/          # Lesson plans
├── starter_code/        # Your coding templates
├── solutions/           # Reference solutions (don't peek!)
├── data/               # Training datasets
└── slides/             # Presentation materials
```

---

## Week-by-Week Checklist

### Week 1: Data Pipeline
**Before Class**:
- [ ] Review: What is a CSV file?
- [ ] Read: curriculum/week1_data_pipeline.md

**During Class**:
- [ ] Complete: starter_code/week1_starter.py
- [ ] Test: Load sample_snps.csv successfully

**After Class**:
- [ ] Explore OpenSNP.org
- [ ] Try filtering different chromosomes

---

### Week 2: Machine Learning
**Before Class**:
- [ ] Review: What is machine learning? (Watch 5-min YouTube video)
- [ ] Read: curriculum/week2_eye_color_model.md

**During Class**:
- [ ] Complete: starter_code/week2_starter.py
- [ ] Train your first model!
- [ ] Save model to models/ folder

**After Class**:
- [ ] Test model on different SNP combinations
- [ ] Read about Random Forests

---

### Week 3: Multi-Trait Models
**Before Class**:
- [ ] Review Week 2 code
- [ ] Read: curriculum/week3_multi_trait.md
- [ ] Think about ethics questions

**During Class**:
- [ ] Complete: starter_code/week3_starter.py
- [ ] Train hair color and ancestry models
- [ ] Participate in ethics discussion

**After Class**:
- [ ] Sketch GUI design on paper
- [ ] List features you want in the app

---

### Week 4: GUI & Demo
**Before Class**:
- [ ] Review all previous code
- [ ] Read: curriculum/week4_gui_deployment.md
- [ ] Prepare 2-minute demo script

**During Class**:
- [ ] Complete: starter_code/week4_starter.py
- [ ] Build working GUI
- [ ] Demo to class!

**After Class**:
- [ ] Polish your app
- [ ] Add to GitHub portfolio
- [ ] Share with friends/family

---

## Troubleshooting Common Issues

### "ModuleNotFoundError: No module named 'pandas'"
**Fix**: Run `pip install pandas`

### "FileNotFoundError: [Errno 2] No such file or directory"
**Fix**: Check you're in the right folder. Use `cd` to navigate:
```bash
cd path/to/workshop
```

### "PermissionError" when saving model
**Fix**: Create models folder first:
```bash
mkdir models
```

### GUI window doesn't appear
**Fix**: Make sure you have `root.mainloop()` at the end

### Model accuracy is very low (<60%)
**Fix**: Check your genotype encoding (AA=0, AG=1, GG=2)

---

## Keyboard Shortcuts (Save Time!)

### Python/IDE
- `Ctrl + S` (Windows) / `Cmd + S` (Mac): Save file
- `Ctrl + /`: Comment/uncomment line
- `F5` or `Ctrl + Enter`: Run code

### Terminal
- `↑` (Up arrow): Previous command
- `Ctrl + C`: Stop running program
- `Tab`: Auto-complete file names

---

## Resources

### Learning Python
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Codecademy Python Course](https://www.codecademy.com/learn/learn-python-3)

### Learning Machine Learning
- [scikit-learn Tutorials](https://scikit-learn.org/stable/tutorial/index.html)
- [StatQuest YouTube](https://www.youtube.com/c/joshstarmer)
- [Google's ML Crash Course](https://developers.google.com/machine-learning/crash-course)

### Genetics Background
- [Khan Academy Genetics](https://www.khanacademy.org/science/biology/classical-genetics)
- [OpenSNP.org](https://opensnp.org/) - Public genetic data
- [SNPedia](https://www.snpedia.com/) - SNP database

### GUI Development
- [tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Real Python tkinter Tutorial](https://realpython.com/python-gui-tkinter/)

---

## Extension Ideas (After Workshop)

### Easy
- [ ] Add more SNPs to improve accuracy
- [ ] Change GUI colors and layout
- [ ] Add "Export Results" button (save to text file)

### Medium
- [ ] Add new trait: Lactose intolerance
- [ ] Create bar chart for confidence scores
- [ ] Parse 23andMe raw data format

### Hard
- [ ] Build web version with Flask
- [ ] Add database to store predictions
- [ ] Implement deep learning model

---

## Getting Help

### During Workshop
1. Ask your neighbor
2. Raise hand for instructor
3. Check solutions/ folder (last resort!)

### After Workshop
1. Re-read curriculum files
2. Google the error message
3. Check Stack Overflow
4. Email instructor: [instructor email]

---

## Certificate of Completion

To earn your certificate, complete:
- ✅ All 4 weeks of coding
- ✅ Working GUI demo
- ✅ 2-minute presentation

**Congratulations on building your DNA Trait Predictor!** 🧬🎉

---

## Share Your Work

- Add to GitHub with README
- Post demo video on LinkedIn
- Write blog post about what you learned
- Help teach next cohort!

### Sample GitHub README Template
```markdown
# DNA Trait Predictor

AI-powered application that predicts eye color, hair color, and ancestry from genetic data.

## Features
- Random Forest machine learning models
- Analyzes 14 key SNPs
- User-friendly GUI
- Confidence scoring

## Tech Stack
Python, pandas, scikit-learn, tkinter

## Demo
[Screenshot or GIF here]

## What I Learned
- Genetic data processing
- Machine learning fundamentals
- GUI development
- Ethics in genetics
```

Good luck and have fun! 🚀
