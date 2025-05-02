import sys
from enum import Enum

steps = 0

def increment_steps():
	global steps
	steps+=1

class Results(Enum):
		CONSISTENT = 1
		INCONSISTENT = 2

# A class for representing clauses. Pretty much every operation you do with clauses will increment the global step counter
# Try to use the provided methods for handling clauses whenever possible, instead of working directly with its attributes
# Feel free to also increment steps whenever you feel like you're doing a significant action
class clause:
	def __init__(self,negatives,positive):
		self.negatives = negatives
		self.positive = positive
		# We create a new set called remaining which will have all negative atoms that have not yet been solved
		# The practical reason to use a set and not a simple counter is that we will want to iterate over the negative literals of a clause while possibly removing, and Python doesn't like when you do that
		self.remaining = negatives.copy()

	def __str__(self):
		return "remaining {} negatives : {}, positive {}".format(self.remaining,self.negatives,self.positive)

	def __eq__(self,other):
		increment_steps()
		if self.positive == other.positive and self.negatives == other.negatives:
			return True
		return False

	def is_empty(self):
		increment_steps()
		if self.positive == "" and self.negatives == set():
			return True
		return False

	def is_fact(self):
		increment_steps()
		if self.positive != "" and self.negatives == set():
			return True
		return False

	def is_unsolved(self):
		increment_steps()
		if len(self.remaining) > 0:
			return True
		return False

	def resolve(self,condition):
		increment_steps()
		self.remaining.remove(condition)

	def get_negatives(self):
		increment_steps()
		return self.negatives

	def get_remaining(self):
		increment_steps()
		return self.remaining

	def get_positive(self):
		increment_steps()
		return self.positive


# Sample method for reading a file into a set of clauses. Do not change this method
# In the input file, atoms are separated by spaces, and a negative atom has a - before it
# Do not change this method
def read_file(file):
	KB = []
	facts = set()
	with open(file) as f:
		lines = f.readlines()
		for l in lines:
			negatives = set()
			positive = ""
			literals = l.split()
			for l in literals:
				if l.startswith("-"):
					negatives.add(l[1:])
				else:
					if positive != "":
						raise Error("Clause may have at most one positive literal") 
					else:
						positive = l
			c = clause(negatives,positive)
			KB.append(c)
			if c.is_fact():
				facts.add(c.positive)
	return KB,facts

# Method to return a map from each symbol present in the KB to every clause where it appears as a negative literal
# You must implement this method as part of your smart FC implementation
def make_on_clauses_map(KB):
	on_clauses = {}
	
	return on_clauses

# Naive method to check if the KB entails a contradiction (empty clause)
# The method should have at least four nested loops: 
#     a) the outermost loop simply checks if a new clause was added to the KB since the last iteration
#     	b) the second loop iterates over clauses
#				c) the third loop iterates over all negative literals of that clause (if a negative literal appears in multiple clauses, it should be processed multiple times)
#     			d) the innermost loop iterates over the list of facts and checks if it is the same symbol as the negative literal from the middle loop, and marks that negative literal as solved (using clause.resolve(literal))
#        at the end of each iteration of loop b, if a clause had all its negative literals matched, add the positive literal from that clause (if new) to the KB
# Return Results.INCONSISTENT if at any point you produce (or check) an empty clause, and Results.CONSISTENT if the outermost loop finishes
# Feel free to use the set facts on loop d, or when checking if a literal is repeated.
# You must implement this method
def naiveFC(KB,facts):
	return Results.CONSISTENT

# Similar to above, but with one extra data structure: the map on_clauses produced by make_on_clauses_map()
# You should also make use of the set facts
# The method should contain at least two nested loops:
#      a) the outermost loop pops a new fact f (note you may need to convert facts to a list. For efficiency, it is better if you do this only once, then update the set and the list in parallel)
#      		b) the inner loop goes over every clause in on_clauses[f] and resolves the corresponding negative literal
#           Add new facts to the KB as before, and return INCONSISTENT if at any point you produce the empty clause, and CONSISTENT otherwise
# You must implement this method
def smartFC(KB,facts):
	return Results.CONSISTENT

# The main method. You probably don't have to change this. If you do, make sure you print steps at the end
# Usage: python  FC_filename.py KB_filename.py mode
# Where mode == 1 to run the naive version and mode == 2 to run the "smart" version
if __name__ == "__main__":
   file = sys.argv[1]
   mode = sys.argv[2]
   KB, facts = read_file(file)
   print("Starting KB:")
   for c in KB:
      print("   " +str(c))
   print(facts)
   if mode == '1':
      result = naiveFC(KB,facts)
   elif mode == '2':
   	result = smartFC(KB,facts)
   if result is Results.INCONSISTENT:
      print("KB is inconsistent")
   else:
	   print("KB is consistent")
   print("Forward chaining resolution took {} steps".format(steps))
   


   
