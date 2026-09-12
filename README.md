# Skin Cancer Lesion Classification Using Deep Learning

A deep learning-based academic project for classifying skin lesion images into seven diagnostic categories using the HAM10000 dataset.

The project compares two ImageNet-pretrained CNN models — EfficientNetB0 and ResNet50 — and provides a Django REST API with a simple web interface for image prediction.

> ⚠️ **Medical Disclaimer:** This project is an academic/research prototype and is not a medical diagnostic tool. Predictions should not be used for clinical decisions.

---

## 📌 Project Overview

Skin lesion classification is a challenging computer vision problem because different lesion types can have visually similar characteristics and the dataset is highly imbalanced.

This project uses transfer learning to classify skin lesion images into seven classes.

### Main Objectives

- Train and evaluate EfficientNetB0 and ResNet50.
- Handle class imbalance using class weights.
- Use lesion-level splitting to reduce data leakage.
- Compare model performance using accuracy and F1-score.
- Save the best-performing model.
- Build a Django REST API for model inference.
- Provide a web interface where users can upload an image and receive a prediction.

---

## 🧠 Models

Two pretrained CNN architectures were evaluated.

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

### Dataset Distribution

| Class | Images |
|------|-------:|
| nv | 6705 |
| mel | 1113 |
| bkl | 1099 |
| bcc | 514 |
| akiec | 327 |
| vasc | 142 |
| df | 115 |

The dataset is highly imbalanced, so class weights were used during model training.

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
```

Batch size:

```text
32
```

Pixel values were kept in the `0–255` range because EfficientNetB0 includes its own preprocessing.

Class weights were used to reduce the effect of the severe class imbalance.

---

## 📈 Model Performance

### Final Comparison

| Metric | EfficientNetB0 | ResNet50 |
|---|---:|---:|
| Best Validation Accuracy | **66.78%** | 64.88% |
| Best Validation Loss | 0.9501 | **0.9393** |
| Test Accuracy | **66.31%** | 65.63% |
| Macro F1 | **49.03%** | 45.39% |
| Weighted F1 | **69.49%** | 68.89% |

### Selected Model

**EfficientNetB0** was selected as the final model because it achieved better test accuracy, macro F1, and weighted F1 compared with ResNet50.

Final model:

```text
model/final_efficientnetb0.keras
```

---

## 🔍 Example Prediction

The application accepts an image through the web interface and sends it to the Django REST API.

Example API response:

```json
{
    "predicted_class": "bkl",
    "confidence": 31.39
}
```

The frontend converts the class code into a human-readable diagnosis name.

---

## 🏗️ Project Structure

```text
skin-cancer-lesion-classification/
│
├── Skin_Cancer_Detection.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── .gitattributes
├── manage.py
├── test_prediction.py
│
├── model/
│   └── final_efficientnetb0.keras
│
├── backend/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── prediction/
│   ├── model_loader.py
│   ├── views.py
│   ├── models.py
│   ├── admin.py
│   └── tests.py
│
└── frontend/
    ├── index.html
    ├── style.css
    └── script.js
```

---

## 🛠️ Technologies Used

### Machine Learning

- Python
- TensorFlow
- Keras
- EfficientNetB0
- ResNet50
- NumPy
- Pandas
- Scikit-learn

### Backend

- Django
- Django REST Framework
- django-cors-headers

### Frontend

- HTML
- CSS
- JavaScript

### Tools

- Google Colab
- Git
- GitHub
- Git LFS
- VS Code

---

## 🚀 Running the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/sumityadavgh/skin-cancer-lesion-classification.git
```

```bash
cd skin-cancer-lesion-classification
```

---

### 2. Create a Virtual Environment

Using Python 3.13:

```bash
python3.13 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Run Django Migrations

```bash
python manage.py migrate
```

---

### 5. Start the Django Backend

```bash
python manage.py runserver
```

The backend will run at:

```text
http://127.0.0.1:8000/
```

---

### 6. Start the Frontend

Open another terminal and activate the virtual environment if needed.

Then:

```bash
cd frontend
```

Start the frontend server:

```bash
python -m http.server 5500
```

Open the application at:

```text
http://127.0.0.1:5500
```

---

## 🔌 API Endpoint

### Prediction

```text
POST /api/predict/
```

Full local endpoint:

```text
http://127.0.0.1:8000/api/predict/
```

The API expects an image uploaded using the field:

```text
image
```

Example response:

```json
{
    "predicted_class": "nv",
    "confidence": 82.45
}
```

---

## 🔄 Application Workflow

```text
User uploads image
        ↓
Frontend sends image
        ↓
Django REST API
        ↓
Image preprocessing
        ↓
EfficientNetB0 model
        ↓
7-class prediction
        ↓
Predicted class + confidence
        ↓
Frontend displays result
```

---

## 🖥️ Web Application Features

The frontend provides:

- Image upload
- Image preview
- File name display
- Prediction button
- Loading indicator
- EfficientNetB0 prediction
- Human-readable diagnosis name
- Confidence percentage
- Confidence progress bar
- Try Another Image button
- Responsive design
- Medical disclaimer

---

## 📚 Project Notebook

The complete model training and evaluation process is available in:

```text
Skin_Cancer_Detection.ipynb
```

The notebook contains:

- Dataset loading
- Dataset analysis
- Class distribution
- Lesion-level data splitting
- Image preprocessing
- Class weighting
- EfficientNetB0 training
- EfficientNetB0 fine-tuning
- ResNet50 training
- Model evaluation
- Classification reports
- Confusion matrices
- Training graphs
- Model comparison
- Prediction examples
- Project conclusion
- Limitations
- Future improvements

---

## ⚠️ Limitations

- The dataset is highly imbalanced.
- Some lesion classes have very few samples.
- Visually similar classes such as melanoma, benign keratosis, and melanocytic nevi can be difficult to distinguish.
- The model may produce unreliable predictions for images outside the HAM10000 distribution.
- Overall accuracy does not fully represent performance across all classes.
- The model has not been clinically validated.
- The application should not be used to diagnose skin diseases.

---

## 🔮 Future Improvements

Possible improvements include:

- Larger and more diverse datasets.
- Stronger data augmentation.
- Improved class balancing.
- Hyperparameter optimization.
- More advanced transfer-learning strategies.
- Explainable AI techniques such as Grad-CAM.
- Out-of-distribution image detection.
- Model calibration.
- Cloud deployment.
- Improved UI/UX.
- Clinical validation with appropriate medical datasets and expert review.

---

## 📌 Key Findings

- EfficientNetB0 achieved better overall performance than ResNet50.
- EfficientNetB0 achieved **66.31% test accuracy**.
- EfficientNetB0 achieved **49.03% macro F1**.
- EfficientNetB0 achieved **69.49% weighted F1**.
- Both models performed best on the majority `nv` class.
- Minority classes were more difficult to classify.
- Confusion was observed among visually similar classes such as `nv`, `mel`, and `bkl`.
- Class imbalance remains an important limitation.

---

## 👨‍💻 Author

**Sumit Yadav**

B.Tech Computer Science Engineering

GitHub:  
https://github.com/sumityadavgh

LinkedIn:  
https://www.linkedin.com/in/sumitydv007

---

## 📄 License

This project is intended for **educational and research purposes**.

The model and application should not be used for medical diagnosis or clinical decision-making.

---

## ⭐ Acknowledgement

This project uses the HAM10000 dataset for academic and research purposes.

The project demonstrates the application of transfer learning and deep learning techniques to multi-class skin lesion image classification.