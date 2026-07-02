# Oxford Scholarship Eligibility Checker

This is a simple Python program designed to check if an applicant meets the basic age and WAEC grade requirements for an undergraduate scholarship. 

## How It Works
1. **User Input:** The program asks the user to enter their name, age, and their WAEC grades for both Mathematics and English.
2. **Eligibility Logic:** It uses simple conditional statements (`if` checks) to verify:
   * If the applicant's age is **25 or below**.
   * If their Mathematics grade is either **A1, B2, or B3**.
   * If their English grade is either **A1, B2, B3, or C4**.
3. **Output:** It prints a personalized success message if all conditions are met, or a polite rejection message if any requirement is missed.

## Concepts Demonstrated
* Using variables to store user data.
* Converting input text into integers (`int()`) for numerical comparison.
* Working with lists to verify valid passing grades using the `in` keyword.
