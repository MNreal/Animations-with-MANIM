from manim import *

# If you are using the get_ffmp script, you need this to get ffmpg into your project
# from get_ffmp import ffmp_get
# ffmp_get(r'Your/ffmpeg/bin/path')

class FirstAnimation(Scene):
    def construct(self):
        
        #Create Shapes
        circle = Circle()
        square = Square()

        #define Text
        text = Text("#SPACEHOLDER", font_size=40)
        text.color = RED

        #Create Circle and wait 1 s
        self.play(Create(circle))
        self.wait(1)

        #Fill Circle with color and wait 1 s
        self.play(circle.animate.set_fill(RED, opacity=1))
        self.wait(1)

        #Move Circle Up
        self.play(circle.animate.shift(UP))

        #transform Circle to Square and wait 1 s whyle keeping the red colorsceme
        square.set_stroke(RED, 1)
        square.set_fill(RED, opacity=1)
        self.play(Transform(circle, square))
        self.wait(1)	

        #Fade Out Square, add the Text "#PACEHOLDER" and wait 1 s
        self.play(FadeOut(circle))
        self.play(Write(text))
        self.wait(1)
       
