#-------------------------------------------------------------------------
# Note: please don't use any additional package except the following packages
import numpy as np
from problem1 import TicTacToe,PlayerRandom,get_valid_moves,check_game,Node
#-------------------------------------------------------------------------
'''
    Problem 2: Monte Carlo Tree Search (MCTS)
    In this problem, you will implement the AI player based upon Monte-Carlo Tree Search for TicTacToe game.

------------------------------------------------------------
Now let's implement tree nodes first.
Then we can connect the nodes into a search tree.
------------------------------------------------------------
'''
#-----------------------------------------------
class MCNode(Node):
    '''
        Monte Carlo Search Tree Node

        --------------------------------------------
        List of Attributes:
            s: the current state of the game, an integer matrix of shape 3 by 3.
                s[i,j] = 0 denotes that the i-th row and j-th column is empty
                s[i,j] = 1 denotes that the i-th row and j-th column is taken by "X".
                s[i,j] = -1 denotes that the i-th row and j-th column is taken by the "O".
            x: who's turn in this step of the game (if X player: x=1, or if O player: x=-1)
            p: the parent node of this node
            m: the move that it takes from the parent node to reach this node.  m is a tuple (r,c), r:row of move, c:column of the move
            c: a python list of all the children nodes of this node
                ------(statistics of simulation results)-----
            v: the sum of game results for all games that used this node during simulation.
                For example, if we have 5 game simulations used this node, and the results of the games are (1,-1,0,1,1),
                the sum of the game results will be 2.
            N: the number games that used this node for simulation.
                We can use the these two statistics (v and N) to compute the average pay-offs of each node.
                ----------------------------------------------
        --------------------------------------------
    '''
    def __init__(self,s,x=1, p=None,c=None,m=None):
        super(MCNode, self).__init__(s,x,p=p,c=c,m=m,v=0)
        self.N=0 # number of times being selected in the simulation


#----------------------------------------------
def sample(n):
    '''
   Simulation: Use a Monte-Carlo simulation to sample a game result from one node of the tree.
   Simulate a game starting from the selected node until it reaches an end of the game. In the simulation, both players are random players.

   Input:
       n: the MC_Node selected for running a simulation.
   Outputs:
       e: the result of the game (X player won:1, tie:0, lose: -1), an integer scalar.

    For example, if the game state in the selected node (n) is:
   |-------------------
   | Selected Node n
   |
   |    s=[[ 0, 1, 1],
   |       [ 0,-1, 1],
   |       [-1, 1,-1]]     -- the game state in the node
   |    x= -1              -- it's "O" player's turn in this step of the game
   |    ...
   |-------------------

    Let's run one random game (where both players are random players, who choose random moves in the game).
    # Game Result 1: Suppose in the simulation, the "O" player chooses the move (r=1,c=0),
    then "X" player chooses the move (r=0,c=0), so "X" player wins (e=1).
    # Game Result 2: If the "O" player chooses the move (0,0), then the game ends, "O" player wins (e=-1)
    If we run this sample() function multiple times, the function should have equal chance to
    return Result 1 and Result 2.

    Hint: you could use PlayerRandom and learn from the game() function in TicTacToe in problem 1.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    p1=PlayerRandom()
    p2=PlayerRandom()
    s=np.copy(n.s)
    x=n.x
    for _ in range(5):
        e = check_game(s)
        if e is not None:
            break
        r,c = p1.play(s,x)
        s[r,c]=x
        e = check_game(s)
        if e is not None:
            break
        r,c = p2.play(s,(-1*x))
        s[r,c]=(-1*x)
    #########################################
    return e

''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_sample' in the terminal.  '''


