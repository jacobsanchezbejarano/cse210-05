import constants
from game.scripting.action import Action
from game.shared.point import Point
from game.shared.color import Color

class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        score1 = cast.get_first_actor("scores")
        score2 = cast.get_second_actor("scores")

        food = cast.get_first_actor("foods")

        trail1 = cast.get_first_actor("trails")
        trail2 = cast.get_second_actor("trails")
        segments1 = trail1.get_segments()
        segments2 = trail2.get_segments()

        messages = cast.get_actors("messages")



        self._video_service.clear_buffer()
        self._video_service.draw_actor(food)

        self._video_service.draw_actors(segments1)
        self._video_service.draw_actors(segments2)

        score1 = cast.get_first_actor('scores')
        score2 = cast.get_second_actor('scores')

        self._video_service.draw_actor(score1)
        score2.set_position(Point((constants.MAX_X-100),0))
        self._video_service.draw_actor(score2)

        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()