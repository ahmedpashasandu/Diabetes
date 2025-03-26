# import pickle
# import os

# # -*- coding: utf-8 -*-
# """
# Created on Wed Mar 26 11:38:52 2025

# @author: chotu s
# """

# import numpy as np
# import pickle
# import streamlit as st

# loaded_model =  pickle.load(open("trained_model.sav", "rb"))




# #creating a function for predisction

# def diabetes_prediction(input_data):
#     input_data_as_numpy_array=np.asarray(input_data)
    
#     input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    
#     prediction=loaded_model.predict(input_data_reshaped)
#     print(prediction)

#     if (prediction[0]==0):
#         return "the person is deabetics"
#     else:
#         return "the person is not deabetics"
    
# def main():
    
    
#     #giving a title
#     st.title("Diabetes prediction web App")
    
#     #getting the input data from users
    
#     Pregnancies=st.text_input("number of Pregnancies")
#     Glucose=st.text_input("glucose leve")
#     BloodPressure=st.text_input("BloodPressure value")
#     SkinThickness=st.text_input("SkinThickness value")
#     Insulin=st.text_input("Insulin level")
#     BMI=st.text_input("BMI value")
#     DiabetesPedigreeFunction=st.text_input("Diabetes Pedigree Function value")
#     Age=st.text_input("Age of the person")
    
    
#     #code for prediction 
#     diagnosis=" "
    
#     #creating a button for prediction
    
#     if st.button("Diabetes test result"):
#         diagnosis=diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
        
#     st.success(diagnosis)

# if __name__=="__main__":
#     main()



# model_path = "trained_model.sav"

# if os.path.exists(model_path):
#     try:
#         with open(model_path, "rb") as file:
#             loaded_model = pickle.load(file)
#         print("Model loaded successfully!")
#     except Exception as e:
#         print(f"Error loading model: {e}")
# else:
#     print(f"Error: Model file not found at {model_path}")


import pickle
import os
import numpy as np
import streamlit as st

# Load the trained model
model_path = "trained_model.sav"
loaded_model =  pickle.load(open("trained_model.sav", "rb"))


if os.path.exists(model_path):
    try:
        with open(model_path, "rb") as file:
            loaded_model = pickle.load(file)
        print("Model loaded successfully!")
    except Exception as e:
        st.error(f"Error loading model: {e}")
else:
    st.error(f"Error: Model file not found at {model_path}")

# Function for prediction
def diabetes_prediction(input_data):
    try:
        input_data_as_numpy_array = np.asarray(input_data, dtype=np.float32).reshape(1, -1)
        prediction = loaded_model.predict(input_data_as_numpy_array)

        return "The person is diabetic." if prediction[0] == 1 else "The person is not diabetic."
    except ValueError:
        return "Invalid input! Please enter numeric values."

# Streamlit app
def main():
    st.title("Diabetes Prediction Web App")

    # User inputs
    try:
        Pregnancies = float(st.text_input("Number of Pregnancies", "0"))
        Glucose = float(st.text_input("Glucose Level", "0"))
        BloodPressure = float(st.text_input("Blood Pressure Value", "0"))
        SkinThickness = float(st.text_input("Skin Thickness Value", "0"))
        Insulin = float(st.text_input("Insulin Level", "0"))
        BMI = float(st.text_input("BMI Value", "0"))
        DiabetesPedigreeFunction = float(st.text_input("Diabetes Pedigree Function", "0"))
        Age = float(st.text_input("Age of the Person", "0"))

        # Prediction button
        diagnosis = ""
        if st.button("Diabetes Test Result"):
            diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])

        st.success(diagnosis)

    except ValueError:
        st.error("Please enter valid numeric values.")

if __name__ == "__main__":
    main()

