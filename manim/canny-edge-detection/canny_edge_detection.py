from manim import *
import numpy as np


config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 16
config.frame_height = 9


class GradientVectorExplanation(Scene):
    def construct(self):
        Ix = 4
        Iy = 3
        theta_deg = np.degrees(np.arctan2(Iy, Ix))

        given_text = MathTex(
            r"I_x = " + str(Ix),
            r"\quad",
            r"I_y = " + str(Iy),
        ).scale(0.9).to_edge(UP, buff=0.35)

        plane = NumberPlane(
            x_range=[-1, 6, 1],
            y_range=[-1, 5, 1],
            x_length=7.0,
            y_length=5.5,
            background_line_style={"stroke_opacity": 0.4},
        ).to_edge(LEFT, buff=0.6).shift(DOWN * 0.35)

        x_label = MathTex("x").scale(0.85).next_to(plane.x_axis.get_end(), RIGHT, buff=0.15)
        y_label = MathTex("y").scale(0.85).next_to(plane.y_axis.get_end(), UP, buff=0.15)

        ix_value = MathTex(r"I_x = " + str(Ix), color=BLUE)
        iy_value = MathTex(r"I_y = " + str(Iy), color=GREEN)
        given_pair = VGroup(ix_value, iy_value).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        given_pair.to_edge(RIGHT, buff=0.8).shift(UP * 1.0)

        result_label = MathTex(
            r"\nabla I = \begin{bmatrix} I_x \\ I_y \end{bmatrix}"
            + r" = \begin{bmatrix}"
            + str(Ix)
            + r" \\ "
            + str(Iy)
            + r"\end{bmatrix}"
        ).set_color(YELLOW).scale(0.9)
        result_label.next_to(given_pair, DOWN, aligned_edge=LEFT, buff=0.45)

        self.play(Write(given_text))
        self.play(Create(plane), Write(x_label), Write(y_label))
        self.play(Write(given_pair))
        self.wait(0.4)
        self.play(Write(result_label))
        self.wait(0.5)

        x_vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(Ix, 0),
            buff=0,
            color=BLUE,
        )
        x_vec_label = MathTex("I_x").set_color(BLUE).next_to(x_vec, DOWN, buff=0.15)

        y_vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(0, Iy),
            buff=0,
            color=GREEN,
        )
        y_vec_label = MathTex("I_y").set_color(GREEN).next_to(y_vec, LEFT, buff=0.12)

        result_vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(Ix, Iy),
            buff=0,
            color=YELLOW,
        )

        self.play(GrowArrow(result_vec))
        self.wait(0.4)

        horizontal_helper = DashedLine(
            plane.c2p(0, Iy),
            plane.c2p(Ix, Iy),
            color=GRAY,
        )
        vertical_helper = DashedLine(
            plane.c2p(Ix, 0),
            plane.c2p(Ix, Iy),
            color=GRAY,
        )

        self.play(Create(horizontal_helper), Create(vertical_helper))
        self.wait(0.4)

        moved_y_vec = Arrow(
            start=plane.c2p(Ix, 0),
            end=plane.c2p(Ix, Iy),
            buff=0,
            color=GREEN,
        )
        moved_y_label = MathTex("I_y").set_color(GREEN).next_to(moved_y_vec, RIGHT, buff=0.12)

        self.play(GrowArrow(x_vec), Write(x_vec_label))
        self.wait(0.3)
        self.play(GrowArrow(y_vec), Write(y_vec_label))
        self.wait(0.4)
        self.play(Transform(y_vec, moved_y_vec), Transform(y_vec_label, moved_y_label))
        self.wait(0.7)

        self.play(FadeOut(given_pair))
        self.play(result_label.animate.to_corner(UR, buff=0.6).shift(DOWN * 0.35))
        self.wait(0.5)

        x_base_line = Line(plane.c2p(0, 0), plane.c2p(Ix, 0))
        result_line_for_angle = Line(plane.c2p(0, 0), plane.c2p(Ix, Iy))

        angle_arc = Angle(
            x_base_line,
            result_line_for_angle,
            radius=0.7,
            color=RED,
        )
        theta_label = MathTex(r"\theta").set_color(RED).move_to(plane.c2p(1.15, 0.45))

        self.play(Create(angle_arc), Write(theta_label))
        self.wait(0.7)

        equations = VGroup(
            MathTex(r"\tan(\theta) = \frac{I_y}{I_x}"),
            MathTex(rf"\tan(\theta) = \frac{{{Iy}}}{{{Ix}}}"),
            MathTex(rf"\theta = \arctan\left(\frac{{{Iy}}}{{{Ix}}}\right)"),
            MathTex(rf"\theta \approx {theta_deg:.2f}^\circ"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.28).scale(0.74)
        equations.next_to(result_label, DOWN, aligned_edge=LEFT, buff=0.45)

        self.play(Write(equations[0]))
        self.wait(0.5)
        self.play(Write(equations[1]))
        self.wait(0.5)
        self.play(Write(equations[2]))
        self.wait(0.5)
        self.play(Write(equations[3]))
        self.wait(1.5)


class NMSPatch45(Scene):
    def construct(self):
        values = [
            [0, 0, 2, 4, 7],
            [0, 2, 4, 7, 4],
            [2, 4, 9, 4, 2],
            [4, 7, 4, 2, 0],
            [7, 4, 2, 0, 0],
        ]

        title = Text("Non-Maximum Suppression at One Pixel", font_size=32).to_edge(UP, buff=0.3)

        table = MathTable(
            [[str(v) for v in row] for row in values],
            include_outer_lines=True,
        ).scale(0.62).to_edge(LEFT, buff=0.55).shift(UP * 0.2)

        center_cell = table.get_highlighted_cell((3, 3), color=YELLOW)
        center_entry = table.get_entries((3, 3))

        center_label = Text("Current pixel", font_size=24, color=YELLOW)
        center_label.next_to(table, DOWN, buff=0.2)

        plane = NumberPlane(
            x_range=[-1, 5, 1],
            y_range=[-1, 5, 1],
            x_length=3.8,
            y_length=3.8,
            background_line_style={"stroke_opacity": 0.35},
        ).to_edge(RIGHT, buff=0.7).shift(UP * 0.2)

        x_label = MathTex("I_x").scale(0.8).next_to(plane.x_axis.get_end(), RIGHT, buff=0.12)
        y_label = MathTex("I_y").scale(0.8).next_to(plane.y_axis.get_end(), UP, buff=0.12)

        Ix = 4
        Iy = 4
        theta = np.degrees(np.arctan2(Iy, Ix))

        grad_text = MathTex(
            r"\nabla I = \begin{bmatrix} I_x \\ I_y \end{bmatrix}"
            r" = \begin{bmatrix} 4 \\ 4 \end{bmatrix}"
        ).scale(0.72)
        grad_text.next_to(plane, UP, buff=0.25)

        vec = Arrow(
            start=plane.c2p(0, 0),
            end=plane.c2p(Ix, Iy),
            buff=0,
            color=BLUE,
        )

        x_base = Line(plane.c2p(0, 0), plane.c2p(2.2, 0))
        diag_line = Line(plane.c2p(0, 0), plane.c2p(2.2, 2.2))
        angle_arc = Angle(x_base, diag_line, radius=0.5, color=RED)
        theta_label = MathTex(rf"\theta = {theta:.0f}^\circ", color=RED).scale(0.72)
        theta_label.move_to(plane.c2p(1.3, 0.42))

        quant_text = VGroup(
            MathTex(r"\theta = \arctan(4/4) = 45^\circ"),
            MathTex(r"45^\circ \;\rightarrow\; \text{45-degree direction bin}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).scale(0.62)
        quant_text.next_to(plane, DOWN, buff=0.28)
        quant_text.align_to(plane, LEFT).shift(LEFT * 0.45)

        nbr1_cell = table.get_highlighted_cell((2, 4), color=GREEN)
        nbr2_cell = table.get_highlighted_cell((4, 2), color=GREEN)
        nbr1_entry = table.get_entries((2, 4))
        nbr2_entry = table.get_entries((4, 2))

        compare_text = VGroup(
            Tex(r"For $45^\circ$, compare the two neighbors on that diagonal."),
            MathTex(r"\text{center} = 9,\quad \text{top-right} = 7,\quad \text{bottom-left} = 7"),
            MathTex(r"9 \ge 7 \text{ and } 9 \ge 7 \Rightarrow \text{ keep the center pixel}"),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.22).scale(0.6)
        compare_text.set(width=14.0)
        compare_text.to_edge(DOWN, buff=0.25)

        self.play(Write(title))
        self.play(Create(table))
        self.wait(0.4)
        self.play(FadeIn(center_cell), Indicate(center_entry), Write(center_label))
        self.wait(0.5)

        self.play(Create(plane), Write(x_label), Write(y_label))
        self.play(Write(grad_text))
        self.play(GrowArrow(vec))
        self.play(Create(angle_arc), Write(theta_label))
        self.wait(0.5)

        self.play(Write(quant_text[0]))
        self.wait(0.4)
        self.play(Write(quant_text[1]))
        self.wait(0.6)
        self.play(
            FadeOut(angle_arc),
            FadeOut(theta_label),
            FadeOut(quant_text),
            vec.animate.set_stroke(opacity=0.25),
        )
        self.wait(0.3)

        self.play(FadeIn(nbr1_cell), FadeIn(nbr2_cell))
        self.play(Indicate(nbr1_entry), Indicate(nbr2_entry))
        self.wait(0.4)

        self.play(FadeOut(center_label))
        self.play(Write(compare_text[0]))
        self.wait(0.4)
        self.play(Write(compare_text[1]))
        self.wait(0.5)
        self.play(Write(compare_text[2]))
        self.wait(0.9)

        keep_box = table.get_highlighted_cell((3, 3), color=BLUE)
        self.play(ReplacementTransform(center_cell, keep_box))
        self.wait(1.2)
