import unittest
import tests_12_3


f = unittest.TestSuite()
f.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
f.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

r = unittest.TextTestRunner(verbosity=2)
r.run(f)

