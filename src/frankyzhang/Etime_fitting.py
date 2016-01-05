# coding=utf8
__author__ = 'zhangfan'
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

def dwelltime_by_result_extraction():
    validusers, u2config = loadValidUsers()

    dwelltime_by_result = defaultdict(lambda: defaultdict(lambda: {}))
    cx = sqlite3.connect("../../db.sqlite3")
    cu = cx.cursor()
    cu.execute('select * from anno_annotation')
    while True:
        logitem  = cu.fetchone()
        if logitem == None:
            break
        studentid = logitem[1]
        taskid = logitem[2]
        result = int(logitem[4][3])
        score = int(logitem[6])
        if studentid in validusers:
            dwelltime_by_result[studentid][taskid][result] = [-1, score]

    cx = sqlite3.connect("../../db.sqlite3")
    cu = cx.cursor()
    cu.execute('select * from anno_log')
    while True:
        logitem = cu.fetchone()
        if logitem == None:
            break
        studentid = logitem[1]
        taskid = logitem[2]
        action = logitem[3]
        content = logitem[5]
        if studentid in validusers and action == 'CLICK':
            result = int(content.split('\t')[7].split('=')[1][3])
            rank = int(content.split('\t')[9].split('=')[1])
            time_jump_out = 0
            time_jump_in = 0
            '''while True:
                logitem2 = cu.fetchone()
                if logitem2 == None:
                    break
                studentid2 = logitem2[1]
                taskid2 = logitem2[2]
                action2 = logitem2[3]
                content2 = logitem2[5]
                if studentid2 == studentid and taskid2 == taskid and action2 == 'JUMP_OUT':
                    time_jump_out = int(content2.split('\t')[0].split('=')[1])
                if studentid2 == studentid and taskid2 == taskid and action2 == 'JUMP_IN':
                    time_jump_in = int(content2.split('\t')[0].split('=')[1])
                    break
            '''
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
            print studentid, taskid, result, rank
            if result in dwelltime_by_result[studentid][taskid].keys():
                dwelltime_by_result[studentid][taskid][result][0] = time
            else:
                if rank in dwelltime_by_result[studentid][taskid].keys():
                    dwelltime_by_result[studentid][taskid][rank][0] = time

    fout = open('../../data/dwelltime_by_result.txt','w')
    for user in dwelltime_by_result.keys():
        for task in dwelltime_by_result[user].keys():
            fout.write(str(user) + '\t' + str(task) + '\t')
            for result in dwelltime_by_result[user][task].keys():
                fout.write(str(dwelltime_by_result[user][task][result][0]) + '\t' + str(dwelltime_by_result[user][task][result][1]) + '\t')
            fout.write('\n')
    fout.close()

dwelltime_by_result_extraction()
