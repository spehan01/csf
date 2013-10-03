# Name: Hannah Spencer
# Evergreen Login: spehan01, helped by linzac03
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"
# x^2-5.86 x+8.5408
a = 1
b = -5.86
c = 8.5408

x1=(-b+math.sqrt(b**2-4*a*c))/2*a
x2=(-b-math.sqrt(b**2-4*a*c))/2*a

print x1
print x2
 # Answers found using the hint

###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f
# Answers found using import and print commands


###
### Problem 3
###

print "Problem 3 solution follows:"

BE = ((hw1_test.a and hw1_test.b) or (not hw1_test.c) and not (hw1_test.d or hw1_test.e or hw1_test.f))
print BE
# BE stands for boolean expression


###
### Collaboration 
###

# ... List your collaborators here, as a comment (on a line starting with "#").
# linzac03 
# Reflection: This assignment took about 45 mins. The readings, tutorials and lectures helped. 
# Once my few questions were answered, I was able to set off.