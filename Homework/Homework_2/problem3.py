import pandas as pd

#-------------------------------------------------------------------------
'''
    Problem 3: getting familiar with pandas package.
    In this problem, please install the following python package:
        * pandas
    Pandas is the library for tabular data analysis in Python.
    It provides fast, flexible, and expressive data structures designed to make working with tabular and multidimensional data both easy and intuitive.
    To install numpy using pip, you could type `pip3 install pandas` in the terminal.

    Reference: you could read the tutorials for Pandas:
                    https://www.learndatasci.com/tutorials/python-pandas-tutorial-complete-introduction-for-beginners/
                    https://pandas.pydata.org/pandas-docs/stable/getting_started/10min.html
'''


#--------------------------
def dataframe():
    '''
       Create the following data frame using Pandas:
                    |'height'| 'width' |
                    |--------|---------|
                    |    1   |    4    |
                    |    2   |    5    |
                    |    3   |    6    |
        Output:
                X: a pandas dataframe with two columns and 3 rows,
                        the first column is "height" including 3 records with values 1, 2, 3
                        the second column is "width" including  3 records with values 4, 5, 6
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X = pd.DataFrame({'height':[1,2,3],'width':[4,5,6]})
    #########################################
    return X

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_dataframe' in the terminal.  '''


#--------------------------
def load_csv(filename="A.csv"):
    '''
        Load a data frame from CSV file.
        The CSV file contains a header line (the first row), indicating the names of all the columns.
        Input:
                filename: a string indicating the filename of the CSV file.
        Output:
                X: a pandas dataframe loaded from the CSV file
        Hint: you could solve this problem using one line of code with a function in pandas package.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X = pd.read_csv(filename)
    #########################################
    return X

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_load_csv' in the terminal.  '''



#--------------------------
def search_height(X, t=2):
    '''
        Search for all the records in a dataframe with height (column) greater or equals to the threshold value
        Input:
                X: a dataframe
                t: an integer scalar, the threshold of the height.
        Output:
                Y: the result dataframe, containing only the records with height greater or equals to the threshold
        Hint: you could solve this problem using one line of code using pandas package.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = X[X.height>=t]
    print(Y)
    #########################################
    return Y

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_search_height' in the terminal.  '''



#--------------------------
def save_csv(X, filename="A2.csv"):
    '''
        save a data frame into a CSV file.
        Note, the CSV file should contain no index column.
        Input:
                X: a pandas dataframe to be saved into the CSV file
                filename: a string indicating the filename of the CSV file.
        Hint: You could solve this problem using one line of code with a function in pandas package.
              You could set the index parameter to avoid adding an index column in the CSV file.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    X.to_csv(filename, index=False)
    #########################################
    return

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_save_csv' in the terminal.  '''



#--------------------------
def sum_column(X, key='count'):
    '''
        Compute the sum of values in the key column of a data frame.
        Suppose we have the following data frame X:
                    | 'ID'   | 'count' |
                    |--------|---------|
                    |    1   |    4    |
                    |    1   |    5    |
                    |    2   |    6    |
                    |    2   |    7    |
        and if key = 'count', we want to compute the sum of all values in the 'count' column: 4+5+6+7 = 22
        The result in this case should be 22.

        Input:
                X: a dataframe
                key: a string indicating the column to be used for summing the values.
        Output:
                S: an integer scalar, the sum of the values in the column
        Hint: you could solve this problem using one line of code using pandas package.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    S = X[key].sum()
    #########################################
    return S

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_sum_column' in the terminal.  '''


#--------------------------
def aggregate(X, key = 'ID'):
    '''
        Suppose we have the following data frame X:
                    | 'ID'   | 'count' |
                    |--------|---------|
                    |    1   |    4    |
                    |    1   |    5    |
                    |    2   |    6    |
                    |    2   |    7    |
        We have duplicated values in ID column. Now we want to aggregate the 'count' values according to their 'ID's.
        So that the record with ID=1, should have a count = 4+5
        and the record with ID=2, should have a count = 6+7
        The output should be:
                    | 'ID'   | 'count' |
                    |--------|---------|
                    |    1   |    9    |
                    |    2   |    13   |
        Input:
                X: a pandas dataframe with duplicated key values
                key: a string indicating the column to be used for grouping the rows.
        Output:
                Y: the aggregated dataframe, containing no duplicated ID's.
        Hint: you could use the groupby() function of pandas and solve this problem using two line of code.
              To convert an index into a column, you could use reset_index() method in pandas.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = X.groupby(key).sum()
    Y.reset_index(level=0,inplace=True)
    #########################################
    return Y

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_aggregate' in the terminal.  '''



#--------------------------
def join(X,Y, key = 'ID'):
    '''
        Suppose we have the following data frame X:
                    | 'ID'   | 'count' |
                    |--------|---------|
                    |    1   |    9    |
                    |    2   |    13   |

        and we have another data frame  Y:
                    | 'ID'   | 'name'  |
                    |--------|---------|
                    |    1   | 'Alex'  |
                    |    2   | 'Bob'   |
                    |    3   | 'Tom'   |

        Join the two tables with 'ID'. The output should be:
                    | 'ID'   | 'count' |  'name'  |
                    |--------|---------| ---------|
                    |    1   |    9    |   'Alex' |
                    |    2   |    13   |   'Bob'  |
        Input:
                X: a pandas dataframe
                Y: another pandas dataframe
                key: a string indicating the column to be used for joining the tables
        Output:
                Z: the result dataframe, containing the join of the two tables.
        Hint: you could use the merge() function of pandas and solve this problem using one lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Z = pd.merge(X,Y,on=key)
    #########################################
    return Z

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_join' in the terminal.  '''



#--------------------------
def filtering(X, key = 'ID', values=[1,3]):
    '''
        Suppose we have the following data frame X:
                    | 'ID'   | 'name'  |
                    |--------|---------|
                    |    1   | 'Alex'  |
                    |    2   | 'Bob'   |
                    |    3   | 'Tom'   |
        Filter the table with 'ID' (key), the values should be in the list "values".
        If the value list is [1,3], which means that we only want to keep the rows with ID=1 or ID=3.
        The output should be:
                    | 'ID'   | 'name'  |
                    |--------|---------|
                    |    1   | 'Alex'  |
                    |    3   | 'Tom'   |
        Input:
                X: a pandas dataframe
                key: a string indicating the column to be used for filtering the tables
                values: a list of values to keep in the table
        Output:
                Y: the result dataframe, containing the filtered table.
        Hint: you could use the isin() function of pandas and solve this problem using one line of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    Y = X[X[key].isin(values)]
    #########################################
    return Y

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test3.py:test_filtering' in the terminal.  '''





#--------------------------------------------

''' TEST ALL functions in Problem 3:
        Now you can test the correctness of all the above functions by typing `nosetests -v test3.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ---------- Problem 3 (10 points in total) ------------ ... ok
            (1 points) dataframe ... ok
            (1 points) load_csv ... ok
            (1 points) search_height ... ok
            (1 points) save_csv ... ok
            (1 points) sum_column ... ok
            (2 points) aggregate ... ok
            (2 points) join ... ok
            (1 points) filtering ... ok
            ----------------------------------------------------------------------
            Ran 6 tests in 0.758s

            OK

'''

#--------------------------------------------
