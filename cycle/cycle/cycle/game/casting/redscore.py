from game.casting.score import Score


class Redscore(Score):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    It also changes the player's number to 2

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        


    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"Player 2: {self._points}")
    
