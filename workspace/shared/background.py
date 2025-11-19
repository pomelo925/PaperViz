from manim import *

class BaseScene(Scene):
    """
    A base scene for all paper videos.
    Sets the background color and adds a brandmark.
    """
    def setup(self):
        # Set background color to dark gray
        self.camera.background_color = "#222222"
        
        # Brandmark (Yellow Circle in bottom right)
        self.brandmark = Circle(radius=0.4, color=YELLOW, fill_opacity=0.8, fill_color=YELLOW)
        self.brandmark.to_corner(DR, buff=0.5)
        self.add(self.brandmark)
