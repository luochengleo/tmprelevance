# coding=utf8
__author__ = 'zhangfan'
import numpy as np
from collections import defaultdict
from numpy import mean
import matplotlib.pyplot as plt
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def user_deviation():
    deviation_valid = defaultdict(lambda: [])
    for l in open('../../result/user_personalization_etime_analyse.csv').readlines()[1: ]:
        _, configid, taskid, _, _, _, deviation, _ = l.strip().split(',')
        if int(taskid) < 11 or int(taskid) > 14:
            deviation_valid[configid].append(float(deviation))
    high_deviation_mean = []
    high_deviation_std = []
    low_deviation_mean = []
    low_deviation_std = []
    for i in range(0, 25):
        high_deviation_mean.append(0)
        high_deviation_std.append(0)
        low_deviation_mean.append(0)
        low_deviation_std.append(0)
    for configid in deviation_valid.keys():
        if int(configid) < 26:
            high_deviation_mean[int(configid) - 1] = mean(deviation_valid[configid])
            high_deviation_std[int(configid) - 1] = np.std(deviation_valid[configid])
        if int(configid) > 25:
            low_deviation_mean[int(configid) - 26] = mean(deviation_valid[configid])
            low_deviation_std[int(configid) - 26] = np.std(deviation_valid[configid])
    for i in range(0, 24):
        for j in range(0, 24 - i):
            if high_deviation_mean[j] > high_deviation_mean[j + 1]:
                temp = high_deviation_mean[j]
                high_deviation_mean[j] = high_deviation_mean[j + 1]
                high_deviation_mean[j + 1] = temp
                temp = high_deviation_std[j]
                high_deviation_std[j] = high_deviation_std[j + 1]
                high_deviation_std[j + 1] = temp
            if low_deviation_mean[j] > low_deviation_mean[j + 1]:
                temp = low_deviation_mean[j]
                low_deviation_mean[j] = low_deviation_mean[j + 1]
                low_deviation_mean[j + 1] = temp
                temp = low_deviation_std[j]
                low_deviation_std[j] = low_deviation_std[j + 1]
                low_deviation_std[j + 1] = temp
    fig = plt.figure()

    ax1 = fig.add_subplot(211)
    index = np.arange(25)
    bar_width = 0.5
    opacity = 0.4
    rects1 = plt.bar(index, low_deviation_mean, bar_width, alpha=opacity, color='b', yerr=low_deviation_std)
    plt.title('control group')
    plt.xticks(())
    ax1.spines['right'].set_color('none')
    ax1.spines['top'].set_color('none')
    ax1.spines['bottom'].set_position(('data', 0))
    ax1.yaxis.set_ticks_position('left')

    ax2 = fig.add_subplot(212)
    index = np.arange(25)
    opacity = 0.4
    rects1 = plt.bar(index, high_deviation_mean, bar_width, alpha=opacity, color='b', yerr=high_deviation_std)
    plt.title('treatment group')
    plt.xticks(())
    ax2.spines['right'].set_color('none')
    ax2.spines['top'].set_color('none')
    ax2.spines['bottom'].set_position(('data', 0))
    ax2.yaxis.set_ticks_position('left')

    plt.savefig('../../result/result4.png')
    plt.show()


user_deviation()