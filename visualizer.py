import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt
import plotly.express as px


def visualize(df, x_axis, y_axes, plot_type, plot_size):
    columns = df.columns.tolist()
    # Allow the user to select columns for plotting

    # Set plot size based on user selection
    if plot_size == "Small":
        plot_width = 600
        plot_height = 400
    elif plot_size == "Medium":
        plot_width = 800
        plot_height = 600
    elif plot_size == "Large":
        plot_width = 800
        plot_height = 800

    if plot_type == "Area Plot":
        st.area_chart(
            data=df,
            x=x_axis,
            y=y_axes,
            width=plot_width,
            height=plot_height,
            use_container_width=False,
        )
    elif plot_type == "Bar Chart":
        st.bar_chart(
            data=df,
            x=x_axis,
            y=y_axes,
            width=plot_width,
            height=plot_height,
            use_container_width=False,
        )
    elif plot_type == "Line Plot":
        st.line_chart(
            data=df,
            x=x_axis,
            y=y_axes,
            width=plot_width,
            height=plot_height,
            use_container_width=False,
        )
    elif plot_type == "Map Plot":
        st.map(
            data=df,
            latitude=x_axis,
            longitude=y_axes,
            zoom=None,
            use_container_width=False,
        )
    elif plot_type == "Scatter Plot":
        st.scatter_chart(
            data=df,
            x=x_axis,
            y=y_axes,
            width=plot_width,
            height=plot_height,
            use_container_width=False,
        )
    elif plot_type == "Histogram":
        fig = px.histogram(
            data_frame=df, x=x_axis, y=y_axes, width=plot_width, height=plot_height
        )
        st.plotly_chart(
            fig, use_container_width=False, sharing="streamlit", theme="streamlit"
        )
    elif plot_type == "Density Heatmaps":
        fig = px.density_heatmap(
            data_frame=df, x=x_axis, y=y_axes, width=plot_width, height=plot_height
        )
        st.plotly_chart(
            fig, use_container_width=False, sharing="streamlit", theme="streamlit"
        )
    elif plot_type == "Heatmaps":
        fig = px.imshow(df, x=x_axis, y=y_axes, width=plot_width, height=plot_height)
        st.plotly_chart(
            fig, use_container_width=False, sharing="streamlit", theme="streamlit"
        )

    elif plot_type == "Pie Chart":
        fig = px.pie(
            data_frame=df,
            names=x_axis,
            labels=y_axes,
            height=plot_height,
            width=plot_width,
        )
        st.plotly_chart(
            fig, use_container_width=False, sharing="streamlit", theme="streamlit"
        )


# Matplotlib:

# Histogram
# Box Plot
# Pie Chart
# Heatmap
# Contour Plot

# Seaborn
# Distribution Plot (e.g., KDE Plot, Histogram)
# Pair Plot
# Violin Plot
# Swarm Plot
# Joint Plot
# Heatmap

# Plotly
# Line Plot
# Bar Chart
# Scatter Plot
# Histogram
# Box Plot
# Pie Chart
# Heatmap
# Contour Plot
# 3D Surface Plot
# Violin Plot
# Funnel Chart
# Waterfall Chart
# Radar Chart
