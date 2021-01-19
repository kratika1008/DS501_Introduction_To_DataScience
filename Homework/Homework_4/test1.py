from problem1 import *
import numpy as np
import sys

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
'''


#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (10 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_compute_eigen_pairs():
    '''(5 points) compute_eigen_pairs'''

    X= np.diag((1, 2, 3)) 
    P = compute_eigen_pairs(X)

    assert len(P) == 3
    v,e = P[0] 
    assert type(e) == np.ndarray
    assert len(e) == 3

    c = 0
    for p in P:
        v,e = p
        if v == 1.:
            assert np.allclose(e,[1,0,0]) or  np.allclose(-e,[1,0,0])
            c+=1
        elif v==2.:
            assert np.allclose(e,[0,1,0]) or np.allclose(-e,[0,1,0]) 
            c+=1
        elif v==3.:
            assert np.allclose(e,[0,0,1]) or np.allclose(-e,[0,0,1]) 
            c+=1
        else:
            assert False  # incorrect eigen pair
    assert c ==3 # should return all 3 eigen pairs


    # a 2x2 matrix with two eigen pairs
    v1 = 10
    e1 = np.array([1.,1.])
    e1 = e1/np.linalg.norm(e1)
    v2 = 6 
    e2 = np.array([-1.,1.])
    e2 = e2/np.linalg.norm(e2)
    X = 5* np.ones(2) + 3 * np.array([[1,-1],[-1,1]]) 

    P = compute_eigen_pairs(X)
    assert len(P) == 2
    v,e = P[0] 
    assert len(e) == 2

    c = 0
    for p in P:
        v,e = p
        if v==6.:
            assert np.allclose(e,e2) or np.allclose(e,-e2)
            c+=1
        elif v == 10.:
            assert np.allclose(e,e1) or np.allclose(e,-e1) 
            c+=1
        else:
            assert False  # incorrect eigen pair
    assert c ==2 # should return all 2 eigen pairs



#-------------------------------------------------------------------------
def test_sort_eigen_pairs():
    '''(5 points) sort_eigen_pairs'''
    e1 = np.array([1.,0.,0.])
    e2 = np.array([0.,1.,0.])
    e3 = np.array([0.,0.,1.])
    P = [(2., e1),
         (1., e2),
         (3., e3)]

    Ps = sort_eigen_pairs(P) 

    assert len(Ps) ==3
    v,e = Ps[0]
    assert v == 1. 
    assert np.allclose(e,[0,1,0]) 
    
    v,e = Ps[1]
    assert v == 2. 
    assert np.allclose(e,[1,0,0]) 

    v,e = Ps[2]
    assert v == 3. 
    assert np.allclose(e,[0,0,1]) 

    Ps = sort_eigen_pairs(P, order = 'descending') 

    assert len(Ps) ==3
    v,e = Ps[2]
    assert v == 1. 
    assert np.allclose(e,[0,1,0]) 
    
    v,e = Ps[1]
    assert v == 2. 
    assert np.allclose(e,[1,0,0]) 

    v,e = Ps[0]
    assert v == 3. 
    assert np.allclose(e,[0,0,1]) 










