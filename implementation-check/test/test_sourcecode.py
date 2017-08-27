'''
Created on Aug 26, 2017

@author: vlad
'''
import unittest
import sourcecode


class Test(unittest.TestCase):


    def setUp(self):
        
        # support no-args ctor
        model=sourcecode.Model()
        model.name="m1"
        model.id="/"
        
        model.add(sourcecode.Module("/mod1", "mod1"))
        model.add(sourcecode.Module("/mod2", "mod2"))
        model.add(sourcecode.Uses("u1","/mod1","/mod2"))
        
        
        self.model=model
        

    def tearDown(self):
        pass

    def testPrint(self):
        print self.model.render(pretty=True)

    def testParse(self):
        m=sourcecode.Model.parse(self.model.render())
        self.assert_(m!=None)
        
        print m.name
    
    def testFind(self):
        u=self.model.find("u1")
        
        self.assertEqual(u.source.get(self.model).name, "mod1" )

    def testNavigateToParent(self):
        pass
        
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()