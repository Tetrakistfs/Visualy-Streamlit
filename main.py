import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
import time
from fileUpload import fileUploader

# Set the page config
st.set_page_config(page_title="Visual-ly", layout="wide", page_icon=":roller_coaster:")

# Title
st.title(":roller_coaster:  Visual-ly")
fileUploader()
