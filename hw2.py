# Name: Hannah Spencer
# Evergreen Login: spehan01
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.


###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test
x = 0
y = 0
while (y <= hw2_test.n):
    x = x + y
    y = y + 1
print x 

###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

# 

for x in range (2, 11): 
    print 1.0 / x
else: print "done"
###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range (0, n+1):
    triangular = triangular + i
print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", ( n * (n + 1) / 2)
###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"


n = 10
a = 1
for t in range (1, n+1):
    a = (t * a)
print a
 #can check answer by 1*2*3*4*5*6*7*8*9*10
 
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

numlines = 10
fac = 1

for n in range (numlines,numlines-1, -1):
    for i in range(1, numlines+1):
        fac = (i * fac)
        print fac
    
 #having trouble turning it around
    

 
 ###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"

p = 0
y = 10

for n in range (1, y-1):
    x = 1.0 / n
    p = p + x
print p

# having trouble with 6, since had trouble with 5

### Collaboration
###

# ... linzac03, Think Python

###
### Reflection
### It took me about an hour and a half to two hours to work on the homework.
# I feel like things could be explained slower in lab sometimes.
# It would be helpful for newer people.
