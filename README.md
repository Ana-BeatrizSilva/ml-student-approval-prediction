# Student Approval Prediction / Previsão de Aprovação de Alunos

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)

---

## English Version

### About the Project

**Student Approval Prediction** is an application built with Python that uses Machine Learning to predict whether a student will be approved or fail based on their total hours of study.

The application loads historical student data from a JSON file, trains a Decision Tree classifier, and provides an interactive interface built with Streamlit for real-time predictions.

It was developed for educational and portfolio purposes, aiming to practice Machine Learning model integration, classification algorithms, and interactive web application deployment.

---

### Features

- Data ingestion and preparation from structured JSON format.
- Training of a Machine Learning classification model (`DecisionTreeClassifier`).
- Interactive user interface built with Streamlit.
- Real-time prediction based on user-defined study hours.

---

### Technologies and Tools

- Python
- Scikit-learn
- Streamlit
- JSON

---

### Applied Concepts

- Supervised Learning and Classification algorithms (Decision Trees).
- Machine Learning pipeline modularization (Data Loading, Preparation, Training, Inference).
- Web application interface development using Streamlit.

---

### Project Structure

```text
ml-student-approval-prediction/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── students.json
│
├── models/
│   └── approval_classifier.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

### How to Run

#### 1. Clone the repository

```bash
git clone [https://github.com/Ana-BeatrizSilva/ml-student-approval-prediction.git](https://github.com/Ana-BeatrizSilva/ml-student-approval-prediction.git)
```

#### 2. Navigate to the project directory

```bash
cd ml-student-approval-prediction
```

#### 3. Install dependencies

```bash
pip install -r requirements.txt
```

#### 4. Run the Streamlit application

```bash
streamlit run main.py
```

---

### Future Improvements

- Incorporate additional features (e.g., attendance rate, prior grades).
- Evaluate and compare multiple classification models (e.g., Logistic Regression, Random Forest).
- Persist the trained model using `joblib` or `pickle` to avoid retraining on startup.

---
---

## Versão em Português

### Sobre o Projeto

**Student Approval Prediction** é um projeto desenvolvido em Python que utiliza Machine Learning para prever a aprovação acadêmica de estudantes com base no total de horas dedicadas ao estudo.

A aplicação carrega um histórico de dados em formato JSON, treina um classificador de Árvore de Decisão e fornece uma interface interativa via Streamlit para realizar predições em tempo real.

Foi desenvolvido com finalidade educacional e de portfólio, com o objetivo de praticar e consolidar conhecimentos em integração de modelos de Machine Learning, algoritmos de classificação e criação de aplicações web interativas.

---

### Funcionalidades

- Carregamento e preparação de dados a partir de arquivo JSON.
- Treinamento de modelo de classificação de Machine Learning (`DecisionTreeClassifier`).
- Interface interativa desenvolvida com Streamlit.
- Predição em tempo real com base no número de horas de estudo selecionado pelo usuário.

---

### Tecnologias e Ferramentas

- Python
- Scikit-learn
- Streamlit
- JSON

---

### Conceitos Aplicados

- Aprendizado Supervisionado e algoritmos de classificação (Árvore de Decisão).
- Modularização do fluxo de Machine Learning (Carga de dados, Preparação, Treinamento e Predição).
- Desenvolvimento de interfaces web interativas com Streamlit.

---

### Estrutura do Projeto

```text
ml-student-approval-prediction/
│
├── .streamlit/
│   └── config.toml
│
├── data/
│   └── students.json
│
├── models/
│   └── approval_classifier.py
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

---

### Como Executar

#### 1. Clone o repositório

```bash
git clone [https://github.com/Ana-BeatrizSilva/ml-student-approval-prediction.git](https://github.com/Ana-BeatrizSilva/ml-student-approval-prediction.git)
```

#### 2. Acesse a pasta do projeto

```bash
cd ml-student-approval-prediction
```

#### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

#### 4. Execute a aplicação Streamlit

```bash
streamlit run main.py
```

---

### Possíveis Melhorias Futuras

- Adição de novos atributos para treino (ex.: frequência escolar, notas prévias).
- Avaliação e comparação de outros algoritmos de classificação (ex.: Regressão Logística, Random Forest).
- Salvamento do modelo treinado (`joblib` ou `pickle`) para evitar retreinamento a cada execução.
