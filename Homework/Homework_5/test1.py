from problem1 import *
import numpy as np
import sys

'''
    Unit test 1:
    This file includes unit tests for problem1.py.
    You could test the correctness of your code by typing `nosetests -v test1.py` in the terminal.
'''

#-------------------------------------------------------------------------
def test_terms_and_conditions():
    ''' Read and Agree with Terms and Conditions'''
    assert Terms_and_Conditions() # require reading and agreeing with Terms and Conditions. 


#-------------------------------------------------------------------------
def test_python_version():
    ''' ----------- Problem 1 (45 points in total)---------------------'''
    assert sys.version_info[0]==3 # require python 3 (instead of python 2)


#-------------------------------------------------------------------------
def test_get_valid_moves():
    '''(5 points) get_valid_moves()'''

    s=np.array([[  1 , 0 ,-1 ],
                [ -1 , 1 , 0 ],
                [  1 , 0 ,-1 ]])

    m=get_valid_moves(s)
    assert type(m)==list
    assert len(m)==3
    assert m[0]== (0,1) or m[0]== (1,2) or m[0] == (2,1)
    assert m[1]== (0,1) or m[1]== (1,2) or m[1] == (2,1)
    assert m[2]== (0,1) or m[2]== (1,2) or m[2] == (2,1)
    assert m[0]!=m[1] and m[1]!=m[2]

    
    m=get_valid_moves(np.zeros((3,3)))
    assert len(m)==9

    s=np.array([[  1 , 0 ,-1 ],
                [  0 , 0 , 0 ],
                [  1 , 0 ,-1 ]])
    m=get_valid_moves(s)
    assert len(m)==5
    for i in m:
        assert i== (0,1) or i== (1,0) or i== (1,1) or i== (1,2) or i== (2,1)  


#-------------------------------------------------------------------------
def test_check_game():
    '''(5 points) check_game()'''
    s=np.array([[ 1, 0, 1],
                [ 0, 0,-1],
                [ 0,-1, 0]])
    e = check_game(s)
    assert e is None # the game has not ended yet

    s=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [-1, 1,-1]])
    e = check_game(s)
    assert e is None # the game has not ended yet

    s=np.array([[ 1, 1, 1],
                [ 0, 0,-1],
                [ 0,-1, 0]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 0],
                [ 1, 1, 1],
                [ 0,-1, 0]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 0],
                [ 0, 0,-1],
                [ 1, 1, 1]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins
    
    s=np.array([[ 1, 0, 0],
                [ 1, 0,-1],
                [ 1,-1, 0]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 1, 0 ],
                [ 0, 1, 0 ],
                [-1, 1, 0 ]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 1],
                [ 0, 0, 1],
                [-1, 0, 1]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[ 1, 0, 0],
                [ 0, 1,-1],
                [-1, 0, 1]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins

    s=np.array([[-1, 0, 1],
                [ 0, 1, 0],
                [ 1, 0,-1]])
    e = check_game(s)
    assert e == 1  # x player wins
    e = check_game(-s)
    assert e ==-1  # O player wins


    s=np.array([[-1, 1,-1],
                [ 1, 1,-1],
                [ 1,-1, 1]])
    e = check_game(s)
    assert e == 0 # a tie


#-------------------------------------------------------------------------
def test_random_play():
    '''(5 points) random play()'''
    p = PlayerRandom()
    s=np.array([[ 0, 1, 1],
                [ 1, 0,-1],
                [ 1, 1, 0]])

    s_=np.array([[ 0, 1, 1],
                 [ 1, 0,-1],
                 [ 1, 1, 0]])
    count=np.zeros(3)
    for _ in range(100):
        r,c = p.play(s)
        assert s[r,c]==0 # player needs to choose a valid move 
        assert r==c # in this example the valid moves are on the diagonal of the matrix
        assert r>-1 and r<3
        assert np.allclose(s,s_) # the player should never change the game state object
        count[c]+=1
    assert count[0]>20 # the random player should give roughly equal chance to each valid move
    assert count[1]>20
    assert count[2]>20
    
    s=np.array([[ 1, 1, 0],
                [ 1, 0,-1],
                [ 0, 1, 1]])

    for _ in range(100):
        r,c = p.play(s)
        assert s[r,c]==0 
        assert r==2-c 
        assert r>-1 and r<3
 


