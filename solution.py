class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.dir = direction


     def forward(self, plateau_x, plateau_y):
        if self.dir == 'N' and self.y < plateau_y:
            self.y += 1
        elif self.dir == 'E' and self.x < plateau_x:
            self.x += 1
        elif self.dir == 'S' and self.y > 1:
            self.y -= 1
        elif self.dir == 'W' and self.x > 1:
            self.x -= 1    

    def turn_left(self):
        if self.dir== 'N':
            self.dir= 'W'
        elif self.dir== 'W':
            self.dir= 'S'
        elif self.dir== 'S':
            self.dir= 'E'
        elif self.dir== 'E':
            self.dir = 'N'

    def turn_right(self):
        if self.dir== 'N':
            self.dir= 'E'
        elif self.dir== 'E':
            self.dir= 'S'
        elif self.dir == 'S':
            self.dir= 'W'
        elif self.dir== 'W':
            self.dir= 'N'

   

def navigate_robot(plateau_x, plateau_y, commands):
    robot = Robot(1, 1, 'N')

    for command in commands:
        if command == 'L':
            robot.turn_left()
        elif command == 'R':
            robot.turn_right()
        elif command == 'F':
            robot.forward(plateau_x, plateau_y)

    return robot.x, robot.y, robot.direction

if __name__ == '__main__':
    plateau_x, plateau_y = map(int, input().split('x'))
    commands = input().strip()
    x, y, direction = navigate_robot(plateau_x, plateau_y, commands)
    print(f'{x},{y},{direction}')