import os
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def visualize(df, x_axis, y_axis, plot_type, plot_size, plot_label_size):
    columns = df.columns.tolist()
    # Allow the user to select columns for plotting

    # Set plot size based on user selection
    if plot_size == "Small":
        plot_width = 4
        plot_height = 3
    elif plot_size == "Medium":
        plot_width = 6
        plot_height = 4
    elif plot_size == "Large":
        plot_width = 8
        plot_height = 6

    # Generate the plot based on user selection
    fig, ax = plt.subplots(figsize=(plot_width, plot_height))

    if plot_type == "Line Plot":
        sns.lineplot(x=df[x_axis], y=df[y_axis], ax=ax)
    elif plot_type == "Bar Chart":
        sns.barplot(x=df[x_axis], y=df[y_axis], ax=ax)
    elif plot_type == "Scatter Plot":
        sns.scatterplot(x=df[x_axis], y=df[y_axis], ax=ax)
    elif plot_type == "Distribution Plot":
        sns.histplot(df[x_axis], kde=True, ax=ax)
        y_axis = "Density"
    elif plot_type == "Count Plot":
        sns.countplot(x=df[x_axis], ax=ax)
        y_axis = "Count"

    # Adjust label sizes
    ax.tick_params(axis="x", labelsize=plot_label_size)  # Adjust x-axis label size
    ax.tick_params(axis="y", labelsize=plot_label_size)  # Adjust y-axis label size

    # Adjust title and axis labels with a smaller font size
    plt.title(f"{plot_type} of {y_axis} vs {x_axis}", fontsize=10)
    plt.xlabel(x_axis, fontsize=plot_label_size)
    plt.ylabel(y_axis, fontsize=plot_label_size)

    # Show the results
    return fig


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
