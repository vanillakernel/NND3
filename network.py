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
from random import randint


# Start simple with 5 animals: Beetle, Bird, Cow, Wasp, and Cat
# Start with 3 simple questions: Bigger then a badger?, Animal?, Vicious Psycopath?
# In the nodes dict each question is given a weight. LATER we can
#   make these more granular with backpropagation for multiple sessions by 
#   understanding if people say, think cows are murderers.
nodes = {'beetle':[0,0,0] , 'bird':[0,1,0] , 'cow':[1,1,0] , 'wasp':[0,0,1] , 'cat':[0,1,1] }
for node in nodes:
 print (node,nodes[node], nodes[node][0])

# For each question weigh how important the other questions are to make a decision. 
# Once again backpropagation could be used to make these more intellgent with multiple passes.
# Each question is the key, and the value is a dict of the other question's index and weight to ask that questions next.
questions = [{'Is it bigger than a badger?': {'1':0 ,'2':1} } , {'Is it an Animal?':{'0':1,'2':0}} , {'Is it a vicious psycopath?':{'0':0,'1':1} }]

# Then the inputs look something like this:

# select a question at random
question = questions [randint(0,len(questions)-1) ] 

for key,value in question.iteritems():
  text = key
  relationships = value
print " The question: %r" % text

# Get input

# Update weighting based on input.

# Pick the next most likely based on the weighting. Backpropagation will be a thing I promise.
for index in relationships:
  if (relationships[index] > .5):#abitrary trigger, make this a max.
    for key in questions[int(index)]:
      next_text = key
print "The next question is: %r " % key




