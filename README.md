# Remote Sensing Computer Vision

A collection of academic Computer Vision projects exploring **machine learning and deep learning for Earth Observation**, including satellite image classification and object detection.

The projects cover traditional feature extraction, CNNs, transfer learning, object detection, and model evaluation using the EuroSAT and DIOR datasets.

## Projects

### 1. EuroSAT — Land Use / Land Cover Classification

Satellite image classification using traditional machine learning and deep learning techniques.

**Dataset:** EuroSAT — 27,000 RGB satellite image patches across 10 land-cover classes.

**Methods:**

- Feature extraction: HOG, Gabor filters, and color moments
- Traditional machine learning: SVM and KNN
- Neural networks: ANN, CNN, and MobileNetV2 transfer learning
- Exploratory decision fusion

**Selected results:**

- MobileNetV2 with frozen backbone: approximately 90% accuracy
- MobileNetV2 with partial fine-tuning: approximately 91% accuracy

Both results are reported on a 5,400-image test directory.

[Explore EuroSAT Project](eurosat/README.md)

### 2. DIOR — Object Detection in Remote Sensing Imagery

Object detection using YOLOv8 architectures on aerial and satellite imagery.

**Dataset:** DIOR — experiments conducted on an 800-image subset.

**Methods:**

- Annotation conversion from XML to YOLO format
- YOLOv8n and YOLOv8s fine-tuning
- Model evaluation using precision, recall, and mean Average Precision (mAP)

**Selected results — YOLOv8s (`freeze=10`):**

- mAP@0.50: 0.5339
- mAP@0.50:0.95: 0.3443

These results are from 120 validation images after fine-tuning with the first 10 model modules frozen.

[Explore DIOR Project](dior/README.md)

## Technologies

**Programming:** Python

**Machine Learning:** scikit-learn, SVM, KNN

**Deep Learning:** TensorFlow, Keras, PyTorch, ANN, CNN, MobileNetV2, YOLOv8

**Computer Vision:** OpenCV, HOG, Gabor Filters, Feature Extraction, Transfer Learning, Object Detection

**Tools:** Jupyter Notebook, NumPy, Pandas, Matplotlib

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

## Reproducibility

Each project contains its own documentation, notebooks, dependencies, and available experimental results.

The reported metrics are drawn from saved notebook outputs and have not been independently reproduced. For details on evaluation procedures, limitations, and dataset preparation, see the individual project documentation.

Datasets and trained model weights are not included in this repository.
