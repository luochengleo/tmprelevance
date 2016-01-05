# coding=utf8
__author__ = 'franky'

from collections import defaultdict

import sys
reload(sys)
sys.setdefaultencoding('utf8')

def loadvalidusers():
    users2config = dict()
    for l in open('../../data/validusers.txt').readlines():
        user, config = l.strip().split(' ')
        users2config[user] = config
    return users2config.keys(), users2config

def loadconfig():
    config = defaultdict(lambda:defaultdict(lambda:[]))
    for l in open('../../data/settings.csv').readlines()[1:]:
        _, config_id, task_id, satisfaction, temporal_relevance, _ = l.strip().split('\t')
        if satisfaction != 'HIDDEN':
            config[config_id][task_id] = [satisfaction, temporal_relevance]
    return config

def num_of_users_etime_sign():
    validusers, users2config = loadvalidusers()  # 用户对应的设置编号
    config = loadconfig()  # 设置编号对应的设置内容

    etime = defaultdict(lambda: defaultdict(lambda: 0))
    for l in open('../../data/timeestimation.csv'):
        user_id, task_id, est_time = l.strip().split(',')
        etime[user_id][task_id] = int(est_time) * 1000

    dtime = defaultdict(lambda: defaultdict(lambda: 0))
    for l in open('../../data/dwelltime.txt'):
        user_id, task_id, _, _, _, dwell_time = l.strip().split('\t')
        dtime[user_id][task_id] = int(dwell_time)

    num_of_etime_sign = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0, 0])
    for user in validusers:
        for task in etime[user].keys():
            if etime[user][task] > dtime[user][task]:
                num_of_etime_sign[user][0] += 1
                if config[users2config[user]][task][0] == 'SAT':
                    num_of_etime_sign[user][2] += 1
                if config[users2config[user]][task][0] == 'MIDSAT':
                    num_of_etime_sign[user][4] += 1
                if config[users2config[user]][task][0] == 'UNSAT':
                    num_of_etime_sign[user][6] += 1
            else:
                num_of_etime_sign[user][1] += 1
                if config[users2config[user]][task][0] == 'SAT':
                    num_of_etime_sign[user][3] += 1
                if config[users2config[user]][task][0] == 'MIDSAT':
                    num_of_etime_sign[user][5] += 1
                if config[users2config[user]][task][0] == 'UNSAT':
                    num_of_etime_sign[user][7] += 1

    fout = open('../../result/num_of_users_etime_sign.csv', 'w')
    fout.write('user id,config,total num of etime > dtime,total num of dtime > etime,sat num of etime > dtime,sat num of dtime > etime,midsat num of etime > dtime,midsat num of dtime > etime,unsat num of etime > dtime,unsat num of dtime > etime\n')
    for user in validusers:
        fout.write(','.join([str(item) for item in [user, users2config[user]] + num_of_etime_sign[user]]))
        fout.write('\n')
    fout.close()
# num_of_users_etime_sign()

