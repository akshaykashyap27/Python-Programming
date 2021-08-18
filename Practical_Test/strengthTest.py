import unittest
from Python_PracticalExam.compareFunc import compareStrength
class TestStrength(unittest.TestCase):
    def teststrength1(self):
        EnemyData = [10,20,30,40]
        HeroData = [10,20,30,40]
        result = compareStrength(EnemyData,HeroData)
        self.assertEqual(result,"Both are equal")

    def teststrength2(self):
        EnemyData = [10,20,30,40]
        HeroData = [20,30,40,5]
        result = compareStrength(EnemyData,HeroData)
        self.assertEqual(result,"Result - WIN")

    def teststrength3(self):
        EnemyData = [100,200,300,400]
        HeroData = [10,20,30,40]
        result = compareStrength(EnemyData,HeroData)
        self.assertEqual(result,"Result - LOSE")


if __name__ == '__main__':
    unittest.main()


'''
IMPORTANT TERMS:
test fixture
test case
test suite
test runner
'''