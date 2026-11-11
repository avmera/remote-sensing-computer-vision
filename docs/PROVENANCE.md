# Provenance and preparation

This publishing copy was prepared from four supplied academic notebooks and existing DIOR run artifacts. No training, inference, metric recomputation, dataset download, or expensive computation was performed. Original notebooks, weights, and other workspace files were not edited or removed.

## Source mapping

- `EuroSAT/ErouSat.ipynb` → `eurosat/01_features_and_classifiers.ipynb`
- `EuroSAT/transfer.ipynb` → `eurosat/02_transfer_learning.ipynb`
- `EuroSAT/decision_Fustion.ipynb` → `eurosat/03_decision_fusion.ipynb`
- `DIOR/Detection.ipynb` → `dior/01_yolo_detection.ipynb`

[source_manifest.json](source_manifest.json) records SHA-256 hashes of the unchanged originals. Each published source cell has an ID `source-NNN` corresponding to its original zero-based index; a new introductory markdown cell precedes them.

## Publishing edits

- Replaced machine-specific EuroSAT data paths with paths relative to `eurosat/`. Start notebook kernels in their project directory.
- Added the Keras imports needed by the first ANN section before their original later import location.
- Replaced in-notebook package installation commands with comments pointing to requirements files.
- Corrected the MobileNetV2 save filename to the `.weights.h5` suffix used by the fusion loader, and the CNN fusion load path to the training notebook's `dropout_weights/` directory.
- Passed the local `data.yaml` explicitly during DIOR validation so relocated checkpoints do not depend on embedded machine paths. This reconstructed config must be edited before use; it is not evidence of the original split.
- Removed machine/editor metadata, rich HTML representations, and ANSI terminal formatting. Sanitized local user paths in text outputs. Kept numerical outputs and PNG figures. Historical outputs have not been regenerated after code portability edits.
- Extracted existing plot images directly from notebook outputs, and copied selected DIOR CSV / plot evidence. Sanitized `save_dir` in copied training arguments. CSV values and image pixels are unchanged.
- Excluded model weights, cached arrays, pickled scalers, train-batch montages, redundant validation batches, and incomplete `train_scratch2` artifacts. The supplementary `train_scratch` evidence is explicitly separated from verified notebook comparisons.

## Evidence limitations

Notebooks preserve code and outputs from interactive sessions, which can disagree after edits or out-of-order execution. In particular, the color ANN's current source tracks and saves the best fold, but its saved output only prints the earlier best-fold summary. DIOR class-count output also reflects a different mapping from the current preceding cell. Source and saved-output evidence are described separately where they conflict.

The project READMEs document data leakage, incomplete split provenance, missing checkpoints, preprocessing mismatches, validation population differences, and the absence of a verified feature-fusion experiment. These limitations were not silently corrected because doing so would change the experimental methodology and invalidate correspondence to the historical outputs.

## Validation performed

Offline checks validate notebook schema and Python cell syntax (without execution), documentation links, original source hashes, preserved notebook cell count / order, selected numerical evidence, and publication exclusions. Notebook export to HTML provides an additional rendering smoke check. Full end-to-end reproduction is not claimed: datasets and required EuroSAT weights are unavailable, and no training was authorized for this preparation.

## Attribution

Dataset background is sourced from the [EuroSAT authors](https://github.com/phelber/EuroSAT) and the [DIOR paper](https://arxiv.org/abs/1909.00133). All portfolio performance values come from supplied notebook outputs, not published dataset benchmark scores. Existing example imagery and plots remain subject to applicable dataset terms. No blanket license has been applied to third-party data or assets.
