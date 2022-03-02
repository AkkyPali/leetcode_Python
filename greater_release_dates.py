D = "2020-03-01"
L1 = [
    "2020-01-21", 
    "2020-01-09",
    "2020-01-10",
    "2020-02-14",
    "2020-03-01"
]
L2 = [
    "2020-01-20", 
    "2020-04-02",
    "2020-02-08",
    "2020-03-01"
]

from datetime import datetime
def greater_release_dates(l1, l2, D):
    i = 0
    j = 0
    for ind in range(len(l1)):
        if datetime.strptime(l1[ind], '%Y-%m-%d') > datetime.strptime(D, '%Y-%m-%d'):
            i = i + 1
    
    for ind in range(len(l2)):
        if datetime.strptime(l2[ind], '%Y-%m-%d') > datetime.strptime(D, '%Y-%m-%d'):
            j = j + 1  
    if i > j:
        return l1
    else:
        return l2


