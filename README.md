# Remote Sensing Computer Vision

Two undergraduate Computer Vision course projects applying **machine learning and deep learning to remote sensing imagery**. The work explores land-cover classification with EuroSAT and object detection with DIOR, from image preparation and feature extraction to model training and evaluation.

## Projects

### EuroSAT — Land Use / Land Cover Classification

Classify **27,000 RGB satellite image patches across 10 land-cover classes** using handcrafted features and neural networks.

- Extract and visualize HOG features, Gabor filter responses, and color moments.
- Train SVM, KNN, and ANN classifiers using HOG and color moments.
- Explore CNNs with and without dropout, MobileNetV2 transfer learning, and decision fusion.
- Evaluate predictions using accuracy, precision, recall, F1 scores, and confusion matrices.

**Recorded highlights:** MobileNetV2 achieved approximately **90% accuracy with a frozen backbone** and **91% with partial fine-tuning** on a 5,400-image test directory.

[Explore the EuroSAT project →](eurosat/README.md)

### DIOR — Object Detection in Remote Sensing Imagery

Detect objects in optical remote sensing imagery using **YOLOv8n and YOLOv8s**, with coursework experiments on an **800-image DIOR subset**.

- Convert XML bounding-box annotations to YOLO format.
- Prepare training, validation, and test subsets.
- Fine-tune pretrained detectors with full-network and partially frozen configurations.
- Inspect precision–recall curves, confusion matrices, and detection visualizations.

**Recorded highlight:** YOLOv8s with the first 10 modules frozen achieved **0.5339 mAP@0.50** and **0.3443 mAP@0.50:0.95** on 120 validation images. Reported class coverage and evaluation populations vary across runs; details accompany the project results.

[Explore the DIOR project →](dior/README.md)

## Technologies

- **Language and notebooks:** Python, Jupyter Notebook
- **Machine learning:** scikit-learn, SVM, KNN
- **Deep learning:** TensorFlow, Keras, PyTorch, Ultralytics YOLO
- **Image processing and analysis:** OpenCV, scikit-image, NumPy, SciPy, Pandas
- **Visualization:** Matplotlib, Seaborn

## Repository Structure

```text
remote-sensing-computer-vision/
├── eurosat/
│   ├── README.md
│   ├── 01_features_and_classifiers.ipynb
│   ├── 02_transfer_learning.ipynb
│   ├── 03_decision_fusion.ipynb
│   ├── requirements.txt
│   └── figures/
├── dior/
│   ├── README.md
│   ├── 01_yolo_detection.ipynb
│   ├── data.yaml
│   ├── requirements.txt
│   └── evidence/
├── docs/
├── tools/
├── .gitignore
├── .gitattributes
└── README.md
```

## Exploring the Projects

Start with the project READMEs, then open the notebooks to view the implementations, saved outputs, and visualizations. Each project includes dependencies and dataset setup instructions for running experiments locally.

Results are from the original coursework experiments and have not been independently reproduced. Evaluation settings may differ between experiments; brief qualifications accompany the relevant results.

Datasets and trained model weights are not included in this repository.
