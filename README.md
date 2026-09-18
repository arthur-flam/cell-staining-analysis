# Lamin B1 Analysis Notebook

Semi-automated pipeline for measuring Lamin B1 in GP-16 astrocytes from DAPI and Lamin B1 fluorescence images. Lamin B1 is a nuclear lamina protein and cellular senescence marker. The notebook and derived exports support exploratory analysis and internal figures.

## Repository layout
- `main.py` – placeholder CLI; the analysis workflow is in the notebook.
- `notebook.ipynb` – scratchpad notebook containing plots and sanity checks.
- `cells.csv`, `lamin_b1_intensity_outliers.csv` – derived measurements used for QC and threshold tuning (generated locally; not tracked by Git).
- `outputs/` – intermediate exports (saved figures, masks, feature tables).
- `acel13521-fig-0004-m.jpg` – reference micrograph for the GP-16 laminate condition.

## Workflow highlights
1. Organize raw confocal fields by sample → field, with `Lamin B1.tif` and `dapi.tif` in each field directory. Set `LAMIN_B1_IMAGES_DIR` to the parent sample directory (or use the default `data/`). The raw image dataset is not tracked by this repository.
2. Run the notebook to generate per-cell measurements.
3. Inspect `cells.csv` for global intensity trends and flag outliers.
4. Iterate inside `notebook.ipynb` to refine segmentation thresholds, morphology descriptors, and narrative figures.

## Environment
```
uv sync
uv run python -m unittest discover -s tests -v
```
Open `notebook.ipynb` in a Jupyter-capable editor with `.venv/bin/python` as its kernel. Configure `LAMIN_B1_IMAGES_DIR` in that kernel's environment before running the notebook, or place the data in `data/`.

> Note: SAM2 from Meta Research is an optional dependency; install it separately when running advanced segmentation experiments.

## Data handling
- DAPI (nuclei, blue) and Lamin B1 (nuclear lamina, green) are the only stains used. The RGB image passed to Cellpose contains these two signals; its unused red plane is zero.
- The TIFFs contain three planes; the notebook reads plane 1 from `Lamin B1.tif` and plane 2 from `dapi.tif` (zero-based indexing). Verify these plane assignments for a different acquisition/export format.
- Regenerate locally saved tables and figures before citing them; older ignored exports are not updated by Git changes.
- Images are assumed to be non-overlapping across fields; overlapping captures must be cropped before analysis.
- Keep any human or animal identifiers out of file names to preserve anonymity.

## Citation
If this repository supports a manuscript or presentation, please cite it explicitly (update the date/version if you rely on a different snapshot).

> Arthur Flam. (2025). *Lamin B1 Analysis Notebook* (Version 0.1.0) [Computer software]. GitHub. https://github.com/arthur-flam/cell-staining-analysis. Accessed November 16, 2025.

### BibTeX
```
@software{flam_lamin_b1_analysis_2025,
  author  = {Arthur Flam},
  title   = {Lamin B1 Analysis Notebook},
  year    = {2025},
  version = {0.1.0},
  url     = {https://github.com/arthur-flam/cell-staining-analysis},
  note    = {GP-16 astrocyte Lamin B1 quantification pipeline},
  urldate = {2025-11-16}
}
```

## Personal license grant
The copyright holder hereby grants **Elisa Gozlan** a perpetual, worldwide, non-transferable, non-sublicensable license to use, modify, and adapt this repository for her personal research work. No other party may exercise these rights without prior written authorization. Redistribution in any form requires explicit approval from the copyright holder.

## General reservation of rights
Except for the personal license specified above, all rights are reserved. The software is provided “as is” without warranty of any kind, express or implied. The author assumes no liability for any damages arising from use, misuse, or inability to use this material.
