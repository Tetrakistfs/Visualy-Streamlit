import streamlit as st
import pandas as pd
import json


# from dfEditorLoader import loadDataframeEditor
@st.cache_data
def loadDataframeEditor(df, edited_df):
    edited_df = st.data_editor(df, num_rows="dynamic", hide_index=True)
    return edited_df
