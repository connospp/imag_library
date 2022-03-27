import re


class SimpleComplexSet: #This is the base class for the simple_complex methods. Will validate numbers and prepare them

    def __init__(self):
        pass

    def _prepare_numbers(self, complex_values: list):
        """Prepares numbers for math execution by removing j"""
        normal_numbers = []
        for pointer in range(len(complex_values)):  # sweeps through list of numbers
            current_number = complex_values[pointer]
            if current_number == "j" or current_number == "-j":  # check if number is just a j without digit
                current_number = current_number.replace("j", "1j")  # will add "1" to be compatible with rest of code

            normal_numbers.append(int(current_number.replace('j', '')))  # Remove "j"s to be able to do the math
                                                                         # TODO For the future convert to float
        return normal_numbers  # return new list

    def _validate_inputs(self, complex_values: list):
        """Will validate parsed numbers. Allows only digits ending with 'j' (positive or negative) or just 'j' """
        for number in complex_values:
            check_input = re.findall("^\d+j$|^[j]$|^-\d+[j]$|^-[j]$", #TODO For the future allow dot for float
                                     number)  # Will allow only digits ending with 'j' (positive or negative) or just 'j'

            if not check_input:  # If not valid complex number,
                raise ValueError(f"Number '{number}' not a valid imaginary number. Only digits followed by j allowed")
