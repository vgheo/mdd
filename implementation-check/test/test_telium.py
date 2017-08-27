
import unittest
import telium

class TestTelium(unittest.TestCase):
    
    DATA1="data/test1.teliumProject"

    def setUp(self):
        fIn = open(self.DATA1, "r")
        self.tp1 = telium.teliumProject.parse(fIn)

    def testRender(self):
        print self.tp1.render(encoding="UTF-8", pretty=True)