# ----------------------------------------------
def expand(n):
    '''
    Expand the current tree node by adding one layer of children nodes by adding one child node for each valid next move.
    Then select one of the children nodes to return.

    Input:
        n: the MC_Node to be expanded
    Output:
        c: one of the children nodes of the current node (self)

    For example, if the current node (BEFORE expanding) is like:
   |-------------------
   |Current Node:
   |    s=[[ 0, 1,-1],
   |       [ 0,-1, 1],
   |       [ 0, 1,-1]]     -- the game state in the node
   |    x= 1               -- it's "X" player's turn in this step of the game
   |    p= None
   |    m= None
   |    c=[] -- no children node
   |    v= 0
   |    N= 0
   |-------------------

    There are 3 valid next moves from the current game state.
    AFTER expanding this node, we add three children nodes to the current node.
    The tree looks like this after being expanded:

                        |--> Child Node A
       Current Node --> |--> Child Node B
                        |--> Child Node C

    Here are the details of the tree (attributes of each tree node):
   |-------------------
   |Current Node:
   |    s=[[ 0, 1,-1],
   |       [ 0,-1, 1],
   |       [ 0, 1,-1]]
   |    x= 1        -- it's "X" player's turn in this step of the game
   |    p= None
   |    m= None
   |    c=[Child_A, Child_B, Child_C] -- Three children nodes are created and added here
   |    v= 0
   |    N= 0
   |-------------------------------
           |Child Node A:
           |    s=[[ 1, 1,-1],
           |       [ 0,-1, 1],
           |       [ 0, 1,-1]]
           |    x=-1            -- it's "O" player's turn in this step of the game
           |    p= Current_Node -- The parent node of this node is "Current_Node"
           |    m= (0,0)        -- The move it takes from parent node
           |                         to this node: first row (0), first column (0)
           |    c=[] -- this node has not been expanded yet
           |    v= 0
           |    N= 0
           |-----------------------
           |Child Node B:
           |    s=[[ 0, 1,-1],
           |       [ 1,-1, 1],
           |       [ 0, 1,-1]]
           |    x=-1            -- it's "O" player's turn in this step of the game
           |    p= Current_Node -- The parent node of this node is "Current_Node"
           |    m= (1,0)        -- The move it takes from parent node
           |                        to this node: second row (1), first column (0)
           |    c=[] -- this node has not been expanded yet
           |    v= 0
           |    N= 0
           |-----------------------
           |Child Node C:
           |    s=[[ 0, 1,-1],
           |       [ 0,-1, 1],
           |       [ 1, 1,-1]]
           |    x=-1            -- it's "O" player's turn in this step of the game
           |    p= Current_Node -- The parent node of this node is "Current_Node"
           |    m= (2,0)        -- The move it takes from parent node
           |                        to this node: third row (2), first column (0)
           |    c=[] -- this node has not been expanded yet
           |    v= 0
           |    N= 0
           |-----------------------
    After the expansion, you need to return one of the children nodes as the output.
    For example, you could return Child Node A, or Child Node B, or Child Node C.

    Hint: This step is similar to the expand() in problem 1.
          You could solve this problem using 6 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    # get the list of valid next moves from the current game state
    m = get_valid_moves(n.s)
    if n.x == 1:   xVal = -1
    elif n.x == -1: xVal = 1
    # expand the node with one level of children nodes
    for move in m:
        child_s = np.copy(n.s)
        child_s[move] = n.x
        c = MCNode(child_s,xVal,n,None,move)
        n.c.append(c)
    #########################################
    return c

''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_expand' in the terminal.  '''



