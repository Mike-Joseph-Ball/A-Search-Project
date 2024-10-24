import random
import heapq
import math
import sys
from collections import defaultdict, deque, Counter
from itertools import combinations


class Problem(object):
    """The abstract class for a formal problem. A new domain subclasses this,
    overriding `actions` and `results`, and perhaps other methods.
    The default heuristic is 0 and the default action cost is 1 for all states.
    When yiou create an instance of a subclass, specify `initial`, and `goal` states 
    (or give an `is_goal` method) and perhaps other keyword args for the subclass."""

    def __init__(self, initial=None, goal=None, **kwds): 
        self.__dict__.update(initial=initial, goal=goal, **kwds) 
        
    def actions(self, state):        raise NotImplementedError
    def result(self, state, action): raise NotImplementedError
    def is_goal(self, state):        return state == self.goal
    def action_cost(self, s, a, s1): return 1
    def h(self, node):               return 0
    
    def __str__(self):
        return '{}({!r}, {!r})'.format(
            type(self).__name__, self.initial, self.goal)
    

class Node:
    "A Node in a search tree."
    def __init__(self, total_courses, state_courses, g_value, h_value, parent=None):
        self.__dict__.update(total_courses = total_courses, state_courses=state_courses, g_value = g_value, h_value = h_value, parent=parent)

    def __repr__(self): return '<{}>'.format(self.state_courses)
    def __len__(self): return 0 if self.parent is None else (1 + len(self.parent))
    def __lt__(self, other):
        # Define comparison based on the 'f_value' attribute
        return (self.g_value+self.h_value) < (other.g_value+other.h_value)
    
    
#failure = Node('failure', path_cost=math.inf) # Indicates an algorithm couldn't find a solution.
#cutoff  = Node('cutoff',  path_cost=math.inf) # Indicates iterative deepening search was cut off.
    
    
def expand(problem, node):
    """Expand a node, generating the children nodes."""
    s = node.total_courses
    possible_semesters = problem.possible_semesters(problem.actions(s))
    listOfNodes = []
    for semester in possible_semesters:
        #combines courses taken so far (state of parent node) with courses in the possible semester
        s1 = problem.result(s, semester)
        g_value = node.g_value + problem.action_cost(semester)
        h_value = problem.depth_heuristic(semester) + problem.semester_size_heuristic(semester) + problem.balance_heuristic_short_term(semester) + problem.distance_from_graduation(s1) + problem.goal_heuristic(s1)
        #self.__dict__.update(total_courses = total_courses, state_courses=state_courses, g_value = g_value, h_value = h_value, parent=parent,path_cost=path_cost)
        listOfNodes.append(Node(s1, semester, g_value, h_value, node))
    return listOfNodes
        

def path_actions(node):
    "The sequence of actions to get to this node."
    if node.parent is None:
        return []  
    return path_actions(node.parent) + [node.action]

'''
def path_states(node):
    "The sequence of states to get to this node."
    if node in (cutoff, failure, None): 
        return []
    return path_states(node.parent) + [node.state]
'''