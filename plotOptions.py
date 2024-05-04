import streamlit as st
import time
from visualizer import visualize


def enableGeneratePlotState():
    st.session_state.generatePlot = True


def plot(df):
    columns = df.columns.tolist()
    # Allow the user to select columns for plotting
    x_axis = st.selectbox("Select the X-axis", options=["None"] + columns)
    y_axes = st.multiselect("Select the Y-axis", options=["None"] + columns)

    # x_axis = str(x_axis)
    # y_axis = str(y_axis)

    # since i've moved from plotpy to st charts i don't need this anymore
    # plot_label_size = st.number_input(
    #     "Select label size", min_value=2, max_value=10, value=8, step=1
    # )

    plot_list = [
        "Area Plot",
        "Bar Chart",
        "Line Plot",
        "Map Plot",
        "Scatter Plot",
        "Histogram",
        "Density Heatmaps",
        "Heatmaps",
        "Pie Chart",
        # "Distribution Plot",
        # "Count Plot",
    ]
    # Allow the user to select the type of plot
    plot_type = st.selectbox("Select the type of plot", options=plot_list)
    plot_size = st.selectbox("Select Plot Resolution", ["Small", "Medium", "Large"])

    if "generatePlot" not in st.session_state:
        st.session_state.generatePlot = False

    st.button("Generate Plot", on_click=enableGeneratePlotState)

    if st.session_state.generatePlot:
        # with st.spinner("Loading...."):
        # time.sleep(1)
        fig = visualize(df, x_axis, y_axes, plot_type, plot_size)
