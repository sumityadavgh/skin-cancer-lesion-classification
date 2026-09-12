# Skin Cancer Lesion Classification Using Deep Learning

A deep learning-based academic project for classifying skin lesion images into seven diagnostic categories using the HAM10000 dataset.

The project compares two ImageNet-pretrained CNN models — EfficientNetB0 and ResNet50 — and provides a Django REST API with a simple web interface for image prediction.

> ⚠️ **Medical Disclaimer:** This project is an academic/research prototype and is not a medical diagnostic tool. Predictions should not be used for clinical decisions.

---

## 📌 Project Overview

Skin lesion classification is a challenging computer vision problem because different lesion types can have visually similar characteristics and the dataset is highly imbalanced.

This project uses transfer learning to classify skin lesion images into seven classes.

### Main objectives

- Train and evaluate EfficientNetB0 and ResNet50.
- Handle class imbalance using class weights.
- Use lesion-level splitting to reduce data leakage.
- Compare model performance using accuracy and F1-score.
- Save the best-performing model.
- Deploy the trained model through a Django REST API.
- Provide a simple web interface where users can upload an image and receive a prediction.

---

## 🧠 Models

Two pretrained CNN architectures were evaluated:

### EfficientNetB0

- ImageNet pretrained
- Global Average Pooling
- Dropout
- 7-class Softmax output
- Selected as the final model

### ResNet50

- ImageNet pretrained
- Global Average Pooling
- Dropout
- 7-class Softmax output
- Used as a comparison model

---

## 📊 Dataset

The project uses the **HAM10000 (Human Against Machine with 10000 training images)** dataset.

The dataset contains **10,015 dermatoscopic images** belonging to seven lesion categories.

### Classes

| Code | Diagnosis |
|------|-----------|
| `akiec` | Actinic Keratoses |
| `bcc` | Basal Cell Carcinoma |
| `bkl` | Benign Keratosis-like Lesions |
| `df` | Dermatofibroma |
| `mel` | Melanoma |
| `nv` | Melanocytic Nevi |
| `vasc` | Vascular Lesions |

### Dataset distribution

| Class | Images |
|------|-------:|
| nv | 6705 |
| mel | 1113 |
| bkl | 1099 |
| bcc | 514 |
| akiec | 327 |
| vasc | 142 |
| df | 115 |

Because the dataset is highly imbalanced, class weights were used during training.

---

## 🔀 Data Splitting

The dataset was split at the **lesion level** rather than randomly splitting individual images.

This helps reduce data leakage because multiple images can belong to the same lesion.

| Split | Images | Lesions |
|------|-------:|--------:|
| Training | 7,002 | 5,229 |
| Validation | 1,532 | 1,120 |
| Test | 1,481 | 1,121 |

---

## ⚙️ Image Preprocessing

Images were resized to:

```text
224 × 224