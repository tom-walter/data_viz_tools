"""
Stacked Bar Chart Function 
Created on 03.03.2021
@author: Tom-Walter
"""


def plot_stacked_bar(data, series_labels, category_labels=None,
                     show_values=False, value_format="{}", y_label=None,
                     colors=None, grid=False, reverse=False):
    """Plots a stacked bar chart with the data and labels provided.

    Keyword arguments:
    data            -- 2-dimensional numpy array or nested list
                       containing data for each series in rows
    series_labels   -- list of series labels (these appear in
                       the legend)
    category_labels -- list of category labels (these appear
                       on the x-axis)
    show_values     -- if True then numeric value labels will 
                       be shown on each bar (badly handles nan-type)
    value_format    -- format string for numeric value labels
                       (default is "{}")
    y_label         -- label for y-axis (str)
    colors          -- list of color labels
                       (will cycle through default colors if none are given)
    grid            -- if True display grid in background
    reverse         -- if True reverse the order that the
                       series are displayed (left-to-right
                       or right-to-left)
    """
    # source code: https://stackoverflow.com/questions/44309507/stacked-bar-plot-using-matplotlib

    if grid:
        plt.style.use('seaborn-whitegrid')
    else:
        plt.style.use('default')

    ny = len(data[0])
    ind = list(range(ny))

    axes = []
    cum_size = np.zeros(ny)

    data = np.array(data)

    if reverse:
        data = np.flip(data, axis=1)
        category_labels = reversed(category_labels)

    for i, row_data in enumerate(data):
        color = colors[i] if colors is not None else None
        axes.append(plt.bar(ind, row_data, bottom=cum_size,
                            label=series_labels[i], color=color, edgecolor='k'))
        cum_size += row_data

    if category_labels:
        plt.xticks(ind, category_labels)

    if y_label:
        plt.ylabel(y_label)

    plt.legend()

    if show_values:
        for axis in axes:
            for bar in axis:
                w, h = bar.get_width(), bar.get_height()
                plt.text(bar.get_x() + w / 2, bar.get_y() + h / 2,
                         value_format.format(h), ha="center",
                         va="center")


import numpy as np
import matplotlib.pyplot as plt
