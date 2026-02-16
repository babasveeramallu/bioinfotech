# Week 3: Multi-Trait Models
**Sprint Goal**: Add hair color, ancestry, and unified pipeline

## Session Outline (2 hours)

### Part 1: Expanding the System (15 min)
- Review Week 2 model
- New traits: Hair color genetics (MC1R gene)
- Ancestry prediction: Population genetics basics

### Part 2: Hands-On Coding (80 min)

#### Activity 1: Hair Color Model (25 min)
**Learning Goal**: Apply same ML workflow to new trait
```python
# Students complete: train_hair_color_model()
# Key SNPs: rs1805007, rs1805008, rs1805009 (MC1R), rs1042602 (TYR)
# Classes: black, brown, blonde, red
# Train and evaluate
```

#### Activity 2: Ancestry Model (30 min)
**Learning Goal**: Multi-class probability prediction
```python
# Students complete: train_ancestry_model()
# Use 20+ ancestry-informative SNPs
# Output: Probability distribution (e.g., 60% European, 30% East Asian, 10% African)
# Visualize with bar chart
```

#### Activity 3: Unified Pipeline (25 min)
**Learning Goal**: Integrate all models
```python
# Students complete: predict_all_traits()
# Input: Single SNP file
# Output: Dictionary with all predictions + confidence scores
# Add confidence thresholds (e.g., "Low confidence" if <60%)
```

### Part 3: Ethics Discussion (20 min)
- Genetic privacy concerns
- Limitations of trait prediction
- Why ancestry ≠ race
- Responsible use of genetic data

### Part 4: Wrap-Up (5 min)
- Preview Week 4: Building the GUI
- Homework: Design GUI mockup on paper

## Materials Needed
- `hair_color_training.csv` (400 samples)
- `ancestry_training.csv` (600 samples)
- `week3_starter.py` template
- Slides: Population genetics, ethics

## Success Criteria
✅ Students train 2 additional models  
✅ Students create unified prediction function  
✅ Students add confidence scores  
✅ Students understand ethical implications
