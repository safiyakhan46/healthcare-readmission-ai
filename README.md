# 🏥 Healthcare Readmission Risk Predictor

A machine learning web application that predicts the likelihood of hospital patient readmission using clinical and demographic information.

Built with **Python**, **scikit-learn**, and **Streamlit**, this project demonstrates the complete machine learning workflow—from data preprocessing and model training to deployment as an interactive web application.

---

## 🚀 Live Demo

https://healthcare-readmission-ai-bjrschq9zeuv8nz7bq8anc.streamlit.app/

---

## 📌 Features

- Predicts patient readmission risk
- Interactive Streamlit web interface
- Machine learning model trained using Random Forest
- Real-time prediction probability
- Easy-to-use healthcare dashboard
- Clean and responsive interface

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- Joblib
- Git & GitHub

---

## 📊 Dataset

This project uses the **Diabetes 130-US Hospitals** dataset, which contains over 100,000 hospital encounters collected from 130 US hospitals between 1999 and 2008.

The dataset includes patient demographics, diagnoses, medications, laboratory procedures, hospital stay information, and readmission outcomes.

---

## 🤖 Machine Learning Pipeline

1. Data Cleaning
2. Missing Value Handling
3. Label Encoding
4. Feature Engineering
5. Train/Test Split
6. Random Forest Classification
7. Model Evaluation
8. Streamlit Deployment

---

## 📈 Model Features

The model uses patient information including:

- Age
- Time in Hospital
- Number of Lab Procedures
- Number of Medications
- Number of Procedures
- Previous Inpatient Visits
- Diagnosis Codes
- Medical Specialty
- Additional encoded clinical features

---

## 📷 Application Preview
<img width="712" height="585" alt="Screenshot 2026-08-05 194610" src="https://github.com/user-attachments/assets/b0bb62fe-4ee0-429d-9fea-067b9ef2b96f" />
<img width="730" height="420" alt="Screenshot 2026-08-05 194529" src="https://github.com/user-attachments/assets/b3ec0191-9dfb-4f73-95c4-a97916b312fc" />
<img width="701" height="642" alt="Screenshot 2026-08-05 194547" src="https://github.com/user-attachments/assets/8e2ae5ef-7c49-4694-adcc-f885ac3f67b2" />

---

## 📂 Project Structure

```text
healthcare-readmission-ai/
│
├── app/
│   ├── app.py
│   ├── readmission_model.pkl
│   ├── feature_names.pkl
│   └── defaults.pkl
│
├── data/
│   ├── diabetic_data.csv
│   └── IDS_mapping.csv
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   ├── predict.py
│   ├── evaluate.py
│   └── utils.py
│
├── images/
├── requirements.txt
├── README.md
└── 01_data_exploration.ipynb
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/safiyakhan46/healthcare-readmission-ai.git
```

Navigate into the project:

```bash
cd healthcare-readmission-ai
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app/app.py
```

---

## 🎯 Future Improvements

- XGBoost implementation
- SHAP explainability
- Feature importance visualization
- Better clinical input interface
- Docker deployment
- Cloud model storage
- Authentication
- REST API

---

## ⚠️ Disclaimer

This application is intended for educational and portfolio purposes only. It should not be used for medical diagnosis or clinical decision-making.

---

## 👩‍💻 Author

**Safiya Salman Khan**

Computer Science (Artificial Intelligence) Student

GitHub: https://github.com/safiyakhan46

LinkedIn: *(Add your LinkedIn profile here)*

---

## ⭐ If you found this project interesting, consider giving it a star!
