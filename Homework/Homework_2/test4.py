from problem4 import *
from problem3 import save_csv, load_csv
import pandas as pd 
import sys

'''
    Unit test 4:
    This file includes unit tests for problem4.py.
'''
#-------------------------------------------------------------------------
def test_python_version():
    ''' ---------- Problem 4 (15 points in total) ------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_load_batting():
    '''(2 points) load_batting'''
    x=load_batting()
    assert type(x) == pd.DataFrame
    assert x.shape == (105861, 22) 
    #assert x.dtypes.H == int 
    #assert x.dtypes.AB == int 
    assert x.iloc[0,6] == 4
    assert x.iloc[330,6] == 136



#-------------------------------------------------------------------------
def test_search_batting():
    '''(2 points) search_batting'''
    x=load_batting()

    y=search_batting(x, year=1999)
    assert y.shape == (1299, 22) 
    print(y)
    #assert y.dtypes.H == int 
    #assert y.dtypes.AB == int 
    assert y.iloc[0,1] == 1999
    assert y.iloc[1200,1] == 1999
    assert y.iloc[0,6] == 57 
    assert y.iloc[1,6] == 21 

    y=search_batting(x)
    assert type(y) == pd.DataFrame
    assert y.shape == (1339, 22) 
    #assert y.dtypes.H == int 
    #assert y.dtypes.AB == int 
    assert y.iloc[0,1] == 2001
    assert y.iloc[1338,1] == 2001
    assert y.iloc[0,6] == 1
    assert y.iloc[1,6] == 42 


    # Now let's save the dataset of year 2001 into a CSV file, for further analysis
    save_csv(y,'Batting2001.csv')

    # check the correctness of the saved data 
    z= load_csv('Batting2001.csv')
    assert type(z) == pd.DataFrame
    assert z.shape == (1339, 22) 
    #assert z.dtypes.H == int 
    #assert z.dtypes.AB == int 
    assert z.iloc[0,1] == 2001
    assert z.iloc[1338,1] == 2001
    assert z.iloc[0,6] == 1
    assert z.iloc[1,6] == 42 



#-------------------------------------------------------------------------
def test_aggregate_batting():
    '''(3 points) aggregate_batting'''

    x= load_csv('Batting2001.csv')
    y=aggregate_batting(x)

    # after removing the column 'teamID' and 'lgID' (string cannot be added in aggregation), we have 20 columns
    assert y.shape == (1220, 20)  
    #assert y.dtypes.H == int 
    #assert y.dtypes.AB == int 
    assert y.iloc[1,3] == 28  # the 'G' column for player 'abbotje01'
    assert y.iloc[1,4] == 42  # the 'AB' column for player 'abbotje01'
    assert y.iloc[7,3] == 59  # the 'G' column for player 'aceveju01'
    assert y.iloc[7,4] == 3  # the 'AB' column for player 'aceveju01'
    assert y.iloc[84,3] == 46 # the 'G' column for player 'bennega01'
    assert y.iloc[84,4] == 131  # the 'AB' column for player 'bennega01'
    assert y.iloc[84,-1] == 1  # the 'GIDP' column for player 'bennega01'
 
    # Now let's save the result into a CSV file, for further analysis
    save_csv(y,'Batting2001A.csv')

#-------------------------------------------------------------------------
def test_join_batting():
    '''(3 points) join_batting'''

    x= load_csv('Batting2001A.csv')
    y= load_csv('People.csv')
    z=join_batting(x,y)
    
    assert z.shape == (1220, 43)  
    #assert z.dtypes.H == int 
    #assert z.dtypes.AB == int 
    assert z[z.playerID=='abreubo01'].iloc[0].G ==162
    assert z[z.playerID=='abreubo01'].iloc[0].birthYear ==1974

    assert z[z.playerID=='bradlmi01'].iloc[0].G == 77
    assert z[z.playerID=='bradlmi01'].iloc[0].birthYear == 1978
    assert z[z.playerID=='bradlmi01'].iloc[0].nameLast =='Bradley' 
    assert z[z.playerID=='bradlmi01'].iloc[0].nameFirst =='Milton' 

    # Now let's save the result into a CSV file, for further analysis
    save_csv(z,'Batting2001AJ.csv') 


#-------------------------------------------------------------------------
def test_search_salary():
    '''(2 points) search_salary'''

    x= load_csv('Salaries.csv')
    y=search_salary(x)
    
    # Now let's save the result into a CSV file, for further analysis
    save_csv(y,'Salaries2002.csv') 

    assert y.shape == (846, 5)  
    assert y[y.playerID=='anderga01'].iloc[0].yearID == 2002
    assert y[y.playerID=='anderga01'].iloc[0].salary == 5000000
    assert y[y.playerID=='miltoer01'].iloc[0].yearID == 2002
    assert y[y.playerID=='miltoer01'].iloc[0].salary == 4000000
    assert y[y.playerID=='woodwch01'].iloc[0].yearID == 2002
    assert y[y.playerID=='woodwch01'].iloc[0].salary == 235000




#-------------------------------------------------------------------------
def test_join_salary():
    '''(3 points) join_salary'''

    x= load_csv('Batting2001AJ.csv')
    y= load_csv('Salaries2002.csv')
    z= join_salary(x,y)

    assert z.shape == (786, 47)  
    assert z[z.playerID=='anderga01'].iloc[0].G== 161
    assert z[z.playerID=='anderga01'].iloc[0].nameLast== 'Anderson' 
    assert z[z.playerID=='anderga01'].iloc[0].salary == 5000000
    assert z[z.playerID=='miltoer01'].iloc[0].G == 35 
    assert z[z.playerID=='miltoer01'].iloc[0].nameLast=='Milton' 
    assert z[z.playerID=='miltoer01'].iloc[0].salary == 4000000
    assert z[z.playerID=='woodwch01'].iloc[0].G== 37
    assert z[z.playerID=='woodwch01'].iloc[0].nameLast == "Woodward"
    assert z[z.playerID=='woodwch01'].iloc[0].salary == 235000

    
    # Now let's save the result into a CSV file, for further analysis
    save_csv(z,'Batting2001AJS.csv') 

