import streamlit as st
import pygwalker as pyg
from pygwalker.api.streamlit import StreamlitRenderer


@st.cache_data
def get_pyg_renderer(df) -> "StreamlitRenderer":
    return StreamlitRenderer(
        df, spec="./gw_config.json", spec_io_mode="rw", kernel_computation=True
    )
