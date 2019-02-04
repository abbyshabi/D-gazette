import unittest
from app.models import Articles


class ArticleTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test 
        '''
        self.new_article = Articles(12,'abc','abcdef','ab@ab.com','abc','au','utl@ue.com')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
