from problem1 import *
import sys
from io import BytesIO
import numpy as np

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
    You could test the correctness of your code by typing `nosetests test1.py` in the terminal.
'''

#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (15 points in total)--------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_SuitCount():
    '''(5 points) SuitCount'''

    # create an object
    w = CardsSuitCount()

    #-------------------
    # mapper
    outs = w.mapper(None,'H10') 
    # read one key-value pair from the output generator 
    k,v= next(outs)
    assert type(k) == str
    assert k=='H' 

    #-------------------
    # reducer
    outs = w.reducer('S',[1,1,1]) 
    k,v= next(outs)
    assert type(k) == str
    assert k == 'S'
    assert v == 3

    #-------------------
    # map-reduce

    data = open('cards.txt','rb')
    stdin = BytesIO(data.read())

    # create a map reduce job (in a sandbox)
    job = CardsSuitCount()
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
        count+=1
        if key == 'H':
            assert value == 10
        elif key == 'D':
            assert value == 11
        elif key == 'S':
            assert value == 12
        elif key == 'C':
            assert value == 13
        else:
            assert False # the output key is incorrect
    assert count==4

    #-------------------
    # test with random data 

    nH = np.random.randint(1, high=100)
    nS = np.random.randint(1, high=100)
    nD = np.random.randint(1, high=100)
    nC = np.random.randint(1, high=100)
    tH = b'H10\n' * nH
    tS = b'S11\n' * nS
    tD = b'D2\n' * nD
    tC = b'C12\n' * nC
    text = b"".join([tH,tS,tD,tC])
    stdin = BytesIO(text)

    # create a map reduce job (in a sandbox)
    job = CardsSuitCount()
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
        count+=1
        if key == 'H':
            assert value == nH
        elif key == 'S':
            assert value == nS
        elif key == 'C':
            assert value == nC
        elif key == 'D':
            assert value == nD
        else:
            assert False # the output key is incorrect
    assert count==4




#-------------------------------------------------------------------------
def test_SuitSum():
    '''(5 points) SuitSum'''

    # create an object
    w = CardsSuitSum()

    #-------------------
    # mapper
    outs = w.mapper(None,'H10') 
    # read one key-value pair from the output generator 
    k,v= next(outs)
    assert type(k) == str
    assert k=='H' 

    #-------------------
    # reducer 
    outs = w.reducer('S',[1,2,3]) 
    k,v= next(outs)
    assert type(k) == str
    assert k == 'S'
    assert v == 6

    #-------------------
    # map-reduce


    data = open('cards.txt','rb')
    stdin = BytesIO(data.read())

    # create a map reduce job (in a sandbox)
    job = CardsSuitSum()
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
        count+=1
        if key == 'H':
            assert value == 55 
        elif key == 'D':
            assert value == 66
        elif key == 'S':
            assert value == 78
        elif key == 'C':
            assert value == 91
        else:
            assert False # the output key is incorrect
    assert count==4


    #-------------------
    # test with random data 
    nH = np.random.randint(1, high=100)
    nS = np.random.randint(1, high=100)
    nD = np.random.randint(1, high=100)
    nC = np.random.randint(1, high=100)
    tH = b'H10\n' * nH
    tS = b'S11\n' * nS
    tD = b'D2\n' * nD
    tC = b'C12\n' * nC
    text = b"".join([tH,tS,tD,tC])
    stdin = BytesIO(text)

    # create a map reduce job (in a sandbox)
    job = CardsSuitSum()
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
        count+=1
        if key == 'H':
            assert value == nH*10
        elif key == 'S':
            assert value == nS*11
        elif key == 'C':
            assert value == nC*12
        elif key == 'D':
            assert value == nD*2
        else:
            assert False # the output key is incorrect
    assert count==4



#-------------------------------------------------------------------------
def test_NumberCount():
    '''(5 points) NumberCount'''

    # create an object
    w = CardsNumberCount()

    #-------------------
    # mapper
    outs = w.mapper(None,'H10') 
    # read one key-value pair from the output generator 
    k,v= next(outs)
    assert type(k) == str

    #-------------------
    # reducer 
    outs = w.reducer('1',[1,1,1]) 
    # read one key-value pair from the output generator 
    out_pair = next(outs)
    k,v = out_pair
    assert type(k) == str
    assert k == '1'
    assert v == 3

    #-------------------
    # map-reduce
    data = open('cards.txt','rb')
    stdin = BytesIO(data.read())

    # create a map reduce job (in a sandbox)
    job = CardsNumberCount()
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
        count+=1
        if key == '1':
            assert value == 4 
        elif key == '2':
            assert value == 4 
        elif key == '3':
            assert value == 4
        elif key == '4':
            assert value == 4
        elif key == '5':
            assert value == 4
        elif key == '6':
            assert value == 4
        elif key == '7':
            assert value == 4
        elif key == '8':
            assert value == 4
        elif key == '9':
            assert value == 4
        elif key == '10':
            assert value == 4
        elif key == '11':
            assert value == 3
        elif key == '12':
            assert value == 2
        elif key == '13':
            assert value == 1
        else:
            assert False # the output key is incorrect
    assert count==13


    #-------------------
    # test with random data 
    nH = np.random.randint(1, high=100)
    nS = np.random.randint(1, high=100)
    nD = np.random.randint(1, high=100)
    nC = np.random.randint(1, high=100)
    tH = b'H2\n' * nH
    tS = b'S11\n' * nS
    tD = b'D2\n' * nD
    tC = b'C12\n' * nC
    text = b"".join([tH,tS,tD,tC])
    stdin = BytesIO(text)

    # create a map reduce job (in a sandbox)
    job = CardsNumberCount()
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
        count+=1
        if key == '2':
            assert value == nH+nD
        elif key == '11':
            assert value == nS
        elif key == '12':
            assert value == nC
        else:
            assert False # the output key is incorrect
    assert count==3


