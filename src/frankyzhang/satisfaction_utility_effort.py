# coding=utf8
__author__ = 'zhangfan'

from scipy.stats.stats import pearsonr
from collections import defaultdict
import math
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def compute_pearsonr_raw_clicks_log():
    satisfaction = defaultdict(lambda: {})
    for l in open('../../data/querysat.txt').readlines():
        studentid, taskid, sat = l.strip().split('\t')
        satisfaction[studentid][taskid] = int(sat)

    num_of_clicks = defaultdict(lambda: {})
    for l in open('../../data/numofclicks.txt').readlines():
        studentid, taskid, clicks = l.strip().split('\t')
        num_of_clicks[studentid][taskid] = int(clicks)

    log_dtime = defaultdict(lambda: {})
    for l in open('../../data/dwelltime.txt').readlines():
        studentid, taskid, _, _, _, dtime = l.strip().split('\t')
        log_dtime[studentid][taskid] = float(int(dtime))

    log_etime = defaultdict(lambda: {})
    for l in open('../../data/timeestimation.csv').readlines():
        studentid, taskid, etime = l.strip().split(',')
        log_etime[studentid][taskid] = float(int(etime) * 1000)

    satisfaction_list = []
    utility_divided_by_dtime_list = []
    utility_divided_by_etime_list = []
    for student in satisfaction.keys():
        for task in satisfaction[student].keys():
            if task in num_of_clicks[student].keys() and task in log_dtime[student].keys() and task in log_etime[student].keys():
                satisfaction_list.append(satisfaction[student][task])
                utility_divided_by_dtime_list.append(num_of_clicks[student][task] / log_dtime[student][task])
                utility_divided_by_etime_list.append(num_of_clicks[student][task] / log_etime[student][task])
    print pearsonr(satisfaction_list, utility_divided_by_dtime_list)
    print pearsonr(satisfaction_list, utility_divided_by_etime_list)

compute_pearsonr_raw_clicks_log()

def compute_pearsonr_zscore_clicks_log():
    satisfaction = defaultdict(lambda: {})
    for l in open('../../data/satisfaction_zscore.txt').readlines():
        studentid, taskid, sat = l.strip().split('\t')
        satisfaction[studentid][taskid] = float(sat)

    num_of_clicks = defaultdict(lambda: {})
    for l in open('../../data/numofclicks.txt').readlines():
        studentid, taskid, clicks = l.strip().split('\t')
        num_of_clicks[studentid][taskid] = int(clicks)

    log_dtime = defaultdict(lambda: {})
    for l in open('../../data/dwelltime.txt').readlines():
        studentid, taskid, _, _, _, dtime = l.strip().split('\t')
        log_dtime[studentid][taskid] = float(int(dtime))

    log_etime = defaultdict(lambda: {})
    for l in open('../../data/timeestimation.csv').readlines():
        studentid, taskid, etime = l.strip().split(',')
        log_etime[studentid][taskid] = float(int(etime) * 1000)

    satisfaction_list = []
    utility_divided_by_dtime_list = []
    utility_divided_by_etime_list = []
    for student in satisfaction.keys():
        for task in satisfaction[student].keys():
            if task in num_of_clicks[student].keys() and task in log_dtime[student].keys() and task in log_etime[student].keys():
                satisfaction_list.append(satisfaction[student][task])
                utility_divided_by_dtime_list.append(num_of_clicks[student][task] / log_dtime[student][task])
                utility_divided_by_etime_list.append(num_of_clicks[student][task] / log_etime[student][task])
    print pearsonr(satisfaction_list, utility_divided_by_dtime_list)
    print pearsonr(satisfaction_list, utility_divided_by_etime_list)

compute_pearsonr_zscore_clicks_log()

def compute_pearsonr_raw_satisfiedclicks_log():
    satisfaction = defaultdict(lambda: {})
    for l in open('../../data/querysat.txt').readlines():
        studentid, taskid, sat = l.strip().split('\t')
        satisfaction[studentid][taskid] = int(sat)

    num_of_clicks = defaultdict(lambda: {})
    for l in open('../../data/num_of_satisfied_clicks.txt').readlines():
        studentid, taskid, clicks = l.strip().split('\t')
        num_of_clicks[studentid][taskid] = int(clicks)

    log_dtime = defaultdict(lambda: {})
    for l in open('../../data/dwelltime.txt').readlines():
        studentid, taskid, _, _, _, dtime = l.strip().split('\t')
        log_dtime[studentid][taskid] = float(int(dtime))

    log_etime = defaultdict(lambda: {})
    for l in open('../../data/timeestimation.csv').readlines():
        studentid, taskid, etime = l.strip().split(',')
        log_etime[studentid][taskid] = float(int(etime) * 1000)

    satisfaction_list = []
    utility_divided_by_dtime_list = []
    utility_divided_by_etime_list = []
    for student in satisfaction.keys():
        if student in num_of_clicks.keys():
            for task in satisfaction[student].keys():
                if task in num_of_clicks[student].keys() and task in log_dtime[student].keys() and task in log_etime[student].keys():
                    satisfaction_list.append(satisfaction[student][task])
                    utility_divided_by_dtime_list.append(num_of_clicks[student][task] / log_dtime[student][task])
                    utility_divided_by_etime_list.append(num_of_clicks[student][task] / log_etime[student][task])
    print pearsonr(satisfaction_list, utility_divided_by_dtime_list)
    print pearsonr(satisfaction_list, utility_divided_by_etime_list)

compute_pearsonr_raw_satisfiedclicks_log()

def compute_pearsonr_zscore_satisfiedclicks_log():
    satisfaction = defaultdict(lambda: {})
    for l in open('../../data/satisfaction_zscore.txt').readlines():
        studentid, taskid, sat = l.strip().split('\t')
        satisfaction[studentid][taskid] = float(sat)

    num_of_clicks = defaultdict(lambda: {})
    for l in open('../../data/num_of_satisfied_clicks.txt').readlines():
        studentid, taskid, clicks = l.strip().split('\t')
        num_of_clicks[studentid][taskid] = int(clicks)

    log_dtime = defaultdict(lambda: {})
    for l in open('../../data/dwelltime.txt').readlines():
        studentid, taskid, _, _, _, dtime = l.strip().split('\t')
        log_dtime[studentid][taskid] = float(int(dtime))

    log_etime = defaultdict(lambda: {})
    for l in open('../../data/timeestimation.csv').readlines():
        studentid, taskid, etime = l.strip().split(',')
        log_etime[studentid][taskid] = float(int(etime) * 1000)

    satisfaction_list = []
    utility_divided_by_dtime_list = []
    utility_divided_by_etime_list = []
    for student in satisfaction.keys():
        if student in num_of_clicks.keys():
            for task in satisfaction[student].keys():
                if task in num_of_clicks[student].keys() and task in log_dtime[student].keys() and task in log_etime[student].keys():
                    satisfaction_list.append(satisfaction[student][task])
                    utility_divided_by_dtime_list.append(num_of_clicks[student][task] / log_dtime[student][task])
                    utility_divided_by_etime_list.append(num_of_clicks[student][task] / log_etime[student][task])
    print pearsonr(satisfaction_list, utility_divided_by_dtime_list)
    print pearsonr(satisfaction_list, utility_divided_by_etime_list)

compute_pearsonr_zscore_satisfiedclicks_log()
