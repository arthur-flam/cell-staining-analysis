# Laminin Analysis Notebook

Semi-automated pipeline for inspecting GP-16 astrocyte laminin organization from multiplexed fluorescence images. The aim is to keep one reproducible place for exploratory notebooks, small scripts, and the data exports used in internal figures.

## Repository layout
- `main.py` – quick CLI entry point for batch processing and CSV generation.
- `notebook.ipynb` – scratchpad notebook containing plots and sanity checks.
- `cells.csv`, `laminin_intensity_outliers.*` – derived measurements used for QC and threshold tuning.
- `outputs/` – intermediate exports (saved figures, masks, feature tables).
- `acel13521-fig-0004-m.jpg` – reference micrograph for the GP-16 laminate condition.

## Workflow highlights
1. Organize raw confocal fields by sample → field → fluorophore.
2. Run `uv run python main.py /path/to/data` to generate per-cell measurements.
3. Inspect `cells.csv` for global intensity trends and flag outliers.
4. Iterate inside `notebook.ipynb` to refine segmentation thresholds, morphology descriptors, and narrative figures.

## Environment
```
uv sync
pip install -e .  # optional, if you need editable local imports
```
> Note: SAM2 from Meta Research is an optional dependency; install it separately when running advanced segmentation experiments.

## Data handling
- DAPI (nuclei, blue), Laminin β1 (membranes, green), GFAP (astrocytes, red).
- Images are assumed to be non-overlapping across fields; overlapping captures must be cropped before analysis.
- Keep any human or animal identifiers out of file names to preserve anonymity.

## Citation
If this repository supports a manuscript or presentation, please cite it explicitly (update the date/version if you rely on a different snapshot).

> Arthur Flam. (2025). *Laminin Analysis Notebook* (Version 0.1.0) [Computer software]. GitHub. https://github.com/arthur-flam/cell-staining-analysis. Accessed November 16, 2025.

### BibTeX
```
@software{flam_laminin_analysis_2025,
  author  = {Arthur Flam},
  title   = {Laminin Analysis Notebook},
  year    = {2025},
  version = {0.1.0},
  url     = {https://github.com/arthur-flam/cell-staining-analysis},
  note    = {GP-16 astrocyte laminin quantification pipeline},
  urldate = {2025-11-16}
}
```

## Personal license grant
The copyright holder hereby grants **Elisa Gozlan** a perpetual, worldwide, non-transferable, non-sublicensable license to use, modify, and adapt this repository for her personal research work. No other party may exercise these rights without prior written authorization. Redistribution in any form requires explicit approval from the copyright holder.

## General reservation of rights
Except for the personal license specified above, all rights are reserved. The software is provided “as is” without warranty of any kind, express or implied. The author assumes no liability for any damages arising from use, misuse, or inability to use this material.
