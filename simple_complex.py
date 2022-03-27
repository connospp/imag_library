from simple_complex_set import SimpleComplexSet


class SimpleComplex(SimpleComplexSet):

    def add_complex(self, first_num: str, second_num: str,third_num: str = "0j") -> str:
        """Accepts 2-3 strings and returns sum in string."""

        numbers_entered = [first_num, second_num, third_num]  # Places strings into list
        self._validate_inputs(numbers_entered)  # Make sure valid input
        normal_numbers = self._prepare_numbers(numbers_entered)  # Will convert string to numbers for operations

        addition = sum(normal_numbers)  # Add numbers together

        result = str(addition) + "j"  # Append j to end result

        return result  # return end result

    def sub_complex(self, first_num=str, second_num=str) -> str:
        """Accepts 2 strings and returns the difference in string."""

        numbers_entered = [first_num, second_num]  # Places strings into list
        self._validate_inputs(numbers_entered)  # Make sure valid input
        normal_numbers = self._prepare_numbers(numbers_entered)  # Will convert string to numbers for operations

        subst = normal_numbers[0]
        for pointer in range(1, len(normal_numbers)):  # Subtracts numbers together
            subst -= normal_numbers[pointer]

        result = str(subst) + "j"  # Append j to end result

        return result

    def multiple_complex(self, first_num=str, second_num=str, third_num: str = "j") -> str:
        """Accepts 2-3 strings and returns string. Execution is first/second."""

        numbers_entered = [first_num, second_num, third_num]  # Places strings into list
        self._validate_inputs(numbers_entered)  # Make sure valid input
        normal_numbers = self._prepare_numbers(numbers_entered)  # Will convert string to numbers for operations

        mult = normal_numbers[0]
        for pointer in range(1, len(normal_numbers)):  # multiplies numbers together
            mult *= normal_numbers[pointer]

        result = str(mult) + "j"  # Append j to end result

        return result

    def divide_complex(self, first_num=str, second_num=str) -> str:
        """Accepts 2 strings and returns the quotient in string."""

        numbers_entered = [first_num, second_num] # Places strings into list
        self._validate_inputs(numbers_entered) # Make sure valid input
        normal_numbers = self._prepare_numbers(numbers_entered) # Will convert string to numbers for operations

        div = normal_numbers[0]
        for pointer in range(1, len(normal_numbers)): # divides numbers together
            div /= normal_numbers[pointer]

        result = str(div) + "j" # Append j to end result

        return result
