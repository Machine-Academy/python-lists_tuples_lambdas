# Let's get some practice using tuples.

# ==== Challenge 1: Creating Tuples ====
# HR needs some information on the new interns put into a database.
# Given an id, email, first name, and gender. Create an object for each person in the company list:

# 1, mmelloy0@psu.edu, Mitzi, F
# 2, kdiben1@tinypic.com, Kennan, M
# 3, kmummery2@wikimedia.org, Keven, M
# 4, gmartinson3@illinois.edu, Gannie, M
# 5, adaine5@samsung.com, Antonietta, F

# Example format of an intern object: 1, examples@you.edu, Example, F
example = (0, "Example", "examples@you.edu", "F")

# Write your tuples here:


# ==== Challenge 2: Reading Object Data ====
# Once your tuples are created, print out the following requests from HR into the console:

# Mitzi's name

# Kennan's ID

# Keven's email

# Gannie's name

# Antonietta's Gender

# ==== Challenge 3: Named Tuples ====
# Pickig out data from a tuple can be cumbersome, esp when we have lots of fields in our data.
# However we can make things easier using a **named tuple**. Named tuples allow us to
# assign names to the values in our tuples.
from collections import namedtuple

# example
color = namedtuple("Color", "r g b")

#                 r    g    b
my_color = color(255, 128, 78)
print(my_color.r)
print(my_color.g)
print(my_color.b)

# reusing the data that HR gave us, create named tuples

# 1, mmelloy0@psu.edu, Mitzi, F
# 2, kdiben1@tinypic.com, Kennan, M
# 3, kmummery2@wikimedia.org, Keven, M
# 4, gmartinson3@illinois.edu, Gannie, M
# 5, adaine5@samsung.com, Antonietta, F

# === Challenge 4 ===
# Once your **name tuples** are created, print out the following requests from HR into the console:

# Mitzi's name

# Kennan's ID

# Keven's email

# Gannie's name

# Antonietta's Gender


# === Great work! === Head over to the the lists.py!
