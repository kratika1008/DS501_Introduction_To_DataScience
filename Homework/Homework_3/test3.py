from problem3 import *
import sys
import numpy as np

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
    You could test the correctness of your code by typing `nosetests test2.py` in the terminal.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 3 (25 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_cosine_similarity():
    '''(5 points) cosine_similarity'''

    x = np.array([ 2.])
    y = np.array([ 3.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,1.)

    x = np.array([ 1., 1.])
    y = np.array([ 1., 1.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,1.)

    x = np.array([ 2., 2.])
    y = np.array([ 2., 2.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,1.)

    x = np.array([ 1., -1.])
    y = np.array([ -1., 1.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,-1.)

    x = np.array([ 0., 1.])
    y = np.array([ 1., 0.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,0.)

    x = np.array([ 1., 0.,1.])
    y = np.array([ 0., 1.,1.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,0.5)


    x = np.array([ 1., 0.])
    y = np.array([ 1., 1000.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,0.001)

    x = np.array([ 0., 1.])
    y = np.array([ 1000., 1.])
    S = cosine_similarity(x, y)
    assert np.allclose(S,0.001)


#-------------------------------------------------------------------------
def test_pairwise_item_sim():
    '''(5 points) pairwise_item_sim'''

    # 3 movies, 5 users 
    R = np.array( [ [   4.,   5.,   3., None,   1.],
                    [ None,   2.,   3.,   2.,   3.],
                    [   5., None,   1.,   2., None]])
    S = pairwise_item_sim(R)
    assert type(S) == np.ndarray
    assert S.shape == (3,3)
    s_true= np.array([[   1,.792,.902],
                      [.792,   1,.868],
                      [.902,.868,1   ] ])
    assert np.allclose(S,s_true,atol=0.01)



#-------------------------------------------------------------------------
def test_weighted_average():
    '''(5 points) weighted_average'''

    X = np.array( [1., 3.])
    W = np.array( [.5, .5])
    a = weighted_average(X,W)
    assert np.allclose(a,2)

    X = np.array( [1., 3.])
    W = np.array( [1., 1.])
    a = weighted_average(X,W)
    assert np.allclose(a,2)

    X = np.array( [1., 3.])
    W = np.array( [0., 1.])
    a = weighted_average(X,W)
    assert np.allclose(a,3)

    X = np.array( [1., 3.])
    W = np.array( [1., 0.])
    a = weighted_average(X,W)
    assert np.allclose(a,1)

    X = np.array( [1., 2., 3.])
    W = np.array( [1., 2., 1.])
    a = weighted_average(X,W)
    assert np.allclose(a,2)


#-------------------------------------------------------------------------
def test_predict():
    '''(10 points) predict'''

    # 3 movies, 5 users 
    R = np.array( [ [   4.,   5.,   3., None,   1.],
                    [ None,   2.,   3.,   2.,   3.],
                    [   5., None,   1.,   2., None]])
    S= np.array([[   1,.792,.902],
                 [.792,   1,.868],
                 [.902,.868,1   ] ])
    p = predict(R,S,1,0)
    assert np.allclose(p,4.5,atol=0.1)

    p = predict(R,S,2,1)
    assert np.allclose(p,3.5,atol=0.1)

    p = predict(R,S,0,3)
    assert np.allclose(p,2,atol=0.1)



