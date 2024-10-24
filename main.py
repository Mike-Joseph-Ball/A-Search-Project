from Graduation_Subclass import *
from superclass import *
from download_data import prereq_dict,units_dict,type_dict, course_names_list, depth_dict
from courses_to_units import courses_to_units
import heapq

# Define the initial state (courses already taken)
#We will use 3 different initial states to test our algorithm

#INITIAL STATES
initial_state_courses_new_student = [] # we only need courses in the state, because we can always find the units for each course and the prerequisites for each course from the courses dictionary and the prerequisites dictionary
transfer_student_course_load = ['CPSC 120A+L', 'MATH 170A', 'CS Elective 1', 'GE 1', 'CPSC 121A+L', 'CPSC 253', 'MATH 150B', 'GE 2', 'CS Elective 2','GE 3','GE 4','CPSC 131']
mike_ball_course_load = ['CPSC 120A+L', 'MATH 150A', 'MATH 170A', 'CS Elective 1', 'GE 1','CPSC 121A+L', 'CPSC 253', 'MATH 150B', 'CS Elective 2', 'GE 2','CPSC 131', 'MATH 170B', 'MATH 338', 'CS Elective 3', 'GE 3','CPSC 335', 'CPSC 351', 'CPSC 362', 'CS Elective 4', 'GE 4','CPSC 240','GE 5','GE 6', 'GE 7','GE 8']
#int 1 = Core CS courses        - 66 units
#int 2 = CS elective courses    - 15 units
#int 3 = science/math elective  - 12 units
#int 4 = general education      - 24 units
#int 5 = graduation requirement - 3 units 
#                         total - 120 units

#USER INPUT


final_state_courses = course_names_list
userInput = "0"
while(userInput != "1" and userInput != "2" and userInput != "3"):
    print("Choose from 1 of 3 possible simulations:")
    print("1. New Student")
    print("2. Transfer Student")
    print("3. Mike Ball")
    userInput = input("Please enter a number: ")

    if userInput == "1":
        problem = GraduationPathProblem(initial_state_courses_new_student, final_state_courses, prereq_dict, units_dict, type_dict,depth_dict)
        currentNode = Node(initial_state_courses_new_student, initial_state_courses_new_student, 0, 0, None)
    elif userInput == "2":
        problem = GraduationPathProblem(transfer_student_course_load, final_state_courses, prereq_dict, units_dict, type_dict,depth_dict)
        currentNode = Node(transfer_student_course_load, initial_state_courses_new_student, 0, 0, None)
    elif userInput == "3":
        problem = GraduationPathProblem(initial_state_courses_new_student, final_state_courses, prereq_dict, units_dict, type_dict,depth_dict)
        currentNode = Node(mike_ball_course_load, initial_state_courses_new_student, 0, 0, None)
    else:
        print("DO IT AGAIN BUT CORRECTLY!!!")
        

initial_state_unit_dict = {
        "CS Core Course": 0,
        "CS Electives": 0,
        "Science/Math Elective": 0,
        "General Education": 0,
        "Graduation Requirement": 0
    }

#GOAL STATES
final_state_units_dict = {
    "CS Core Course": 66,
    "CS Electives": 15,
    "Science/Math Elective": 12,
    "General Education": 24,
    "Graduation Requirement": 3
}




#problem = GraduationPathProblem(initial_state_courses_new_student, final_state_courses, prereq_dict, units_dict, type_dict,depth_dict)

############################################################################################


############################################################################################

# 0. define the initial state - node.state
# self.__dict__.update(total_courses = total_courses, state_courses=state_courses, g_value = g_value, h_value = h_value, parent=parent,path_cost=path_cost)

semester_number = 0

def priorityQueue(expanded_nodes):
    priority_queue = []
    for node in expanded_nodes:
        heapq.heappush(priority_queue, (node.g_value + node.h_value, node))
    return priority_queue
    
problem.distance_from_graduation(currentNode.total_courses)
#print("final state:",final_state_courses)
while(problem.is_goal(currentNode.total_courses) == False):
    #print("semester number:",semester_number)
    if(semester_number > 0):
        print(str(semester_number)+"th semester:", currentNode.state_courses)
    semester_number += 1
    #print("total courses:",currentNode.total_courses)
    #print(len(currentNode.total_courses))
    #print(final_state_courses)
    #print(len(final_state_courses))

    difference2 = list(set(final_state_courses) - set(currentNode.total_courses))
    #print("difference:",difference2)

    #print(problem.prerequisites)
    actions = problem.actions(currentNode.total_courses)
    #print("actions:",actions)
    expanded_nodes = expand(problem, currentNode)


    if semester_number == 1:
        TOTAL_PRIORITY_QUEUE = priorityQueue(expanded_nodes)
    else:
        combined_pq = list(heapq.merge(TOTAL_PRIORITY_QUEUE,priorityQueue(expanded_nodes)))
        TOTAL_PRIORITY_QUEUE = combined_pq
    if(len(actions) < 5):
        lastNode = Node(currentNode.total_courses + actions, actions, currentNode.g_value, currentNode.h_value, currentNode)
        currentNode = lastNode
        continue

    next_semester = heapq.heappop(TOTAL_PRIORITY_QUEUE)

    #print("next semester:",next_semester)
    #print("f-value:",next_semester[1].g_value + next_semester[1].h_value)
    currentNode = next_semester[1]
    #currentNode.total_courses = next_semester[1] + currentNode.total_courses  
    #print("LOOK HERE",next_semester)
print(str(semester_number)+"th Semester:",currentNode.state_courses)
print("SUCCESS")