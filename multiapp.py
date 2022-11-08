"""Frameworks for running multiple Streamlit applications as a single app.
"""
import streamlit as st
import pandas as pd
import os


class MultiApp:
    """Framework for combining multiple streamlit applications.
    """

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        """Adds a new application.
        Parameters
        ----------
        func:
            the python function to render this app.
        title:
            title of the app. Appears in the dropdown in the sidebar.
        """
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        #url = os.environ['CSV_URL']
        url = "https://raw.githubusercontent.com/hrdyam/Data_Labelling_Tool/main/hansard_data.csv"
        df = pd.read_csv(url)
        # app = st.sidebar.radio(
        app = st.selectbox(
            'Please select the drop down - Exit when done with labelling, thank you!',
            self.apps,
            format_func=lambda app: app['title'])

        app['function'](df)
