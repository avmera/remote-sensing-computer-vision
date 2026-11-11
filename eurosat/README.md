# EuroSAT — Land Use / Land Cover Classification

**Objective:** compare handcrafted image representations and learned visual features for classifying optical satellite image patches, then explore combining model decisions.

The [EuroSAT dataset](https://github.com/phelber/EuroSAT) was introduced by Helber et al., *EuroSAT: A Novel Dataset and Deep Learning Benchmark for Land Use and Land Cover Classification* (2019). This implementation reads the RGB image version, with saved outputs confirming 27,000 images of shape 64 × 64 × 3. It does not use all 13 Sentinel-2 bands.

Classes: AnnualCrop, Forest, HerbaceousVegetation, Highway, Industrial, Pasture, PermanentCrop, Residential, River, and SeaLake.

## Notebook guide

1. [Features and classifiers](01_features_and_classifiers.ipynb): exploration, HOG / Gabor / color extraction, SVM and KNN baselines, ANN experiments, and CNNs with and without dropout.
2. [Transfer learning](02_transfer_learning.ipynb): ImageNet MobileNetV2 with a frozen backbone, followed by a separately initialized experiment that unfreezes its final 20 layers.
3. [Decision fusion](03_decision_fusion.ipynb): load three trained models; compare majority vote and mean probability predictions on a sampled collection of images.

## Methodology

**Handcrafted representations.** OpenCV loads and resizes images to 64 × 64. HOG uses grayscale, 9 orientations, 8 × 8 pixel cells, and 2 × 2 cell blocks, producing 1,764 values. Gabor extraction applies 24 kernels (8 orientations × wavelengths 4, 8, 12), with 11 × 11 support, sigma 4, gamma 0.5, phase 0; response means and standard deviations produce 48 values. RGB color moments compute mean, standard deviation, and skewness per channel, producing 9 values.

Gabor extraction and visualization are implemented, but no Gabor classifier result or concatenated feature-fusion experiment is present. These are not claimed as evaluated methods.

**Classical and dense models.** HOG and color moments feed RBF SVMs (`C=10`, `gamma='scale'`, probability enabled), distance-weighted Euclidean KNN (`k=5`), and ANNs. The color ANN has 256 / 128 hidden units; the HOG ANN has 512 / 256. Both use batch normalization, dropout 0.3, Adam at 0.001, categorical cross-entropy, batch size 64, up to 80 epochs, and early stopping on validation loss with patience 10. Evaluation uses shuffled stratified three-fold CV with seed 42.

**CNNs.** Three Conv2D / max-pooling blocks with 32, 64, and 128 filters feed a 128-unit dense layer and a 10-class softmax. An alternate model adds dropout 0.5. Images remain OpenCV BGR and are scaled by 1/255. Adam uses 0.0008. The notebook includes a stratified 80/20 split (10 epochs, batch 64), then separate three-fold generator experiments (10 epochs, batch 32).

**Transfer learning.** Directory generators read RGB images resized to 128 × 128 and scale by 1/255. The classification head is global average pooling → Dense(256) → batch normalization → dropout 0.3 → softmax. The frozen ImageNet backbone trains for 5 epochs with Adam 0.001, batch 64. The second experiment constructs a fresh ImageNet backbone, trains its final 20 layers and head for 10 epochs at 0.00001, batch 32. It does not continue the first model's trained head. Saved directory counts are 17,280 training, 4,319 validation, and 5,400 test images; their sum is 26,999, and the one-image discrepancy cannot be resolved from the supplied files.

## Recorded results

Values below are copied from saved outputs; four-decimal values are rounded from printed metrics, and two-decimal classification-report values retain their original precision. Source cell indices are zero-based, before the added introductory cell; matching notebook IDs are `source-NNN`.

### Handcrafted models: selected best fold, not CV means

| Model | Input | Accuracy | Weighted F1 | Source cell |
|---|---|---:|---:|---:|
| SVM | RGB color moments | 0.8101 | 0.8074 | 26 |
| SVM | HOG | 0.7443 | 0.7443 | 30 |
| KNN | RGB color moments | 0.7510 | 0.7474 | 34 |
| KNN | HOG | 0.4202 | 0.3673 | 38 |
| ANN | RGB color moments | 0.8478 | 0.8461 | 43 |
| ANN | HOG | 0.7332 | 0.7311 | 48 |

Each selected fold has 9,000 validation images. Fold selection uses weighted F1. Feature scaling is fit on the entire dataset before splitting, so these estimates contain preprocessing leakage and should not be treated as unbiased generalization scores.

### Image models: separate evaluation protocols

| Experiment | Reported accuracy | Evaluation | Source notebook / cell |
|---|---:|---|---|
| CNN, no dropout | 0.81 | 5,400-image holdout also used during training validation | Features / 57 |
| CNN, dropout | 0.83 | Same holdout used for early stopping | Features / 63 |
| CNN, no dropout | 0.83 | Report for selected CV fold; 9,000 images | Features / 81 |
| CNN, dropout | 0.87 | Report for selected CV fold; 9,000 images | Features / 90 |
| MobileNetV2, frozen backbone | 0.90 | Separate 5,400-image test directory | Transfer / 6 |
| MobileNetV2, final 20 layers trainable | 0.91 | Separate 5,400-image test directory | Transfer / 14 |

CNN best-epoch validation accuracies of 0.8429 (no dropout) and 0.8737 (dropout) are also printed in cells 77 and 86. They differ from the classification-report measurements: the no-dropout notebook saves final-epoch weights, and the generators use floor-divided validation steps during fitting. Do not substitute peak epoch accuracy for the saved-model report.

![MobileNetV2 confusion matrix from the original saved output](figures/mobilenet_confusion_0.png)

### Decision fusion: exploratory sample, not a held-out benchmark

Source: decision-fusion cell 12, 500 randomly sampled images from the full 27,000-image directory, without a fixed sampling seed or enforced exclusion of training images.

| Predictor | Sample accuracy |
|---|---:|
| MobileNetV2 | 0.520 |
| CNN | 0.914 |
| ANN + color moments | 0.234 |
| Majority vote | 0.590 |
| Mean probabilities | 0.678 |

The ensemble underperforms the CNN on this sample. The training notebook uses **RGB** color moments, while the fusion notebook computes **HSV** moments. MobileNetV2 training reads **RGB**, while fusion supplies OpenCV **BGR**. These mismatches are preserved and are plausible contributors to degraded predictions, not proven causal explanations. The sampled majority-vote metric uses raw `argmax` voting (lowest class index breaks ties); it does not evaluate the separately defined probability-based tie-break rule used by the single-image demonstration.

## Reproduce or inspect

Start Jupyter from `eurosat/` after installing `requirements.txt`. Obtain EuroSAT RGB from the official project and arrange:

```text
eurosat/
  data/EuroSAT/AnnualCrop/*.jpg   # all ten class directories
  training/<class>/*.jpg         # externally prepared transfer-learning split
  testing/<class>/*.jpg
```

For notebook 01, an already populated `data/` skips ZIP extraction; otherwise place `EuroSAT.zip` under `data/` and ensure the extracted classes end up in `data/EuroSAT/`. Verify the layout before continuing. Notebook 02 requires the separately prepared training/testing directories. Their creation code and file membership were not supplied; regenerating a split produces a new experiment, not an exact historical reproduction.

Notebook 03 requires `mobilenet_best_weights.weights.h5`, `ann_color_best_weights.weights.h5`, `dropout_weights/dropout_fold_1.weights.h5`, and `cm_scaler.pkl`. The original scaler exists locally but is excluded as a generated serialized object; its fit provenance is not established by the notebook. The required neural-network checkpoints were absent from the supplied EuroSAT folder. Historical outputs remain readable, but inference cannot be reproduced from this checkout alone. A future corrected experiment must align preprocessing and persist its scaler and split membership together; do not silently reinterpret the recorded results as corrected results.

Read cells before execution: the notebooks train models and write checkpoints. Portability edits add missing early ANN imports and correct weight filenames / paths, without changing feature definitions, splits, architecture, or training settings. No training was performed for publication.

## Interpretation for Earth Observation

The experiments exercise patch-level land-cover recognition, feature representation, and class-specific error analysis. They do not assess geographic transfer, spatially independent splits, multispectral inputs, SAR imagery, or GIS-ready prediction layers. Those are follow-up research directions, not delivered capabilities.
