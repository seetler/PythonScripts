from numpy import random
import numpy
import pandas

#Define dice
dnorm=[1,2,3,4,5,6]
dload=[2,3,4,5]

"""
Section 1
"""


"""
This is the main function that incorporates the function_probmat and function_tolist. It returns a table with each possible combination and the percentage that it could occur. the inputs are the dice being used.
"""
def function_probnum(setdie1=dnorm,setdie2=dnorm):
    problist=function_tolist(function_probmat(setdie1, setdie2))
    distlist=list(set(problist))
    perctable=numpy.zeros((len(distlist),2))
    for distlistx in range(0,len(distlist)):
        perctable[distlistx, 0]=distlist[distlistx]
        perctable[distlistx, 1]=problist.count(distlist[distlistx])/len(problist)        
    return perctable

"""
This creates a matrix from the dice and then gets the sum of the items for the matrix.
"""

def function_probmat(dice1=dnorm, dice2=dnorm):
    probs=numpy.zeros((len(dice1),len(dice2)))
    droll1=dice1[0]
    for droll2 in range(0, len(dice2)):
        drnum2=dice2[droll2]
        for droll1 in range (0, len(dice1)):
            drnum1=dice1[droll1]
      #      print(drnum2)
      #      print(drnum1)
            probs[droll1,droll2]=drnum1+drnum2
     #       print(probs)
    return probs

"""
This is to turn the matrix from function_probmat into a list used for the main function_probnum
"""

def function_tolist(probmats):
    problist=[]
    for dim1 in range(0, len(probmats)):
     #   print(dim1)
        for dim2 in range (0, len(probmats[0])):
      #      print(dim2)
            problist.append(probmats[dim1,dim2])
      #      print(problist)
    return problist



"""
This is the primary function, that sets the variables based on how many rolls. It is primarily used to call the subsequent subsequent functions. 

The columns are [roll number, did it go to craps, monetary value: -1, or 1, win==true]
"""

def function_rollmain(rollamount, dice1=dload, dice2=dload):
    results=numpy.zeros((rollamount,4))
#    print(results)
    function_roll(rollamount, results, dice1, dice2)    
#    print(results)  
    return results


"""
This is the function for the initial roll.
"""
def function_roll(rolls, results, dice1=dload, dice2=dload):

#    print('Number of rolls ' + str(rolls))
    for x in range (0, rolls):
        # print(results)
        # print('New Game')
        # print('Game number ' + str(x))
        results[x,0]=x
        combo=random.choice(dice1)+random.choice(dice2)
     #   print('Rolls ' + str(combo))
        if combo in [7,11]:
         #   print('win')
            results[x,2]=1
            results[x,3]=1
        elif combo in [2,3,12]:
          #  print('lose')
            results[x,2]=-1
            results[x,3]=0
        else:
         #   print('Craps ' + str(combo))
            function_craps(combo, x, results, dice1, dice2)

"""
This is the function for the craps roll.
"""

def function_craps(combo, x, results, dice1, dice2):

    results[x,1]=1
    placenum=combo
    combox=0
    while combox not in [placenum, 7]:
        combox=random.choice(dice1)+random.choice(dice2)
    #    print('Craps roll ' + str(combox))
        if combox==placenum:
          #  print('win')
            results[x,2]=1
            results[x,3]=1
        elif combox in [7]:
          #  print('lose')
            results[x,2]=-1
            results[x,3]=0

"""
This is to analyze the dataset generated for the question in the problem statement.

"""
crapodds=0.208333333

def function_anasum(resdata, pwin=crapodds):
    anadata = resdata.sum(axis=0)
    anadata=anadata.tolist()
    anadata[0]=len(resdata)
    anadata.append(anadata[2]/anadata[0])
    anadata.append(anadata[3]/anadata[0]-pwin)

    return anadata
    
           
