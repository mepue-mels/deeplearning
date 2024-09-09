"""
File: main.py

Description: Script for mainline logic

Dependencies: outline_gen

Usage: 
    Input: Course from standard input
    Returns: null
    Outputs: File
"""
from outline_gen import create_outline

course = input("Enter course: ")
output = create_outline(course)

with open(f"{course}.txt", "w") as file:
    for x in output:
        file.write(x + "\n")

print(f"Output written to {course}.txt")
