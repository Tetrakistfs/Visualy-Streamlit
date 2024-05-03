import streamlit as st
from editor import pygWalker
from plotOptions import plot


def showQuickChartsMenu():
    st.session_state.enableQuickCharts = True
    st.session_state.enableEditor = False


def showEditor():
    st.session_state.enableEditor = True
    st.session_state.enableQuickCharts = False


def reload():
    st.session_state.enableQuickCharts = False
    st.session_state.enableEditor = False


def visualizationOptions(df):
    if "enableQuickCharts" not in st.session_state:
        st.session_state.enableQuickCharts = False

    if "enableEditor" not in st.session_state:
        st.session_state.enableEditor = False

    if "enableReloadButton" not in st.session_state:
        st.session_state.enableReloadButton = False

    # Quick Charts Button
    st.button("Quick Charts", on_click=showQuickChartsMenu)

    # Pygwalker Editor Button
    st.button("Editor", on_click=showEditor)

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

    elif st.session_state.enableEditor:
        with st.container():
            pygWalker(df)
