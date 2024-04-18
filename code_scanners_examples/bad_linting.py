def add(x, y):
    return x + y

result = add(3, 5)
print("Result is:", result)

# Unused variable
unused_variable = "This variable is not used"

# Function name does not conform to snake_case convention
def InvalidFunctionName():
    return "This function name is invalid"

# Indentation is inconsistent
def inconsistent_indentation():
  print("This line has inconsistent indentation")

# Undefined variable
print(undefined_variable)

# Missing docstring
def missing_docstring():
    pass

missing_docstring()

# Line too long
long_variable_name_for_testing_purpose = "This is a long string used for testing purposes to create a line that exceeds the maximum line length as per PEP 8 guidelines"

# Incorrect indentation
if result > 5:
  print("Result is greater than 5")
else:
  print("Result is less than or equal to 5")