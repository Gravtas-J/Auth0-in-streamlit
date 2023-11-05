from auth0_component import login_button
import streamlit as st
from dotenv import load_dotenv
import os





st.set_page_config(
    page_title=("Auth0 Example"),
    page_icon="🔐",
)
hide_st_style = """
            <style>
            #MainMenu {visibility: visable;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
load_dotenv()

clientId = os.environ['clientid']
domain = os.environ['domainid']



def main():
    st.write('this is an example of auth0 in streamlit')

# Initialize session states if they don't exist
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if 'user_id' not in st.session_state:
    st.session_state.user_id = None

# If user is not logged in, show the login button
if not st.session_state.logged_in:
    user_info = login_button(clientId=clientId, domain=domain)
    if user_info:
        st.session_state.logged_in = True
        st.session_state.user_id = user_info.get('sub', None)  # Assuming 'sub' is a unique identifier for the user
        st.rerun()
        main()
elif st.session_state.user_id:
    
    main()
