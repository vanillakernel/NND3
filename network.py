#!/bin/python

# http://natureofcode.com/book/chapter-10-neural-networks/
# http://www.google.com/patents/US20060230008?dq=Artificial%20neural%20network%20guessing%20method%20and%20game

'''
  This will be a simple neural network that takes input
  and determines which choice is the most likely.

  This will eventually tie in with a visualization that lets people
  track the state of each node and edge as input progresses.
'''
import pprint

# Start simple with 5 animals: Beetle, Bird, Cow, Wasp, and Cat
nodes = {'beetle':[0,0,0] , 'bird':[0,1,0] , 'cow':[1,1,0] , 'wasp':[0,0,1] , 'cat':[0,1,1] }
for node in nodes:
 print (node,nodes[node], nodes[node][0])
# Start with 3 simple questions: Bigger then a badger?, Animal?, Vicious Psycopath?


# Then the inputs look something like this:



