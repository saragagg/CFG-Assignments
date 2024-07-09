import unittest

from exam_python import no_of_handshakes


class TestProgram(unittest.TestCase):

    def test_case_1(self):
        self.assertEqual(no_of_handshakes(3), 3)

    def test_case_2(self):
        self.assertEqual(no_of_handshakes(4), 6)

    def test_case_3(self):
        self.assertEqual(no_of_handshakes(20), 190)

    def test_case_4(self):
            self.assertEqual(no_of_handshakes('blabla'), None) # checking error handling