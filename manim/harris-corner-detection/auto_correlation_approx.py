from manim import *


config.pixel_width = 1920
config.pixel_height = 1080
config.frame_width = 16
config.frame_height = 9


class MainScene(Scene):
    def construct(self):
        # Title position: increase/decrease `buff` to move it slightly down/up.
        title = Text("Auto-Correlation Function", font_size=40).to_edge(UP, buff=0.6)

        # Top equation.
        # Change `.shift(UP * 1.0)` if you want the whole top line higher or lower.
        formula = MathTex(
            r"E(u,v)",
            r"=",
            r"\sum_{x,y}",
            r"\left[",
            r"I(x+u,y+v)",
            r"-",
            r"I(x,y)",
            r"\right]^2",
        ).scale(1.0).shift(UP * 2.0)

        # Second line: Taylor approximation.
        # Change `buff=0.45` to control the gap between the top line and this one.
        approximation = MathTex(
            r"I(x+u,y+v)",
            r"\approx",
            r"I(x,y)",
            r"+",
            r"u\,\frac{\partial I}{\partial x}",
            r"+",
            r"v\,\frac{\partial I}{\partial y}",
        ).scale(1.0)
        approximation.next_to(formula, DOWN, buff=0.45)

        approximation_rest = VGroup(*approximation[1:])

        taylor_label = Text(
            "Taylor expansion",
            font_size=28,
        )
        taylor_label.next_to(approximation, RIGHT, buff=0.45)

        # Same equation, but rewritten using Ix and Iy notation.
        shorthand = MathTex(
            r"I(x+u,y+v)",
            r"\approx",
            r"I(x,y)",
            r"+",
            r"u\,I_x",
            r"+",
            r"v\,I_y",
        ).scale(1.0)
        shorthand.move_to(approximation)
        shorthand_lhs = VGroup(shorthand[0], shorthand[1])
        shorthand_rhs = VGroup(*shorthand[2:])

        # This is the "opened" summation with a fake blank slot inside the brackets.
        # The blank slot is controlled by the `\phantom{...}` text below.
        # To make more room before the `- I(x,y)` term, add more content inside
        # `\phantom{...}` or add extra spacing commands like `\quad` / `\qquad`.
        # To make less room, remove some of that phantom content.
        opened_formula = MathTex(
            r"E(u,v)",
            r"=",
            r"\sum_{x,y}",
            r"\left[",
            r"\phantom{I(x,y) + u\,I_x + v\,I_y }",
            r"-",
            r"I(x,y)",
            r"\right]^2",
        ).scale(1.0)
        opened_formula.move_to(formula)

        # This controls where the moved-up RHS lands inside the summation.
        # Increase/decrease `buff` to move the inserted expression right/left.
        inserted_expression = MathTex(
            r"I(x,y)",
            r"+",
            r"u\,I_x",
            r"+",
            r"v\,I_y",
        ).scale(1.0)
        inserted_expression.next_to(opened_formula[3], RIGHT, buff=0.30)

        # Final simplified form after the matching I(x,y) terms drop out.
        simplified_formula = MathTex(
            r"E(u,v)",
            r"=",
            r"\sum_{x,y}",
            r"\left[",
            r"u\,I_x",
            r"+",
            r"v\,I_y",
            r"\right]^2",
        ).scale(1.0)
        simplified_formula.next_to(formula, DOWN, buff=0.7)

        expanded_square_formula = MathTex(
            r"E(u,v)",
            r"=",
            r"\sum_{x,y}",
            r"\left(",
            r"u^2 I_x^2",
            r"+",
            r"2uv\,I_x I_y",
            r"+",
            r"v^2 I_y^2",
            r"\right)",
        ).scale(0.95)
        expanded_square_formula.next_to(simplified_formula, DOWN, buff=0.55)

        separated_sums_formula = MathTex(
            r"E(u,v)",
            r"=",
            r"u^2 \sum_{x,y} I_x^2",
            r"+",
            r"2uv \sum_{x,y} I_x I_y",
            r"+",
            r"v^2 \sum_{x,y} I_y^2",
        ).scale(0.9)
        separated_sums_formula.next_to(expanded_square_formula, DOWN, buff=0.55)

        final_separated_sums_formula = MathTex(
            r"E(u,v)",
            r"=",
            r"u^2 \sum_{x,y} I_x^2",
            r"+",
            r"2uv \sum_{x,y} I_x I_y",
            r"+",
            r"v^2 \sum_{x,y} I_y^2",
        ).scale(0.9)
        final_separated_sums_formula.move_to(formula)

        why_correct = Text(
            "Where did this matrix even come from?",
            font_size=30,
        )
        solve_text = Text(
            "Let's solve it out.",
            font_size=30,
        )
        quadratic_form_top = MathTex(
            r"E(u,v)",
            r"=",
            r"\begin{bmatrix} u & v \end{bmatrix}",
            r"\begin{bmatrix} \sum_{x,y} I_x^2 & \sum_{x,y} I_x I_y \\ \sum_{x,y} I_x I_y & \sum_{x,y} I_y^2 \end{bmatrix}",
            r"\begin{bmatrix} u \\ v \end{bmatrix}",
        ).scale(0.64)
        quadratic_form_top.move_to(final_separated_sums_formula)

        quadratic_form_line = MathTex(
            r"E(u,v)",
            r"=",
            r"\begin{bmatrix} u & v \end{bmatrix}",
            r"\begin{bmatrix} \sum_{x,y} I_x^2 & \sum_{x,y} I_x I_y \\ \sum_{x,y} I_x I_y & \sum_{x,y} I_y^2 \end{bmatrix}",
            r"\begin{bmatrix} u \\ v \end{bmatrix}",
        ).scale(0.64)
        quadratic_form_line.next_to(final_separated_sums_formula, DOWN, buff=0.75)
        why_correct.next_to(quadratic_form_line, DOWN, buff=0.55)
        solve_text.next_to(why_correct, DOWN, buff=0.4)

        matrix_vector_line = MathTex(
            r"E(u,v)",
            r"=",
            r"\begin{bmatrix} u & v \end{bmatrix}",
            r"\begin{bmatrix} u \sum_{x,y} I_x^2 + v \sum_{x,y} I_x I_y \\ u \sum_{x,y} I_x I_y + v \sum_{x,y} I_y^2 \end{bmatrix}",
        ).scale(0.60)
        matrix_vector_line.next_to(quadratic_form_top, DOWN, buff=0.45)

        row_vector_line = MathTex(
            r"E(u,v)",
            r"=",
            r"u\left(u \sum_{x,y} I_x^2 + v \sum_{x,y} I_x I_y\right) + v\left(u \sum_{x,y} I_x I_y + v \sum_{x,y} I_y^2\right)",
        ).scale(0.60)
        row_vector_line.next_to(matrix_vector_line, DOWN, buff=0.45)

        expanded_match_line = MathTex(
            r"E(u,v)",
            r"=",
            r"u^2 \sum_{x,y} I_x^2 + uv \sum_{x,y} I_x I_y + uv \sum_{x,y} I_x I_y + v^2 \sum_{x,y} I_y^2",
        ).scale(0.63)
        expanded_match_line.next_to(row_vector_line, DOWN, buff=0.45)

        collected_match_line = MathTex(
            r"E(u,v)",
            r"=",
            r"u^2 \sum_{x,y} I_x^2 + 2uv \sum_{x,y} I_x I_y + v^2 \sum_{x,y} I_y^2",
        ).scale(0.63)
        collected_match_line.next_to(expanded_match_line, DOWN, buff=0.45)

        matrix_check = Text("✓", font_size=36, color=GREEN)
        matrix_check.next_to(collected_match_line, RIGHT, buff=0.35)

        matrix_definition = MathTex(
            r"M",
            r"=",
            r"\begin{bmatrix} \sum_{x,y} I_x^2 & \sum_{x,y} I_x I_y \\ \sum_{x,y} I_x I_y & \sum_{x,y} I_y^2 \end{bmatrix}",
        ).scale(0.82)
        matrix_definition.next_to(quadratic_form_top, DOWN, buff=0.8)

        done_text = Text("That's it!", font_size=32)
        done_text.next_to(matrix_definition, DOWN, buff=0.55)

        # Temporary top-right note explaining the notation change.
        notation_note = Text(
            "* notation change",
            font_size=24,
        ).to_corner(UR, buff=0.45)

        # Timing notes:
        # Larger `run_time` = slower animation.
        # Smaller `run_time` = faster animation.
        self.play(Write(title), run_time=1.1)
        self.wait(0.7)
        self.play(Write(formula), run_time=2.15)
        self.wait(1.6)
        self.play(
            TransformFromCopy(formula[4], approximation[0]),
            FadeIn(taylor_label),
            run_time=1.0,
        )
        self.play(
            Write(approximation_rest),
            run_time=1.05,
        )
        self.play(
            TransformMatchingTex(approximation, shorthand),
            FadeIn(notation_note),
            FadeOut(taylor_label),
            run_time=1.1,
        )
        self.wait(1.6)
        self.play(FadeOut(notation_note), run_time=0.45)
        self.play(
            TransformMatchingTex(formula, opened_formula, path_arc=0),
            run_time=0.95,
        )
        # This is the main "move the approximation into the summation" step.
        # If it lands wrong, tweak `inserted_expression.next_to(...)` above.
        self.play(
            FadeOut(shorthand_lhs),
            shorthand_rhs.animate.move_to(inserted_expression),
            run_time=1.2,
        )
        self.play(Write(simplified_formula), run_time=1.2)
        self.wait(0.9)
        self.play(Write(expanded_square_formula), run_time=1.35)
        self.wait(0.9)
        self.play(Write(separated_sums_formula), run_time=1.35)
        self.wait(1.0)
        self.play(
            FadeOut(VGroup(opened_formula, shorthand_rhs, simplified_formula, expanded_square_formula)),
            TransformMatchingTex(separated_sums_formula, final_separated_sums_formula),
            run_time=1.2,
        )
        self.wait(0.8)
        self.play(Write(quadratic_form_line), run_time=1.15)
        self.wait(0.8)
        self.play(Write(why_correct), run_time=0.9)
        self.wait(0.8)
        self.play(Write(solve_text), run_time=0.8)
        self.wait(0.9)
        self.play(
            FadeOut(why_correct),
            FadeOut(solve_text),
            FadeOut(final_separated_sums_formula),
            TransformMatchingTex(quadratic_form_line, quadratic_form_top),
            run_time=1.0,
        )
        self.remove(quadratic_form_line)
        self.wait(0.9)
        self.play(Write(matrix_vector_line), run_time=1.15)
        self.wait(0.8)
        self.play(Write(row_vector_line), run_time=1.15)
        self.wait(0.8)
        self.play(Write(expanded_match_line), run_time=1.1)
        self.wait(0.8)
        self.play(Write(collected_match_line), run_time=1.0)
        self.play(FadeIn(matrix_check), run_time=0.4)
        self.wait(1.0)
        self.play(
            FadeOut(
                VGroup(
                    matrix_vector_line,
                    row_vector_line,
                    expanded_match_line,
                    collected_match_line,
                    matrix_check,
                )
            ),
            Write(matrix_definition),
            run_time=1.0,
        )
        self.wait(0.8)
        self.play(Write(done_text), run_time=0.7)
        self.wait(1.6)