# ----------------------------------------------
def backprop(S,e):
    '''
     back propagation: after one simulation in node S, use the game result to update the statistics in the nodes on the path from node S to the root node.
     Along the way, update v (sum of simulation results) and N (count of simulations).
      Inputs:
            S: the selected node (S), where the Monte-Carlo simulation was started from.
            e: the result of the Monte-Carlo simulation (X player won:1, tie:0, lose: -1), an integer scalar.

     For example, the current game state is
     |-------------------
     | Root Node:
     |    s=[[ 1,-1, 1],
     |       [ 0, 0, 0],
     |       [ 0, 0,-1]]     -- the game state in the node
     |    x= 1               -- it's "X" player's turn in this step of the game
     |    p= None
     |    m= None
     |    c=[] -- list of children nodes
     |    v= None
     |-------------------

     Suppose the tree looks like this:

                    |--> Child Node A -->|--> Grand Child A1 (v=1,N=1)
                    |     1,-1, 1 (v=3)  |--> Grand Child A2 (v=1,N=1)
                    |     1, 0, 0 (N=8)  |--> Grand Child A3 (v=0,N=4)
                    |     0, 0,-1        |--> Grand Child A4 (v=1,N=1)
                    |
                    |--> Child Node B -->|--> Grand Child B1 (v=1,N=1)
                    |     1,-1, 1 (v=4)  |--> Grand Child B2 (v=1,N=1)
                    |     0, 1, 0 (N=9)  |--> Grand Child B3 (v=0,N=5)
                    |     0, 0,-1        |--> Grand Child B4 (v=1,N=1)
                    |
     Root Node ---> |--> Child Node C -->|--> Grand Child C1 (v=0,N=1)
      1,-1, 1 (v=19)|     1,-1, 1 (v=-3) |--> Grand Child C2 (v=0,N=1)
      0, 0, 0 (N=54)|     0, 0, 1 (N=7)  |--> Grand Child C3 (v=0,N=1)
      0, 0,-1       |     0, 0,-1        |--> Grand Child C4 (v=-3,N=3)
                    |
                    |--> Child Node D -->|--> Grand Child D1 (v=3,N=5)
                    |     1,-1, 1 (v=13) |--> Grand Child D2 (v=3,N=5)
                    |     0, 0, 0 (N=21) |--> Grand Child D3 (v=4,N=5)(S: selected node)
                    |     1, 0,-1        |--> Grand Child D4 (v=2,N=5)
                    |
                    |--> Child Node E -->|--> Grand Child E1 (v=0,N=1)
                          1,-1, 1 (v=1)  |--> Grand Child E2 (v=0,N=1)
                          0, 0, 0 (N=5)  |--> Grand Child E3 (v=1,N=1)
                          0, 1,-1        |--> Grand Child E4 (v=0,N=1)

     Here v is the sum of simulation results, N is the count of game simulations.
     Suppose the selected node for running simulation is "Grand Child D3".
     Now we run a simulation starting from D3 node, and get one sample result: X player win (e=1).
     The back-propagation is to update the nodes on the path from D3 to Root node.
     In each node on the path, the statistics are updated with the game result (e=1)
     After back-propagation, the tree looks like this:

                    |--> Child Node A -->|--> Grand Child A1 (v=1,N=1)
                    |     1,-1, 1 (v=3)  |--> Grand Child A2 (v=1,N=1)
                    |     1, 0, 0 (N=8)  |--> Grand Child A3 (v=0,N=4)
                    |     0, 0,-1        |--> Grand Child A4 (v=1,N=1)
                    |
                    |--> Child Node B -->|--> Grand Child B1 (v=1,N=1)
                    |     1,-1, 1 (v=4)  |--> Grand Child B2 (v=1,N=1)
                    |     0, 1, 0 (N=9)  |--> Grand Child B3 (v=0,N=5)
                    |     0, 0,-1        |--> Grand Child B4 (v=1,N=1)
                    |
     Root Node ---> |--> Child Node C -->|--> Grand Child C1 (v=0,N=1)
      1,-1, 1 (v=20)|     1,-1, 1 (v=-3) |--> Grand Child C2 (v=0,N=1)
      0, 0, 0 (N=55)|     0, 0, 1 (N=7)  |--> Grand Child C3 (v=0,N=1)
      0, 0,-1       |     0, 0,-1        |--> Grand Child C4 (v=-3,N=3)
                    |
                    |--> Child Node D -->|--> Grand Child D1 (v=3,N=5)
                    |     1,-1, 1 (v=14) |--> Grand Child D2 (v=3,N=5)
                    |     0, 0, 0 (N=22) |--> Grand Child D3 (v=5,N=6)(S: selected node)
                    |     1, 0,-1        |--> Grand Child D4 (v=2,N=5)
                    |
                    |--> Child Node E -->|--> Grand Child E1 (v=0,N=1)
                          1,-1, 1 (v=1)  |--> Grand Child E2 (v=0,N=1)
                          0, 0, 0 (N=5)  |--> Grand Child E3 (v=1,N=1)
                          0, 1,-1        |--> Grand Child E4 (v=0,N=1)
    There are three nodes on the path and their statistics are updated as:
    (1) Grand Child D3: v =(4 -> 5),    N =(5 -> 6)
    (2) Child Node D:   v =(13 -> 14),  N =(21 -> 22)
    (3) Root Node:      v =(19 -> 20),  N =(54 -> 55)

    Hint: you could use recursion to solve this problem using 4 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    S.v = (S.v)+e
    S.N = (S.N)+1
    if(S.p != None):
        backprop(S.p,e)
    #########################################

''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_backprop' in the terminal.  '''


#----------------------------------------------
def compute_UCB(vi, ni, N, x ,c=1.142):
    '''
      compute UCB (Upper Confidence Bound) of a child node (the i-th child node).
      The UCB score is the sum of two terms:
      (1) Exploitation: the average payoffs of the child node = x*vi/ni
      (2) Exploration: the need for exploring the child node = sqrt( log(N) / ni ).
                        Note: when ni=0, this term should equals to positive infinity (instead of a divide-by-zero error).
      The final score is computed as  (1)+ c* (2).
      A larger UCB score means that the child node leads to a better average pay-offs for the player, or the child node needs exploring.

      Inputs:
            vi: the sum of game results after choosing the i-th child node, an integer scalar
            ni: the number of simulations choosing the i-th child node, an integer scalar
            N: total number of simulations for the parent node, an integer scalar
            x: the role of the parent node (X player:1 or O player:-1)
            c: the parameter to trade-off between exploration and exploitation, a float scalar
        Outputs:
            b: the UCB score of the child node, a float scalar.
    Hint: you could solve this problem using 4 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    if ni==0:
        b = float('inf')
    else:
        ext = x*vi/ni
        exr = np.power((np.log(N)/ni),0.5)
        b = ext + (c*exr)
    #########################################
    return b

''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_compute_UCB' in the terminal.  '''


