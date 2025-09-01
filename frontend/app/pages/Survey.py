import streamlit as st
import pandas as pd

if 'username' in st.session_state:
    st.session_state["username"] = st.session_state["username"]

st.write("This survey asks you for your experiences of and opinions on ML in Healthcare")

with st.form("survey_form"):
   st.write("Please only click submit after you have answered every question")
   st.write('''
        For freetext questions, please remember as detailed in the consent process
        to avoid including any identifying information, and only include details 
        you would be happy to have published in anonymised form
            ''')

   st.write("Questions on Experience of ML")
   st.write("Questions on Opinions on ML")
   user_no = st.session_state["username"]
   my_number = st.slider('I have a lot of experience using ML', 1, 10)
   my_exp = st.selectbox('I have used ML in', ['Research','Clinical Practice','Professional Development','Personal Admin'])
   submit_button = st.form_submit_button('Submit my answers')
   
   if submit_button:
        # Create a dictionary for responses
        response = {
            "user": user_no,
            "experience_rating": my_number,
            "experience_area": my_exp,
        }
        
        # Append the response to the list
        response
        
        # Create a DataFrame
        df = pd.DataFrame(response, index = [0])
        
        # Save the responses to a CSV file
        df.to_csv("survey_responses.csv", index=True, mode='w', header=not pd.io.common.file_exists("survey_responses.csv"))
        
        st.success("Thank you for your response!")