#-------------------------------------------------------------------------
def test_expand():
    '''(5 points) expand'''

    # Current Node (root)
    s=np.array([[0, 1,-1],
                [0,-1, 1],
                [0, 1,-1]])
    n = Node(s,x=1) #it's X player's turn
    # expand
    n.expand()
    assert len(n.c) ==3 
    assert n.x==1
    s_=np.array([[0, 1,-1],
                 [0,-1, 1],
                 [0, 1,-1]])
    # the current game state should not change after expanding
    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert c.x==-1
        assert c.p==n
        assert c.c==[]
        assert c.v==None

    # child node A
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
    assert c

    # child node B
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
    assert c

    # child node C
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    #--------------------------

    # Current Node (root)
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    n = Node(s,-1) #it's O player's turn
    n.expand()
    assert n.x==-1
    assert len(n.c) ==2
    for c in n.c:
        assert c.x==1
        assert c.p==n
        assert c.c==[]

    # child node A
    s=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
    assert c

    # child node B
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    #---------------------------
    n = Node(np.zeros((3,3)),1)
    n.expand()
    assert n.x==1
    assert len(n.c) ==9
    for c in n.c:
        assert c.x==-1
        assert c.p==n
        assert c.c==[]
        assert np.sum(c.s)==1
        assert c.v==None



