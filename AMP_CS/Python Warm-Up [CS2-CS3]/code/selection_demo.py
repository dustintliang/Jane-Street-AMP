def get_side_lengths():
    """Prompts the user to enter three side lengths of a triangle.

    Returns:
      Three float values reprsenting the side lengths of the triangle
    """
    side_1 = float(input("Side 1: "))
    side_2 = float(input("Side 2: "))
    side_3 = float(input("Side 3: "))
    
    return side_1, side_2, side_3

def is_valid_triangle(side_1:float, side_2:float, side_3:float)->bool:
  """Given three side lengths, determines whether the three sides form a valid triangle.
     A valid triangle may be formed whenever the sum of two smaller side lengths exceeds the length of the largest side.

        Args:
            side_1: Measurement of side #1 of a triangle
            side_2: Measurement of side #2 of a triangle
            side_3: Measurement of side #3 of a triangle

        Returns:
            A bool value indicating whether or not the triangle exists

        Examples
        --------
        >>> is_valid_triangle(2, 2, 4)
        False

        >>> is_valid_triangle(3, 5, 4)
        True
  """
  if side_1 <= 0 or side_2 <= 0 or side_3 <= 0:  #no negative side lengths allowed!
    return False
  
  #sum of smaller two side legnths must exceed larger side length
  if side_1 >= side_2 and side_1 >= side_3 and side_2 + side_3 <= side_1: 
    return False
  elif side_2 >= side_1 and side_2 >= side_3 and side_1 + side_3 <= side_2:
    return False
  elif side_3 >= side_1 and side_3 >= side_2 and side_1 + side_2 <= side_3:
    return False

  return True
    
if __name__ == "__main__":
    side_1, side_2, side_3 = get_side_lengths()

    if is_valid_triangle(side_1, side_2, side_3): 
        print(f"Side lengths {side_1}, {side_2}, and {side_3} DO form a valid triangle.")
    else:
        print(f"Side lengths {side_1}, {side_2}, and {side_3} DO NOT form a valid triangle.")
