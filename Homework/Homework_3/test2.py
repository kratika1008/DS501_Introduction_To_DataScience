from problem2 import *
import sys
from io import BytesIO
import numpy as np

'''
    Unit test 2:
    This file includes unit tests for problem2.py.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 2 (15 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)



#-------------------------------------------------------------------------
def test_1_1():
    '''(3 points) MatMul1x1'''

    #------------------------
    # test matrix A (1x1) multiplies matrix B (1x1)
    # A = 3
    # B = 5
    # C = A X B = 15

    A = b'A,1,1,3,1,1\n'
    B = b'B,1,1,5,1,1\n'
    text = b"".join([A,B])
    stdin = BytesIO(text)

    # create a map reduce job (in a sandbox)
    job = MatMul()
    job.sandbox(stdin=stdin)

    # create a job runner
    runner = job.make_runner()

    # run the mapreduce job 
    runner.run()

    # parse the outputs
    count=0
    for line in runner.stream_output():
        # Use the job's specified protocol to read an output key-value pair
        key, value = job.parse_output_line(line)
        assert len(key) == 3
        assert key[0] == 'C'
        count+=1
        if key[1:] == [1,1]: # C(1,1)
            assert value == 15.
        else:
            assert False # the output key is incorrect
    assert count==1 # matrix C is a 1x1 matrix


#-------------------------------------------------------------------------
def test_1_2():
    '''(3 points) MatMul1x2'''

    #------------------------
    # test matrix A (1x2) multiplies matrix B (2x1)
    # A = 1,2 
    # B = 3
    #     4
    # C = A X B = 11

    A1 = b'A,1,1,1,1,1\n'
    A2 = b'A,1,2,2,1,1\n'
    B1 = b'B,1,1,3,1,1\n'
    B2 = b'B,2,1,4,1,1\n'
    text = b"".join([A1,A2,B1,B2])
    stdin = BytesIO(text)

    # create a map reduce job (in a sandbox)
    job = MatMul()
    job.sandbox(stdin=stdin)

    # create a job runner
    runner = job.make_runner()

    # run the mapreduce job 
    runner.run()

    # parse the outputs
    count=0
    for line in runner.stream_output():
        # Use the job's specified protocol to read an output key-value pair
        key, value = job.parse_output_line(line)
        assert len(key) == 3
        assert key[0] == 'C'
        count+=1
        if key[1:] == [1,1]: # C(1,1)
            assert value == 11.
        else:
            assert False # the output key is incorrect
    assert count==1 # matrix C is a 1x1 matrix

#-------------------------------------------------------------------------
def test_2_1():
    '''(3 points) MatMul2x1'''

    #------------------------
    # test matrix A (2x1) multiplies matrix B (1x2)
    # A = 1
    #     2
    # B = 3, 4
    # matrix C should be a 2x2 matrix
    # C = 3, 4
    #     6, 8

    A1 = b'A,1,1,1,2,2\n'
    A2 = b'A,2,1,2,2,2\n'
    B1 = b'B,1,1,3,2,2\n'
    B2 = b'B,1,2,4,2,2\n'
    text = b"".join([A1,A2,B1,B2])
    stdin = BytesIO(text)

    # create a map reduce job (in a sandbox)
    job = MatMul()
    job.sandbox(stdin=stdin)

    # create a job runner
    runner = job.make_runner()

    # run the mapreduce job 
    runner.run()

    # parse the outputs
    count=0
    for line in runner.stream_output():
        # Use the job's specified protocol to read an output key-value pair
        key, value = job.parse_output_line(line)
        assert len(key) == 3
        k1,k2,k3 = key
        assert k1 == 'C'
        count+=1
        if (k2,k3) == (1,1): # C(1,1)
            assert value == 3.
        elif (k2,k3) == (1,2) : # C(1,2)
            assert value == 4.
        elif (k2,k3)==(2,1): # C(2,1)
            assert value == 6.
        elif (k2,k3) == (2,2): # C(2,2)
            assert value == 8.
        else:
            assert False # the output key is incorrect
    assert count==4 # matrix C is a 2x2 matrix

#-------------------------------------------------------------------------
def test_2_2():
    '''(3 points) MatMul2x2'''

    #------------------------
    #  test with a dataset file
    data = open('matrix.csv','rb')
    stdin = BytesIO(data.read())

    # create a map reduce job (in a sandbox)
    job = MatMul()
    job.sandbox(stdin=stdin)

    # create a job runner
    runner = job.make_runner()

    # run the mapreduce job 
    runner.run()

    count=0
    # parse the outputs
    for line in runner.stream_output():
        # Use the job's specified protocol to read an output key-value pair
        key, value = job.parse_output_line(line)
        assert len(key) == 3
        k1,k2,k3 = key
        assert k1 == 'C'
        count+=1 
        if [k2,k3] == [1,1]:
            assert value == 6
        elif [k2,k3] == [1,2]:
            assert value == -6
        elif [k2,k3] == [2,1]:
            assert value == 15.
        elif [k2,k3] == [2,2]:
            assert value == -15.
        else:
            assert False # the output key is incorrect

    assert count == 4 # C is a 2 by 2 matrix
    data.close()

#-------------------------------------------------------------------------
def test_rand():
    '''(3 points) MatMul random'''

    #------------------------
    #  test with random matrices
    m = np.random.randint(1, high=50)
    n = np.random.randint(1, high=50)
    p = np.random.randint(1, high=50)
    A = np.random.random((m,p))
    B = np.random.random((p,n))
    # write the random matrics into a csv file
    f = open("random_matrix.csv", "w")
    # write matrix A
    for i in range(m):
        for j in range(p):
            s = "A,%d,%d,%f,%d,%d\n" %(i+1,j+1,A[i,j],m,n)
            f.write(s)
    # write matrix B
    for i in range(p):
        for j in range(n):
            s = "B,%d,%d,%f,%d,%d\n" %(i+1,j+1,B[i,j],m,n)
            f.write(s)            
    f.close()


    data = open('random_matrix.csv','rb')
    stdin = BytesIO(data.read())

    # create a map reduce job (in a sandbox)
    job = MatMul()
    job.sandbox(stdin=stdin)

    # create a job runner
    runner = job.make_runner()

    # run the mapreduce job 
    runner.run()

    C = np.dot(A,B)

    count=0
    # parse the outputs
    for line in runner.stream_output():
        # Use the job's specified protocol to read an output key-value pair
        key, value = job.parse_output_line(line)
        assert len(key) == 3
        k1,k2,k3 = key
        assert k1 == 'C'
        count+=1 
        assert np.allclose(value, C[k2-1,k3-1],atol=0.01)

    assert count == m*n  # C is m x n matrix


