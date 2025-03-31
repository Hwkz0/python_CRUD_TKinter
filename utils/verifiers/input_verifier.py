from utils.exceptions.input_exceptions import InvalidInputException
from utils.exceptions.input_exceptions import InvalidTypeException
from utils.exceptions.input_exceptions import EmptyInputException
from utils.exceptions.input_exceptions import InvalidDateException
from utils.exceptions.input_exceptions import InvalidRangeException

from datetime import datetime

# TODO: TRY TO MAKE A GENERAL MESSAGEBOX FUNCTION TO AVOID REDUNDANCY

# TODO: MAKE A LOGGER FOR EXCEPTIONS AND CLASSIFY THEM BY TYPE AND LEVEL


def validate_date_format(start_datetime, end_datetime):

    # Get today's date
    today = datetime.today().date()

    # Check if the start date is not before today
    if start_datetime < today:
        raise InvalidDateException("Start date cannot be before today")

    # Check if the end date is not before the start date
    if end_datetime < start_datetime:
        raise InvalidDateException("End date cannot be before start date")


def validate_input_length(input_data, max_length):
    if len(input_data) > max_length:
        raise InvalidInputException(f"Input should be less than {max_length} characters long")


def validate_input_type(input_data, expected_type):
    if expected_type == str:
        if input_data.isdecimal():
            raise InvalidTypeException(f"Input should be of type {expected_type.__name__}")
    if expected_type == int:
        if not input_data.isdecimal():
            raise InvalidTypeException(f"Input should be of type {expected_type.__name__}")


def validate_input_range(input_data, min_value, max_value):
    input_data=int(input_data)
    if input_data < min_value or input_data > max_value:
        raise InvalidRangeException(f"Input should be between {min_value} and {max_value}")


def validate_input_not_empty(input_data):
    if not input_data:
        raise EmptyInputException("Input should not be empty")


# is this the best place for this ?
# at least avoids redundancy (IDEA: TRY TO MAKE A GENERAL VERIFIER file FOR SOME THINGS)
def validate_skill(skill):
    validate_input_length(skill, 100)
    validate_input_type(skill, str)
    validate_input_not_empty(skill)
