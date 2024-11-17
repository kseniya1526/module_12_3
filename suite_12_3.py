import unittest

from tests_12_3 import RunnerTest, TournamentTest

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTest(loader.loadTestsFromTestCase(RunnerTest))
suite.addTest(loader.loadTestsFromTestCase(TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)