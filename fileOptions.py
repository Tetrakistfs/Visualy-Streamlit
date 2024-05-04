import streamlit as st
from editor import pygWalker
from plotOptions import plot
from dataframeEditor import loadDataframeEditor


def save_edits():
    df = st.session_state.edited_df.copy()


def enableDfEditor():
    st.session_state.enableDfEditor = True
    st.session_state.enableQuickCharts = False
    st.session_state.enableChartEditor = False


def showQuickChartsMenu():
    st.session_state.enableDfEditor = False
    st.session_state.enableQuickCharts = True
    st.session_state.enableChartEditor = False


def showEditor():
    st.session_state.enableDfEditor = False
    st.session_state.enableChartEditor = True
    st.session_state.enableQuickCharts = False


def reload():
    st.session_state.enableDfEditor = False
    st.session_state.enableQuickCharts = False
    st.session_state.enableChartEditor = False


def visualizationOptions(df):

    if "enableDfEditor" not in st.session_state:
        st.session_state.enableDfEditor = False

    if "enableQuickCharts" not in st.session_state:
        st.session_state.enableQuickCharts = False

    if "enableChartEditor" not in st.session_state:
        st.session_state.enableChartEditor = False

    if "enableReloadButton" not in st.session_state:
        st.session_state.enableReloadButton = False

    # DataFrame Editor
    st.button("DataFrame Editor", on_click=enableDfEditor)

    # Quick Charts Button
    st.button("Quick Charts", on_click=showQuickChartsMenu)

    # Pygwalker Editor Button
    st.button("Advanced Chart Editor", on_click=showEditor)

    st.button("Close", on_click=reload)

    if st.session_state.enableQuickCharts:
        # st.write("charts")
        with st.container():
            col1, col2 = st.columns([2, 3])
            with col1:
                st.write("")
                st.write(df)
            with col2:
                plot(df)

    elif st.session_state.enableChartEditor:
        with st.container():
            pygWalker(df)

    elif st.session_state.enableDfEditor:
        with st.container():
            editor_col1, editor_col2 = st.columns([4, 1])
            with editor_col1:
                st.session_state.edited_df = loadDataframeEditor(
                    df, st.session_state.edited_df
                )
            with editor_col2:
                st.button("Save", on_click=save_edits(df))
