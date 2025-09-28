def get_side_lengths():
    """Prompts the user to enter three side lengths of a triangle.

    Returns:
      Three float values reprsenting the side lengths of the triangle
    """
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    return side_1, side_2, side_3

def classify_triangle(side_1:float, side_2:float, side_3:float)->str:
    """Classifies a triangle into 1 of 4 categories: "does not exist", "acute", "obtuse", or "right"

        NOTE: Your implementation whousl not use the built-in sort or sorted functions
      
        HINT:
        - Right Triangles: the sum of the squares of the two smaller sides equals the square of the largest side
        - Obtuse Triangles: the sum of the squares of the two smaller sides is less than the square of the largest side
        - Acute Triangles: the sum of the squares of the two smaller sides is greater than the square of the largest side
        - Does Not Exist: the sum of the smaller two sides doesn't exceed the length of the largest side

        Args:
          side_1: The measurement of one side of the triangle
          side_2: The measurement of one side of the triangle
          side_3: The measurement of one side of the triangle

        Returns:
          A single string label- "does not exist", "acute", "obtuse", or "right"

        Examples
        --------
        >>> classify_triangle(2, 2, 4)
        "does not exist"

        >>> classify_triangle(3, 5, 4)
        "right"
    """
    #your code goes here
    if side_1 <=0 or side_2 <= 0 or side_3 <=0:
        return "does not exist"
    elif side_1 >= side_2 and side_1 >= side_3 and side_2 + side_3 <= side_1:
        return "does not exist"
    elif side_2 >= side_1 and side_2 >= side_3 and side_1 + side_3 <= side_2:
        return "does not exist"
    elif side_3 >= side_1 and side_3 >= side_2 and side_1 + side_2 <= side_3:
        return "does not exist"
    elif side_1 >= side_2 and side_1 >= side_3 and side_2**2 + side_3**2 > side_1**2:
        return "acute"
    elif side_2 >= side_1 and side_2 >= side_3 and side_1**2 + side_3**2 > side_2**2:
        return "acute"
    elif side_3 >= side_1 and side_3 >= side_2 and side_1**2 + side_2**2 > side_3**2:
        return "acute"
    elif side_1 >= side_2 and side_1 >= side_3 and side_2**2 + side_3**2 < side_1**2:
        return "obtuse"
    elif side_2 >= side_1 and side_2 >= side_3 and side_1**2 + side_3**2 < side_2**2:
        return "obtuse"
    elif side_3 >= side_1 and side_3 >= side_2 and side_1**2 + side_2**2 < side_3**2:
        return "obtuse"
    elif side_1 >= side_2 and side_1 >= side_3 and side_2**2 + side_3**2 == side_1**2:
        return "right"
    elif side_2 >= side_1 and side_2 >= side_3 and side_1**2 + side_3**2 == side_2**2:
        return "right"
    elif side_3 >= side_1 and side_3 >= side_2 and side_1**2 + side_2**2 == side_3**2:
        return "right"

if __name__ == "__main__":
    side1, side2, side3 = get_side_lengths()
    result = classify_triangle(side1, side2, side3)

    print(f"The given side lengths {side1}, {side2}, {side3}", end="") #skips line break
    if result == "does not exist":
        print(" DO NOT form a valid triangle.")
    else:
        print(f" form a valid {result} triangle.")