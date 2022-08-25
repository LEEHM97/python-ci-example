import unittest

from main import hello


class MainTest(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello World!")


if __name__ == "__main__":  # pragma: no cover
    unittest.main()

    # unittest 실행
    # python -m unittest discover -p "*_test.py"
    # coverage 만들기
    # python -m coverage run --source=./ -m unittest discover -p "*_test.py"
    # python -m coverage xml
