# Instructor Guide
## Teaching Tips & Best Practices

### Pre-Workshop Preparation

#### 1 Week Before
- [ ] Test all code on fresh Python environment
- [ ] Generate training datasets (run `data/generate_datasets.py`)
- [ ] Create models directory: `mkdir models`
- [ ] Prepare demo SNP file with your own data (optional)
- [ ] Review biology concepts (HERC2, MC1R genes)

#### 1 Day Before
- [ ] Test projector/screen sharing
- [ ] Have backup USB with all files
- [ ] Print handouts (SNP reference sheet)
- [ ] Prepare ice breaker activity

### Week-by-Week Teaching Strategy

## Week 1: Data Pipeline

### Opening (First 10 minutes)
**Ice Breaker**: "What trait would you want to predict about yourself?"
- Gets students thinking about genetics personally
- Reveals their interests (eye color, ancestry, health)

### Common Student Questions
**Q: "Why do we use CSV files instead of real DNA sequences?"**
A: "Real DNA files (FASTA/FASTQ) are huge (gigabytes). SNP data is pre-processed and compact. Think of it like using a summary instead of reading the entire book."

**Q: "What if I don't have my own genetic data?"**
A: "We'll use simulated data that's statistically realistic. You can also download free data from OpenSNP.org if you're curious."

### Live Coding Tips
- Type slowly and explain each line
- Make intentional mistakes and debug together
- Use print() statements liberally to show intermediate results

### Troubleshooting
**Issue**: Students get "FileNotFoundError"
**Fix**: Check working directory with `import os; print(os.getcwd())`

**Issue**: Pandas not installed
**Fix**: `pip install pandas` (have this ready on slides)

---

## Week 2: Machine Learning

### Opening Hook
Show this comparison:
- "Traditional programming: Rules + Data → Answers"
- "Machine learning: Data + Answers → Rules"

### Explaining Random Forest
**Analogy**: "Imagine asking 100 doctors for a diagnosis. Each doctor looks at different symptoms. The majority opinion is usually right."

### Common Student Questions
**Q: "Why Random Forest and not neural networks?"**
A: "Random Forests are interpretable - we can see which SNPs matter most. Neural networks are 'black boxes'. For genetics, explainability is crucial."

**Q: "Why is accuracy only 85%?"**
A: "Genetics is probabilistic, not deterministic. Environment matters (sun exposure for skin/hair). Also, we're using only 6 SNPs - real tests use 20+."

### Activity Variation
**For Advanced Students**: "Try changing n_estimators from 100 to 10. What happens to accuracy?"

**For Struggling Students**: Provide pre-filled feature extraction code, focus on understanding train/test split.

### Troubleshooting
**Issue**: Model accuracy is 50% (random guessing)
**Fix**: Check genotype encoding - make sure AA=0, AG=1, GG=2 is consistent

---

## Week 3: Multi-Trait Models

### Opening Discussion
"Last week we predicted one trait. Today we're building a complete genetic profile. What ethical concerns come to mind?"

Let students brainstorm before showing ethics slides.

### Ancestry Discussion (Handle Sensitively)
**Key Points**:
- Ancestry ≠ race (race is social construct)
- Genetic variation is continuous, not discrete
- More genetic diversity within Africa than all other continents combined
- Use terms: "continental ancestry" not "race"

**If Student Asks About "Racial Differences"**:
"Genetic differences between populations are tiny (0.01%) and mostly about adaptation to environment (skin color, lactose tolerance). There's no genetic basis for social categories of race."

### Common Student Questions
**Q: "Can we predict intelligence or personality?"**
A: "Those traits are highly polygenic (thousands of genes) and heavily environmental. Current science can't reliably predict them. Be skeptical of companies claiming otherwise."

### Activity: Ethics Debate
Split class into groups:
- Group A: Benefits of genetic prediction (medical, ancestry)
- Group B: Risks (privacy, discrimination, eugenics)
- 10-minute debate

