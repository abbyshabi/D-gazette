import unittest
from app.models import Sources


class SourceTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the source class
    '''
    def setUp(self):
        '''
        set up method that will run before every test 
        '''
        self.new_source = Sources(12,'abc','abcdef','ab@ab.com','abc','au')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))
