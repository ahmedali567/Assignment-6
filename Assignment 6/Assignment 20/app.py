class InvalidAgeError(Exception):
    """Exception raised for invalid age."""
    pass

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Age {age} is below the minimum required age of 18.")
    return f"Age {age} is valid."

try:
    print(check_age(16))
except InvalidAgeError as e:
    print(f"Error: {e}")
