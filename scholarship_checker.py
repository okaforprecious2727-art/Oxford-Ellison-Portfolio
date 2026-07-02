# ==========================================
# PROJECT 1: OXFORD SCHOLARSHIP ELIGIBILITY CHECKER
# Author: Precious Okafor Chinelo
# Description: A program to check if a student meets basic WAEC and age requirements.
# ==========================================

# Step 1: Get data from the user
print("--- Welcome to the Scholarship Eligibility Checker ---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
math_grade = input("Enter your WAEC Mathematics grade (e.g., A1, B2): ")
english_grade = input("Enter your WAEC English grade (e.g., B3, C4): ")

# Step 2: List out the accepted passing grades
accepted_math = ["A1", "B2", "B3"]
accepted_english = ["A1", "B2", "B3", "C4"]

# Step 3: Run the checks using an IF statement
if age <= 25 and math_grade in accepted_math and english_grade in accepted_english:
    print("\n==============================")
    print("Congratulations, " + name + "!")
    print("You meet the basic eligibility requirements.")
    print("==============================")
else:
    print("\n==============================")
    print("Sorry, you do not meet the basic requirements.")
    print("==============================")

