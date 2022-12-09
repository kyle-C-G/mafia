import unittest
from player import TestMafia
from player import TestDoctor
from player import TestGodfather
from player import TestInvestigator
from player import TestTown

def run_some_tests():
    # Run only the tests in the specified classes

    test_classes_to_run = [TestMafia, TestDoctor, TestGodfather, TestInvestigator, TestTown]

    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
        
    big_suite = unittest.TestSuite(suites_list)

    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)

    # ...

if __name__ == '__main__':
    run_some_tests()