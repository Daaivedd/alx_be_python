def safe_divide(numerator, denominator):
  """Performs division with error handling.

  Args:
    numerator: The numerator.
    denominator: The denominator.

  Returns:
    The result of the division or an error message.
  """

  try:
    result = float(numerator) / float(denominator)
    return result
  except ZeroDivisionError:
    return "Error: Division by zero."
  except ValueError:
    return "Error: Please enter numeric values only."