#----------------------------------------------
def select_a_child(p):
    '''
     Select a child node of this node with the highest UCB score.

    Inputs:
        p: the parent node
    Outputs:
        c: the child node with the highest UCB score

    For example, suppose we have a parent node with two children nodes:
    ---------------------
    Parent Node:  N = 12, x= -1 (O player)
        |Child Node A: v =-1, N = 2
        |Child Node B: v =-5, N = 10
    ---------------------
    The UCB bound of Child Node A: vi=-1, ni=2, N= 12, x=-1
    The UCB bound of Child Node B: vi=-5, ni=10, N= 12, x=-1
    In this example, the average payoffs (x*vi/ni) for the two nodes are the same.
    The second term (exploration) determines which nodes get higher score: Child Node A is under-explored.
    So the Child Node A will have a higher UCB score, and this function will select Child Node A to return.

    When there is a tie in the UCB score, use the index of the child node as the tie-breaker.
    Hint: you could solve this problem using 6 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    B = []
    c = p
    if(len(p.c)!=0):
        for child in p.c:
            vi = child.v
            ni = child.N
            N = p.N
            x = p.x
            B.append(compute_UCB(vi,ni,N,x))
        c = p.c[B.index(max(B))]
    #########################################
    return c


''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_select_a_child' in the terminal.  '''




#----------------------------------------------
def selection(r):
    '''
        Select a leaf node by traveling down the tree from root. Here a leaf node is a node with no child node.
        In each step, choose the child node with the highest UCB score, until reaching a leaf node.

        Inputs:
            r: the root node of the search tree
        Outputs:
            l: the leaf node selected
        For example, suppose we have a search tree:

                            (O's turn)
                    |--> Child Node A -->|--> Grand Child A1 (v=1,N=1)
                    |     1,-1, 1 (v=3)  |--> Grand Child A2 (v=1,N=1)
                    |     1, 0, 0 (N=8)  |--> Grand Child A3 (v=0,N=4)
                    |     0, 0,-1        |--> Grand Child A4 (v=1,N=1)
                    |
                    |--> Child Node B -->|--> Grand Child B1 (v=1,N=1)
                    |     1,-1, 1 (v=4)  |--> Grand Child B2 (v=1,N=1)
                    |     0, 1, 0 (N=9)  |--> Grand Child B3 (v=0,N=5)
                    |     0, 0,-1        |--> Grand Child B4 (v=1,N=1)
      (X's turn)    |
     Root Node ---> |--> Child Node C -->|--> Grand Child C1 (v=0,N=1)
      1,-1, 1 (v=20)|     1,-1, 1 (v=-3) |--> Grand Child C2 (v=0,N=1)
      0, 0, 0 (N=55)|     0, 0, 1 (N=7)  |--> Grand Child C3 (v=0,N=1)
      0, 0,-1       |     0, 0,-1        |--> Grand Child C4 (v=-3,N=3)
                    |
                    |--> Child Node D -->|--> Grand Child D1 (v=3,N=5)
                    |     1,-1, 1 (v=14) |--> Grand Child D2 (v=3,N=5)
                    |     0, 0, 0 (N=22) |--> Grand Child D3 (v=5,N=6)
                    |     1, 0,-1        |--> Grand Child D4 (v=2,N=5)
                    |
                    |--> Child Node E -->|--> Grand Child E1 (v=0,N=1)
                          1,-1, 1 (v=1)  |--> Grand Child E2 (v=0,N=1)
                          0, 0, 0 (N=5)  |--> Grand Child E3 (v=1,N=1)
                          0, 1,-1        |--> Grand Child E4 (v=0,N=1)

        We will call the function l = selection(Root_Node)
        Among the first level of children nodes,  the "Child Node D" has the highest UCB score.
        Then in the second level, we travel down to the "Child Node D" and find that "Grand Child D3" has the highest score
        among all the children nodes of "Child Node D".
        Then we travel down to the "Grand Child D3" and find that this node is a leaf node (no child).
        So we return "Grand Child D3" as the selected node to return.
        Hint: you could use recursion to solve this problem using 4 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    # if the root node is a leaf node (no child), return root node
    if(len(r.c)==0):
        l = r
    # otherwise: select a child node (c) of the root node
    else:
        c = select_a_child(r)
        #recursively select the children nodes of node (c).
        l = selection(c)
    #########################################
    return l


''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_selection' in the terminal.  '''



