# coding=utf8
__author__ = 'zhangfan'

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import ttest_ind
plt.rc('text', usetex=True)


def compare_difference():
    high_dtime = []
    high_etime = []
    low_dtime = []
    low_etime = []
    font = {
        'family': 'Times New Roman',
        'weight': 'normal',
        'size': 16,
    }
    for l in open('../../result/time_comparison.csv').readlines():
        configid, taskid, dtime, etime = l.strip().split(',')
        if int(configid) <= 25 and (int(taskid) < 11 or int(taskid) > 14):
            high_dtime.append(int(dtime))
            high_etime.append(int(etime))
        if int(configid) > 25 and (int(taskid) < 11 or int(taskid) > 14):
            low_dtime.append(int(dtime))
            low_etime.append(int(etime))
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    low_dtime_mean = np.mean(low_dtime)
    low_etime_mean = np.mean(low_etime)
    print low_dtime_mean, low_etime_mean
    print ttest_ind(low_dtime, low_etime, equal_var=False)
    plt.boxplot([low_dtime, low_etime])
    ax1.set_title('control group')
    ax1.set_ylabel('time(s)')
    ax1.set_xticklabels(('dtime', 'ptime'))
    ax1.set_yticklabels(('0', '100', '200', '300', '400', '500'))
    plt.ylim(0, 600000)
    plt.scatter([1, ], [low_dtime_mean, ], 10, color='black')
    plt.annotate(str(int(low_dtime_mean)/1000), xy=(1, low_dtime_mean), xycoords='data', xytext=(+10, -3), textcoords='offset points', fontsize=10)
    plt.scatter([2, ], [low_etime_mean, ], 10, color='black')
    plt.annotate(str(int(low_etime_mean)/1000), xy=(2, low_etime_mean), xycoords='data', xytext=(+10, -3), textcoords='offset points', fontsize=10)
    plt.figtext(0.83, 0.128, '.', color='black', weight='roman', size=30)
    plt.figtext(0.84, 0.123, 'Mean', color='black', weight='roman', size=10)
    plt.figtext(0.41, 0.128, '.', color='black', weight='roman', size=30)
    plt.figtext(0.42, 0.123, 'Mean', color='black', weight='roman', size=10)
    ax2 = fig.add_subplot(122)
    high_dtime_mean = np.mean(high_dtime)
    high_etime_mean = np.mean(high_etime)
    print high_dtime_mean, high_etime_mean
    print ttest_ind(high_dtime, high_etime, equal_var=False)
    plt.boxplot([high_dtime, high_etime])
    ax2.set_title('treatment group')
    ax2.set_xticklabels(('dtime', 'ptime'))
    ax2.set_yticklabels(())
    plt.ylim(0, 600000)
    plt.scatter([1, ], [high_dtime_mean, ], 10, color='black')
    plt.annotate(str(int(high_dtime_mean)/1000), xy=(1, high_dtime_mean), xycoords='data', xytext=(+10, -3), textcoords='offset points', fontsize=10)
    plt.scatter([2, ], [low_etime_mean, ], 10, color='black')
    plt.annotate(str(int(high_etime_mean)/1000), xy=(2, high_etime_mean), xycoords='data', xytext=(+10, -5), textcoords='offset points', fontsize=10)
    plt.savefig('../../result/result1.eps')
    plt.show()

#compare_difference()

