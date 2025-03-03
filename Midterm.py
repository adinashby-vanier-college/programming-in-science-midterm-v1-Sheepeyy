import math

# Q1: Calculate the area of a circle
def area_of_circle(radius):
    result = math.pi * radius ** 2
    rounded_result = round(result, 2)
    return rounded_result

# Q2: Hollow Right Triangle
def hollow_right_triangle(n):
    if n < 3:
        print("The triangle height should be at least 4.")

    Result = ""
    Height = n
    Height <= n

    while Height == 0 or Height == 1 or Height == (n - 1):
        print("*" * n +"\n")
        
    while Height <= n:
        print("*" + " " * (n - 2) + "*")
        Height += 1
    
    return ""

# Q3: Inverted Pyramid
def inverted_pyramid(n):
    if n < 2:
        print("The pyramid height should be at least 3.")

    row = ""
    row = n
    while row == 0:
        print("*" * (n + (n - 1)))
    while row <= n:
        print(" " * (n + (n - 3)))
        row += 1
    row != n
    return ""

# ----------------------------------------------------------------
print(area_of_circle(5))
print()

print(hollow_right_triangle(3))
print()

print(hollow_right_triangle(4))
print()

print(hollow_right_triangle(5))
print()

print(inverted_pyramid(3))
print()

print(inverted_pyramid(4))
print()

print(inverted_pyramid(5))
print()