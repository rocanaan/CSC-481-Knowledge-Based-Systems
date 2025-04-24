import sys
from enum import Enum


# Declaration of a global step counter and a function to increment it.
# increment_steps() is called whenever two clauses need to be resolved
# You can use this counter to estimate how many steps of resolution your algorithm is doing
steps = 0
def increment_steps():
	global steps
	steps+=1

# An Enum with the possible results of the  algorithm: consistent or inconsistent
class Results(Enum):
		CONSISTENT = 1
		INCONSISTENT = 2

# A class for representing clauses. 
# Do not change this
# Use  is_empty() and is_tautology() to check if a clause is empty (a contradition) or a tautology
# Use get_positives() and get_negatives() to get a set with the positive/negative atoms
class Clause:
	def __init__(self,negatives,positives):
		self.negatives = negatives
		self.positives = positives

	def __str__(self):
		return str(list(self.positives) + ["-"+x for x in self.negatives])

	def __eq__(self,other):
		if self.positives == other.positives and self.negatives == other.negatives:
			return True
		return False

	def is_empty(self):
		if self.positives == set() and self.negatives == set():
			return True
		return False

	def is_tautology(self):
		if(self.positives.intersection(self.negatives)):
			return True
		return False

	def get_negatives(self):
		return self.negatives

	def get_positives(self):
		return self.positives


# Method for reading a file into a set of clauses. Do not change this method
# In the input file, atoms are separated by spaces, and a negative atom has a - before it
def read_file(file):
	KB = []
	with open(file) as f:
		lines = f.readlines()
		for l in lines:
			negatives = set()
			positives = set()
			literals = l.split()
			for l in literals:
				if l.startswith("-"):
					negatives.add(l[1:])
				else:
					positives.add(l)
			c = Clause(negatives,positives)
			KB.append(c)
	return KB

# Returns None if c1 and c2 has no resolvents, and the result of resolution otherwise
def resolve_clauses(c1,c2):
	increment_steps()

	###### YOUR CODE HERE  ######
	# Check whether c1.positives shares an atom with c2.negatives of vice-versa. 
	# That atom is the resolvent of the two clauses
	# If there are no resolvents, return None (caution: do NOT return the empty clause)
	# Otherwise, return a new clause with all positives and negatives of c1 and c2,
	#            except for the resolvent
	# Note 1: set operations may be helpful as they automatically get rid of duplicates
	# Note 2: there may be multiple resolvents, but you can ignore all but the first
	#          This is because if c1 and  c2 have multiple resolvents
	#          the resulting clause is a tautology


# Iterate over all pairs of clauses trying to resolve them, adding new clauses (that are not tautologies) to the KB
# Returns Results.INCONSISTENT if an empty clause is produced
# Returns Results.CONSISTENT if no new clauses can be added to the KB 
def check_consistency_resolution(KB):
	terminate = False
	KB2 = KB.copy()
	while not terminate:
		terminate = True
		
			######## YOUR CODE HERE #####
			# Iterate over all pairs of clauses trying to resolve them
			# If two clauses resolve to an empty clause (use Clause.is_empty()),
			#      return Results.INCONSISTENT)
			# Otherwise, if the clauses resolve to something that is not a tautology 
			#      and is new to the KB, add it to KB2 and set terminate back to false

		# After iterating through all pairs of clauses, make KB2 the new KB
		# This is done to avoid modifying a set we're iterating
		KB =  KB2

	# If we ever leave the while loop, it's because we ran out of clauses to resolve
	# In this case, the KB is consistent
	return Results.CONSISTENT


# Main function.  Do not change this.
if __name__ == "__main__":
	file = sys.argv[1]
	KB = read_file(file)
	print("Starting KB:")
	for c in KB:
		print("   " +str(c))

	result = check_consistency_resolution(KB)

	print("Final KB")
	for c in KB:
		print("   " +str(c))

	if result is Results.INCONSISTENT:
		print("KB is inconsistent")
	else:
		print("KB is consistent")
	print("Resolution required {} steps".format(steps))
   


   
