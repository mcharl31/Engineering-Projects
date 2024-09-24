# Class: CSE 1321L
# Section: BJF
# Term: Fall 2024
# Instructor: Nisha Bagdwal
# Name: Micah Charles
# Lab:5B

size = int(input("Please enter a value for the size: "))

print(f"This is the requested {size}x{size} box: ")
for j in range(size):
    for i in range(size):
        print("*", end="")
    print()

print(f"This is the requested right-facing {size}x{size} right-triangle: ")
for j in range(size):
    for i in range(j+1):
        print("*", end="")
    print()

print(f"This is the requested left-facing {size}x{size} right-triangle: ")
for j in range(size):
    for i in range(size-1-j):
        print(" ",end="")
    for i in range(1+j):
        print("*", end="")
    print()