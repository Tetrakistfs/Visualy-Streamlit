import os
import streamlit as st
import pandas as pd
from fileOptions import visualizationOptions


# @st.cache_data
def read_file(file_path, selected_file):
    file_name = selected_file
    file_extension = file_name.split(".")[-1]
    if file_extension == "csv":
        return pd.read_csv(file_path)
    else:
        return pd.read_excel(file_path)


def fileUploader():

    working_dir = os.path.dirname(os.path.abspath(__file__))

    # Specify the folder where your CSV files are located
    folder_path = f"{working_dir}/data"  # Update this to your folder path

    # List all files in the folder
    files = [f for f in os.listdir(folder_path) if f.endswith((".csv", ".xlsx"))]

    # Dropdown to select a file
    if "readFile" not in st.session_state:
        st.session_state.readFile = False

    selected_file = st.selectbox("Select a file", files, index=None)

    if selected_file:
        # Construct the full path to the file
        file_path = os.path.join(folder_path, selected_file)

        # if st.session_state.readFile:           //giving a problem as when we don't select any file it gets path error
        df = read_file(file_path=file_path, selected_file=selected_file)
        df = pd.DataFrame(df)

        df = df.replace("", pd.NA).fillna(0)
        df.reset_index(drop=True, inplace=True)
        visualizationOptions(df)
