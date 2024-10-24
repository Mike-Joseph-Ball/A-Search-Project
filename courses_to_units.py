from download_data import units_dict,type_dict

#int 1 = Core CS courses        - 66 units
#int 2 = CS elective courses    - 15 units
#int 3 = science/math elective  - 12 units
#int 4 = general education      - 24 units
#int 5 = graduation requirement - 3 units 
#                         total - 120 units

def courses_to_units(courses):
    unit_dict = {
        "CS Core Courses": 0,
        "CS Electives": 0,
        "Science/Math Elective": 0,
        "General Education": 0,
        "Graduation Requirement": 0
    }

    # for loop that loops through every item in the list courses
        # 5 different conditionals, testing which category the course is in
        # inside those conditionals, it finds the unit worth of the course, and adds to the tuple in the correct spot
    for course in courses:
        if type_dict[course] in ["Upper Division Core", "Lower Division Core", "Math Requirements"]:
            unit_dict["CS Core Courses"] += units_dict[course]
        elif type_dict[course] == "CS Electives":
            unit_dict["CS Electives"] += units_dict[course]
        elif type_dict[course] == "Science/Math Elective":
            unit_dict["Science/Math Elective"] += units_dict[course]
        elif type_dict[course] == "General Education":
            unit_dict["General Education"] += units_dict[course]
        elif type_dict[course] == "Graduation Requirement":
            unit_dict["Graduation Requirement"] += units_dict[course]
        else:
            print("Something went wrong in the courses_to_units function")
            print("The course that caused the error is:", course)

    return unit_dict

#dict1 should be the larger dictionary
def subtract_unit_dicts(dict1,dict2):
    unit_dict = {
        "CS Core Courses": 0,
        "CS Electives": 0,
        "Science/Math Elective": 0,
        "General Education": 0,
        "Graduation Requirement": 0
    }

    unit_dict["CS Core Courses"] = dict1["CS Core Courses"] - dict2["CS Core Courses"]
    unit_dict["CS Electives"] = dict1["CS Electives"] - dict2["CS Electives"]
    unit_dict["Science/Math Elective"] = dict1["Science/Math Elective"] - dict2["Science/Math Elective"]
    unit_dict["General Education"] = dict1["General Education"] - dict2["General Education"]
    unit_dict["Graduation Requirement"] = dict1["Graduation Requirement"] - dict2["Graduation Requirement"]

    return unit_dict