#----------------------------------------------
def build_tree(r, n_iter=100):
    '''
    Given a node of the current game state, build a Monte-Carlo Search Tree by n iteration of (selection->expand->sample->backprop).
    Inputs:
        r: a MC_Node for the current game state
        n_iter: number of iterations, an integer scalar



        For example, suppose the current game state:

            Root Node
             1,-1, 1 (v=0)
             0, 0, 0 (N=0)
             0, 0,-1 (X player's turn)

        Now let's run one iteration of Monte-Carlo Tree Search (selection->expand->sample->backprop):
        ---------------------------------
        Iteration 1:
        ---------------------------------
        (1) selection:  starting from root node, select one leaf node (L)
            In this case, the root node is a leaf node (no child node yet)
        (2) expand: Since the game in the leaf node has not ended yet, we need to expand the node.
            Then one of the children nodes will be selected, the tree becomes:
                            (O's turn)
                    |--> Child Node A
                    |     1,-1, 1 (v=0) (S: Selected Node)
                    |     1, 0, 0 (N=0)
                    |     0, 0,-1
                    |
                    |--> Child Node B
                    |     1,-1, 1 (v=0)
                    |     0, 1, 0 (N=0)
                    |     0, 0,-1
      (X's turn)    |
     Root Node ---> |--> Child Node C
      1,-1, 1 (v= 0)|     1,-1, 1 (v= 0)
      0, 0, 0 (N= 0)|     0, 0, 1 (N=0)
      0, 0,-1       |     0, 0,-1
                    |
                    |--> Child Node D
                    |     1,-1, 1 (v= 0)
                    |     0, 0, 0 (N= 0)
                    |     1, 0,-1
                    |
                    |--> Child Node E
                          1,-1, 1 (v=0)
                          0, 0, 0 (N=0)
                          0, 1,-1

        (3) Sample: run a Monte-Carlo simulation on the selected Node (S), suppose the result of the game is a draw (e=0)
        (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
            The statistics of the tree look like this:
                         |--> Child Node A (v=0,N=1) (S: Selected Node)
                         |--> Child Node B (v=0,N=0)
     Root (v=0,N=1) ---> |--> Child Node C (v=0,N=0)
                         |--> Child Node D (v=0,N=0)
                         |--> Child Node E (v=0,N=0)

        ---------------------------------
        Iteration 2:
        ---------------------------------
        (1) selection:  starting from root node, select one leaf node (L)
            In the first level of children nodes, "Child Node B" has the largest UCB score (with index as tie-breaker).
            It is also a leaf node (no child node yet), so this node will be selected as the leaf node.
        (2) expand: Since the game in the leaf node has not ended yet, we need to expand the node.
            Then one of the children nodes will be selected, the tree becomes:

                            (O's turn)                       (X's turn)
                         |--> Child Node A (v=0,N=1)
                         |--> Child Node B (v=0,N=0)--> |--> Grand Child B1 (v=0,N=0) (S: Selected Node)
                         |                              |--> Grand Child B2 (v=0,N=0)
                         |                              |--> Grand Child B3 (v=0,N=0)
       (X's turn)        |                              |--> Grand Child B4 (v=0,N=0)
     Root (v=0,N=1) ---> |--> Child Node C (v=0,N=0)
                         |--> Child Node D (v=0,N=0)
                         |--> Child Node E (v=0,N=0)
        (3) Sample: run a Monte-Carlo simulation on the selected Node (S), suppose the result of the game is X win (e=1)
        (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
            The statistics of the tree look like this:

                            (O's turn)                       (X's turn)
                         |--> Child Node A (v=0,N=1)
                         |--> Child Node B (v=1,N=1)--> |--> Grand Child B1 (v=1,N=1) (S: Selected Node)
                         |                              |--> Grand Child B2 (v=0,N=0)
                         |                              |--> Grand Child B3 (v=0,N=0)
       (X's turn)        |                              |--> Grand Child B4 (v=0,N=0)
     Root (v=1,N=2) ---> |--> Child Node C (v=0,N=0)
                         |--> Child Node D (v=0,N=0)
                         |--> Child Node E (v=0,N=0)

        ---------------------------------
        Iteration 3:
        ---------------------------------
        (1) selection:  starting from root node, select one leaf node (L)
            In the first level of children nodes, "Child Node C" has the largest UCB score (with index as tie-breaker).
            It is also a leaf node (no child node yet), so this node will be selected as the leaf node.
        (2) expand: Since the game in the leaf node has not ended yet, we need to expand the node.
            Then one of the children nodes will be selected, the tree becomes:

                            (O's turn)                       (X's turn)
                         |--> Child Node A (v=0,N=1)
                         |--> Child Node B (v=1,N=1)--> |--> Grand Child B1 (v=1,N=1)
                         |                              |--> Grand Child B2 (v=0,N=0)
                         |                              |--> Grand Child B3 (v=0,N=0)
                         |                              |--> Grand Child B4 (v=0,N=0)
       (X's turn)        |
     Root (v=1,N=2) ---> |--> Child Node C (v=0,N=0)--> |--> Grand Child c1 (v=0,N=0) (S: Selected Node)
                         |                              |--> Grand Child c2 (v=0,N=0)
                         |                              |--> Grand Child c3 (v=0,N=0)
       (X's turn)        |                              |--> Grand Child c4 (v=0,N=0)
                         |--> Child Node D (v=0,N=0)
                         |--> Child Node E (v=0,N=0)

        (3) Sample: run a Monte-Carlo simulation on the selected Node (S), suppose the result of the game is (e=-1)
        (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
            The statistics of the tree look like this:

                            (O's turn)                       (X's turn)
                         |--> Child Node A (v= 0,N=1)
                         |--> Child Node B (v= 1,N=1)--> |--> Grand Child B1 (v=1,N=1)
                         |                               |--> Grand Child B2 (v=0,N=0)
                         |                               |--> Grand Child B3 (v=0,N=0)
                         |                               |--> Grand Child B4 (v=0,N=0)
       (X's turn)        |
     Root (v=1,N=2) ---> |--> Child Node C (v=-1,N=1)--> |--> Grand Child C1 (v=-1,N=1) (S: Selected Node)
                         |                               |--> Grand Child C2 (v=0,N=0)
                         |                               |--> Grand Child C3 (v=0,N=0)
       (X's turn)        |                               |--> Grand Child C4 (v=0,N=0)
                         |--> Child Node D (v= 0,N=0)
                         |--> Child Node E (v= 0,N=0)

        ...


        ---------------------------------
        Suppose that, after 55 iterations, the tree looks like this:
                            (O's turn)             (X's turn)
                    |--> Child Node A -->|--> Child A1 (v= 1,N=1) -->| ...
                    |     1,-1, 1 (v=3)  |--> Child A2 (v= 1,N=1) -->| ...
                    |     1, 0, 0 (N=8)  |--> Child A3 (v= 0,N=4) -->| ...
                    |     0, 0,-1        |--> Child A4 (v= 1,N=1) -->| ...
                    |
                    |--> Child Node B -->|--> Child B1 (v= 1,N=1) -->| ...
                    |     1,-1, 1 (v=4)  |--> Child B2 (v= 1,N=1) -->| ...
                    |     0, 1, 0 (N=9)  |--> Child B3 (v= 0,N=5) -->| ...
                    |     0, 0,-1        |--> Child B4 (v= 1,N=1) -->| ...
      (X's turn)    |
     Root Node ---> |--> Child Node C -->|--> Child C1 (v=-1,N=1) -->| ...
      1,-1, 1 (v=25)|     1,-1, 1 (v=-3) |--> Child C2 (v= 0,N=1) -->| ...
      0, 0, 0 (N=55)|     0, 0, 1 (N=7)  |--> Child C3 (v= 0,N=1) -->| ...
      0, 0,-1       |     0, 0,-1        |--> Child C4 (v=-3,N=3) -->| ...
                    |
                    |--> Child Node D -->|--> Child D1 (v= 5,N=6) -->| Child D11 (v= 5,N=5) (game ends)
                    |     1,-1, 1 (v=20) |--> Child D2 (v= 5,N=5) -->| ...
                    |     0, 0, 0 (N=22) |--> Child D3 (v= 5,N=5) -->| ...
                    |     1, 0,-1        |--> Child D4 (v= 5,N=5) -->| ...
                    |
                    |--> Child Node E -->|--> Child E1 (v= 0,N=1) -->| ...
                          1,-1, 1 (v=1)  |--> Child E2 (v= 0,N=1) -->| ...
                          0, 0, 0 (N=5)  |--> Child E3 (v= 1,N=1) -->| ...
                          0, 1,-1        |--> Child E4 (v= 0,N=1) -->| ...

        ---------------------------------
        Iteration 56:
        ---------------------------------
        (1) selection:  starting from root node, select one leaf node (L)
            In the first level of children nodes, "Child Node D" has the largest UCB score for X player.
            In the second level of children nodes, "Child D1" has the largest UCB score for O player.
            In the third level of children nodes, "Child D11" has the largest UCB score for X player.
            It is also a leaf node (no child node), so this node will be selected as the leaf node.
        (2) expand: Since the game in the D11 node has ended, we DON'T expand the node.
            So Node D11 will be selected.
        (3) Sample: run a Monte-Carlo simulation on the selected Node (D11), suppose the result of the game is X win (e=1)
        (4) Back Prop: Back propagate the simulation result from Node (S) to the root.
            The statistics of the tree look like this:

                            (O's turn)             (X's turn)
                    |--> Child Node A -->|--> Child A1 (v= 1,N=1) -->| ...
                    |     1,-1, 1 (v=3)  |--> Child A2 (v= 1,N=1) -->| ...
                    |     1, 0, 0 (N=8)  |--> Child A3 (v= 0,N=4) -->| ...
                    |     0, 0,-1        |--> Child A4 (v= 1,N=1) -->| ...
                    |
                    |--> Child Node B -->|--> Child B1 (v= 1,N=1) -->| ...
                    |     1,-1, 1 (v=4)  |--> Child B2 (v= 1,N=1) -->| ...
                    |     0, 1, 0 (N=9)  |--> Child B3 (v= 0,N=5) -->| ...
                    |     0, 0,-1        |--> Child B4 (v= 1,N=1) -->| ...
      (X's turn)    |
     Root Node ---> |--> Child Node C -->|--> Child C1 (v=-1,N=1) -->| ...
      1,-1, 1 (v=26)|     1,-1, 1 (v=-3) |--> Child C2 (v= 0,N=1) -->| ...
      0, 0, 0 (N=56)|     0, 0, 1 (N=7)  |--> Child C3 (v= 0,N=1) -->| ...
      0, 0,-1       |     0, 0,-1        |--> Child C4 (v=-3,N=3) -->| ...
                    |
                    |--> Child Node D -->|--> Child D1 (v= 6,N=7) -->| Child D11 (v=6,N=6) (selected)
                    |     1,-1, 1 (v=21) |--> Child D2 (v= 5,N=5) -->| ...
                    |     0, 0, 0 (N=23) |--> Child D3 (v= 5,N=5) -->| ...
                    |     1, 0,-1        |--> Child D4 (v= 5,N=5) -->| ...
                    |
                    |--> Child Node E -->|--> Child E1 (v= 0,N=1) -->| ...
                          1,-1, 1 (v=1)  |--> Child E2 (v= 0,N=1) -->| ...
                          0, 0, 0 (N=5)  |--> Child E3 (v= 1,N=1) -->| ...
                          0, 1,-1        |--> Child E4 (v= 0,N=1) -->| ...

    Hint: you could use the functions implemented above to solve this problem using 5 lines of code.
    '''
    # iterate n_iter times
    for _ in range(n_iter):
        #########################################
        ## INSERT YOUR CODE HERE
        # Step 1: selection: starting from root node, select one leaf node (L)
        l = selection(r)
        # Step 2: expansion: if in the leaf node L, the game has not ended yet,
        #                    expand node (L) with one level of children nodes
        #                    and then select one of L's children nodes (C) as the leaf node
        if check_game(l.s) == None:
            l = expand(l)
        # Step 3: simulation: sample a game result from the selected leaf node:
        #               the selected node is node C (if L is not a terminal node)
        #                                 or node L (if L is a terminal node, game ended)
        e = sample(l)
        # Step 4: back propagation: backprop the result of the game sample
        backprop(l,e)

        #########################################

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_build_tree' in the terminal.  '''

