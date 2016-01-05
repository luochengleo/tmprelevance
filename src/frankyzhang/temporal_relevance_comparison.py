# coding=utf8
__author__ = 'zhangfan'
import numpy as np
from collections import defaultdict
import sqlite3
from numpy import mean
import re

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def loadValidUsers():
    u2config = dict()
    for l in open('../../data/validusers.txt').readlines():
        u, config = l.strip().split(' ')
        u2config[u] = config
    return u2config.keys(), u2config

def loadConfig():
    config = defaultdict(lambda: defaultdict(lambda: []))
    for l in open('../../data/settings.csv').readlines()[1:]:
        _, configid, taskid, option, temporal, _ = l.strip().split('\t')
        if option != 'HIDDEN':
            config[configid][taskid] = [option, temporal]
    return config

def analysis_difference_on_temporal_relevance():
    config = loadConfig()
    validusers, u2config = loadValidUsers()
    difference = defaultdict(lambda: {})
    deviation_ratio = defaultdict(lambda: {})
    for l in open('../../data/dwelltime.txt').readlines():
        studentid, taskid, _, _, _, dtime = l.strip().split('\t')
        configid = u2config[studentid]
        difference[configid][taskid] = int(dtime)
    for l in open('../../data/timeestimation.csv').readlines():
        studentid, taskid, etime = l.strip().split(',')
        configid = u2config[studentid]
        deviation_ratio[configid][taskid] = (int(etime) * 1000 - difference[configid][taskid]) / float(difference[configid][taskid])
        difference[configid][taskid] = int(etime) * 1000 - difference[configid][taskid]
    fout = open('../../result/temporal_relevance_comparison_difference.csv', 'w')
    for configid in difference.keys():
        for taskid in difference[configid].keys():
            fout.write(','.join(str(item) for item in [configid, taskid, difference[configid][taskid]]))
            fout.write('\n')
    fout.close()
    fout = open('../../result/temporal_relevance_comparison_deviation_ratio.csv', 'w')
    for configid in difference.keys():
        for taskid in difference[configid].keys():
            fout.write(','.join(str(item) for item in [configid, taskid, deviation_ratio[configid][taskid]]))
            fout.write('\n')
    fout.close()

# analysis_difference_on_temporal_relevance()

def time_comparison():
    config = loadConfig()
    validusers, u2config = loadValidUsers()
    dwelltime = defaultdict(lambda: {})
    estimatedtime = defaultdict(lambda: {})
    for l in open('../../data/dwelltime.txt').readlines():
        studentid, taskid, _, _, _, dtime = l.strip().split('\t')
        configid = u2config[studentid]
        dwelltime[configid][taskid] = int(dtime)
    for l in open('../../data/timeestimation.csv').readlines():
        studentid, taskid, etime = l.strip().split(',')
        configid = u2config[studentid]
        estimatedtime[configid][taskid] = int(etime) * 1000
    fout = open('../../result/time_comparison.csv', 'w')
    for configid in dwelltime.keys():
        for taskid in dwelltime[configid].keys():
            fout.write(','.join(str(item) for item in [configid, taskid, dwelltime[configid][taskid], estimatedtime[configid][taskid]]))
            fout.write('\n')
    fout.close()

# time_comparison()

def comparison_by_task():
    high_average = defaultdict(lambda: defaultdict(lambda: []))
    low_average = defaultdict(lambda: defaultdict(lambda: []))
    for l in open('../../result/time_comparison.csv').readlines():
        configid, taskid, dwelltime, estimatetime = l.strip().split(',')
        if int(configid) <= 25:
            high_average[taskid]['dtime'].append(int(dwelltime))
            high_average[taskid]['etime'].append(int(estimatetime))
        else:
            low_average[taskid]['dtime'].append(int(dwelltime))
            low_average[taskid]['etime'].append(int(estimatetime))
    fout = open('../../result/comparison_by_task.csv', 'w')
    for taskid in high_average.keys():
        for timetype in high_average[taskid].keys():
            fout.write(','.join(str(item) for item in [taskid, timetype, mean(high_average[taskid][timetype]), np.std(high_average[taskid][timetype]), mean(low_average[taskid][timetype]), np.std(low_average[taskid][timetype])]))
            fout.write('\n')
    fout.close()

comparison_by_task()

def comparison_by_config():
    high_average = defaultdict(lambda: defaultdict(lambda: []))
    low_average = defaultdict(lambda: defaultdict(lambda: []))
    for l in open('../../result/time_comparison.csv').readlines():
        configid, taskid, dwelltime, estimatetime = l.strip().split(',')
        if int(configid) <= 25:
            high_average[configid]['dtime'].append(int(dwelltime))
            high_average[configid]['etime'].append(int(estimatetime))
        else:
            low_average[configid]['dtime'].append(int(dwelltime))
            low_average[configid]['etime'].append(int(estimatetime))
    fout = open('../../result/comparison_by_config.csv', 'w')
    for configid in high_average.keys():
        for timetype in high_average[configid].keys():
            fout.write(','.join(str(item) for item in [configid, timetype, mean(high_average[configid][timetype]), mean(low_average[str(int(configid) + 25)][timetype])]))
            fout.write('\n')
    fout.close()

# comparison_by_config()

