# Week 2: Eye Color ML Model
**Sprint Goal**: Train, evaluate, and save Random Forest classifier

## Session Outline (2 hours)

### Part 1: ML Crash Course (25 min)
- What is machine learning?
- Supervised learning: features → labels
- Random Forest intuition (decision trees voting)
- Train/test split concept

### Part 2: Hands-On Coding (70 min)

#### Activity 1: Prepare Training Data (20 min)
**Learning Goal**: Convert SNPs to ML features
```python
# Students complete: prepare_eye_color_data()
# Input: SNP data + eye color labels
# Output: X (features), y (labels)
# Key SNPs: rs12913832, rs1800407, rs12896399, rs16891982, rs1393350, rs12203592
```

#### Activity 2: Train Model (15 min)
**Learning Goal**: Use scikit-learn
```python
# Students complete: train_eye_color_model()
# Split data 80/20
# Train RandomForestClassifier
# Print training accuracy
```

#### Activity 3: Evaluate Model (20 min)
**Learning Goal**: Understand accuracy metrics
```python
# Students complete: evaluate_model()
# Calculate test accuracy
# Show confusion matrix
# Discuss: Why 85% accuracy is good for genetics
```

#### Activity 4: Save & Load Model (15 min)
**Learning Goal**: Model persistence
```python
# Students complete: save_model() and load_model()
# Use pickle to serialize
# Test: Load model and make prediction
```

### Part 3: Live Demo (20 min)
- Instructor predicts own eye color
- Show how wrong predictions happen (mixed ancestry)
- Discuss model limitations

### Part 4: Wrap-Up (5 min)
- Preview Week 3: Hair color + ancestry models
- Homework: Test model on family members' data

## Materials Needed
- `eye_color_training.csv` (500 samples)
- `week2_starter.py` template
- Slides: ML basics, Random Forest

## Success Criteria
✅ Students train a classifier  
✅ Students evaluate with test set  
✅ Students save/load models  
✅ Students understand accuracy metrics
