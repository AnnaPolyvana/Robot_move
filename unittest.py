import unittest

from robot import navigate_robot

class TestNavigateRobot(unittest.TestCase):
    def test_navigate_robot(self):
        plateau_x, plateau_y = 5, 5
        commands = 'LFLRFLFF'
        x, y, direction = navigate_robot(plateau_x, plateau_y, commands)
        self.assertEqual(x, 1)
        self.assertEqual(y, 4)
        self.assertEqual(direction, 'W')

    def test_navigate_robot_at_ontop(self):
        plateau_x, plateau_y = 5, 5
        commands = 'FFFFFFFFFF'
        x, y, direction = navigate_robot(plateau_x, plateau_y, commands)
        self.assertEqual(x, 1)
        self.assertEqual(y, 5)
        self.assertEqual(direction, 'N')

    def test_navigate_robot_at_right(self):
        plateau_x, plateau_y = 3, 5
        commands = 'RRR'
        x, y, direction = navigate_robot(plateau_x, plateau_y, commands)
        self.assertEqual(x, 1)
        self.assertEqual(y, 5)
        self.assertEqual(direction, 'N')
        

if __name__ == '__main__':
    unittest.main()