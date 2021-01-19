from problem3 import *
import pandas as pd 
import sys

'''
    Unit test 3:
    This file includes unit tests for problem3.py.
'''
#-------------------------------------------------------------------------
def test_python_version():
    ''' ---------- Problem 3 (10 points in total) ------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)

#-------------------------------------------------------------------------
def test_dataframe():
    '''(1 points) dataframe'''
    x=dataframe()

    assert type(x) == pd.DataFrame
    assert x.shape == (3,2) 
    #assert x.dtypes.height == int 
    #assert x.dtypes.width == int  
    assert x.iloc[0,0] == 1
    assert x.iloc[0,1] == 4
    assert x.iloc[1,0] == 2
    assert x.iloc[1,1] == 5
    assert x.iloc[2,0] == 3
    assert x.iloc[2,1] == 6

#-------------------------------------------------------------------------
def test_load_csv():
    '''(1 points) load_csv'''
    x=load_csv()

    assert type(x) == pd.DataFrame
    assert x.shape == (3,2) 
    #assert x.dtypes.height == int 
    #assert x.dtypes.width == int 
    assert x.iloc[0,0] == 1
    assert x.iloc[0,1] == 4
    assert x.iloc[1,0] == 2
    assert x.iloc[1,1] == 5
    assert x.iloc[2,0] == 3
    assert x.iloc[2,1] == 6



#-------------------------------------------------------------------------
def test_search_height():
    '''(1 points) search_height'''
    x=dataframe()
    y=search_height(x)

    assert type(y) == pd.DataFrame
    assert y.shape == (2,2) 
    #assert y.dtypes.height == int 
    #assert y.dtypes.width == int 
    assert y.iloc[0,0] == 2
    assert y.iloc[0,1] == 5
    assert y.iloc[1,0] == 3
    assert y.iloc[1,1] == 6

    y=search_height(x,t=0)
    assert type(y) == pd.DataFrame
    assert y.shape == (3,2) 
    #assert y.dtypes.height == int 
    #assert y.dtypes.width == int 
    assert y.iloc[0,0] == 1
    assert y.iloc[0,1] == 4
    assert y.iloc[1,0] == 2
    assert y.iloc[1,1] == 5
    assert y.iloc[2,0] == 3
    assert y.iloc[2,1] == 6



#-------------------------------------------------------------------------
def test_save_csv():
    '''(1 points) save_csv'''
    x=dataframe()
    save_csv(x,'A1.csv')
    y=load_csv('A1.csv')

    assert type(y) == pd.DataFrame
    assert y.shape == (3,2) 
    #assert y.dtypes.height == int 
    #assert y.dtypes.width == int 
    assert y.iloc[0,0] == 1
    assert y.iloc[0,1] == 4
    assert y.iloc[1,0] == 2
    assert y.iloc[1,1] == 5
    assert y.iloc[2,0] == 3
    assert y.iloc[2,1] == 6

#-------------------------------------------------------------------------
def test_sum_column():
    '''(1 points) sum_column'''
    x=load_csv('B.csv')
    y=sum_column(x)
    assert y == 22 
    y=sum_column(x,key='ID')
    assert y == 6 


#-------------------------------------------------------------------------
def test_aggregate():
    '''(2 points) aggregate'''
    x=load_csv('B.csv')
    y=aggregate(x,key='ID')

    assert type(y) == pd.DataFrame
    assert y.shape == (2,2)  # to convert an index into a column, you could use reset_index() method.
    assert y.iloc[0,0] == 1
    assert y.iloc[1,0] == 2
    assert y.iloc[0,1] == 9
    assert y.iloc[1,1] == 13

#-------------------------------------------------------------------------
def test_join():
    '''(2 points) join'''
    x=load_csv('B.csv')
    x=aggregate(x,key='ID')
    y=load_csv('C.csv')
    z=join(x,y,key='ID')

    assert type(z) == pd.DataFrame
    assert z.shape == (2,3)  
    assert z.iloc[0,0] == 1
    assert z.iloc[1,0] == 2
    assert z.iloc[0,1] == 9
    assert z.iloc[1,1] == 13
    assert z.iloc[0,2] == 'Alex'
    assert z.iloc[1,2] == 'Bob'

#-------------------------------------------------------------------------
def test_filtering():
    '''(1 points) filtering'''
    x=load_csv('C.csv')
    y=filtering(x)

    assert type(y) == pd.DataFrame
    assert y.shape == (2,2)  
    assert y.iloc[0,0] == 1
    assert y.iloc[1,0] == 3
    assert y.iloc[0,1] == 'Alex'
    assert y.iloc[1,1] == 'Tom'

    # now let's filter with the names
    y=filtering(x,key='name',values=['Bob','Tom'])
    assert type(y) == pd.DataFrame
    assert y.shape == (2,2)  
    assert y.iloc[0,0] == 2
    assert y.iloc[1,0] == 3
    assert y.iloc[0,1] == 'Bob'
    assert y.iloc[1,1] == 'Tom'



