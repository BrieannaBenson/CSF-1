# Name: Kevin Bedard
# Evergreen Login: bedkev01
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

                    # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

# Plug in numbers into the variables to solve for x using a quadratic formula.
# This problem was not very difficult and took only a minute to code. The part
# that took the longest was recalling which numbers where represented in the
# formula as my math memory has decayed a bit. 

import math

a = 1
b = -5.86
c = 8.5408

d = 2*a

x = (-b - math.sqrt(math.pow(b,2) - 4*a*c))/d

print x

x = (-b + math.sqrt(math.pow(b,2) - 4*a*c))/d

print x



###
### Problem 2
###

print "Problem 2 solution follows:"

# This will pull the specified variables from hw1_test and list them.
# With it like this, if more variables are added to hw1_test then it 
# will not list them. This can be changed if user desires by adding
# more variables to the first line. 

from hw1_test import a , b , c , d , e , f

print a
print b
print c
print d
print e
print f


###
### Problem 3
###

print "Problem 3 solution follows:"

# I have the import set up again though I am sure I do not need it
# however, by having it I can easily set this as its own script apart
# from the previous portions. This will also permit an easier way for
# the script to update itself if the values of hw1_test are ever changed.

from hw1_test import a , b , c , d , e , f

print bool((a and b) or (not c) and not (d or e or f))

###
### Collaboration
###

# ... List your collaborators here, as a comment (on a line starting with "#").