#-------------------------------------------------------------------------
def test_build_tree():
    '''(5 points) build_tree'''

    # current node (root node)
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    n = Node(s, x=1) # it's X player's turn
    n.build_tree()

    assert len(n.c) ==3 
    assert n.x==1
    assert n.v==None
    assert n.p==None
    assert n.m==None

    s_=np.array([[0, 1,-1],
                 [0,-1, 1],
                 [0, 1,-1]])
    # the current game state should not change after expanding
    assert np.allclose(n.s,s_) 
    for c in n.c:
        assert c.x==-1
        assert c.p==n
        assert len(c.c)==2
        assert c.v==None

    #-----------------------
    # child node A
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            ca=x
    assert c

    # child node B
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
            cb=x
    assert c

    # child node C
    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in n.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
            cc=x
    assert c

    #-----------------------
    # Child Node A's children
    for c in ca.c:
        assert c.x==1
        assert c.p==ca
        assert c.v==None

    # grand child node A1
    s=np.array([[ 1, 1,-1],
                [-1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in ca.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
            assert len(x.c)==1
            #-----------------------
            # Great Grand Child Node A11
            assert x.c[0].x==-1
            assert x.c[0].p==x
            assert x.c[0].v==None
            assert x.c[0].c==[]
    assert c

    # grand child node A2
    s=np.array([[ 1, 1,-1],
                [ 0,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in ca.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
            assert x.c== []
    assert c
    
    #-----------------------
    # Child Node B's children
    for c in cb.c:
        assert c.x==1
        assert c.p==cb
        assert c.c==[]
        assert c.v==None

    # grand child node B1
    s=np.array([[-1, 1,-1],
                [ 1,-1, 1],
                [ 0, 1,-1]])
    c = False
    for x in cb.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
    assert c

    # grand child node B2
    s=np.array([[ 0, 1,-1],
                [ 1,-1, 1],
                [-1, 1,-1]])
    c = False
    for x in cb.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(2,0)
    assert c

    #-----------------------
    # Child Node C's children
    for c in cc.c:
        assert c.x==1
        assert c.p==cc
        assert c.v==None

    # grand child node C1
    s=np.array([[-1, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in cc.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(0,0)
            assert x.c== []
    assert c

    # grand child node C2
    s=np.array([[ 0, 1,-1],
                [-1,-1, 1],
                [ 1, 1,-1]])
    c = False
    for x in cc.c:
        if np.allclose(x.s,s):
            c=True
            assert x.m==(1,0)
            assert len(x.c)==1
            # Great Grand Child Node C21
            assert x.c[0].x==-1
            assert x.c[0].p==x
            assert x.c[0].v==None
            assert x.c[0].c==[]
    assert c


    #-----------------------
    s=np.array([[ 0, 0, 1],
                [ 0, 1, 1],
                [-1, 0,-1]])
    n = Node(s,x=-1) #it's O player's turn
    n.build_tree()

    assert len(n.c) ==4 
    assert n.x==-1
    assert n.v==None
    assert n.p==None
    assert n.m==None
    
    s1=np.array([[-1, 0, 1],
                 [ 0, 1, 1],
                 [-1, 0,-1]])
    s2=np.array([[ 0,-1, 1],
                 [ 0, 1, 1],
                 [-1, 0,-1]])
    s3=np.array([[ 0, 0, 1],
                 [-1, 1, 1],
                 [-1, 0,-1]])
    s4=np.array([[ 0, 0, 1],
                 [ 0, 1, 1],
                 [-1,-1,-1]])

    for c in n.c:
        assert c.x== 1
        assert c.v==None
        assert c.p==n
        if np.allclose(c.s,s1):
            assert c.m == (0,0)
            assert len(c.c) ==3
        if np.allclose(c.s,s2):
            assert c.m == (0,1)
            assert len(c.c) ==3
        if np.allclose(c.s,s3):
            assert c.m == (1,0)
            assert len(c.c) ==3
        if np.allclose(c.s,s4):
            assert c.m == (2,1)
            assert c.c == [] #terminal node, no child



#-------------------------------------------------------------------------
def test_compute_v():
    '''(5 points) compute_v()'''
    #-------------------------
    # the value of a terminal node is its game result
    s=np.array([[ 1, 0, 0],
                [ 0, 1,-1],
                [ 0,-1, 1]])
    n = Node(s, x=-1)
    n.compute_v() 
    assert  n.v== 1 # X player won the game

    # the value of a terminal node is its game result
    s=np.array([[ 1, 1,-1],
                [-1, 1, 1],
                [ 1,-1,-1]])
    n = Node(s, x=-1)
    n.compute_v() 
    assert  n.v== 0 # A tie 

    # the value of a terminal node is its game result
    s=np.array([[ 1, 0, 1],
                [ 0, 0, 1],
                [-1,-1,-1]])
    n = Node(s, x= 1)
    n.compute_v() 
    assert  n.v==-1 # O player won the game

    #-------------------------
    # if it is X player's turn, the value of the current node is the max value of all its children nodes.

    s=np.array([[ 0,-1, 1],
                [ 0, 1,-1],
                [ 0,-1, 1]])
    n = Node(s, x=1)
    n.build_tree()
    # the current node has 3 children nodes, two of which are terminal nodes (X player wins)
    n.compute_v() 
    # so the max value among the three children nodes max(1,?,1) = 1 (here ? is either 1 or 0 or -1)
    assert  n.v== 1 # X player won the game

    #-------------------------
    # if it is O player's turn, the value of the current node is the min value of all its children nodes.

    s=np.array([[ 0, 1,-1],
                [ 0,-1, 1],
                [ 1, 1,-1]])
    n = Node(s, x=-1)
    n.build_tree()
    # the current node has 2 children nodes, one of them is a terminal node (O player wins)
    n.compute_v() 
    # so the min value among the two children nodes min(-1,0) =-1 
    assert  n.v==-1 # O player won the game


    #-------------------------
    # a tie after one move
    s=np.array([[-1, 1,-1],
                [-1, 1, 1],
                [ 0,-1, 1]])
    n = Node(s, x= 1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 0  


    #-------------------------
    # optimal moves lead to: O player wins
    s=np.array([[-1, 1,-1],
                [ 1, 0, 0],
                [ 1, 0, 0]])
    n = Node(s, x=-1)
    n.build_tree()
    n.compute_v() 
    assert  n.v==-1

    #-------------------------
    # optimal moves lead to a tie
    s=np.array([[ 0, 1, 0],
                [ 0, 1, 0],
                [ 0, 0,-1]])
    n = Node(s, x=-1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 0

    #-------------------------
    # optimal moves lead to: X player wins
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0,-1, 0]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0,-1]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 0, 0]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [-1, 0, 0],
                [ 0, 0, 0]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [-1, 0, 0]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 1


    s=np.array([[ 1,-1, 1],
                [ 0, 0, 1],
                [ 0, 0,-1]])
    n = Node(s, x=-1)
    n.build_tree()
    n.compute_v() 
    assert  n.v==-1

    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 1

    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 1,-1]])
    n = Node(s, x=-1)
    n.build_tree()
    n.compute_v() 
    assert  n.v== 0


#-------------------------------------------------------------------------
def test_choose_optimal_move():
    '''(5 points) choose_optimal_move()'''
    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    n = Node(s, x=1)
    n.build_tree()
    n.compute_v() 
    r,c=choose_optimal_move(n,x=1)
    assert r == 2
    assert c == 0

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 1,-1],
                [ 0, 1,-1]])
    n = Node(s, x=-1)
    n.build_tree()
    n.compute_v() 
    r,c=choose_optimal_move(n,x=-1)
    assert r == 2
    assert c == 0

    #-------------------------
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    n = Node(s, x=-1)
    n.build_tree()
    n.compute_v() 
    r,c=choose_optimal_move(n,x=-1)
    assert r == 1
    assert c == 1


#-------------------------------------------------------------------------
def test_minmax_play():
    '''(10 points) minmax play()'''

    # two possible moves: one leads to win
    p = PlayerMiniMax()
    s=np.array([[ 0,-1, 1],
                [-1, 1, 1],
                [ 0, 1,-1]])
    r, c = p.play(s,x=1)
    assert r==2  
    assert c==0  


    # three possible moves, one leads to win
    p = PlayerMiniMax()
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])

    r, c = p.play(s,x=1) 
    assert r==2  
    assert c==0  

    #-------------------------
    p = PlayerMiniMax()
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0, 0]])
    r, c = p.play(s,x=-1) # O player's turn
    assert r == 1
    assert c == 1


    #-------------------------
    # play against random player in the game

    # starting the game with this state
    p1 = PlayerMiniMax()
    p2=PlayerRandom()

    # X Player: MinMax
    # O Player: Random 
    s=np.array([[ 1,-1, 1],
                [ 0, 0, 0],
                [ 0, 0,-1]])
    w=0
    for i in range(100):
        g = TicTacToe()
        g.s= s
        p1 = PlayerMiniMax()
        e = g.game(p1,p2)
        w += e
    assert w==100


    #-------------------------
    # play against MinMax player in the game

    # X Player: MinMax 
    # O Player: MinMax  
    s=np.array([[ 1,-1, 1],
                [ 0, 0,-1],
                [ 0, 1,-1]])
    w=0
    for i in range(100):
        g = TicTacToe()
        g.s=s
        p1 = PlayerMiniMax()
        e = g.game(p1,p1)
        w += e
    assert w==100

    g = TicTacToe()
    g.s=np.array([[ 0, 0, 1],
                  [ 0,-1, 0],
                  [ 1,-1, 0]])
    e = g.game(p1,p1)
    assert e==0

    g = TicTacToe()
    g.s=np.array([[ 0, 0, 0],
                  [ 0,-1, 0],
                  [ 1, 0, 0]])
    e = g.game(p1,p1)
    assert e==0

    g = TicTacToe()
    g.s=np.array([[ 0, 0, 0],
                  [ 0, 0, 0],
                  [ 1,-1, 0]])
    e = g.game(p1,p1)
    assert e==1

    g = TicTacToe()
    g.s=np.array([[ 0, 0, 0],
                  [ 0, 1, 0],
                  [ 0,-1, 0]])
    e = g.game(p1,p1)
    assert e==1

    g = TicTacToe()
    g.s=np.array([[ 0, 0, 0],
                  [ 0, 1, 0],
                  [-1, 0, 0]])
    e = g.game(p1,p1)
    assert e==0

    ##the following test run a complete game, but it may take one minute to run
    ## uncomment the following test to try a complete game
    #g = TicTacToe()
    #e = g.game(p1,p1)
    #assert e==0

