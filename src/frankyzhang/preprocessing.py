# coding=utf8
__author__ = 'zhangfan'

from collections import defaultdict
import sqlite3
import numpy
import sys
reload(sys)
sys.setdefaultencoding('utf8')

def loadValidUsers():
    u2config = dict()
    for l in open('../../data/validusers.txt').readlines():
        u, config = l.strip().split(' ')
        u2config[u] = config
    return u2config.keys(), u2config

def satisfaction_zscore():
    satisfaction = defaultdict(lambda: {})
    for l in open('../../data/querysat.txt').readlines():
        studentid, taskid, sat = l.strip().split('\t')
        satisfaction[studentid][taskid] = int(sat)
    print satisfaction
    zscore = defaultdict(lambda: {})
    for studentid in satisfaction.keys():
        sat_list = []
        for taskid in satisfaction[studentid].keys():
            sat_list.append(satisfaction[studentid][taskid])
        mean = numpy.mean(sat_list)
        std = numpy.std(sat_list)
        for taskid in satisfaction[studentid].keys():
            zscore[studentid][taskid] = (satisfaction[studentid][taskid] - mean) / std
    print zscore
    fout = open('../../data/satisfaction_zscore.txt', 'w')
    for studentid in zscore.keys():
        for taskid in zscore[studentid].keys():
            fout.write('\t'.join([str(item) for item in [studentid, taskid, zscore[studentid][taskid]]]))
            fout.write('\n')
    fout.close()

# satisfaction_zscore()

def satisfied_click():
    validusers, u2config = loadValidUsers()
    num_of_satisfied_clicks = defaultdict(lambda: defaultdict(lambda: 0))
    cx = sqlite3.connect('../../db.sqlite3')
    cu = cx.execute('select * from anno_log')
    while True:
        logitem = cu.fetchone()
        if logitem == None:
            break
        studentid = logitem[1]
        taskid = logitem[2]
        action = logitem[3]
        if action == 'CLICK' and studentid in validusers:
            time_jump_out = 0
            time_jump_in = 0
            while True:
                logitem = cu.fetchone()
                if logitem == None:
                    break
                action = logitem[3]
                if action == 'JUMP_OUT':
                    time_jump_out = int(logitem[5].split('\t')[0].split('=')[1])
                    break
            while True:
                logitem = cu.fetchone()
                if logitem == None:
                    break
                action = logitem[3]
                if action == 'JUMP_IN':
                    time_jump_in = int(logitem[5].split('\t')[0].split('=')[1])
                    break
            time = time_jump_in - time_jump_out
            if time > 30000:
                num_of_satisfied_clicks[studentid][taskid] += 1

    fout = open('../../data/num_of_satisfied_clicks.txt', 'w')
    for studentid in num_of_satisfied_clicks.keys():
        for taskid in num_of_satisfied_clicks[studentid].keys():
            fout.write('\t'.join([str(studentid), str(taskid), str(num_of_satisfied_clicks[studentid][taskid])]))
            fout.write('\n')
    fout.close()

satisfied_click()
