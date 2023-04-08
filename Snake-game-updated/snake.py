from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake():

    def __init__(self): 
        self.segments = []
        self.starting_pos = self.starting_position()
        self.defining_snake(self.starting_pos) 
        self.head = self.segments[0]
    
    def starting_position(self):
        starting_pos = [(0, 0), (-20, 0), (-40, 0)]
        return starting_pos

    def segments_list(self):
        segments = []
        return segments
    
    def defining_snake(self, starting_pos):
        for pos in starting_pos:
           self.add_segment(pos) 

    def move(self):
        # # what we're trying to achieve here is after 1 changes place [2 go to 1 and 3 goto 2]place then 1 changes place and loop goes on.
        # # here range( starting point , steps needed, stopping point)
        for segment_number in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_number - 1].xcor() 
            new_y = self.segments[segment_number - 1].ycor() 
            
            self.segments[segment_number].goto(new_x, new_y)
        
        self.segments[0].forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    
    def add_segment(self, position):
        mr_turtle = Turtle("square")
        mr_turtle.color("white")
        mr_turtle.penup()
        mr_turtle.goto(position)
        self.segments.append(mr_turtle)

    def extend_snake(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.defining_snake(self.starting_pos)
        self.head = self.segments[0]
