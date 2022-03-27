Complex numbers
– Developed on Python –

Functionality:
1. Four functions provided that will add, subtract, divide and multiply 2 numbers parsed as string (3 numbers optional for add and multiply)
2. Two functions provided that will add and multiply an entire list of string as parsed
3. Each string parsed in function must be:
    a) Ending with a “j” with digits preceding (CAP or low but will only return low)
    b) Just “j” (CAP or low)
    c) Positive or negative number (positive without sign)
4. All invalid inputs will cause termination of the execution and the user will be informed of the invalid value
5. String numbers must be integers. Parsing floats is not supported at the moment, but will return floats when required

Assumptions:
1. We will only use it for complex numbers
2. We only need basic functionality such as Addition, Subtraction, Multiplication and Division


Test:
Extensive testing was done to verify behaviour of the library and verify invalid strings will stop execution and inform of invalid value
Test can be accessed from under "Tests" folder (test_number_validation , test_simple_batch_complex, test_simple.complex)
To run all 26 test cases:
    1. Install packages from requirements.txt
    2. Open terminal
    3. Type "python -m unittest discover "python -m unittest discover .\Tests\"
Test cases covered can be found under "tests/test cases covered.txt" in more detail


Future work:
1. Must allow parsing positive number with “+” sign (at the moment only positive numbers without a sign allowed)
2. Ability to work with exponents (square root, powers etc.)
3. Be able to handle real numbers not just imaginary
4. Add support for parsing float numbers
5. Testing input and expected result must be imported from json or CSV file. At the moment they are hardcoded