#-----------------------------------------------
'''
    AI Player 2 (MCTS Player): Now let's implement the Monte-Carlo Tree Search agent for the game.
    The goal of this agent is to find the approximately optimal move for the current game state.
    (1) Build Tree: we will first build a Monte-Carlo Search Tree, where the root of the tree is the current game state.
    (2) Choose Optimal Next Move: the agent will choose the child node with the largest number (N) as the next move.
'''

# ----------------------------------------------
# Let's implement step (2): choose optimal next move
def choose_optimal_move(n):
    '''
        Assume we have a Monte-Carlo search tree, and the statistics of all nodes are already computed.

        (3) Choose Next Move: the agent will choose the child node with the largest N value as the next move.

       Inputs:
            n: the root node of the search tree, assuming the statistics in all nodes are already computed.
       Outputs:
            r: the row number of the optimal next move, an integer scalar with value 0, 1, or 2.
            c: the column number of the optimal next move, an integer scalar with value 0, 1, or 2.

        For example, suppose we have the following search tree (X player's turn):
                            (O's turn)             (X's turn)
                    |--> Child Node A -->|--> Child A1 (v= 1,N=1) -->| ...
                    |     1,-1, 1 (v=3)  |--> Child A2 (v= 1,N=1) -->| ...
                    |     1, 0, 0 (N=8)  |--> Child A3 (v= 0,N=4) -->| ...
                    |     0, 0,-1        |--> Child A4 (v= 1,N=1) -->| ...
                    |
                    |--> Child Node B -->|--> Child B1 (v= 1,N=1) -->| ...
                    |     1,-1, 1 (v=4)  |--> Child B2 (v= 1,N=1) -->| ...
                    |     0, 1, 0 (N=9)  |--> Child B3 (v= 0,N=5) -->| ...
                    |     0, 0,-1        |--> Child B4 (v= 1,N=1) -->| ...
      (X's turn)    |
     Root Node ---> |--> Child Node C -->|--> Child C1 (v=-1,N=1) -->| ...
      1,-1, 1 (v=26)|     1,-1, 1 (v=-3) |--> Child C2 (v= 0,N=1) -->| ...
      0, 0, 0 (N=56)|     0, 0, 1 (N=7)  |--> Child C3 (v= 0,N=1) -->| ...
      0, 0,-1       |     0, 0,-1        |--> Child C4 (v=-3,N=3) -->| ...
                    |
                    |--> Child Node D -->|--> Child D1 (v= 6,N=7) -->| ...
                    |     1,-1, 1 (v=21) |--> Child D2 (v= 5,N=5) -->| ...
                    |     0, 0, 0 (N=23) |--> Child D3 (v= 5,N=5) -->| ...
                    |     1, 0,-1        |--> Child D4 (v= 5,N=5) -->| ...
                    |
                    |--> Child Node E -->|--> Child E1 (v= 0,N=1) -->| ...
                          1,-1, 1 (v=1)  |--> Child E2 (v= 0,N=1) -->| ...
                          0, 0, 0 (N=5)  |--> Child E3 (v= 1,N=1) -->| ...
                          0, 1,-1        |--> Child E4 (v= 0,N=1) -->| ...

        The optimal next move will be child node with the largest N (Child Node D) in the first level of the tree.
        So in this example, the next move should be (r=2, c=0)
        Hint: you could solve this problem using 5 lines of code.
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    val = []
    optimalVal = 0
    for c in n.c:
        val.append(c.N)
    optimalVal = max(val)
    index = val.index(optimalVal)
    r,c = n.c[index].m
    #########################################
    return r,c

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_choose_optimal_move' in the terminal.  '''


