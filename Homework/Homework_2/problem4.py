import pandas as pd
from problem3 import load_csv, aggregate, join
#-------------------------------------------------------------------------
'''
    Problem 4: Baseball Data Preprocessing
    In this problem, you will practise data preprocessing with baseball dataset.
'''

#-------------------------------------------------------------------------
'''
    Let's start with the raw data, 'Batting.csv'. Let's load the CSV file into a data frame.
'''

#--------------------------
def load_batting(filename='Batting.csv'):
    '''
        load batting data from a CSV file.
        Input:
                filename: a string indicating the filename of the CSV file.
        Output:
                X: a pandas dataframe, loaded from the CSV file
        Hint: you could solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X = load_csv(filename)
    #########################################
    return X


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_load_batting' in the terminal.  '''


#-------------------------------------------------------------------------
'''
   The dataset contains records of all years. In this study, suppose we want to choose players for year 2002, based upon data of year 2001.
   We need to first search the data records of year 2001 only.
'''
#--------------------------
def search_batting(X, year=2001):
    '''
        search batting data of one year.
        For example, if we want to evaluate players for year 2002, we need to search for data from the previous year 2001 and use the data to evaluate players.
        Input:
                X: a dataframe containing the batting data of all players in all years.
                year: an integer scalar, the year to be searched
        Output:
                Y: a dataframe containing the batting data only in the searched year.
        Hint: you could solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = X[X.yearID==year]
    #########################################
    return Y


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_search_batting' in the terminal.  '''

#-------------------------------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'Batting2001.csv'.
'''

#-------------------------------------------------------------------------
'''
   The 2001 dataset contains multiple records for each player: a same player may have two/three records, because the player has changed team in year 2001.
   For example, playerID='guilljo01' or 'houstty01', which has two rows.
   We need to add the game statistics together for each of these players, so that each player only contains one row and the data is the sum of all the records for the same player.
'''
#--------------------------
def aggregate_batting(X):
    '''
        Given a data frame of batting statistics, aggregate data records with respect to playerID, so that the game statistics are added together for each player.
        For example, player 'houstty01' has two rows, where the number of hits (column H) has values: 58, 4
        We want to combine these two rows into one row, such that all the game statistics are the sum of the raw values (for example, number hits now should be 58+4 = 62)
        Input:
                X: a dataframe containing the batting data of all players in year 2001 (containing duplicated records).
        Output:
                Y: a dataframe containing the batting data after aggregating the statistics for players.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = aggregate(X, 'playerID')
    #########################################
    return Y


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_aggregate_batting' in the terminal.  '''

#-------------------------------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'Batting2001A.csv'.
'''


#-------------------------------------------------------------------------
'''
   Now the dataset only contains game statistics, but no information about the player, like first name, last name, weight, height, etc.
   We have another CSV file 'People.csv', which contains the player information, such as first name, weight, height, etc.
   It would be better if we can combine these two datasets into one data frame, so the new data frame contains both game statistics and player information.
'''

#--------------------------
def join_batting(X,Y):
    '''
        Given a data frame of batting statistics X, and a data frame of player information Y (loaded from 'People.csv'),
        Combine the two data frames into one, according to the playerID column.
        Input:
                X: a dataframe containing the batting data of all players in year 2001
                Y: a dataframe containing the player information, such as first name, weight, height.
        Output:
                Z: a dataframe containing both batting data and player information.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Z = join(X,Y, 'playerID')
    #########################################
    return Z


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_join_batting' in the terminal.  '''

#-------------------------------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'Batting2001AJ.csv'.
'''

#-------------------------------------------------------------------------
'''
   Now the dataset contains both game statistics and player information.
   However, we still need to know the salary of a player in year 2002, which represents the price we need to pay in order to hire the player into our team.
   We have another CSV file 'Salaries.csv', which contains the player's salary information in all years.
   We first need to search the players' salaries in year 2002, then we want to merge the salary information into the dataset.
'''


#--------------------------
def search_salary(X, year=2002):
    '''
        search salary data of one year.
        For example, if we want to evaluate players for year 2002, we need to search for salary of the players in year 2002.
        Input:
                X: a dataframe containing the salary data of all players in all years.
                year: an integer scalar, the year to be searched
        Output:
                Y: a dataframe containing the salary data only in the searched year.
        Hint: you could solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = X[X.yearID==year]
    #########################################
    return Y


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_search_salary' in the terminal.  '''
#-------------------------------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'Salaries2002.csv'.
'''

#-------------------------------------------------------------------------
'''
   Now let's merge the salary information into the dataset.
'''

#--------------------------
def join_salary(X,Y):
    '''
        Given a data frame X (containing both batting statistics and player information, loaded from 'Batting2001AJ.csv'), and a data frame of salary information Y (loaded from 'Salaries2002.csv'),
        Combine the two data frames into one, according to the playerID column.
        Input:
                X: a dataframe containing the batting data and player info in year 2001
                Y: a dataframe containing the salary information in year 2002
        Output:
                Z: a dataframe containing batting data, player information and salary information.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Z = join(X,Y,'playerID')
    #########################################
    return Z


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_join_salary' in the terminal.  '''



#-------------------------------------------------------------------------
'''
    If you have passed the previous test case, the result data frame should have been saved into a file, called 'Batting2001AJS.csv'.
    This file contains all the information we need for player evaluation.
'''









#--------------------------------------------

''' TEST ALL functions in Problem 4:
        Now you can test the correctness of all the above functions by typing `nosetests -v test4.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ---------- Problem 4 (15 points in total) ------------ ... ok
            (2 points) load_batting ... ok
            (2 points) search_batting ... ok
            (3 points) aggregate_batting ... ok
            (3 points) join_batting ... ok
            (2 points) search_salary ... ok
            (3 points) join_salary ... ok
            ----------------------------------------------------------------------
            Ran 6 tests in 0.758s

            OK

'''

#--------------------------------------------
