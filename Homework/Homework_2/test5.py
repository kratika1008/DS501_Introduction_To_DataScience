from problem5 import *
import sys
import numpy as np

'''
    Unit test 5:
    This file includes unit tests for problem5.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 5 (10 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_batting_average():
    '''(2 points) batting_average'''

    BA = batting_average(3, 17)

    # test whether or not the result is a float number 
    #assert type(BA) == float 

    # check the correctness of the result 
    assert np.allclose(BA, .1765, atol = 1e-3)

    BA = batting_average(672, 9079)
    assert np.allclose(BA, .074, atol = 1e-3)


#-------------------------------------------------------------------------
def test_on_base_percentage():
    '''(2 points) on_base_percentage'''

    OBP = on_base_percentage(3, 37, 29, 5, 2)

    # test whether or not the result is a float number 
    #assert type(OBP) == float 

    # check the correctness of the result 
    assert np.allclose(OBP, .507, atol = 1e-3)


    OBP = on_base_percentage(2, 35, 28, 6, 1)
    assert np.allclose(OBP, .514, atol = 1e-3)


#-------------------------------------------------------------------------
def test_slugging_percentage():
    '''(2 points) slugging_percentage'''

    SLG = slugging_percentage(11, 12, 13, 14, 123)

    # test whether or not the result is a float number 
    #assert type(SLG) == float 

    # check the correctness of the result 
    assert np.allclose(SLG, .7398, atol = 1e-3)


    SLG = slugging_percentage(12, 13, 14,15, 234)
    assert np.allclose(SLG, .4188, atol = 1e-3)



#-------------------------------------------------------------------------
def test_runs_created():
    '''(2 points) runs_created'''

    RC = runs_created(11, 12, 13, 14, 15, 123)

    # test whether or not the result is a float number 
    #assert type(RC) == float 

    # check the correctness of the result 
    assert np.allclose(RC, 17.145, atol = 1e-2)


    RC = runs_created(12, 13, 14,15,16, 234)
    assert np.allclose(RC, 10.976, atol = 1e-3)


#-------------------------------------------------------------------------
def test_win_ratio():
    '''(2 points) win_ratio'''

    WR = win_ratio(884,645) # this is the goal of OAK team in year 2002.

    # test whether or not the result is a float number 
    #assert type(WR) == float 

    # check the correctness of the result 
    assert np.allclose(WR, .6526, atol = 1e-3)