---

## Week 4: GUI Development

### Opening Demo
Show a badly designed GUI vs. your polished one. Ask: "What makes the good one better?"
- Clear labels
- Logical layout
- Visual feedback
- Error messages

### Common Student Questions
**Q: "Why tkinter and not a web app?"**
A: "Tkinter is built-in (no setup), runs locally (privacy), and teaches GUI fundamentals. You can convert to Flask later!"

**Q: "Can I customize the colors/layout?"**
A: "Absolutely! That's the fun part. Try changing bg='#f0f0f0' to your favorite color."

### Demo Day Structure
- Each student gets 2 minutes
- Show: Input → Prediction → Confidence
- Peer feedback: One thing they liked

### Troubleshooting
**Issue**: GUI window doesn't appear
**Fix**: Check if `root.mainloop()` is called

**Issue**: Button click does nothing
**Fix**: Verify `command=self.function_name` (no parentheses!)

---

## General Teaching Tips

### Pacing
- **Too Fast**: Students typing frantically, not understanding
- **Too Slow**: Students browsing phones, getting bored
- **Just Right**: Students finish code 30 seconds before you move on

### Engagement Strategies
1. **Cold Calling (Gently)**: "Sarah, what do you think this line does?"
2. **Think-Pair-Share**: "Take 1 minute to discuss with your neighbor"
3. **Live Polls**: "Raise hand if your model got >80% accuracy"

### Handling Different Skill Levels
**Beginner Students**:
- Provide more starter code
- Pair with advanced student
- Focus on concepts over syntax

**Advanced Students**:
- Give bonus challenges
- Ask them to help debug others' code
- Suggest extensions (add new traits)

### When Students Are Stuck
1. Ask: "What error message do you see?"
2. Ask: "What did you expect to happen?"
3. Ask: "What actually happened?"
4. Guide them to solution, don't give answer immediately

### Celebrating Success
- Applaud when someone's model trains successfully
- Screenshot and share cool predictions
- Give certificates at end of Week 4

---

## Emergency Backup Plans

### If Code Doesn't Work
- Have pre-trained models ready to load
- Use Google Colab as backup (cloud-based)
- Pair programming: 2 students per computer

### If Time Runs Short
**Week 1**: Skip visualization, focus on loading data
**Week 2**: Provide pre-trained model, focus on evaluation
**Week 3**: Skip ancestry, do only hair color
**Week 4**: Provide complete GUI, students customize colors

### If Time Runs Long
**Week 1**: Add chromosome visualization
**Week 2**: Explore feature importance
**Week 3**: Add more traits (skin color)
**Week 4**: Add export to PDF feature

---

## Assessment Ideas

### Formative (During Workshop)
- Quick polls: "What does this function do?"
- Code reviews: Students explain their code
- Debugging challenges: Fix intentional errors

### Summative (End of Workshop)
- Working GUI demo
- Short presentation: "What I learned"
- GitHub repository with documented code

### Grading Rubric (If Needed)
- Code functionality: 40%
- Code documentation: 20%
- Presentation/demo: 20%
- Creativity/extensions: 20%

---

## Resources for You

### Biology Background
- Khan Academy: Genetics playlist
- NIH Genetics Home Reference
- "The Gene" by Siddhartha Mukherjee (book)

### Machine Learning
- scikit-learn documentation
- "Hands-On Machine Learning" by Aurélien Géron
- StatQuest YouTube channel (Josh Starmer)

### Ethics
- "The Social Life of DNA" by Alondra Nelson
- ASHG position statements on genetic ancestry
- GINA (Genetic Information Nondiscrimination Act)

---

## Student Feedback Form

After Week 4, ask students:
1. What was the most interesting thing you learned?
2. What was the most challenging part?
3. What would you add to this workshop?
4. Would you recommend this to a friend? (1-10)
5. Any other comments?

Use feedback to improve next iteration!
