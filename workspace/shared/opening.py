from manim import *
import sys
from pathlib import Path

# Add workspace to Python path
sys.path.insert(0, str(Path(__file__).parent.parent))

from shared.background import BaseScene

class OpeningScene(BaseScene):
    """
    A template for the opening scene of a paper video.
    Users should subclass this and override the class attributes.
    """
    title_str = "Paper Title"
    subtitle_str = "Paper Subtitle"
    author_str = "Author Name"
    publish_date_str = "Date"
    
    def construct(self):
        # Create text objects
        title = Text(self.title_str, font_size=48, weight=BOLD)
        title.to_edge(UP, buff=1.5)
        
        subtitle = Text(self.subtitle_str, font_size=32, color=BLUE)
        subtitle.next_to(title, DOWN, buff=0.5)
        
        author = Text(f"Author: {self.author_str}", font_size=24, color=GRAY)
        author.next_to(subtitle, DOWN, buff=1.0)
        
        date = Text(f"Published: {self.publish_date_str}", font_size=24, color=GRAY)
        date.next_to(author, DOWN, buff=0.2)
        
        # Animation
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP), run_time=1)
        self.play(FadeIn(author), FadeIn(date), run_time=1)
        
        self.wait(2)
        
        # Transition out (optional, or leave it to the user to clear)
        self.play(
            FadeOut(title),
            FadeOut(subtitle),
            FadeOut(author),
            FadeOut(date),
        )
