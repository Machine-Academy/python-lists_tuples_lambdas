# Let's get some practice using tuples.
from collections import namedtuple


def main():
    interns = [
        {"id": 1, "email": "mmelloy0@psu.edu", "name": "Mitzi", "gender": "F"},
        {"id": 2, "email": "kdiben1@tinypic.com", "name": "Kennan", "gender": "M"},
        {"id": 3, "email": "kmummery2@wikimedia.org", "name": "Keven", "gender": "M"},
        {"id": 4, "email": "gmartinson3@illinois.edu", "name": "Gannie", "gender": "M"},
        {"id": 5, "email": "adaine5@samsung.com", "name": "Antonietta", "gender": "F"},
    ]

    # === **Scoll down to challenege 1 ** ===
    intern_tuples = create_intern_tuples(interns)

    # ==== Challenge 2: Reading Tuple Data ====
    # Once your tuples are created, print out the following requests from HR :
    #   - Mitzi's name
    #   - Kennan's ID
    #   - Keven's email
    #   - Gannie's name
    #   - Antonietta's Gender

    # === **Scroll down to challenge 3** ===
    intern_named_tuples = create_named_tuples(interns)

    # === Challenge 4 ===
    # Once your **named tuples** are created, print out the following requests from HR into the console:

    # Mitzi's name
    # Kennan's ID
    # Keven's email
    # Gannie's name
    # Antonietta's Gender


# ==== Challenge 1: Creating Tuples ====
# HR needs some information on the new interns put into a database.
# Given an id, email, first name, and gender. Create an tuple for each person in the company list:

# Example format of an intern dict: {"id": 1, "email": "mmelloy0@psu.edu", "name": "Mitzi", "gender": "F"}
def create_intern_tuples(interns_list):
    interns = []

    return interns


# ==== Challenge 3: Named Tuples ====
# Pickig out data from a tuple can be cumbersome, esp when we have lots of fields in our data.
# However we can make things easier using a **named tuple**. Named tuples allow us to
# assign names to the values in our tuples.

# example
# color = namedtuple("Color", "r g b")
#                   r    g    b
# my_color = color(255, 128, 78)
# print(my_color.r)
# print(my_color.g)
# print(my_color.b)

# reusing the data that HR gave us, create named tuples
# Example format of an intern dict: {"id": 1, "email": "mmelloy0@psu.edu", "name": "Mitzi", "gender": "F"}
def create_named_tuples(interns_list):
    interns = []

    return interns


if __name__ == "__main__":
    # call your main function
    pass
