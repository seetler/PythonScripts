"""
Created on Fri Nov 20 12:03:40 2020

@author: JSNZE
"""
import numpy as np

garden1 = np.array([[5, 7, 8, 6, 3],
[0, 0, 7, 0, 4],
[4, 6, 3, 4, 9],
[3, 1, 0, 5, 8]])

gdx1=np.random.randint(10, size=(7,5))

"""
This function finds the middle area of an array, and then calls another function to find the high value amongst the selection.
"""

def function_center(gdx1):
    gdx1=np.array(gdx1)
    totalrows = len(gdx1)
    totalcolumns = len(gdx1[0])
    dumrow=[]
    dumcol=[]
    

    if (totalrows %2)==0:
        dumrow=np.append(dumrow, totalrows/2)
        dumrow=np.append(dumrow, totalrows/2-1)
    else:
        dumrow=np.append(dumrow, totalrows/2-.5)
    
    
    if (totalcolumns% 2)==0:
        dumcol=np.append(dumcol, totalcolumns/2)
        dumcol=np.append(dumcol, totalcolumns/2-1)
    else:
        dumcol=np.append(dumcol, totalcolumns/2-.5)
    
    return function_maxvalue(dumrow,dumcol,gdx1)

"""
This takes an array of coordinates and find the coordinate and the value of the highest value component.
"""

def function_maxvalue(dumrow, dumcol, gdx1):
    class centerval:
        row=0
        col=0
        highcentervalue=0
    for irow in range(len(dumrow)):
        for icol in range(len(dumcol)):
            print('Column: ' + str(dumcol[icol]) + '. Row: '+str(dumrow[irow])+ '. High Value: ' + str(gdx1[int(dumrow[irow]), int(dumcol[icol])])) 
            if gdx1[int(dumrow[irow]), int(dumcol[icol])]>centerval.highcentervalue:
                centerval.highcentervalue=gdx1[int(dumrow[irow]), int(dumcol[icol])]
                centerval.row = int(dumrow[irow])
                centerval.col = int(dumcol[icol])
    return centerval

    
"""
This takes a coordinate and finds its value, and if it is in bounds of the array.
"""

def function_movement(rowloc, colloc, arrayx, highval):
    counter=0
    if (rowloc >=0) and (rowloc< len(arrayx)) and (colloc >=0) and (colloc < len(arrayx[0])):
        if arrayx[rowloc, colloc]>highval:
            highval=arrayx[rowloc, colloc]
        elif arrayx[rowloc, colloc]==0:
            counter=1
    else:
        counter=1
    return rowloc, colloc, highval, counter

"""
Combine everything together.

>>>function_main(gdx1)
>>>([array of final plot], total carrots eaten, (coordinates))
"""

def function_main(gdx1):
    
    currlocr=function_center(gdx1).row
    currlocc=function_center(gdx1).col
    cumeat=0
    
    #If it's 4, it means all 4 directions are blocked.
    i=0
    while i<4:

        northr=currlocr-1
        southr=currlocr+1
        westc=currlocc-1
        eastc=currlocc+1
        tplocationr=currlocr
        tplocationc=currlocc
        currhighvalue=0
        
        i=0

        print('\nTop Cycle: Current Row: '+str(currlocr)+' Column: '+str(currlocc)+' Location Value: '+str(gdx1[currlocr,currlocc]))
        print(gdx1)
        
        #All these depends on the other functions to get the values for this part.
        valuesx=function_movement(northr, currlocc, gdx1, currhighvalue)
        if valuesx[2]>currhighvalue:
            tplocationr=valuesx[0]
            tplocationc=valuesx[1]
            currhighvalue=valuesx[2]
        i=valuesx[3]+i
        
        valuesx=function_movement(southr, currlocc, gdx1, currhighvalue)
        if valuesx[2]>currhighvalue:
            tplocationr=valuesx[0]
            tplocationc=valuesx[1]
            currhighvalue=valuesx[2]
        i=valuesx[3]+i
        
        valuesx=function_movement(currlocr, westc, gdx1, currhighvalue)
        if valuesx[2]>currhighvalue:
            tplocationr=valuesx[0]
            tplocationc=valuesx[1]
            currhighvalue=valuesx[2]
        i=valuesx[3]+i
        
        valuesx=function_movement(currlocr, eastc, gdx1, currhighvalue)
        if valuesx[2]>currhighvalue:
            tplocationr=valuesx[0]
            tplocationc=valuesx[1]
            currhighvalue=valuesx[2]
        i=valuesx[3]+i
        
        
        cumeat=cumeat+gdx1[currlocr,currlocc]              
        gdx1[currlocr,currlocc]=0
        currlocr=tplocationr
        currlocc=tplocationc
        
        print('Counters: '+ str(i))
        print('Heading Towards: Current Row: '+str(tplocationr)+' Column: '+str(tplocationc)+' Top Value: '+str(currhighvalue))
        print('Total Eaten: '+str(cumeat))

    return gdx1, cumeat, currlocr, currlocc



