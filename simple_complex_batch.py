from simple_complex_set import SimpleComplexSet


class SimpleComplexBatch(SimpleComplexSet):  # Same as simple_complex but will accept lists of string instead of strings

    def add_complex_list(self, numbers_entered: list) -> str:
        """Accepts list of strings and returns sum of list in string."""

        numbers_entered = [x.lower() for x in numbers_entered] # Validation accepts only lower J. Hence making sure

        self._validate_inputs(numbers_entered)  # Make sure valid input
        normal_numbers = self._prepare_numbers(numbers_entered)  # Will convert string to numbers for operations

        addition = sum(normal_numbers)  # Add numbers together

        result = str(addition) + "j"  # Append j to end result

        return result  # return end result

    def multiple_complex_list(self, numbers_entered: list) -> str:
        """Accepts list of strings and returns product of list in string."""

        numbers_entered = [x.lower() for x in numbers_entered]

        self._validate_inputs(numbers_entered)  # Make sure valid input
        normal_numbers = self._prepare_numbers(numbers_entered)  # substract numbers together

        mult = normal_numbers[0]
        for pointer in range(1, len(normal_numbers)):  # multiplies numbers together
            mult *= normal_numbers[pointer]

        result = str(mult) + "j"

        return result  # return end result
