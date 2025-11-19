"""
PLD: SELF-IMPROVING VISION-LANGUAGE-ACTION MODELS WITH DATA GENERATION VIA RESIDUAL RL

This Manim scene visualizes key concepts from the PLD paper.
"""

from manim import *


class PLDIntro(Scene):
    def construct(self):
        # Title
        title = Text("PLD: Self-Improving VLA Models", font_size=48)
        title.to_edge(UP)
        
        subtitle = Text(
            "Data Generation via Residual RL",
            font_size=32,
            color=BLUE
        )
        subtitle.next_to(title, DOWN)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        
        # Clear title
        self.play(FadeOut(title), FadeOut(subtitle))
        
        # Key concept: VLA Model
        vla_title = Text("Vision-Language-Action (VLA) Model", font_size=36)
        vla_title.to_edge(UP)
        
        # Components
        vision = Rectangle(width=2, height=1.5, color=GREEN)
        vision_text = Text("Vision", font_size=24).move_to(vision)
        vision_group = VGroup(vision, vision_text)
        vision_group.shift(LEFT * 4)
        
        language = Rectangle(width=2, height=1.5, color=YELLOW)
        language_text = Text("Language", font_size=24).move_to(language)
        language_group = VGroup(language, language_text)
        
        action = Rectangle(width=2, height=1.5, color=RED)
        action_text = Text("Action", font_size=24).move_to(action)
        action_group = VGroup(action, action_text)
        action_group.shift(RIGHT * 4)
        
        self.play(Write(vla_title))
        self.play(
            FadeIn(vision_group),
            FadeIn(language_group),
            FadeIn(action_group)
        )
        self.wait(1)
        
        # Arrows showing flow
        arrow1 = Arrow(vision.get_right(), language.get_left(), buff=0.1)
        arrow2 = Arrow(language.get_right(), action.get_left(), buff=0.1)
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(2)
        
        # Clear scene
        self.play(
            *[FadeOut(mob) for mob in self.mobjects]
        )


class PLDResidualRL(Scene):
    def construct(self):
        title = Text("Residual RL Concept", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Base policy
        base_box = Rectangle(width=3, height=1.5, color=BLUE)
        base_text = Text("Base Policy\n(VLA)", font_size=24)
        base_text.move_to(base_box)
        base_group = VGroup(base_box, base_text)
        base_group.shift(LEFT * 3 + UP * 0.5)
        
        # Residual policy
        residual_box = Rectangle(width=3, height=1.5, color=ORANGE)
        residual_text = Text("Residual\nPolicy", font_size=24)
        residual_text.move_to(residual_box)
        residual_group = VGroup(residual_box, residual_text)
        residual_group.shift(RIGHT * 1 + UP * 0.5)
        
        # Combined action
        combined_box = Rectangle(width=3, height=1.5, color=GREEN)
        combined_text = Text("Combined\nAction", font_size=24)
        combined_text.move_to(combined_box)
        combined_group = VGroup(combined_box, combined_text)
        combined_group.shift(RIGHT * 1 + DOWN * 2)
        
        self.play(FadeIn(base_group))
        self.wait(0.5)
        self.play(FadeIn(residual_group))
        self.wait(0.5)
        
        # Show addition
        plus_sign = MathTex("+", font_size=60)
        plus_sign.move_to((base_group.get_right() + residual_group.get_left()) / 2)
        
        arrow_down = Arrow(
            residual_group.get_bottom(),
            combined_group.get_top(),
            buff=0.1
        )
        
        self.play(Write(plus_sign))
        self.play(GrowArrow(arrow_down))
        self.play(FadeIn(combined_group))
        self.wait(2)
        
        # Clear scene
        self.play(*[FadeOut(mob) for mob in self.mobjects])


class PLDWorkflow(Scene):
    def construct(self):
        title = Text("PLD Training Workflow", font_size=40)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create workflow boxes
        step1 = Rectangle(width=3, height=1, color=BLUE)
        step1_text = Text("1. Collect\nData", font_size=20).move_to(step1)
        step1_group = VGroup(step1, step1_text).shift(UP * 1.5 + LEFT * 4)
        
        step2 = Rectangle(width=3, height=1, color=YELLOW)
        step2_text = Text("2. Train\nResidual", font_size=20).move_to(step2)
        step2_group = VGroup(step2, step2_text).shift(UP * 1.5)
        
        step3 = Rectangle(width=3, height=1, color=GREEN)
        step3_text = Text("3. Generate\nData", font_size=20).move_to(step3)
        step3_group = VGroup(step3, step3_text).shift(UP * 1.5 + RIGHT * 4)
        
        step4 = Rectangle(width=3, height=1, color=ORANGE)
        step4_text = Text("4. Improve\nVLA", font_size=20).move_to(step4)
        step4_group = VGroup(step4, step4_text).shift(DOWN * 1)
        
        # Arrows
        arrow1 = Arrow(step1_group.get_right(), step2_group.get_left(), buff=0.1)
        arrow2 = Arrow(step2_group.get_right(), step3_group.get_left(), buff=0.1)
        arrow3 = Arrow(step3_group.get_bottom(), step4_group.get_top(), buff=0.1)
        arrow4 = CurvedArrow(
            step4_group.get_left() + LEFT * 0.5,
            step1_group.get_bottom() + DOWN * 0.5,
            angle=-TAU/4
        )
        
        # Animate workflow
        self.play(FadeIn(step1_group))
        self.wait(0.5)
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(step2_group))
        self.wait(0.5)
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(step3_group))
        self.wait(0.5)
        self.play(GrowArrow(arrow3))
        self.play(FadeIn(step4_group))
        self.wait(0.5)
        self.play(Create(arrow4))
        
        # Add cycle annotation
        cycle_text = Text("Iterative\nImprovement", font_size=24, color=RED)
        cycle_text.shift(LEFT * 4 + DOWN * 1.5)
        self.play(FadeIn(cycle_text))
        
        self.wait(3)


# Main scene combining all concepts
class PLDComplete(Scene):
    def construct(self):
        # Title slide
        main_title = Text("PLD Framework", font_size=56, weight=BOLD)
        subtitle = Text(
            "Self-Improving Vision-Language-Action Models",
            font_size=32
        )
        subtitle.next_to(main_title, DOWN)
        
        self.play(Write(main_title))
        self.play(FadeIn(subtitle))
        self.wait(2)
        self.play(FadeOut(main_title), FadeOut(subtitle))
        
        # Show VLA components
        intro_scene = PLDIntro()
        intro_scene.construct()
        
        # Show Residual RL
        residual_scene = PLDResidualRL()
        residual_scene.construct()
        
        # Show Workflow
        workflow_scene = PLDWorkflow()
        workflow_scene.construct()
        
        # Conclusion
        conclusion = Text("Thank you!", font_size=48)
        self.play(Write(conclusion))
        self.wait(2)
