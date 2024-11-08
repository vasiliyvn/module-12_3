from unittest import TestCase

import unit1
import unittest


class RunnerTest(TestCase):
    is_frozen = False
    def decor(self):
        self.is_frozen = True
        if self.is_frozen is True:
            pass
    def test_walk(self):
        w = unit1.Runner('1')
        for i in range(10):
            w.walk()
        self.assertEqual(w.distance, 50)

    def test_run(self):
        r = unit1.Runner('2')
        for j in range(10):
            r.run()
        self.assertEqual(r.distance, 100)

    def test_challenge(self):
        walk1 = unit1.Runner('3')
        run1 = unit1.Runner('4')
        for k in range(10):
            walk1.walk()
            run1.run()
        self.assertNotEqual(walk1.distance, run1.distance)


if __name__ == "__main__":
    unittest.main()

class TournamentTest(TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}
    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.u = unit1.Runner('Усейн', 10)
        self.a = unit1.Runner('Андрей', 9)
        self.n = unit1.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1},{elem}')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        tour = unit1.Tournament(90, self.u, self.n)
        results = tour.start()
        self.all_results = results
        self.assertTrue(results[max(results.keys())] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_run1(self):
        tour = unit1.Tournament(90, self.a, self.n)
        results1 = tour.start()
        self.all_results = results1
        self.assertTrue(results1[max(results1.keys())] == 'Ник')

    @unittest.skipIf(True, 'Тесты в этом кейсе заморожены')
    def test_run2(self):
        tour = unit1.Tournament(90, self.u, self.a, self.n)
        results2 = tour.start()
        self.all_results = results2
        self.assertTrue(results2[max(results2.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
