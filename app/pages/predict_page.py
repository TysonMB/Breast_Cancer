import os
import sys
import streamlit as st
import pickle 
import json
from pathlib import Path
import joblib
import numpy as np


# -------------------------
# The project root folder
# -------------------------


BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "models" / "model.pkl"


#Loading model
# -------------------------
# Load model (cached)
# -------------------------

def load_model():
    model = joblib.load(MODEL_PATH)
    return model

model = load_model()

def show_app_info_page():
    st.title("Breast Cancer Prediction App")
    st.divider()
    st.write("""### How to use this app """)
    st.write('')
    st.write("""1.Fill out the form below (all the fields are required)""")
    st.write("""2.Check the required check-boxes for the final report""")
    st.write("""3.Submit once you are done to get a report (your data wont be shared)""")
    st.write("""4.After submitting, refresh the page if you want to make another submission (to clear up the result of the previous submission)""")

def personnal_info():
    st.subheader('Info')
    st.write('')

    #creating horintal columns
    row1 = st.columns(2) 
    row2 = st.columns(3)
    
    #Creating vairables for the columns and intializing them
    with row1[0]:
        first_name = st.text_input("First Name" )
        st.session_state.first_name = first_name  #Setting a session to allow the vairable to be viewed anywhere in the app

    with row1[1]:
        last_name = st.text_input("Last Name" )
        st.session_state.last_name = last_name #Setting the last name session

    with row2[0]:
        gender = st.radio("Gender",['Famale'])
        st.session_state.gender = gender
    
    with row2[1]:
        age = st.number_input("Age", min_value = 0, max_value = 120, step = 1)
        st.session_state.age = age
    
    with row2[2]:
        status = st.radio("Marital Status",["No", "Yes"])
        st.session_state.status = status


#The fucntion that will have the inputs to put in the model
def show_predict_page():
    st.subheader("""Fill in The Form""")

    #The features which will be used as inputs
    feature_names = {
        "concave_points_mean": None, 
        "perimeter_worst": None, 
        "concave_points_worst": None
    }
    
    #The form where the inputs will be entered
    with st.form(key = "User_infor_form", clear_on_submit=True):
        update_data = {}
        for (key, value) in feature_names.items(): #Creating inputs of the form from the festure_name
            update_data[key] = st.text_input(key, value)
            st.session_state.update_data = update_data


        submit_button = st.form_submit_button(label = "Submit")
        st.session_state.submit_button = submit_button

    #Catching a ValueError
    try:

        if submit_button:
            if not all (update_data.values()):
                st.warning("Please fill all the the fields, some are missing.")

            #Getting the input features and making a prediction
            else: 
                feature_values = list(update_data.values())
                input_features = np.array([feature_values])
                input_features = input_features.astype(float)
                input_features = np.reshape(input_features, (1, -1))
                condition = model.predict(input_features)

                if condition  == 1:
                    malignant = ("You have Malignant Cancer. See a Medical Doctor for more information")
                    st.session_state.malignant = malignant

                elif condition == 0:
                    bagnin = ("You have Benign Cancer. See a Medical Doctor for more information")
                    st.session_state.bagnin = bagnin

    except (ValueError):
        st.warning("Please note that only use numbers to fill in the form.")
                


#Displaying all the information and the result of the prediction
def results():
    st.subheader("Petient Results")
    st.write('')

    #Getting the input values using a session from other functions
    first_name = st.session_state.get('first_name', '')
    last_name = st.session_state.get('last_name', '')
    gender = st.session_state.get('gender', '')
    age = st.session_state.get('age', '')
    status = st.session_state.get('status', '')
    malignant = st.session_state.get('malignant', '')
    bagnin = st.session_state.get('bagnin', '')
    update_data = st.session_state.get('update_data', '')
    submit_button = st.session_state.get('submit_button', '')
    
    #Writing to the screen the information which was entered
    st.write(f"Name: {first_name} {last_name}")
    st.write(f"Gender: {gender}")
    st.write(f"Age: {age} years old")
    st.write(f"Married: {status}")
    st.write(f"Condition: {malignant} {bagnin}")
    
    
    #Printing a message at the bottom when the button is pressed and when it's not
    if submit_button:
        if all (update_data.values()):
            st.write("""#### Your Information was Submitted Succesfully""")

    else:
        st.write("""#### No Information Has Been Submitted Yet""")

   


    



