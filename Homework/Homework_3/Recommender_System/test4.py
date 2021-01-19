from problem4 import *
import sys
import numpy as np

'''
    Unit test 4:
    This file includes unit tests for problem4.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 4 (10 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)



#-------------------------------------------------------------------------
def test_pairwise_user_sim():
    '''(5 points) pairwise_user_sim'''


    # 2 movies, 3 users 
    R = np.array( [ [1., 1., 1.],
                    [1., 1., 1.]])
    S = pairwise_user_sim(R)
    assert type(S) == np.ndarray
    assert S.shape == (3,3)
    print(S)
    assert np.allclose(S,np.ones((3,3)))

    # 2 movies, 2 users 
    R = np.array( [ [1., 0.],
                    [0., 4.]])
    S = pairwise_user_sim(R)
    assert type(S) == np.ndarray
    assert S.shape == (2,2)
    s_true = [[1.,0.],
              [0.,1.] ]
    assert np.allclose(S,s_true,atol=1e-3)


    # 2 movies, 2 users 
    R = np.array( [ [5., 1.],
                    [1., 5.]])
    S = pairwise_user_sim(R)
    assert type(S) == np.ndarray
    assert S.shape == (2,2)
    s_true = [[1.,0.38461538],
              [0.38461538,1.] ]
    assert np.allclose(S,s_true,atol=1e-3)


    # 5 movies, 3 users 
    R = np.array( [ [   4.,   5.,   3., None,   1.],
                    [ None,   2.,   3.,   2.,   3.],
                    [   5., None,   1.,   2., None]]).T
    print("R:",R)
    S = pairwise_user_sim(R)
    assert type(S) == np.ndarray
    assert S.shape == (3,3)
    s_true= np.array([[   1,.792,.902],
                      [.792,   1,.868],
                      [.902,.868,1   ] ])
    assert np.allclose(S,s_true,atol=0.01)







#-------------------------------------------------------------------------
def test_predict():
    '''(5 points) predict'''


    # 5 movies, 3 users 
    R = np.array( [ [   4.,   5.,   3., None,   1.],
                    [ None,   2.,   3.,   2.,   3.],
                    [   5., None,   1.,   2., None]]).T
    S= np.array([[   1,.792,.902],
                 [.792,   1,.868],
                 [.902,.868,1   ] ])
    p = predict(R,S,0,1)
    assert np.allclose(p,4.5,atol=0.1)

    p = predict(R,S,1,2)
    assert np.allclose(p,3.5,atol=0.1)

    p = predict(R,S,3,0)
    assert np.allclose(p,2,atol=0.1)







