# Workshop Slides Outline

## Week 1: Data Pipeline & SNP Basics

### Slide 1: Title
- DNA Trait Predictor Workshop
- Week 1: Understanding Genetic Data

### Slide 2: What is DNA?
- 4 bases: A, T, C, G
- 3 billion base pairs in human genome
- 99.9% identical between humans

### Slide 3: What are SNPs?
- Single Nucleotide Polymorphisms
- The 0.1% that makes us unique
- Example: Position 123456 - Person A has 'A', Person B has 'G'

### Slide 4: SNPs and Traits
- Some SNPs affect visible traits
- rs12913832: The "blue eye SNP"
- Located in HERC2 gene near OCA2

### Slide 5: Genotype Notation
- AA = homozygous (two A's)
- AG = heterozygous (one A, one G)
- GG = homozygous (two G's)

### Slide 6: CSV Data Format
```
rsid,chromosome,position,genotype
rs12913832,15,28365618,AG
rs1800407,15,28230318,GG
```

### Slide 7: Today's Goals
- Load SNP data from CSV
- Filter by chromosome/position
- Visualize genotype distributions

### Slide 8: Live Demo
- Show final working app
- Input SNPs → Get predictions

---

## Week 2: Eye Color ML Model

### Slide 1: Machine Learning Basics
- Teaching computers to find patterns
- Supervised learning: Learn from examples
- Input (SNPs) → Output (eye color)

### Slide 2: Random Forest Intuition
- Multiple decision trees "voting"
- Each tree asks: "Is rs12913832 = GG?"
- Majority vote wins

### Slide 3: Train/Test Split
- 80% data for training
- 20% data for testing
- Never test on training data!

### Slide 4: Eye Color Genetics
- 6 key SNPs determine eye color
- rs12913832 (HERC2) is most important
- GG = brown, AA = blue, AG = mixed

### Slide 5: Accuracy Metrics
- 85% accuracy is good for genetics
- Why not 100%? Environment, epigenetics, rare variants

### Slide 6: Confusion Matrix
```
           Predicted
           Blue  Brown
Actual Blue  45    5
      Brown   5   45
```

### Slide 7: Model Persistence
- Save trained model with pickle
- Load once, predict many times
- No need to retrain

---

## Week 3: Multi-Trait Models

### Slide 1: Hair Color Genetics
- MC1R gene = "red hair gene"
- Variants in rs1805007/8/9
- 4 classes: black, brown, blonde, red

### Slide 2: Ancestry Prediction
- Population genetics
- Ancestry-informative markers (AIMs)
- Continental groups, not "race"

### Slide 3: Confidence Scores
- Probability distribution
- High (>80%), Medium (60-80%), Low (<60%)
- Show uncertainty to users

### Slide 4: Ethics in Genetics
- Privacy concerns
- Genetic discrimination
- Limitations of predictions
- Responsible data use

### Slide 5: Why Ancestry ≠ Race
- Genetic variation is continuous
- More variation within groups than between
- Social construct vs biological reality

---

## Week 4: GUI & Deployment

### Slide 1: User Experience Principles
- Simple, intuitive interface
- Clear input/output
- Error handling

### Slide 2: tkinter Basics
- Built-in Python GUI library
- Widgets: Label, Entry, Button
- Layout: pack(), grid()

### Slide 3: File Upload Pattern
- filedialog.askopenfilename()
- Parse CSV
- Populate fields

### Slide 4: Visual Feedback
- Color coding (green/yellow/red)
- Progress indicators
- Confidence bars

### Slide 5: Demo Day Tips
- Test with real data
- Handle edge cases
- Explain limitations

### Slide 6: Next Steps
- Add more traits (height, lactose intolerance)
- Web version with Flask
- Integrate 23andMe parser
- Share on GitHub

---

## Bonus Slides

### Biology Deep Dives
- HERC2/OCA2 gene interaction
- MC1R protein structure
- Population migration patterns

### Technical Deep Dives
- Feature engineering techniques
- Hyperparameter tuning
- Cross-validation

### Career Paths
- Bioinformatics
- Computational biology
- Genetic counseling
- Data science in healthcare

### Resources
- OpenSNP.org
- HIrisPlex research papers
- scikit-learn documentation
- Genetics textbooks
