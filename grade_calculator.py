# ==========================================
# PROJECT 2: WAEC GRADE POINTS CALCULATOR
# Author: Precious Okafor Chinelo
# Description: A program that converts WAEC letter grades into numeric points 
#              and calculates a total score for 3 core subjects.
# ==========================================

print("--- Welcome to the WAEC Grade Points Calculator ---")

# Step 1: Get the student's grades for 3 core subjects
math_grade = input("Enter your Mathematics grade (e.g., A1, B2, C4): ")
english_grade = input("Enter your English grade: ")
physics_grade = input("Enter your Physics grade: ")

# We start our total score at 0 points
total_points = 0

# Step 2: Check Mathematics Grade and add points
if math_grade == "A1":
    total_points = total_points + 5
elif math_grade == "B2":
    total_points = total_points + 4
elif math_grade == "B3":
    total_points = total_points + 3
elif math_grade == "C4" or math_grade == "C5" or math_grade == "C6":
    total_points = total_points + 2
else:
    total_points = total_points + 0

# Step 3: Check English Grade and add points
if english_grade == "A1":
    total_points = total_points + 5
elif english_grade == "B2":
    total_points = total_points + 4
elif english_grade == "B3":
    total_points = total_points + 3
elif english_grade == "C4" or english_grade == "C5" or english_grade == "C6":
    total_points = total_points + 2
else:
    total_points = total_points + 0

# Step 4: Check Physics Grade and add points
if physics_grade == "A1":
    total_points = total_points + 5
elif physics_grade == "B2":
    total_points = total_points + 4
elif physics_grade == "B3":
    total_points = total_points + 3
elif physics_grade == "C4" or physics_grade == "C5" or physics_grade == "C6":
    total_points = total_points + 2
else:
    total_points = total_points + 0

# Step 5: Print the final output layout
print("\n==============================")
print("       RESULTS SUMMARY        ")
print("==============================")
print("Total Screening Points: " + str(total_points) + " / 15")
print("==============================")