#-------------------------------------------------------
class PlayerMCTS:
    '''a player, that chooses optimal moves by Monte Carlo tree search. '''
    # ----------------------------------------------
    def play(self,s,x=1,n_iter=100):
        '''
           the policy function of the MCTS player, which chooses one move in the game.
           Build a search tree with the current state as the root. Then find the most visited child node as the next move.
           Inputs:
                s: the current state of the game, an integer matrix of shape 3 by 3.
                    s[i,j] = 0 denotes that the i-th row and j-th column is empty
                    s[i,j] = 1 denotes that the i-th row and j-th column is taken by you. (for example, if you are the "O" player, then i, j-th slot is taken by "O")
                    s[i,j] = -1 denotes that the i-th row and j-th column is taken by the opponent.
                x: the role of the player, 1 if you are the "X" player in the game
                    -1 if you are the "O" player in the game.
                n_iter: number of iterations when building the tree, an integer scalar
           Outputs:
                r: the row number, an integer scalar with value 0, 1, or 2.
                c: the column number, an integer scalar with value 0, 1, or 2.
        Hint: you could solve this problem using 3 lines of code.
        '''
        #########################################
        ## INSERT YOUR CODE HERE
        # create a tree node (n) with the current game state
        n = MCNode(s,x)
        # build a search tree with the tree node (n) as the root and n_iter as the number of simulations
        build_tree(n,n_iter)
        # choose the best next move: the children node of the root node with the largest N
        r,c = choose_optimal_move(n)
        #########################################
        return r,c

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test2.py:test_MCTS_play' in the terminal.  '''



