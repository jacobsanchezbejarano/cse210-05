import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.cast import Cast
from game.casting.trail import Trail

class Redtrail(Trail):
    """
    A long trail.
    
    The responsibility of Snake is to move itself.
    Changes the body color to red, also, it changes the initial direction of the trail

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._prepare_body()

    def grow_tail(self, number_of_segments):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(constants.RED)
            self._segments.append(segment)

    def _prepare_body(self):
        x = int(constants.MAX_X / 1.5)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.TRAIL_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.RED
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)

    