from sklearn.tree import DecisionTreeClassifier

import json

def data_load():

    with open("data/students.json", "r") as json_archive:
        students_data = json.load(json_archive)

    return students_data

def data_preparation(students_data):

    study_hours_data = []
    results_data = []

    for student in students_data:
        study_hours_data.append([student["study_hours"]])
        results_data.append(student["result"])

    return study_hours_data, results_data

def model_training(study_hours_data, results_data):

    classifier_model = DecisionTreeClassifier()
    classifier_model.fit(study_hours_data, results_data)

    return classifier_model

def predict_approval(classifier_model, study_hours):

    student_prediction = classifier_model.predict([[study_hours]])

    return student_prediction