from manim import *
import random
import csv
import numpy as np

class TitleSlide(Scene):
    def construct(self):
        line1 = Text("How to predict accurate cosmological statistics", font_size=50)
        line2 = Text("in any model of gravity", font_size=50)
        title_block = VGroup(line1, line2).arrange(DOWN, buff=0.3).move_to(UP * 0.5)
        author = Text("Maria del Pilar Zarco Villegas", font_size=36)
        author.next_to(title_block, DOWN, buff=0.8)
        self.play(Write(line1))
        self.play(Write(line2))
        self.play(FadeIn(author))
        self.wait(2)

class UniverseStory(Scene):
    def construct(self):
        stars = VGroup(*[Dot(point=[random.uniform(-6, 6), random.uniform(-3.5, 3.5), 0], radius=0.02, color=WHITE) for _ in range(100)])
        self.play(FadeIn(stars, lag_ratio=0.01), run_time=1.5)
        line1 = Text("The universe is full of structure...", font_size=40)
        self.play(Write(line1))
        self.wait(1)
        self.play(FadeOut(line1))

        line2 = Text("...and we use simulations to map and understand", font_size=40)
        line3 = Text("the physics behind it!", font_size=40)
        lines = VGroup(line2, line3).arrange(DOWN, buff=0.3).move_to(ORIGIN)
        self.play(Write(lines))
        self.wait(1)
        self.play(FadeOut(lines))
        self.play(FadeOut(stars))

class MillenniumOverlay(Scene):
    def construct(self):
        self.camera.background_color = BLACK
        credit = Text("Millennium Simulation (Springel et al. 2005)", font_size=15, color=GREY_B)
        credit.to_corner(DR)
        self.add(credit)

        galaxy_label = Text("Each point is a galaxy", font_size=36, color=WHITE).to_edge(UP)
        self.play(FadeIn(galaxy_label))
        self.wait(2)

        filament_arrow = Arrow(start=LEFT * 5 + DOWN * 1, end=ORIGIN, buff=0.2, color=BLUE)
        filament_text = Text("Filament", font_size=30, color=BLUE).next_to(filament_arrow, LEFT)
        self.play(GrowArrow(filament_arrow), FadeIn(filament_text))
        self.wait(1)
        self.play(FadeOut(filament_arrow), FadeOut(filament_text), run_time=0.5)

        void_arrow = Arrow(start=RIGHT * 5 + UP * 1, end=RIGHT * 2 + UP * 0.5, buff=0.2, color=YELLOW)
        void_text = Text("Void", font_size=30, color=YELLOW).next_to(void_arrow, RIGHT)
        self.play(GrowArrow(void_arrow), FadeIn(void_text))
        self.wait(2)

class MatterPowerSpectrum(Scene):
    def construct(self):
        self.play(Write(Text("Matter Power Spectrum", font_size=40).to_edge(UP)))
        self.wait(0.5)

        axes = Axes(
            x_range=[0.0002, 5],
            y_range=[80, 40000],
            x_length=8,
            y_length=4.5,
            tips=True,
            axis_config={"include_numbers": True},
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT},
        ).shift(DOWN * 0.5 + LEFT * 0.5)

        x_label = Text("k [Mpc/h]", font_size=24).next_to(axes.x_axis, DOWN)
        y_label = Text("P(k) [(Mpc/h)^3]", font_size=24).next_to(axes.y_axis, LEFT)
        self.play(Create(axes), Write(x_label), Write(y_label))
        self.wait(0.3)

        # Load and sanitize data
        k_vals, P_vals = [], []
        with open("power_spectrum_sample.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    k = float(row["k"])
                    P = float(row["P"])
                    if (
                        np.isfinite(k) and np.isfinite(P)
                        and 0.0002 < k < 5
                        and 80 < P < 40000
                    ):
                        k_vals.append(k)
                        P_vals.append(P)
                except Exception as e:
                    print(f"Skipping invalid row: {row} due to error: {e}")

        if not k_vals or not P_vals:
            raise ValueError("No valid data points found in power_spectrum_sample.csv")

        # Plot the curve
        curve = axes.plot_line_graph(
            x_values=k_vals,
            y_values=P_vals,
            line_color=WHITE,
            stroke_width=2
        )
        self.play(Create(curve), run_time=2)
        self.wait(0.3)

        vline = DashedLine(
            axes.c2p(0.3, 80),
            axes.c2p(0.3, 40000),
            color=YELLOW
        )
        vlabel = Text("Non-linear transition", font_size=22, color=YELLOW).next_to(vline, UP)
        self.play(Create(vline), FadeIn(vlabel))

        lin = Text("Linear", font_size=24).next_to(axes.c2p(0.001, 1000), LEFT)
        nlin = Text("Non-linear", font_size=24).next_to(axes.c2p(2, 500), RIGHT)
        self.play(FadeIn(lin), FadeIn(nlin))
