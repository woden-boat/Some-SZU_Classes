#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
% Instructions: Plot the positive and negative examples on a
%               2D plot, using the option 'k+' for the positive
%               examples and 'ko' for the negative examples.
%
"""

import numpy as np
import matplotlib.pyplot as plt


def plotData(X, y):
    """
    绘制散点图
    绘图时必须加标签，至于便签叫啥无所谓，原因是不加标签获取不到句柄...，官方文档的解释如下
    '''
    And, get_legend_handles_labels() returns all artists in ax.lines,
    ax.patches and artists in ax.collection which are instance of LineCollection or RegularPolyCollection.
    The label attributes (returned by get_label() method) of collected artists are used as text labels.
    If label attribute is empty string or starts with “_”, those artists will be ignored.
    '''
    :param X:
    :param y:
    :return: ax
    """
    fig, ax = plt.subplots(figsize=(12, 8))
    pass
    # ====================== YOUR CODE HERE ======================
    # You should change this



    # ========== END ==========
    return ax
