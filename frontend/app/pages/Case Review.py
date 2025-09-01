import streamlit as st
import pandas as pd
import sys

sys.path.append('../../')

from backend.app.support_fx import return_case_list

if 'username' in st.session_state:
    st.session_state["username"] = st.session_state["username"]

preop_data = pd.read_csv("../../backend/data/preop_data.csv")
intraop_data = pd.read_csv("../../backend/data/intraop_data.csv")

assessor_cases_df = pd.read_csv("../../backend/data/assessor_cases.csv")
list_cases = return_case_list(st.session_state["username"])

st.write(f'These are the cases: {list_cases}')


st.write("This page will ask you to review data for one case at a time")

st.title("Data Entry and Display")

# Initialize session state variables
if 'current_case_index' not in st.session_state:
    st.session_state.current_case_index = 0
if 'submit_disabled' not in st.session_state:
    st.session_state.submit_disabled = False
if 'response1' not in st.session_state:
    st.session_state.response1 = ""
if 'response2' not in st.session_state:
    st.session_state.response2 = ""


# Display the current case information
st.write("### Case Information")

case_data_preop = preop_data[preop_data["case_id"] == list_cases[st.session_state.current_case_index]]
case_data_intraop = intraop_data[intraop_data["case_id"] == list_cases[st.session_state.current_case_index]]

st.write(f"**Case ID:** {list_cases[st.session_state.current_case_index]}")

with st.form("response_form", clear_on_submit=True):
    # Input fields for responses

    st.table(case_data_preop)

    response1 = st.text_input("Response 1", disabled=st.session_state.submit_disabled)

    st.table(case_data_intraop)

    response2 = st.text_input("Response 2", disabled=st.session_state.submit_disabled)

    # Submit button
    submitted = st.form_submit_button("Submit", disabled=st.session_state.submit_disabled)

    if submitted:
        # Save responses to a CSV file
        response_df = pd.DataFrame({
        'assessor': st.session_state["username"],
        'case': list_cases[st.session_state.current_case_index],
        'first_prediction': [response1],
        'second_prediction': [response2]
         })
    
    # Append to CSV if it exists, otherwise create a new one
    #if os.path.exists('responses.csv'):
    #    responses_df.to_csv('responses.csv', mode='a', header=False, index=False)
    #else:
    #    responses_df.to_csv('responses.csv', index=False)
    
        df = pd.DataFrame(response_df, index = [0])

        responses = pd.read_csv("../../backend/data/responses.csv")

        responses = pd.concat([responses, df], ignore_index = True)

        responses.to_csv("../../backend/data/responses.csv", index = False)

        
        # Immediately disable the submit button
        st.session_state.submit_disabled = True
        st.success("Responses saved successfully!")

        st.rerun()

# Enter new data button
if st.button("Enter New Data"):
    # Move to the next case
    st.session_state.current_case_index += 1
    
    # Reset the submit button state
    st.session_state.submit_disabled = False
    
    # Force a rerun to update the UI
    st.rerun()

# Stop if all cases have been evaluated
#if st.session_state.current_case_index >= len(df):
#    st.write("All cases have been evaluated.")
#    st.stop()
