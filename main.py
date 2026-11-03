import streamlit as st
from models.approval_classifier import (
    data_load,
    data_preparation,
    model_training,
    predict_approval
)

students_data = data_load()

study_hours_data, results_data = data_preparation(students_data)

classifier_model = model_training(
    study_hours_data, 
    results_data
    )

#Streamlit Interface

#Page title
st.set_page_config(
    page_title = "Student Approval Prediction",
    layout = "centered"
)

st.markdown(
    """
    <h1 style='text-align:center; color:#FFFF;'>
        Student Approval Prediction
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <p style='text-align:center; color:#CCCCCC;'>
        Machine Learning model trained to predict student approval.
    </p>
    """,
    unsafe_allow_html=True
)

st.write("")

#Study hours slider
left, center, right = st.columns([2, 3, 2])

with center:
    st.markdown(
        "<h3 style='text-align:center;'>Study Hours</h3>",
        unsafe_allow_html=True
    )

    study_hours = st.slider(
        "",
        0,
        24,
        5
    )

#Prediction button

left, center, right = st.columns([3, 1, 3])

with center:
    predict_button = st.button("Predict")

#Result

if predict_button:

    prediction = predict_approval(
        classifier_model,
        study_hours
    )

    if prediction == 1:
        st.success("✅ Approved")
    else:
        st.error("❌ Failed")
