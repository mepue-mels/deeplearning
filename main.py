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
create_outline(course)
