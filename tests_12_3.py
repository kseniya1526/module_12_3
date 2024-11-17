import unittest
import TestCase


def skip_if_frozen(method):
    def wrapper(self, *args, **kwargs):
        if self.is_frozen:
            self.skipTest('Тесты в этом кейсе заморожены')
        else:
            return method(self, *args, **kwargs)

    return wrapper


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @skip_if_frozen
    def test_walk(self):
        obj = TestCase.Runner('Alex')
        for i in range(10):
            obj.walk()
        self.assertEqual(obj.distance, 50, 'test_walk')

    @skip_if_frozen
    def test_run(self):
        obj = TestCase.Runner('Alex')
        for i in range(10):
            obj.run()
        self.assertEqual(obj.distance, 100, 'test_run')

    @skip_if_frozen
    def test_challenge(self):
        obj1 = TestCase.Runner('Alex')
        obj2 = TestCase.Runner('Max')
        for i in range(10):
            obj1.walk()
            obj2.run()
        self.assertNotEqual(obj1.distance, obj2.distance, 'test_challenge')


if __name__ == '__main__':
    unittest.main()


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @skip_if_frozen
    def setUp(self):
        self.Usain = TestCase.Runner('Усэйн', 10)
        self.Andrey = TestCase.Runner('Андрей', 9)
        self.Nick = TestCase.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results:
            formatted_result = '{' + ', '.join(f'{place}: {runner}' for place, runner in result.items()) + '}'
            print(formatted_result)

    @skip_if_frozen
    def test_Usain_Nick(self):
        tournament = TestCase.Tournament(90, self.Usain, self.Nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

    @skip_if_frozen
    def test_Andrey_Nick(self):
        tournament = TestCase.Tournament(90, self.Andrey, self.Nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')

    @skip_if_frozen
    def test_Usain_Andrey_Nick(self):
        tournament = TestCase.Tournament(90, self.Usain, self.Andrey, self.Nick)
        results = tournament.start()
        self.all_results.append(results)
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == 'Ник')


if __name__ == '__main__':
    unittest.main()