import streamlit as st
import hmac
import sys

def check_password():
    """Returns `True` if the user had a correct password."""

    def login_form():
        """Form with widgets to collect user information"""
        with st.form("Credentials"):
            st.text_input("Username", key="username")
            st.text_input("Password", type="password", key="password")
            st.form_submit_button("Log in", on_click=password_entered)

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if st.session_state["username"] in st.secrets[
            "passwords"
        ] and hmac.compare_digest(
            st.session_state["password"],
            st.secrets.passwords[st.session_state["username"]],
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the username or password.
         #   del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    # Return True if the username + password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show inputs for username + password.
    login_form()
    if "password_correct" in st.session_state:
        st.error("😕 User not known or password incorrect")
    return False

if not check_password():
    st.stop()

st.set_page_config(
    page_title="Landing Page",
    page_icon="👋",
)

st.write("# Welcome to S-OPTIMA Survey! 👋")
st.write(f'Logged in as: {st.session_state["username"]}')

if 'username' in st.session_state:
    st.session_state["username"] = st.session_state["username"]

st.sidebar.success("Please select the survey or a case")

st.markdown(
    """
    Many thanks for taking part in the S-OPTIMA Study 
    Please note you can only submit each form once
    **👈 Select a case from the sidebar** 

"""
)
