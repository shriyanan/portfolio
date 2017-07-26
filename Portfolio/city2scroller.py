
class Building():

    def __init__(self, x_point, y_point, width, height, color):
        self.x_point = x_point
        self.y_point = y_point
        self.width = width
        self.height = height
        self.color = color

    def draw(self):
        """
        uses pygame and the global screen variable to draw the building on the screen
        """
        pygame.draw.rect(screen, self.color, [self.x_point, self.y_point, self.width , self.height])

        
    def move(self, speed):
        self.x_point -= speed
        

    

class Scroller(object):

    def __init__(self, width, height, color, speed):
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.buildings = []

    def add_buildings(self):
        """
        Will call add_building until there the buildings fill up the width of the
        scroller.
        """
        current_w = 0
        while current_w <= self.width:
            self.add_building(current_w)
            #current_w += self.buildings[1].width



    def add_building(self, x):
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """
        height = self.height/2
        width = self.width/4
        y = SCREEN_HEIGHT - height
        building1 = Building(x, y, width, height, self.color)

        pygame.draw.rect(screen, self.color, [x, y, self.width , self.height])




    def draw_buildings(self):
        """
        This calls the draw method on each building.
        """

        for each in self.buildings:
            each.draw()

    def move_buildings(self):
        """
        This calls the move method on each building passing in the speed variable
        As the buildings move off the screen a new one is added.
        """
        for each in self.buildings:
            each.move(self.speed)
        
        self.add_building((self.buildings[-1].x) + self.buildings[-1])

building1 = Building(300, 400, 200, 300, BLACK)
building2 = Scroller(50, 100, BLUE, 15)
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 200, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 500, MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 650, BACK_SCROLLER_COLOR, 1)