def num_of_tasks_etime_sign():
    validusers, users2config = loadvalidusers()  # 用户对应的设置编号
    config = loadconfig()  # 设置编号对应的设置内容

    etime = defaultdict(lambda: defaultdict(lambda: 0))
    for l in open('../../data/timeestimation.csv'):
        user_id, task_id, est_time = l.strip().split(',')
        etime[user_id][task_id] = int(est_time) * 1000

    dtime = defaultdict(lambda: defaultdict(lambda: 0))
    for l in open('../../data/dwelltime.txt'):
        user_id, task_id, _, _, _, dwell_time = l.strip().split('\t')
        dtime[user_id][task_id] = int(dwell_time)

    num_of_etime_sign = defaultdict(lambda: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])  #(high or low)&(sat or midsat or unsat)&(etime>dtime or dtime>etime)
    for user in validusers:
        for task in etime[user].keys():
            if etime[user][task] > dtime[user][task]:
                if config[users2config[user]][task][1] == 'HIGH':
                    if config[users2config[user]][task][0] == 'SAT':
                        num_of_etime_sign[task][0] += 1
                    if config[users2config[user]][task][0] == 'MIDSAT':
                        num_of_etime_sign[task][2] += 1
                    if config[users2config[user]][task][0] == 'UNSAT':
                        num_of_etime_sign[task][4] += 1
                else:
                    if config[users2config[user]][task][0] == 'SAT':
                        num_of_etime_sign[task][6] += 1
                    if config[users2config[user]][task][0] == 'MIDSAT':
                        num_of_etime_sign[task][8] += 1
                    if config[users2config[user]][task][0] == 'UNSAT':
                        num_of_etime_sign[task][10] += 1
            else:
                if config[users2config[user]][task][1] == 'HIGH':
                    if config[users2config[user]][task][0] == 'SAT':
                        num_of_etime_sign[task][1] += 1
                    if config[users2config[user]][task][0] == 'MIDSAT':
                        num_of_etime_sign[task][3] += 1
                    if config[users2config[user]][task][0] == 'UNSAT':
                        num_of_etime_sign[task][5] += 1
                else:
                    if config[users2config[user]][task][0] == 'SAT':
                        num_of_etime_sign[task][7] += 1
                    if config[users2config[user]][task][0] == 'MIDSAT':
                        num_of_etime_sign[task][9] += 1
                    if config[users2config[user]][task][0] == 'UNSAT':
                        num_of_etime_sign[task][11] += 1

    fout = open('../../result/num_of_tasks_etime_sign.csv', 'w')
    fout.write('task id,high&sat num of etime > dtime,high&sat num of dtime > etime,high&midsat num of etime > dtime,high&midsat num of dtime > etime,high&unsat num of etime > dtime,high&unsat num of dtime > etime,low&sat num of etime > dtime,low&sat num of dtime > etime,low&midsat num of etime > dtime,low&midsat num of dtime > etime,low&unsat num of etime > dtime,low&unsat num of dtime > etime\n')
    for task in range(1, 21):
        fout.write(','.join([str(item) for item in [task] + num_of_etime_sign[str(task)]]))
        fout.write('\n')
    fout.close()
# num_of_tasks_etime_sign()

def user_personalization_etime_analyse():
    validusers, users2config = loadvalidusers()  # 用户对应的设置编号
    config = loadconfig()  # 设置编号对应的设置内容

    etime = defaultdict(lambda: defaultdict(lambda: 0))
    for l in open('../../data/timeestimation.csv'):
        user_id, task_id, est_time = l.strip().split(',')
        etime[user_id][task_id] = int(est_time) * 1000

    dtime = defaultdict(lambda: defaultdict(lambda: 0))
    for l in open('../../data/dwelltime.txt'):
        user_id, task_id, _, _, _, dwell_time = l.strip().split('\t')
        dtime[user_id][task_id] = int(dwell_time)

    etime_by_user = defaultdict(lambda: defaultdict(lambda: [0, 0, 0, 0, 0]))  # {user: {task: [Etime, Etime-Dtime, abs(Etime-Dtime), (Etime-Dtime)/Dtime, abs(Etime-Dtime)/Dtime]}}
    for user in validusers:
        for task in etime[user].keys():
            etime_by_user[user][task][0] = etime[user][task]
            etime_by_user[user][task][1] = etime[user][task] - dtime[user][task]
            etime_by_user[user][task][2] = abs(etime[user][task] - dtime[user][task])
            etime_by_user[user][task][3] = (etime[user][task] - dtime[user][task]) / float(dtime[user][task])
            etime_by_user[user][task][4] = abs(etime[user][task] - dtime[user][task]) / float(dtime[user][task])

    fout = open('../../result/user_personalization_etime_analyse.csv', 'w')
    fout.write('user id,config id,task id,Etime,Etime-Dtime,abs(Etime-Dtime),(Etime-Dtime)/Dtime,abs(Etime-Dtime)/Dtime\n')
    for user in validusers:
        for task in etime[user].keys():
            fout.write(','.join([str(item) for item in [user, users2config[user], task] + etime_by_user[user][task]]))
            fout.write('\n')
    fout.close()
user_personalization_etime_analyse()
