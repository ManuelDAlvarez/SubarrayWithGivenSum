# problem summary: Given an unsorted array of non-negative integers, find a continuous sub-array which adds to a given number
# details at: https://practice.geeksforgeeks.org/problems/subarray-with-given-sum/0

#for error handling
import sys

#this solution uses list as are native to Python and easy to use. However, array.array are better when it comes to memory consumption. There is also the popular NumPy.ndarray that is used on mathematical operations

array1 = [[5,12],[1,2,3,7,5]]
array2 = [[10,15],[1,2,3,4,5,6,7,8,9,10]]
array3 = [[7,69],[5,5,5,7,7,7,3]]
probInput = [3,array1,array2,array3]

#get the number of cases to evaluate
intCases = probInput[0]
#starting point 1 as 0 is the number of cases
jIteration=1

#control errors if the list is smaller than the proposed number of errors
if len(probInput)> intCases+1:
    print "error"
    sys.exit()

#iterate cases
while jIteration<= intCases:
    #print probInput[i]
    givenNumber = probInput[jIteration][0][1]
    # givenNumber is what the values must add to
    #iteration of an iteration, using string lenght to simplify
    for i in range(len(probInput[jIteration][1])):
        # as you can see, using the same probInput list is confusing and hard to follow. An alternative is to create a new list that is the sublist(s) you want to evaluate. I want to keep the memory low so I decided not to add new lists. I did not run a benchmark between the two approches to confirm this indeed is better for the memory than creating new arrays
        contSum =0
        iIteration = i
        stopFlag = 0
        while iIteration<len(probInput[jIteration][1]):
            # if you are getting list, add a print to see where you are. For examlee, uncomment the below
            # print "WHAT?! " + str( probInput[jIteration][1][iIteration]) + " " + str(iIteration)
            contSum = contSum + probInput[jIteration][1][iIteration]
            if contSum == givenNumber:
                # this means you found your answer
                print str(i+1) + " " + str(iIteration+1)
                stopFlag = 1
                break
            if contSum> givenNumber:
                #this means, do not bother anymore as the number is higher than the answer
                break
            iIteration=iIteration+1
        if stopFlag==1:
            #this means you have an answer and do not want to keep looking on the same list/array
            break
    if stopFlag==0:
        #print "Array " + str(probInput[jIteration][1]) + " does not add up to " + str(contSum)
        print "-1"
    jIteration=jIteration+1
    #break 