def result2():
    highdtime = []
    highdtimestd = []
    highetime = []
    highetimestd = []
    lowdtime = []
    lowdtimestd = []
    lowetime = []
    lowetimestd = []
    for i in range(0, 16):
        highdtime.append(0)
        highdtimestd.append(0)
        highetime.append(0)
        highetimestd.append(0)
        lowdtime.append(0)
        lowdtimestd.append(0)
        lowetime.append(0)
        lowetimestd.append(0)
    for l in open('../../result/comparison_by_task.csv').readlines():
        taskid, timetype, hightime, highstd, lowtime, lowstd = l.strip().split(',')
        if int(taskid) < 11:
            if timetype == 'dtime':
                highdtime[int(taskid) - 1] = float(hightime)
                highdtimestd[int(taskid) - 1] = float(highstd)
                lowdtime[int(taskid) - 1] = float(lowtime)
                lowdtimestd[int(taskid) - 1] = float(lowstd)
            else:
                highetime[int(taskid) - 1] = float(hightime)
                highetimestd[int(taskid) - 1] = float(highstd)
                lowetime[int(taskid) - 1] = float(lowtime)
                lowetimestd[int(taskid) - 1] = float(lowstd)
        if int(taskid) > 14:
            if timetype == 'dtime':
                highdtime[int(taskid) - 5] = float(hightime)
                highdtimestd[int(taskid) - 5] = float(highstd)
                lowdtime[int(taskid) - 5] = float(lowtime)
                lowdtimestd[int(taskid) - 5] = float(lowstd)
            else:
                highetime[int(taskid) - 5] = float(hightime)
                highetimestd[int(taskid) - 5] = float(highstd)
                lowetime[int(taskid) - 5] = float(lowtime)
                lowetimestd[int(taskid) - 5] = float(lowstd)
    fig = plt.figure()

    ax1 = fig.add_subplot(211)
    index = np.arange(16)
    bar_width = 0.3
    opacity = 0.4
    rects1 = plt.bar(index, lowdtime, bar_width, alpha=opacity, color='b', yerr=lowdtimestd, label='dtime')
    rects2 = plt.bar(index + bar_width, lowetime, bar_width, alpha=opacity, color='r', yerr=lowetimestd, label='ptime')
    plt.title('control group')
    plt.xticks(index + bar_width, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'))
    plt.ylabel('time(s)')
    ax1.set_yticklabels(('0', '100', '200', '300', '400', '500', '600', '700'))
    plt.legend(loc='upper left')

    ax2 = fig.add_subplot(212)
    index = np.arange(16)
    bar_width = 0.3
    opacity = 0.4
    rects1 = plt.bar(index, highdtime, bar_width, alpha=opacity, color='b', yerr=highdtimestd, label='dtime')
    rects2 = plt.bar(index + bar_width, highetime, bar_width, alpha=opacity, color='r', yerr=highetimestd, label='ptime')
    plt.title('treatment group')
    plt.xticks(index + bar_width, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'))
    plt.ylabel('time(s)')
    plt.ylim(0, 600000)
    ax2.set_yticklabels(('0', '100', '200', '300', '400', '500', '600', '700'))

    plt.savefig('../../result/result2.eps')
    plt.show()

#result2()

def result3():
    highlong = []
    highshort = []
    lowlong = []
    lowshort = []
    for i in range(0, 16):
        highlong.append(0)
        highshort.append(0)
        lowlong.append(0)
        lowshort.append(0)
    for l in open('../../result/num_of_tasks_etime_sign.csv').readlines()[1:]:
        taskid, hsl, hss, hml, hms, hul, hus, lsl, lss, lml, lms, lul, lus = l.strip().split(',')
        if int(taskid) < 11:
            highlong[int(taskid) - 1] = (int(hsl) + int(hml) + int(hul)) / 15.0
            highshort[int(taskid) - 1] = (int(hss) + int(hms) + int(hus)) /15.0
            lowlong[int(taskid) - 1] = (int(lsl) + int(lml) + int(lul)) / 15.0
            lowshort[int(taskid) - 1] = (int(lss) + int(lms) + int(lus)) / 15.0
        if int(taskid) > 14:
            highlong[int(taskid) - 5] = (int(hsl) + int(hml) + int(hul)) / 15.0
            highshort[int(taskid) - 5] = (int(hss) + int(hms) + int(hus)) / 15.0
            lowlong[int(taskid) - 5] = (int(lsl) + int(lml) + int(lul)) / 15.0
            lowshort[int(taskid) - 5] = (int(lss) + int(lms) + int(lus)) / 15.0
    index = np.arange(16)
    bar_width = 0.3
    opacity = 0.4
    plt.figure(figsize=(12, 8))
    plowlong = plt.bar(index, lowlong, bar_width, alpha=opacity, color='b', label=r'control: dtime $\textless$ ptime')
    plowshort = plt.bar(index, lowshort, bar_width, alpha=opacity, bottom=lowlong, color='r', label=r'control: dtime $\textgreater$ ptime')
    phighlong = plt.bar(index + bar_width, highlong, bar_width, alpha=opacity, color='y', label=r'treatment: dtime $\textless$ ptime')
    phighshort = plt.bar(index + bar_width, highshort, bar_width, alpha=opacity, bottom=highlong, color='k', label=r'treatment: dtime $\textgreater$ ptime')

    '''plowlong = plt.bar(index, lowlong, bar_width, alpha=opacity, color='b', label=r'dtime')
    plowshort = plt.bar(index, lowshort, bar_width, alpha=opacity, bottom=lowlong, color='r', label=r'dtime')
    phighlong = plt.bar(index + bar_width, highlong, bar_width, alpha=opacity, color='y', label=r'ptimedddddddddddddddddddddddd')
    phighshort = plt.bar(index + bar_width, highshort, bar_width, alpha=opacity, bottom=highlong, color='k', label=r'ptimeddddddddddd')'''

    plt.xticks(index + bar_width, ('1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'))
    plt.xlabel('task', fontsize=16)
    plt.ylabel('')
    plt.yticks()
    plt.legend(bbox_to_anchor=(0., 1., 1., .1), loc="upper left", ncol=2, mode="expand", borderaxespad=0., prop={'size': 18})
    plt.savefig('../../result/result3.eps')
    plt.show()

result3()
