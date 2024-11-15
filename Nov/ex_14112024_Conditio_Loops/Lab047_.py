#Write a program to take a user age and let him know if he can go the club.  21

# Logic Building Formula

# Step 1
# User input i/p -> data type -> int
# o/p -> String -> user if he can go or not.

# Step 2. Rough logic
# age > 21 -> print can go
# age < 21 -> print can't go

# Step 3. Write the logic

age = int(input("Enter the age"))

if age >= 21:
    print("Can go to the Club")
else:
    print("Cannot go to the Club")

# Step 4. Check for the edge cases.
# We should consider edge cases such as :
# Negative ages or extremely high values -> program will break
# Non- numeric input -> ABC
# Age which is valid. > 130

# Step 5. Optimize the code
# handle all the edges.