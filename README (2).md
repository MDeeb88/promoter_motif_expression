# Bioinformatic Analysis of the Relationship Between Promoter Motifs and Gene Expression Levels

## Project Overview

This project investigates the relationship between promoter motif composition and gene expression levels using bioinformatic and statistical approaches.

Promoter regions contain transcription factor binding motifs that contribute to transcriptional regulation. By constructing a promoter motif matrix and integrating gene expression data, regression models were applied to evaluate whether promoter motif patterns can predict transcriptional activity.

---

# Objectives

The main objectives of this project were:

1. Extract promoter-associated motif information from genomic data.
2. Construct a promoter motif feature matrix.
3. Integrate promoter motif data with gene expression measurements.
4. Evaluate the relationship between promoter motifs and expression using regression models.
5. Validate the biological relevance of the observed relationships.

---

# Methods

## Data Processing

- Promoter motif data were extracted from motif scanning outputs.
- Gene expression values were obtained as TPM measurements.
- Promoter IDs were mapped to corresponding gene IDs.
- Expression values were normalized using log2(TPM + 1).

Normalization formula:

y = log2(TPM + 1)

---

## Feature Matrix Construction

A promoter motif matrix was generated where:

- Rows correspond to promoter regions
- Columns correspond to transcription factor motifs
- Values represent motif-associated scores/features

---

## Regression Models

The following regression models were evaluated:

- Linear Regression
- Ridge Regression
- Elastic Net Regression

Performance metrics:

- Pearson correlation
- Spearman correlation
- R² score
- RMSE

---

# Results

## Regression Performance

| Model | Pearson | Spearman | R² | RMSE |
|---|---|---|---|---|
| Linear Regression | 0.602 | 0.639 | 0.361 | 2.038 |
| Ridge Regression | 0.605 | 0.641 | 0.365 | 2.032 |
| Elastic Net | 0.604 | 0.638 | 0.363 | 2.034 |

The Ridge Regression model achieved the best overall performance.

The results demonstrate a moderate relationship between promoter motif composition and gene expression levels.

---

## Validation Using Shuffled Data

To test whether the observed relationships were biologically meaningful, expression values were randomly shuffled and the regression analysis was repeated.

### Shuffled Results

- Pearson correlation: -0.008
- Spearman correlation: -0.024

After randomization, correlations collapsed to nearly zero, indicating that the original predictive signal was not random.

This supports the hypothesis that promoter motif composition contributes to transcriptional regulation.

---

# Biological Interpretation

The analysis suggests that transcription factor motifs located in promoter regions contain biologically relevant regulatory information associated with gene expression.

However, promoter motifs alone do not fully explain transcriptional activity. Additional regulatory mechanisms likely contribute to expression variability, including:

- Chromatin accessibility
- Epigenetic modifications
- Enhancer interactions
- Post-transcriptional regulation

The moderate predictive performance is consistent with the complex and multifactorial nature of gene regulation.

---

# Repository Structure

```text
project/
├── notebooks/
│   └── 02_promoter_motif_regression_new_matrix.ipynb
├── data/
├── results/
└── README.md
```

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

# Conclusion

This project demonstrates that promoter motif composition is associated with transcriptional activity and can partially predict gene expression levels using statistical modeling approaches.

The validation analysis confirmed that the detected relationships are biologically meaningful rather than random artifacts.

The workflow provides a reproducible computational framework for studying promoter architecture and transcriptional regulation.

---

# Author

Bioinformatics project developed for computational analysis of promoter motifs and gene expression regulation.
