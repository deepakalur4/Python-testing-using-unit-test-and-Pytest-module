import unittest
import calc

class Testcalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(10,5),15)
        self.assertEqual(calc.add(-1,1),0)
        self.assertEqual(calc.add(-1,-1),-2)
    
    def test_multiply(self):
        self.assertEqual(calc.multiply(10,5),50)
        self.assertEqual(calc.multiply(-10,5),-50)
        self.assertEqual(calc.multiply(-10,-5),50)

    def test_substraction(self):
        self.assertEqual(calc.substraction(10,5),5)
        self.assertEqual(calc.substraction(-10,5),-15)
        self.assertEqual(calc.substraction(-10,-5),-5)

    def test_devide(self):
        self.assertEqual(calc.devide(10,5),2)
        self.assertEqual(calc.devide(-10,5),-2)
        self.assertEqual(calc.devide(-10,-5),2)

        self.assertRaises(ValueError,calc.devide,10,0)

        with self.assertRaises(ValueError):  
            calc.devide(10,0) 

if __name__=="__main__":
    unittest.main()
