from problem5 import *
import numpy as np
import sys

'''
    Unit test 5:
    This file includes unit tests for problem5.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 5 (35 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_compute_B():
    '''(3 points) compute_B'''

    #-------------------------------
    # an example rating matrix (3 movies, 5 users)
    R = np.array( [ [   4.,   5.,   3., None,   1.],
                    [ None,   2.,   3.,   2.,   3.],
                    [   5., None,   1.,   2., None]])

    # call the function
    B = compute_B(R)

    # true answer
    B_true = np.array( [ [   1.,   1.,   1.,   0.,   1.],
                         [   0.,   1.,   1.,   1.,   1.],
                         [   1.,   0.,   1.,   1.,   0.]])

    # test the result
    assert np.allclose(B,B_true)

#-------------------------------------------------------------------------
def test_compute_L():
    '''(3 points) compute_L'''

    #-------------------------------
    # an example rating matrix (3 movies, 5 users)
    R = np.array( [ [   2.,   2.,   2., None,   2.],
                    [ None,   2.,   2.,   2.,   2.],
                    [   2., None,   2.,   2., None]])
    U = np.array( [ [1.],
                    [1.],
                    [1.]])
    V = np.array( [ [   1.,   1.,   1.,   1.,   1.]])

    # call the function
    L = compute_L(R,U,V)

    # true answer
    L_true = np.array( [ [   1.,   1.,   1.,   0.,   1.],
                         [   0.,   1.,   1.,   1.,   1.],
                         [   1.,   0.,   1.,   1.,   0.]])
    # test the result
    assert np.allclose(L,L_true)

    #-------------------------------
    U = np.array( [ [2.],
                    [2.],
                    [2.]])
    V = np.array( [ [   1.,   1.,   1.,   1.,   1.]])

    L = compute_L(R,U,V)
    assert np.allclose(L,np.zeros((3,5)))

#-------------------------------------------------------------------------
def test_compute_dU():
    '''(5 points) compute_dU'''

    #-------------------------------
    # an example rating matrix (3 movies, 5 users)
    L = np.array( [ [   1.,   1.,   1.,   0.,   1.],
                    [   0.,   1.,   1.,   1.,   1.],
                    [   1.,   0.,   1.,   1.,   0.]])

    U = np.array( [ [1.],
                    [1.],
                    [1.]])
    V = np.array( [ [   1.,   1.,   1.,   1.,   1.]])

    dU = compute_dU(L,U,V,mu=0.)

    # true answer
    dU_true = np.array( [[-8.],
                         [-8.],
                         [-6.]])
    # test the result
    assert np.allclose(dU,dU_true)


    dU = compute_dU(L,U,V,mu=1.)

    # true answer
    dU_true = np.array( [[-6.],
                         [-6.],
                         [-4.]])
    # test the result
    assert np.allclose(dU,dU_true)


#-------------------------------------------------------------------------
def test_compute_dV():
    '''(5 points) compute_dV'''

    #-------------------------------
    # an example rating matrix (3 movies, 5 users)
    L = np.array( [ [   1.,   1.,   1.,   0.,   1.],
                    [   0.,   1.,   1.,   1.,   1.],
                    [   1.,   0.,   1.,   1.,   0.]])

    U = np.array( [ [1.],
                    [1.],
                    [1.]])
    V = np.array( [ [   1.,   1.,   1.,   1.,   1.]])

    dV = compute_dV(L,U,V,mu=0.)

    # true answer
    dV_true = np.array([[  -4.,  -4.,  -6.,  -4.,  -4.]])

    # test the result
    assert np.allclose(dV,dV_true)

    dV = compute_dV(L,U,V,mu=1.)

    # true answer
    dV_true = np.array([[  -2.,  -2.,  -4.,  -2.,  -2.]])
    # test the result
    assert np.allclose(dV,dV_true)


#-------------------------------------------------------------------------
def test_update_U():
    '''(2 points) update_U'''

    U = np.array([[1.],
                  [1.],
                  [1.]])
    dU = np.array([[-8.],
                   [-8.],
                   [-6.]])

    # call the function
    U_new = update_U(U,dU, beta=.1)

    # true answer
    U_true = np.array([[1.8],
                       [1.8],
                       [1.6]])

    # test the result
    assert np.allclose(U_new,U_true)


#-------------------------------------------------------------------------
def test_update_V():
    '''(2 points) update_V'''

    V = np.array( [[   1.,   1.,   1.,   1.,   1.]])
    dV = np.array([[  -4.,  -4.,  -6.,  -4.,  -4.]])
    # call the function
    V_new = update_V(V,dV, beta=.1)

    # true answer
    V_true = np.array( [[   1.4,   1.4,   1.6,   1.4,   1.4]])

    # test the result
    assert np.allclose(V_new,V_true)


#-------------------------------------------------------------------------
def test_matrix_decoposition():
    '''(10 points) matrix decomposition'''

    #-------------------------------
    # an example rating matrix (2 movies, 2 users)
    R = np.array([[1., 1.],
                  [1., 1.]])
    # call the function
    U, V = matrix_decoposition(R,1)

    # test whether or not the result is a float number 
    assert type(U) == np.ndarray 
    assert type(V) == np.ndarray 
    assert U.shape == (2,1)
    assert V.shape == (1,2)

    # check the correctness of the result 
    assert np.allclose(np.dot(U,V),R, atol=0.1)
    # Note: this test should finish in less the 5 second. 
    # If it runs for a long time,  you should check whether you have stopped the iteration when the values of U and V converged.

    #-------------------------
    # another example
    
    # a random rating matrix
    R = np.random.randint(1,6, (10, 5)).astype(float)

    # call the function
    U, V = matrix_decoposition(R,5)

    # test whether or not the result is a float number 
    assert type(U) == np.ndarray 
    assert type(V) == np.ndarray 
    assert U.shape == (10,5)
    assert V.shape == (5,5)

    # check the correctness of the result 
    assert np.allclose(np.dot(U,V), R, atol=.1)



#-------------------------------------------------------------------------
def test_predict():
    '''(5 points) predict'''

    U = np.array( [ [1.],
                    [1.],
                    [1.]])
    V = np.array( [ [   1.,   1.,   1.,   1.,   1.]])
    
    p = predict(U,V,1,0)
    assert np.allclose(p,1)

    U = np.array( [ [1.,2.],
                    [1.,2.],
                    [1.,2.]])
    V = np.array( [ [   1.,   1.,   1.,   1.,   1.],
                    [   2.,   2.,   2.,   2.,   2.]   ])
    
    p = predict(U,V,1,0)
    assert np.allclose(p,5)

    #-------------------------------
    # 5 movies, 3 users 
    R = np.array( [ [   4.,   5.,   3., None,   1.],
                    [ None,   2.,   3.,   2.,   3.],
                    [   5., None,   1.,   2., None]]).T

    U, V = matrix_decoposition(R,1)

    p = predict(U,V,0,1)
    assert np.allclose(p,3.9,atol=0.1)

    p = predict(U,V,1,2)
    assert np.allclose(p,3.5,atol=0.1)

    p = predict(U,V,3,0)
    assert np.allclose(p,2.3,atol=0.1)