#--------------------------------------------

''' TEST Problem 2:
        Now you can test the correctness of all the above functions by typing `nosetests -v test2.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 2 (55 points in total)--------------------- ... ok
            (10 points) sample ... ok
            (5 points) expand ... ok
            (5 points) backprop ... ok
            (5 points) compute_UCB ... ok
            (5 points) select_a_child ... ok
            (5 points) selection ... ok
            (5 points) build_tree ... ok
            (5 points) choose_optimal_move() ... ok
            (10 points) MCTS play ... ok
            ----------------------------------------------------------------------
            Ran 10 tests in 3.117s
            OK
'''

#--------------------------------------------

''' FINAL TEST of your submission:
        Now you can test the correctness of all the problems in this homework by typing `nosetests -v' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 1 (45 points in total)--------------------- ... ok
            (5 points) get_valid_moves() ... ok
            (5 points) check_game() ... ok
            (5 points) random play() ... ok
            (5 points) expand ... ok
            (5 points) build_tree ... ok
            (5 points) compute_v() ... ok
            (5 points) choose_optimal_move() ... ok
            (10 points) minmax play() ... ok
            ----------- Problem 2 (55 points in total)--------------------- ... ok
            (10 points) sample ... ok
            (5 points) expand ... ok
            (5 points) backprop ... ok
            (5 points) compute_UCB ... ok
            (5 points) select_a_child ... ok
            (5 points) selection ... ok
            (5 points) build_tree ... ok
            (5 points) choose_optimal_move() ... ok
            (10 points) MCTS play ... ok
            ----------------------------------------------------------------------
            Ran 20 tests in 6.203s

'''
#--------------------------------------------
