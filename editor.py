from pygwalker.api.streamlit import StreamlitRenderer
import pandas as pd
import streamlit as st
from renderer import get_pyg_renderer


def enableCacheState():
    st.session_state.clearCache = True


def pygWalker(df):
    if "clearCache" not in st.session_state:
        st.session_state.clearCache = False

    title_col1, title_col2 = st.columns([2, 2])

    with title_col1:
        st.title("Editor")

    with title_col2:
        st.button("Clear Cache", on_click=enableCacheState)
        if enableCacheState:
            st.cache_resource.clear()

    # caching the renderer, so the memory doesn't overflow //removed
    renderer = get_pyg_renderer(df)
    renderer.explorer()
