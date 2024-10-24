from superclass import *
from itertools import combinations
from courses_to_units import courses_to_units, subtract_unit_dicts
from download_data import type_dict

final_state_units_dict = {
    "CS Core Courses": 66,
    "CS Electives": 15,
    "Science/Math Elective": 12,
    "General Education": 24,
    "Graduation Requirement": 3
}

class GraduationPathProblem(Problem): # Inherit from the Problem class
    def __init__(self, initial, goal, prerequisites, course_units, course_type,course_depth):
        super().__init__(initial=initial, goal=goal)  # Call the parent class constructor
        self.course_units = course_units
        self.prerequisites = prerequisites
        self.course_type = course_type
        self.course_depth = course_depth

    #we need to keep track of the classes we have taken so far
    #we need to keep track of the classes we can take

    def actions(self, state):
        # Generate possible actions (courses to take) as long as they are not already taken and prerequisites are satisfied.
        actions = []

        #This was pretty much all chatGPT
        for course in self.course_units:
            if course not in state:
                prerequisites = self.prerequisites.get(course)
                if prerequisites is None or (prerequisites == ['None'] and course not in state) or all(prereq in state for prereq in prerequisites):
                    actions.append(course)

        return actions
    
    def possible_semesters(self, actions):
        # Generate all possible semesters given possible courses to take.
        # The semester cannot have more than 17 units and must have at least 12 units.
        # The semesters will be represented as a list of lists of courses.
        # The function returns a list of lists of courses.
        valid_semesters = []

        #This was pretty much all chatGPT
        for r in range(1, min(8, len(actions) + 1)):
            for course_combination in combinations(actions, r):
                if sum(self.course_units[course] for course in course_combination) <= 17:
                    valid_semesters.append(list(course_combination))

        return valid_semesters



    def result(self, state, action):
        # Return the resulting state from taking an action (taking a course).
        return state + action

    def is_goal(self, total_courses):
        # The goal is reached when the total courses taken so far equals the total courses needed to graduate.
        return len(total_courses) == len(self.goal)

    def action_cost(self, a):
        # The cost of an action is the number of units of the course.
        cost = 10
        return cost

    def depth_heuristic(self, semester):
        cost = 0
        for course in semester:
            cost += self.course_depth[course]
        return -cost
    
    def semester_size_heuristic(self,semester):
        cost = 0
        for course in semester:
            cost += self.course_units[course]
        cost = 17 - cost
        return cost
    
    def goal_heuristic(self, courses_so_far):
        cost = 0
        if(len(courses_so_far) == len(self.goal)):
            return -100
        else:
            return 0
    
    def balance_heuristic_short_term(self, semester):
        #This will only check for balance within the semester
        cost = 0
        #print("semester:",semester)
        unit_dict = courses_to_units(semester)
        if(unit_dict["CS Core Courses"] < 12):
            cost -= 3
        else:
            cost += 3
        if(unit_dict["General Education"] < 3):
            cost += 3
        return cost
    
    def distance_from_graduation(self, total_courses):
        cost = 0
        classes_left = subtract_unit_dicts(final_state_units_dict, courses_to_units(total_courses))
        #print("classes left:",classes_left)
        cost += classes_left["CS Core Courses"]
        cost += classes_left["CS Electives"]
        cost += classes_left["Science/Math Elective"]
        cost += classes_left["General Education"]
        cost += classes_left["Graduation Requirement"]
        return cost

