from problem6 import *
import sys
import numpy as np
from problem3 import load_csv
import pandas as pd

'''
    Unit test 6:
    This file includes unit tests for problem6.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 5 (15 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_sum_salaries():
    '''(2 points) sum_salaries'''

    # test with a team of one player
    T=['bradfch01' ] 
    D= load_csv('Batting2001AJS.csv')

    S = sum_salaries(T,D)
    assert S == 235000

    T=[
        'bradfch01', 
        'chaveer01',
        'colanmi01'
        ] 

    S = sum_salaries(T,D)
    print(S)
    assert S == 2660000 




#-------------------------------------------------------------------------
def test_sum_stat():
    '''(2 points) sum_stat'''

    # test with a team of one player
    T=['hernara02' ] 
    D= load_csv('Batting2001AJS.csv')

    S = sum_stat(T,D, key='H')
    assert S == 115

    T=[
        'hernara02',
        'hattesc01'
        ] 

    S = sum_stat(T,D,key='H')
    assert S == (115+68) 

    S = sum_stat(T,D,key='G')
    assert S == (136+94) 


#-------------------------------------------------------------------------
def test_runs():
    '''(2 points) runs'''

    # test with a team of one player
    T=['hernara02' ] 
    D= load_csv('Batting2001AJS.csv')

    R = runs(T,D)
    assert np.allclose(R,57.3877,atol=0.01) 

    T=[
        'hernara02',
        'hattesc01'
        ] 

    R = runs(T,D)
    assert np.allclose(R,88.7553,atol=0.01) 



#-------------------------------------------------------------------------
def test_scout():
    '''(3 points) scout'''

    # new players to hire
    x = scout()
   
    # current members of the team 
    y = [
        'bradfch01', # OAK 2002 
        'chaveer01',
        'colanmi01',
        'dyeje01',
        'hernara02',
        'hiljuer01',
        'holtzmi01',
        'hudsoti01',
        'kochbi01',
        'lidleco01',
        'longte01',
        'magnami01',
        'mecirji01',
        'menecfr01',
        'muldema01',
        'myersgr01',
        'penaca01',
        'saenzol01',
        'tamje01',
        'tejadmi01',
        'valdema02',
        'velarra01',
        'venafmi01',
        'zitoba01'
    ]

    assert type(x) == list 
    assert type(x[0]) == str
    assert len(x)== 3 # only choose 3 players 

    # the hires should not be in the team already
    assert x[0] not in y
    assert x[1] not in y
    assert x[2] not in y

    # cannot hire the same player twice
    assert x[0] != x[1]
    assert x[0] != x[2]
    assert x[1] != x[2]

    # the new team
    T = x+y

    # check budget
    D= load_csv('Batting2001AJS.csv')
    S = sum_salaries(T,D)
    print('salaries:',S)
    assert S <= 40004167 # too expensive, exceed budget

    # the expected number of runs by the team should be larger than 700
    print('runs:', runs(T,D))
    assert runs(T,D) >= 700 


#-------------------------------------------------------------------------
def test_rank_BA():
    '''(3 points) rank_BA'''

    D= load_csv('Batting2001AJS.csv')

    R = rank_BA(D)
    assert type(R)==list
    assert len(R) == 786 


    assert R[0] == 'berkmla01'
    assert R[1] == 'pujolal01'
    assert R[2] == 'pierrju01'
    assert R[3] == 'loducpa01'
    assert R[4] == 'millake01'





#-------------------------------------------------------------------------
def test_rank_OBP():
    '''(3 points) rank_OBP'''

    D= load_csv('Batting2001AJS.csv')

    R = rank_OBP(D)
    assert type(R)==list
    assert len(R) == 786 

    assert R[0] == 'berkmla01'
    assert R[1] == 'pujolal01'
    assert R[2] == 'giambje01' # OAK team hired Jeremy Giambi in 2002
    assert R[3] == 'mientdo01'
    assert R[4] == 'pierrju01'



