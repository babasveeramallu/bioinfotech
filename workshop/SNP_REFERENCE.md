# SNP Reference Sheet
## Key Genetic Markers for Trait Prediction

### Eye Color SNPs

| SNP ID | Gene | Chromosome | Position | Effect |
|--------|------|------------|----------|--------|
| **rs12913832** | HERC2 | 15 | 28365618 | **Most important for eye color** |
| | | | | GG = Brown eyes (dominant) |
| | | | | AG = Mixed (hazel/green) |
| | | | | AA = Blue/green eyes |
| rs1800407 | OCA2 | 15 | 28230318 | Modifies brown/blue |
| rs12896399 | SLC24A4 | 14 | 92773663 | Green vs blue distinction |
| rs16891982 | SLC45A2 | 5 | 33951693 | Pigmentation intensity |
| rs1393350 | TYR | 11 | 89011046 | Melanin production |
| rs12203592 | IRF4 | 6 | 396321 | Blue/green modifier |

**Biology**: The HERC2 gene regulates OCA2, which produces melanin in the iris. Less melanin = blue eyes, more melanin = brown eyes.

---

### Hair Color SNPs

| SNP ID | Gene | Chromosome | Position | Effect |
|--------|------|------------|----------|--------|
| **rs1805007** | MC1R | 16 | 89986117 | **Red hair variant** |
| | | | | T allele = red/blonde hair |
| rs1805008 | MC1R | 16 | 89985940 | Red hair variant |
| rs1805009 | MC1R | 16 | 89986144 | Red hair variant |
| rs1042602 | TYR | 11 | 89017961 | Blonde hair |
| rs2228479 | OCA2 | 15 | 28356859 | Brown/black hair |

**Biology**: MC1R (melanocortin 1 receptor) controls red/yellow pigment (pheomelanin) vs brown/black pigment (eumelanin). Variants cause red hair.

---

### Ancestry-Informative SNPs

| SNP ID | Gene | Chromosome | Position | Ancestry Signal |
|--------|------|------------|----------|-----------------|
| **rs1426654** | SLC24A5 | 15 | 48426484 | **European ancestry** |
| | | | | AA = European (light skin) |
| | | | | GG = African/Asian (dark skin) |
| rs3827760 | EDAR | 2 | 109513601 | East Asian ancestry |
| | | | | T allele = thick hair, shovel-shaped incisors |
| rs2814778 | DARC | 1 | 159174683 | African ancestry |
| | | | | T allele = malaria resistance |
| rs16891982 | SLC45A2 | 5 | 33951693 | European ancestry |
| rs12913832 | HERC2 | 15 | 28365618 | European ancestry (blue eyes) |

**Biology**: These SNPs show different frequencies across populations due to evolutionary adaptation to environment (UV exposure, disease resistance).

---

## Genotype Notation Guide

### Basic Notation
- **AA** = Homozygous (two copies of A allele)
- **AG** = Heterozygous (one A, one G)
- **GG** = Homozygous (two copies of G allele)

### Other Combinations
- **AC**, **AT**, **CT** = Heterozygous variants
- **CC**, **TT** = Homozygous variants

### Dominance
- **Dominant allele**: Shows effect even with one copy (e.g., brown eye allele)
- **Recessive allele**: Needs two copies to show effect (e.g., blue eye allele)

---

## How to Read Your Results

### Example Prediction Output
```
Eye Color: Hazel (75% confidence)
Hair Color: Brown (82% confidence)
Ancestry:
  European: 60%
  East Asian: 30%
  African: 10%
```

### Confidence Levels
- **High (>80%)**: Strong genetic signal, prediction likely accurate
- **Medium (60-80%)**: Moderate signal, some uncertainty
- **Low (<60%)**: Weak signal, prediction less reliable

### Why Predictions Aren't 100% Accurate
1. **Environment**: Sun exposure affects skin/hair color
2. **Epigenetics**: Gene expression changes over time
3. **Rare variants**: We only test common SNPs
4. **Polygenic traits**: Many genes contribute (we test subset)
5. **Mixed ancestry**: Complex genetic backgrounds

---

## Real-World Applications

### Medical Genetics
- Pharmacogenomics (drug response)
- Disease risk prediction
- Carrier screening

### Forensics
- Suspect identification from DNA
- Victim identification
- Cold case investigations

### Ancestry Testing
- 23andMe, AncestryDNA
- Family tree building
- Migration history

### Research
- Population genetics
- Evolutionary biology
- Personalized medicine

---

## Ethical Considerations

### Privacy Concerns
- Genetic data is permanent and identifiable
- Can reveal information about relatives
- Risk of discrimination (insurance, employment)

### Limitations
- Ancestry ≠ race (social construct)
- Predictions are probabilistic, not deterministic
- Don't use for medical decisions without doctor

### Responsible Use
- Informed consent for data collection
- Secure storage and encryption
- Transparent about limitations
- Respect genetic privacy

---

## Further Reading

### Scientific Papers
- "HIrisPlex: DNA-based eye and hair color prediction" (Walsh et al., 2013)
- "A genome-wide association study of skin pigmentation" (Sulem et al., 2007)
- "Genetic determinants of hair color" (Branicki et al., 2011)

### Databases
- **SNPedia**: snpedia.com - Wiki for SNPs
- **dbSNP**: ncbi.nlm.nih.gov/snp - NCBI SNP database
- **OpenSNP**: opensnp.org - Public genetic data

### Books
- "The Gene" by Siddhartha Mukherjee
- "She Has Her Mother's Laugh" by Carl Zimmer
- "The Social Life of DNA" by Alondra Nelson

---

## Quick Reference: Model Training Data

### Dataset Sizes (Recommended)
- Eye color: 500+ samples
- Hair color: 400+ samples
- Ancestry: 600+ samples

### Expected Accuracy
- Eye color: 80-90%
- Hair color: 75-85%
- Ancestry: 85-95%

### Training Time
- Random Forest (100 trees): 1-5 seconds
- Full pipeline: <1 minute

---

**Print this sheet and keep it handy during the workshop!**
