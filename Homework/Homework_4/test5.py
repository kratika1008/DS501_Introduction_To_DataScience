from problem5 import *
import numpy as np
import sys

'''
    Unit test 5:
    This file includes unit tests for problem5.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 5 (20 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_compute_D():
    '''(4 points) compute_D '''

    #-------------------------------
    # an example adjacency matrix (3 nodes)
    A = np.array([[0., 1., 0.],
                  [1., 0., 1.],
                  [0., 1., 0.]])

    # call the function
    D = compute_D(A)

    # test whether or not D is a numpy matrix 
    assert type(D) == np.ndarray

    # true answer
    D_true = np.mat([[1., 0., 0.],
                     [0., 2., 0.],
                     [0., 0., 1.]])

    # test the result
    assert np.allclose(D,D_true)

    #-------------------------------
    # an example adjacency matrix 
    for _ in range(20):
        n = np.random.randint(3,20)
        A = np.random.random((n,n))
        np.fill_diagonal(A,0.)
        A = (A + A.T)/2 # symmetric
        A[A>=0.5]=1.0
        A[A<0.5]=0.
        # call the function
        D = compute_D(A)
        d = np.diagonal(D)
        # test the result
        assert np.allclose(d.sum(), A.sum())
        assert np.allclose(d.sum(), D.sum())
        i = np.random.randint(n)
        assert np.allclose(d[i], D[i].sum())
        

#-------------------------------------------------------------------------
def test_compute_L():
    '''(4 points) compute_L '''

    #-------------------------------
    # an example adjacency matrix (3 nodes)
    A = np.array([[0., 1., 0.],
                  [1., 0., 1.],
                  [0., 1., 0.]])

    D = np.array([[1., 0., 0.],
                  [0., 2., 0.],
                  [0., 0., 1.]])
    # call the function
    L = compute_L(D,A)

    # true answer
    L_true = np.array([[ 1.,-1., 0.],
                       [-1., 2.,-1.],
                       [ 0.,-1., 1.]])

    # test the result
    assert np.allclose(L,L_true)

    #-------------------------------
    # an example adjacency matrix 
    for _ in range(20):
        n = np.random.randint(3,20)
        A = np.random.random((n,n))
        np.fill_diagonal(A,0.)
        A = (A + A.T)/2 # symmetric
        A[A>=0.5]=1.0
        A[A<0.5]=0.
        D = compute_D(A)
        # call the function
        L = compute_L(D,A)
        d = np.diagonal(L)
        # test the result
        assert np.allclose(d.sum(), A.sum())
        assert np.allclose(L.sum(), 0)
        assert np.allclose(L.sum(0), np.zeros(n))
        # whether L is symmetric
        assert np.allclose(L,L.T) 
 


#-------------------------------------------------------------------------
def test_find_e2():
    '''(4 points) find_e2'''

    L = np.array([[1., -1.],
                  [-1., 1.]])
    
    e = find_e2(L) 
    assert type(e) == np.ndarray
    assert e.shape == (2,)
    
    e_true = np.array([-0.70710678, 0.70710678])
    assert np.allclose(e,e_true,atol=1e-2) or np.allclose(e,-e_true,atol=1e-2)



    L= np.diag((1, 0, 3)) 
    e = find_e2(L) 
    e_true= np.array([1,0,0])
    assert np.allclose(e,e_true,atol=1e-2) or np.allclose(e,-e_true,atol=1e-2) 


    L= np.diag((1, 1e-5,3)) 
    e = find_e2(L) 
    e_true= np.array([1,0,0])
    assert np.allclose(e,e_true,atol=1e-2) or np.allclose(e,-e_true,atol=1e-2) 


    L= np.diag((1, 1e-3, 1e-5,3)) 
    e = find_e2(L) 
    e_true= np.array([0,1,0,0])
    assert np.allclose(e,e_true,atol=1e-2) or np.allclose(e,-e_true,atol=1e-2) 




#-------------------------------------------------------------------------
def test_compute_x():
    '''(4 points) compute_x'''
    e2 = np.array([0.7, -0.7])
    x = compute_x(e2)
    assert type(x) == np.ndarray
    assert x.shape == (2,) 
    assert np.allclose(x, [1.,0.])

    e2 = np.array([0.7, -0.7, 0.2, -0.2])
    x = compute_x(e2)
    assert x.shape == (4,) 
    assert np.allclose(x, [1.,0.,1.,0.])

    e2 = np.array([0.7, 0., 0.2, -0.2])
    x = compute_x(e2)
    assert type(x) == np.ndarray
    assert x.shape == (4,) 
    assert np.allclose(x, [1.,0.,1.,0.])




#-------------------------------------------------------------------------
def test_spectral_clustering():
    '''(4 points) spectral clustering'''
    #-------------------------------
    # an example adjacency matrix (2 groups with a link between the two groups) 
    A = np.array([[0., 1., 1., 0., 0., 0.],
                  [1., 0., 1., 0., 0., 0.],
                  [1., 1., 0., 1., 0., 0.],
                  [0., 0., 1., 0., 1., 1.],
                  [0., 0., 0., 1., 0., 1.],
                  [0., 0., 0., 1., 1., 0.]])
    # make sure matrix A is symmetric
    assert np.allclose(A, A.T)

    # call the function
    x = spectral_clustering(A)

    # test the correctness of the result
    assert np.allclose([0,0,0,1,1,1],x) or np.allclose([1,1,1,0,0,0],x)



    #-------------------------------
    # test on random matrix 
    for _ in range(20):
        n1 = np.random.randint(3,20)
        n2 = np.random.randint(3,20)
        A1 = np.random.random((n1,n1))*100
        A2 = np.random.random((n2,n2))*100
        np.fill_diagonal(A1,0.)
        np.fill_diagonal(A2,0.)
        A = np.bmat([[A1,np.zeros((n1,n2))],
                     [np.zeros((n2,n1)),A2]])
        A = (A + A.T)/2 # symmetric
        A[A>=0.5]=1.0
        A[A<0.5]=0.
        i = np.random.randint(n1)
        j = np.random.randint(n2) + n1
        A[i,j] = 0.001
        A[j,i] = 0.001
        
        A =np.asarray(A)
        # call the function
        x = spectral_clustering(A)
        x_true1 = np.asarray(np.bmat([np.zeros(n1), np.ones(n2)]))
        x_true2 = np.asarray(np.bmat([np.ones(n1), np.zeros(n2)]))
        assert np.allclose(x_true1,x) or np.allclose(x_true2,x)

