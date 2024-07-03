import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load the model
with open("D:\college\Practicum\streamlit app\model.pkl", 'rb') as model_file:
    model = pickle.load(model_file)

# Define the Streamlit app
def main():
    st.title("Calories Burnt Prediction App")

    

    # Sidebar for user input
    st.header("User Input")
    gender = st.selectbox("Gender", ['male', 'female'])
    age = st.number_input("Age", 18, 100, 30)
    height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    duration = st.number_input("Duration (min)", 10.0, 300.0, 30.0)
    heart_rate = st.number_input("Heart Rate", 60.0, 200.0, 100.0)
    body_temp = st.number_input("Body Temperature (°F)", 90.0, 105.0, 98.6)

        # Encode gender
    with st.container():
        st.write("         ")  # Adjust spacing
        if st.button("Predict Calories", key="predict_button", help="Click to predict calories."):
            gender_encoded = 0 if gender == 'male' else 1

        # Make prediction
            input_data = np.array([gender_encoded, age, height, weight, duration, heart_rate, body_temp]).reshape(1, -1)
            prediction = model.predict(input_data)[0]

            st.write("### Predicted Calories Burnt:", round(prediction, 2))

if __name__ == '__main__':
    main()

