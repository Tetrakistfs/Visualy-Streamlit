import streamlit as st
from visualizer import visualize


def enableGeneratePlotState():
    st.session_state.generatePlot = True


def plot(df):
    columns = df.columns.tolist()
    # Allow the user to select columns for plotting
    x_axis = st.selectbox("Select the X-axis", options=["None"] + columns)
    y_axis = st.selectbox("Select the Y-axis", options=["None"] + columns)

    plot_label_size = st.number_input(
        "Select label size", min_value=2, max_value=10, value=8, step=1
    )

    plot_list = [
        "Line Plot",
        "Bar Chart",
        "Scatter Plot",
        "Distribution Plot",
        "Count Plot",
    ]
    # Allow the user to select the type of plot
    plot_type = st.selectbox("Select the type of plot", options=plot_list)
    plot_size = st.selectbox("Select Plot Resolution", ["Small", "Medium", "Large"])

    if "generatePlot" not in st.session_state:
        st.session_state.generatePlot = False

    st.button("Generate Plot", on_click=enableGeneratePlotState)

    if st.session_state.generatePlot:
        fig = visualize(df, x_axis, y_axis, plot_type, plot_size, plot_label_size)
        st.pyplot(fig)
