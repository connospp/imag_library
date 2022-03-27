Complex numbers
– Developed on Python –

Functionality:
1. Four functions provided that will add, subtract, divide and multiply 2 numbers parsed as string (3 numbers optional for add and multiply)
2. Two functions provided that will add and multiply an entire list of string as parsed
3. Each string parsed in function must be:
    a) Ending with a “j” with digits preceding or
    b) Can be just “j”.
    c) Can be positive or negative number.
4. All invalid inputs will cause termination of the execution and the user will be informed of the invalid value
5. String numbers must be integers. Floats are not supported at the moment.

Assumptions:
1. We need only use it for complex numbers
2. We only need basic functionality at this moment such as Addition, Subtraction, Multiplication and Division


Test:
Extensive testing was done to verify behaviour of the library and verify invalid strings will stop execution and inform of invalid value
Test can be accessed from under "Tests" folder (test_number_validation , test_simple_batch_complex, test_simple.complex)
To run all 22 test cases:
    1. Install packages from requirements.txt
    2. Open terminal
    3. Type "python -m unittest discover "python -m unittest discover .\Tests\"
Test cases covered can be found under tests/test cases covered.txt in more detail


Future work:

1. Must allow parsing positive number with “+” sign (at the moment positive numbers are parsed without a sign)
2. Ability to work with exponents (square root, powers etc.)
3. Accept real numbers not just imaginary
4. Add support for parsing float numbers
5. Testing input and expected result must be imported from json or CSV file. At the moment they are hardcoded



