import numpy as np

#-------------------------------------------------------------------------
'''
    Problem 4: face recognition
    In this problem, you will use PCA to perform face recogition in a face image dataset.
    We assume you have already passed the unit tests in problem4.py. There will be a file named "face_pca.npy" in your folder.
    This file contains a numpy matrix of shape (400,20), which is the reduced dimensions for the 400 face images.
    We will need to use this file in this problem.

    Notations:
            ---------- input data ------------------------
            n: the number of face images, an integer scalar. (n = 400)
            p: the number of pixels in each image, an integer scalar. (p= 4096)
            c: the number of classes (persons), an integer scalar. (c = 40)
            k: the number of dimensions to reduce to, an integer scalar.
            Xp: the feature matrix with reduced dimensions, a numpy float matrix of shape n by k.
            ----------------------------------------------
'''

#--------------------------
def compute_distance(Xp, q):
    '''
        Compute the Euclidean distance between an query image and all the images in an image dataset.
        Intput:
            Xp: the projected feature matrix of all images, a float numpy matrix of shape (n , k).
            q:  a projected features of a query face image, a numpy vector of length k.
        Output:
            d: distances between the query image and all the images in Xp. A numpy vector of length n, where each element i, is the Euclidean distance between i-th image in X and the query image.

        For example, if Xp is a 3 X 2 matrix (n=3,k =2), 3 images, 2 dimensional features
            Xp = 0,0
                 0,1
                 1,1
        and suppose the query image has a projected feature vector
            q = 1,1
        Then
            the distance between the first image in Xp (0,0) and the query image q (1,1) is: d[0]= square_root_of( (0-1)^2 + (0-1)^2 ) = 1.414
            the distance between the second image in Xp (0,1) and the query image q (1,1) is: d[1]= square_root_of( (0-1)^2 + (1-1)^2 ) = 1
            the distance between the third image in Xp (1,1) and the query image q (1,1) is: d[1]= square_root_of( (1-1)^2 + (1-1)^2 ) = 0
        So in this case, the result should be d = [1.414,1,0]
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    d = []
    for i in range(len(Xp)):
        x = Xp[i]
        distance = np.linalg.norm(x-q)
        d.append(distance)
    d = np.array(d)
    #########################################
    return d

    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_compute_distance' in the terminal.  '''




#--------------------------
def face_recognition(Xp,q):
    '''
        Compute the most similar faces to the query face (id) from all the images in an image dataset.
        We will use one image from olivetti face dataset as the query and search for similar faces to the query.
        Input:
            Xp: the projected feature matrix, a float numpy matrix of shape (n, k).
            q:  a projected features of a query face image, a numpy vector of length k.
        Output:
            ids: the ranked ids of similar face images to the query image.
        For example, suppose we have 3 face images in a dataset (n=3) and after PCA, we reduce the dimensionality to 2 (k=2).
            Xp =  0,0 (id=0)
                  1,1 (id=1)
                  0,1 (id=2)
            and the query image has a feature vector q = 1,1
            The distance between the query and all the three images are: 1.414, 0 , 1
            So the most similar image to the query image is the second image (ID=1),where the distance is the smallest: 0;
                 and the second most similar image is the last image (ID=2), where the distance is the second smallest: 1;
            The least similar image to the query is the first image (ID=0), where the distance is the largest: 1.414;
            So in this case, the sorted id list should be [1,2,0].
    '''
    #########################################
    ## INSERT YOUR CODE HERE
    d = compute_distance(Xp, q)
    ids = np.argsort(d)
    #########################################
    return ids


    ''' TEST: Now you can test the correctness of your code above by typing `nosetests -v test4.py:test_face_recognition' in the terminal.
              The query image will be saved in your current folder with name 'query.jpg',
              Then the top 10 most similar images in the dataset will be saved in your current folder with names 'result_i.jpg'
              Because the query image that we chose is one of the images in the dataset, so if your method works correctly, the most similar image ('result_1.jpg') should be exactly the same image as the query image ('query.jpg'). You could check by opening both images and see if they are the same.
    '''



#--------------------------------------------

''' TEST Problem 4:
        Now you can test the correctness of all the above functions by typing `nosetests -v test4.py' in the terminal.

        If your code passed all the tests, you will see the following message in the terminal:
            ----------- Problem 4 (20 points in total)--------------------- ... ok
            (10 points) compute_distance ... ok
            (10 points) face_recognition ... ok
            ----------------------------------------------------------------------
            Ran 3 tests in 0.075s
            OK
'''

#--------------------------------------------
