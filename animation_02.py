from manim import *

class OctagonAnimation(Scene):
    def construct(self):
        # Create an octagon
        octagon = RegularPolygon(8)
        octagon.set_fill(BLUE, opacity=1)

        # Position the octagon to the left side of the screen
        octagon.shift(LEFT * 6)

        # Play the octagon rolling from left to right
        self.play(FadeIn(octagon))
        self.play(octagon.animate.shift(RIGHT * 6).rotate_about_origin(PI), run_time=4)

        # Transform octagon into a smaller circle
        circle = Circle(radius=0.5)
        circle.set_fill(RED, opacity=1)
        self.play(Transform(octagon, circle))

        # Fade out the circle completely
        self.play(FadeOut(octagon))

        # Transform into the text "HUH?!?!"
        text = Text("HUH?!?!", font_size=96)
        text.set_color(WHITE)
        self.play(FadeIn(text))

        # Wait for a moment to show the final result
        self.wait(2)
