import numpy as np

#-------------------------------------------------------------------------
'''
    Problem 2: getting familiar with numpy package.
    In this problem, please install the following python package:
        * numpy
    Numpy is the library for scientific computing in Python.
    It provides a high-performance multidimensional array object, and tools for working with these arrays.
    To install numpy using pip, you could type `pip3 install numpy` in the terminal.

    Reference: you could read the tutorial for Numpy in Canvas: Tab "Files" -> "doc" folder ->  File name: numpy-intro.pdf
'''


#--------------------------
def ndarray():
    '''
       Create the following 2 x 3 matrix using nd-array in NumPy:
            1,2,3
            4,5,6
        Output:
                X: a numpy matrix of shape 2 X 3, the matrix, each element is an integer
        Note: the data type of the numpy array should be integer
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    x1 = np.array([1,2,3],dtype=np.int)
    x2 = np.array([4,5,6],dtype=np.int)
    X = np.array([x1,x2],dtype=np.int)
    #########################################
    return X

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_ndarray' in the terminal.  '''



#--------------------------
def float_array():
    '''
       Create the following 2 X 3 matrix using nd-array in NumPy:
            0.1, 0.2, 0.3
            0.4, 0.5, 0.6
        Output:
                X: a numpy matrix of shape 2 X 3, the matrix, each element is a float number
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X = np.array([[0.1,0.2,0.3],[0.4,0.5,0.6]],dtype=np.float)
    #########################################
    return X

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_float_array' in the terminal.  '''



#--------------------------
def get_shape(X):
    '''
        Given a NumPy matrix, return the number of rows and columns of the matrix
        Input:
                X: a numpy matrix
        Output:
                h: an integer, the hight of the matrix x (number of rows)
                w: an integer, the width of the matrix x (number of columns)
        Hint: you could solve this problem using one line of code, using a numpy function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    h,w=X.shape
    #########################################
    return h, w

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_get_shape' in the terminal.  '''


#--------------------------
def all_one_matrix(m,n):
    '''
        Create a numpy matrix of shape m X n, all the values in the matrix should be 1.0
        Input:
                m: an integer scalar, the number of rows in the matrix
                n: an integer scalar, the number of columns in the matrix
        Output:
                X: a numpy matrix of shape m X n, the matrix, each element is a float number of value 1.0
        Hint: you could solve this problem using one line of code, using a numpy function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X=np.ones((m,n),dtype=float)
    #########################################
    return X

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_all_one_matrix' in the terminal.  '''


#--------------------------
def mat_sum(X):
    '''
        Given a matrix X of shape m x n, compute the sum of each column in the matrix
        Input:
                X: a numpy matrix of shape m X n
        Output:
                s: a numpy vector of shape (n,) the i-th element of s is the sum of the i-th column of matrix X
        Hint: you could solve this problem using one line of code, using a numpy function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    s = np.sum(X, axis=0)
    #########################################
    return s

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_mat_sum' in the terminal.  '''



#--------------------------
def mat_scalar_multiplication(X, c):
    '''
        Given a matrix X of shape m x n, and a scalar c, the compute the product between the matrix and scalar: Y = cX
        For example, if matrix X is:
                                1,2
                                3,4
        and c = 2

        Then Y = cX should be:
                                2,4
                                6,8

        Input:
                X: a numpy matrix of shape m X n
                c: a float scalar
        Output:
                Y: a numpy matrix of shape (m,n),  each element Y[i,j] = c*X[i,j]
        Hint: you could solve this problem using one line of code, using a numpy function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y=np.array(X)*c
    #########################################
    return Y

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_mat_scalar_multiplication' in the terminal.  '''



#--------------------------
def matrix_vector_multiplication(X, y):
    '''
        Given a matrix X and a vector y, compute the product X*y = z
        For example, if matrix X is:
                                1,2
                                3,4
        and vector y is:
                                5
                                10

        Then z = X y should be:
                                25      =  5*1 + 10 * 2
                                55      =  5*3 + 10 * 4

        Input:
                X: a numpy matrix of shape m x n,
                y: a numpy vector of shape n x 1,
        Output:
                z: the numpy vector of shape m x 1, the result of the matrix vector product.
        Hint: you could solve this problem with one line of code using NumPy
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    z=np.matmul(X,y)
    #########################################
    return z

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_matrix_vector_multiplication' in the terminal.  '''



#--------------------------
def find_zeros(x):
    '''
        Given a vector x of length  n, find indices of all zeros elements in x.
        For example, if vector x is:
                                1,0,4,0
        Then d should be:
                                1,3

        Input:
                x: a numpy vector of length n
        Output:
                d: a numpy vector of length m (m is the number zeros in vector x), the i-th element of d is the index of the i-th zero in x.
        Hint: you could solve this problem using one line of code, using a numpy function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    d=np.where(x==0)[0]
    #########################################
    return d

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_find_zeros' in the terminal.  '''





#--------------------------
def diag_mat(x):
    '''
        Given a vector x of length  n, create a diagonal matrix D where the i-th diagonal element D[i,i] = x[i]
        All the non-diagonal elements of D are zeros: D[i,j] = 0, if i not equal to j.
        For example, if vector x is:
                                1,2,3
        Then D should be:
                                1,0,0
                                0,2,0
                                0,0,3

        Input:
                x: a numpy vector of length n
        Output:
                D: a numpy of shape n x n
        Hint: you could solve this problem using one line of code, using a numpy function.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    D=np.diag(x)
    #########################################
    return D

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_diag_mat' in the terminal.  '''





#--------------------------------------------

''' TEST ALL:
        Now you can test the correctness of all the above functions by typing `nosetests -v test2.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:

            ---------- Problem 2 (10 points in total) ------------ ... ok
            (1 points) nd-array ... ok
            (1 points) float array ... ok
            (1 points) get_shape ... ok
            (1 points) all_one_matrix ... ok
            (1 points) mat sum ... ok
            (1 points) mat_scalar_multiplication ... ok
            (2 points) matrix_vector_multiplication ... ok
            (1 points) find_zeros ... ok
            (1 points) diag_mat ... ok

            ----------------------------------------------------------------------
            Ran 10 tests in 0.004s

            OK
'''

#--------------------------------------------
