import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Title of the application
st.title('Heart Disease Risk Prediction')

# Sidebar with user input fields
st.sidebar.header('Input Parameters')

# Age input
age = st.sidebar.slider('Age', 20, 100, 50)

# Gender input
gender = st.sidebar.selectbox('Gender', ['Male', 'Female'])

# Chest pain type input
chest_pain = st.sidebar.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])

# Blood pressure input
blood_pressure = st.sidebar.slider('Resting Blood Pressure (mm Hg)', 90, 200, 120)

# Cholesterol input
cholesterol = st.sidebar.slider('Serum Cholesterol (mg/dl)', 100, 600, 200)

# Max heart rate input
max_heart_rate = st.sidebar.slider('Maximum Heart Rate', 60, 220, 150)

# Build a dictionary from user inputs
input_data = {
    'age': age,
    'gender': 1 if gender == 'Male' else 0,
    'chest_pain': chest_pain,
    'blood_pressure': blood_pressure,
    'cholesterol': cholesterol,
    'max_heart_rate': max_heart_rate
}

# Convert dictionary to DataFrame
input_df = pd.DataFrame([input_data])

# Display user inputs
st.write('## User Input:')
st.write(input_df)

# Load pre-trained model
@st.cache
def load_model():
    return RandomForestClassifier()

model = load_model()

# Load sample dataset (for demonstration)
data = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/diabetes.csv')

# Sample dataset preview
st.write('## Sample Dataset:')
st.write(data.head())

# Train the model (for demonstration)
X = data.drop('diabetes', axis=1)
y = data['diabetes']
model.fit(X, y)

# Make predictions
prediction = model.predict(input_df)

# Display prediction
st.write('## Prediction:')
if prediction[0] == 0:
    st.write('Low risk of heart disease.')
else:
    st.write('High risk of heart disease.')
