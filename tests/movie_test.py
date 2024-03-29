import unittest
from app.models import Movie

class MovieTest(unittest.TestCase):
    """
    Class that tests the behaviour of the Movie class
    """

    def setUp(self) -> None:
        """
        Set up method that will run before each test case
        """
        self.new_movie = movie(1234, 'Python Must Be Crazy', 'A thrilling new Python Series',
                               'https://image.tmdb.org/t/p/w500/khsjha27hbs', 8.5, 129993)

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie, Movie))


if __name__ == '__main__':
    unittest.main()
