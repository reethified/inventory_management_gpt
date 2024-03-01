# auth.py

import streamlit as st
from streamlit_auth import Auth

# Initialize the Auth object with Google OAuth2 settings
auth = Auth(
    client_id='your_client_id',
    client_secret='your_client_secret',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    token_url='https://accounts.google.com/o/oauth2/token',
    redirect_url='https://your-streamlit-app-url.com/auth/google/callback',
    scope=['email', 'profile']
)

def authenticate():
    """
    Authenticates the user using Google OAuth2.
    """
    if not auth.logged_in:
        if st.button('Login with Google'):
            auth.login()

def logout():
    """
    Logs out the current user.
    """
    if auth.logged_in and st.button('Logout'):
        auth.logout()

def get_user_email():
    """
    Returns the email of the authenticated user.
    """
    if auth.logged_in:
        return auth.user["email"]
    else:
        return None
