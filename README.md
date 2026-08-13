# Student Stress Level Prediction Using Machine Learning

## About

This project aims to develop a Machine Learning model to predict the stress level of university students based on academic, behavioral, lifestyle, and other related factors.

The project will identify the important factors affecting student stress and compare different Machine Learning classification algorithms to find the most suitable model.

## Research Questions

1. What are the key academic, behavioral, and lifestyle factors affecting the stress levels of university students?
2. How effective are Machine Learning methods in predicting student stress levels?
3. Which Machine Learning method is the most accurate in predicting student stress levels?
4. How can Machine Learning help identify students with high stress levels?

## Dataset

The project uses the `StressLevelDataset.csv` dataset.

* **Records:** 1,100
* **Features:** 20
* **Target Variable:** `stress_level`

The dataset contains information related to academic, behavioral, lifestyle, and other factors that can be used to predict student stress.

## Machine Learning Models

The following classification algorithms are used and compared:

* Decision Tree
* Random Forest
* Support Vector Machine (SVM)
* Logistic Regression

## Model Evaluation

The models are evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Seaborn
* Joblib
* Streamlit
* Jupyter Notebook
* VS Code
* Git & GitHub

## Project Structure

```text
Student-Stress-Prediction/
│
├── data/
│   └── StressLevelDataset.csv
│
├── models/
│   └── stress_model.pkl
│
├── notebooks/
│   └── student_stress_prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/KattadigeHiruniDineka/student-stress-prediction
```

### 2. Open the Project

```bash
cd Student-Stress-Prediction
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your web browser.

## Project Links

* **GitHub Repository:** [Student Stress Prediction](https://github.com/KattadigeHiruniDineka/student-stress-prediction)
* **Live Streamlit App:** [Student Stress Prediction App](https://student-stress-prediction-g4gdnc3acldczbmr8ngqxy.streamlit.app/)

## Expected Outcome

The expected outcome is a Machine Learning system that can classify university students into different stress levels.

The project also aims to identify important factors contributing to student stress and provide a prediction tool that can help educational institutions identify students who may have high stress levels.

## Project Status

🚧 **Currently in Development**

## Team Members

* **K. Hiruni Dineka ITBIN 2313- 0028**
* **H. Dewmi Dilhari ITBIN 2313-0024**
* **L.A. Yasith Shavinda ITBIN 2313-0107**
