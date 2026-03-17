from manim import *
import numpy as np

class GradientVectorExplanation(Scene):
    def construct(self):
        # -----------------------------
        # Choose your gradient values
        # -----------------------------
        Ix = 4
        Iy = 3

        # Safer angle computation than arctan(Iy / Ix)
        # because it handles signs and Ix = 0 correctly.
        theta = np.arctan2(Iy, Ix)
        theta_deg = np.degrees(theta)

        # -----------------------------
        # Top text: given values
        # -----------------------------
        given_text = MathTex(
            r"I_x = " + str(Ix),
            r"\quad",
            r"I_y = " + str(Iy)
        ).scale(0.9).to_edge(UP)

        self.play(Write(given_text))
        self.wait(0.5)

        # -----------------------------
        # Coordinate plane
        # -----------------------------
        plane = NumberPlane(
            x_range=[-2, 10, 1],
            y_range=[-2, 8, 1],
            x_length=9,
            y_length=7,
            background_line_style={
                "stroke_opacity": 0.4
            }
        ).shift(DOWN * 0.2 + LEFT * 1.2)

        x_label = MathTex("x").next_to(plane.x_axis.get_end(), RIGHT)
        y_label = MathTex("y").next_to(plane.y_axis.get_end(), UP)

        self.play(Create(plane), Write(x_label), Write(y_label))
        self.wait(0.5)

        # -----------------------------
        # Start with Ix and Iy values, then turn them into a vector
        # -----------------------------
        ix_value = MathTex(r"I_x = " + str(Ix)).set_color(BLUE)
        iy_value = MathTex(r"I_y = " + str(Iy)).set_color(GREEN)
        given_pair = VGroup(ix_value, iy_value).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        given_pair.next_to(given_text, DOWN, buff=0.4).align_to(given_text, LEFT)

        self.play(Write(given_pair))
        self.wait(0.5)

        result_label = MathTex(
            r"\nabla I = \begin{bmatrix} I_x \\ I_y \end{bmatrix} = \begin{bmatrix}"
            + str(Ix)
            + r" \\ "
            + str(Iy)
            + r"\end{bmatrix}"
        ).set_color(YELLOW)
        result_label.next_to(given_pair, DOWN, buff=0.4).align_to(given_pair, LEFT)

        self.play(Write(result_label))
        self.wait(0.6)

        x_vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(Ix, 0),
            buff=0,
            color=BLUE
        )
        x_vec_label = MathTex("I_x").set_color(BLUE).next_to(x_vec, DOWN)

        y_vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(0, Iy),
            buff=0,
            color=GREEN
        )
        y_vec_label = MathTex("I_y").set_color(GREEN).next_to(y_vec, LEFT)

        # -----------------------------
        # Resultant vector
        # -----------------------------
        result_vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(Ix, Iy),
            buff=0,
            color=YELLOW
        )

        self.play(GrowArrow(result_vec))
        self.wait(0.6)
        self.play(FadeOut(given_pair))
        self.play(result_label.animate.to_edge(UP).shift(DOWN * 0.5))
        self.wait(0.8)

        # -----------------------------
        # Dashed helper lines
        # -----------------------------
        horizontal_helper = DashedLine(
            plane.c2p(0, Iy),
            plane.c2p(Ix, Iy),
            color=GRAY
        )
        vertical_helper = DashedLine(
            plane.c2p(Ix, 0),
            plane.c2p(Ix, Iy),
            color=GRAY
        )

        self.play(Create(horizontal_helper), Create(vertical_helper))
        self.wait(0.5)

        # -----------------------------
        # Move Iy to tip of Ix
        # -----------------------------
        moved_y_vec = Arrow(
            start=plane.c2p(Ix, 0),
            end=plane.c2p(Ix, Iy),
            buff=0,
            color=GREEN
        )
        moved_y_label = MathTex("I_y").set_color(GREEN).next_to(moved_y_vec, RIGHT)

        self.play(GrowArrow(x_vec), Write(x_vec_label))
        self.wait(0.4)
        self.play(GrowArrow(y_vec), Write(y_vec_label))
        self.wait(0.6)
        self.play(
            Transform(y_vec, moved_y_vec),
            Transform(y_vec_label, moved_y_label)
        )
        self.wait(1)

        # -----------------------------
        # Angle theta
        # -----------------------------
        x_base_line = Line(plane.c2p(0, 0), plane.c2p(Ix, 0))
        result_line_for_angle = Line(plane.c2p(0, 0), plane.c2p(Ix, Iy))

        angle_arc = Angle(
            x_base_line,
            result_line_for_angle,
            radius=0.7,
            color=RED
        )
        theta_label = MathTex(r"\theta").set_color(RED).move_to(
            plane.c2p(1.15, 0.45)
        )

        self.play(Create(angle_arc), Write(theta_label))
        self.wait(1)

        # -----------------------------
        # Math explanation
        # -----------------------------
        tan_eq = MathTex(
            r"\tan(\theta) = \frac{I_y}{I_x}"
        ).scale(0.85).move_to(RIGHT * 4 + UP * 2.2)

        substitute_eq = MathTex(
            rf"\tan(\theta) = \frac{{{Iy}}}{{{Ix}}}"
        ).scale(0.85).next_to(tan_eq, DOWN, aligned_edge=LEFT, buff=0.35)

        arctan_eq = MathTex(
            rf"\theta = \arctan\left(\frac{{{Iy}}}{{{Ix}}}\right)"
        ).scale(0.85).next_to(substitute_eq, DOWN, aligned_edge=LEFT, buff=0.35)

        theta_num_eq = MathTex(
            rf"\theta \approx {theta_deg:.2f}^\circ"
        ).scale(0.85).next_to(arctan_eq, DOWN, aligned_edge=LEFT, buff=0.35)

        self.play(Write(tan_eq))
        self.wait(0.7)
        self.play(Write(substitute_eq))
        self.wait(0.7)
        self.play(Write(arctan_eq))
        self.wait(0.7)
        self.play(Write(theta_num_eq))
        self.wait(2)