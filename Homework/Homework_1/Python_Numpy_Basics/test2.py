from problem2 import *
import numpy as np
import sys

'''
    Unit test 2:
    This file includes unit tests for problem2.py.
    You could test the correctness of your code by typing `nosetests -v test2.py` in the terminal.
'''
#-------------------------------------------------------------------------
def test_python_version():
    ''' ---------- Problem 2 (10 points in total) ------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_ndarray():
    '''(1 points) nd-array'''
    x=ndarray()

    # check data type
    assert type(x) == np.ndarray
    # should be a matrix (2 dimensional array)
    assert x.ndim == 2
    # check shape of the matrix 
    assert x.shape == (2,3)
    # check type of the data entry
    assert x.dtype == np.int 

    # check the values in the matrix
    assert x[0,0] ==1
    assert x[1,1] ==5
    assert x[0,-1] ==3
    assert x[1,-1] ==6


#-------------------------------------------------------------------------
def test_float_array():
    '''(1 points) float array'''
    x=float_array()

    # check data type
    assert type(x) == np.ndarray
    # should be a matrix (2 dimensional array)
    assert x.ndim == 2
    # check shape of the matrix 
    assert x.shape == (2,3)
    # check type of the data entry
    assert x.dtype == np.float 

    # check the values in the matrix
    assert x[0,0] ==0.1
    assert x[1,1] ==0.5
    assert x[0,-1] ==0.3
    assert x[1,-1] ==0.6



#-------------------------------------------------------------------------
def test_get_shape():
    '''(1 points) get_shape'''
    h,w=get_shape(np.zeros((4,5)))

    # check data type
    #assert type(h) == int 
    #assert type(w) == int 
    assert h == 4
    assert w == 5

#-------------------------------------------------------------------------
def test_all_one_matrix():
    '''(1 points) all_one_matrix'''
    X=all_one_matrix(3,2)

    # check data type
    assert type(X) == np.ndarray
    assert X.shape == (3,2) 
    #assert X.dtype == float 
    for i in range(3):
        for j in range(2):
            assert X[i,j]==1.

#-------------------------------------------------------------------------
def test_mat_sum():
    '''(1 points) mat sum'''
    X= all_one_matrix(3,2)
    s = mat_sum(X)
    
    # check data type
    assert type(s) == np.ndarray
    assert s.shape == (2,) 
    assert s[0]==3. 
    assert s[1]==3. 

#-------------------------------------------------------------------------
def test_mat_scalar_multiplication():
    '''(1 points) mat_scalar_multiplication'''
    X= ndarray()
    Y =  mat_scalar_multiplication(X, 2.)
    # check data type
    assert type(Y) == np.ndarray
    assert Y.shape == (2,3) 
    assert Y[0,0]==2. 
    assert Y[0,1]==4. 
    assert Y[0,-1]==6. 
    assert Y[1,0]==8. 


#-------------------------------------------------------------------------
def test_matrix_vector_multiplication():
    '''(2 points) matrix_vector_multiplication'''

    # create a matrix  [[1., 2.],
    #                   [3., 4.],
    #                   [5., 6.]]
    # of shape (3 by 2)
    X = np.array([[1.,2.],
                  [3.,4.],
                  [5.,6.]])
    print('X:', X)

    # create a vector of shape (2 by 1): [[1.],
    #                                     [2.]]
    y = np.array([[1.], 
                  [2.]])

    # call the function
    z= matrix_vector_multiplication(X,y) 

    # test whether or not z is a numpy matrix 
    assert type(z) == np.ndarray

    # test the shape of the vector
    assert z.shape == (3,1)

    # check the correctness of the result 
    z_real = np.array([[5.],
                       [11.],
                       [17.]])
    assert np.allclose(z, z_real)


    # test on random matrix
    for _ in range(20):
        m,n = np.random.randint(2,20,size= 2) 
        X = np.random.random((m,n))
        y = np.random.random(n).T
        z = matrix_vector_multiplication(X,y)
        i = np.random.randint(m)
        assert np.allclose(z[i],  np.dot(X[i],y))



#-------------------------------------------------------------------------
def test_find_zeros():
    '''(1 points) find_zeros'''
    x= np.array([1,0,4,0])
    print(x.shape)
    d =  find_zeros(x)

    # check data type
    assert type(d) == np.ndarray
    #assert d.dtype == int 
    assert d.shape == (2,) 
    assert d[0]==1 
    assert d[1]==3 




#-------------------------------------------------------------------------
def test_diag_mat():
    '''(1 points) diag_mat'''
    x= np.array([1,2,3])
    D =  diag_mat(x)

    # check data type
    assert type(D) == np.ndarray
    assert D.shape == (3,3) 
    assert D[0,0]==1 
    assert D[1,1]==2 
    assert D[2,2]==3 
    assert D[0,2]==0 
    assert D[2,0]==0 
    assert D[1,0]==0 
    assert D[0,1]==0 


