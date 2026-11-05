# Grid-relevant disclosure audit

Reproduction code for *Public disclosures cannot verify renewable electricity claims by hyperscale data-center operators* by Tina Vartziotis, Lisa Thalheimer, and Francesca Dominici.

The audit identifies missing and incomplete disclosure across five information requirements: data-center electricity quantity, spatial attribution, time-based alignment, boundary clarity, and renewable-electricity accounting transparency. Scores summarize disclosure coverage; interpret them alongside each company's dimension-level profile.

## Reproduce

Use Python 3.12. From the repository root:

```sh
python -m pip install -r requirements.txt
python reproduce.py
```

The command generates PDF/PNG versions of the methodology diagram, main disclosure matrix, minimum-information coverage figure, and supplementary granularity figure in `plots/`. It also writes the five-dimension scores and Partial-weight sensitivity table as CSV files.

Tested with Python 3.12.8, matplotlib 3.11.1, numpy 2.5.2, and pandas 3.0.5.

## Files and data

- `code/`: three plotting notebooks and the methodology-diagram script.
- `data/disclosure_coding.csv`: the derived coding table used by the figures. It includes company reporting periods and source titles. This table is sufficient to reproduce the outputs here; it is not the full source-evidence dataset or a substitute for the corporate reports.
- `reproduce.py`: runs the figures and calculates scores and sensitivity values without Jupyter.
- `requirements.txt`: package requirements.

The notebooks can also be run from the repository root or `code/`. Figure typography uses Arial when available and may differ on other systems.

## Coding version

This is the final coding used in the submitted manuscript. All 50 coded items were coded independently by two human coders (T.V. and L.T., the second coder blind to the first coding). Before reconciliation the coders agreed on 40 of 50 items (80%; Cohen's kappa 0.64; Gwet's AC1 0.72). The 10 disagreements were resolved by consensus in November 2026. Relative to the earlier single-coder version, three cells changed to Yes: Google's renewable-electricity accounting transparency, and Meta's and Apple's boundary clarity. At Partial = 0.5, the scores are Google 3.5, Microsoft 4.0, Amazon 1.0, Meta 4.0, and Apple 4.0. Region-resolved electricity remains a separate descriptive metric.

The manuscript uses a source-selection cutoff of 10 August 2026 and retains each company's disclosed reporting period. This repository does not include confidential material, manuscript files, review comments, or corporate PDF copies.

## Primary reports

- [Google 2026 Environmental Report](https://sustainability.google/reports/)
- [Microsoft 2026 Environmental Data Fact Sheet](https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/msc/documents/presentations/CSR/2026-Microsoft-Environmental-Data-Fact-Sheet-PDF.pdf)
- [Amazon 2025 Sustainability Report](https://sustainability.aboutamazon.com/2025-amazon-sustainability-report.pdf) and [Renewable Energy Methodology](https://sustainability.aboutamazon.com/renewable-energy-methodology.pdf)
- [Meta 2025 Sustainability Report](https://sustainability.atmeta.com/wp-content/uploads/2025/08/Meta_2025-Sustainability-Report_.pdf) and [Environmental Data Index](https://sustainability.atmeta.com/wp-content/uploads/2025/10/Meta_2025-Environmental-Data-Index.pdf)
- [Apple Environmental Progress Report 2026](https://www.apple.com/environment/pdf/Apple_Environmental_Progress_Report_2026.pdf)

The version used for the article (v1.0.0), together with the complete Supplementary Data 1, is archived at Zenodo: https://doi.org/10.5281/zenodo.23983022

## License

Code and associated software documentation: [MIT](LICENSE). Original structured data and authored dataset annotations: [CC BY 4.0](data/LICENSE-CC-BY-4.0.txt). Corporate source documents and other third-party material retain their respective rights.
