from simple_complex import SimpleComplex
from simple_complex_batch import SimpleComplexBatch


class TestingComplex:

    def __init__(self):
        self.my_complex = SimpleComplex()
        self.my_complex_batch = SimpleComplexBatch()

    def project_for_complex(self):  # Testing library

        ###EXAMPLE###
        print(self.my_complex.add_complex("j", "-5j"))
        print(self.my_complex.sub_complex("-5j", "-8j"))
        print(self.my_complex.multiple_complex("-5j", "-8j", "-j"))
        print(self.my_complex.divide_complex("-5j", "-8j"))

        print(self.my_complex_batch.add_complex_list(["3j", "2j", "-3j"]))
        print(self.my_complex_batch.multiple_complex_list(["1j", "3j", "3j", "4j"]))
        ###########

if __name__ == '__main__':
    go_class = TestingComplex()
    go_class.project_for_complex()
