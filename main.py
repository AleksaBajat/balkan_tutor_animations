from manim import *
import numpy as np


class FirstScene(Scene):
    def construct(self):
        # Show the quadratic equation

        qd_equation = MathTex(r"y = ax^2 + bx + c")
        qd_equation.font_size = 128.0

        self.play(Create(qd_equation))
        self.wait(2)

        # Highlight the coefficients

        qd_equation_spoiler = MathTex(
            r"y = ax^2 + bx + c", substrings_to_isolate=["a", "b", "c"]
        )
        qd_equation_spoiler.font_size = 128.0

        qd_equation_spoiler.set_color_by_tex("a", GREEN)

        self.play(Transform(qd_equation, qd_equation_spoiler))
        self.wait(2)

        # Happy and Sad parabola

        # Clear the screen
        self.play(FadeOut(qd_equation))

        # Create axes for parabola demonstration
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(-3, 4, 1)},
            y_axis_config={"numbers_to_include": np.arange(-3, 4, 1)},
        )

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        self.play(Create(axes), Write(axes_labels))

        # Happy parabola (a > 0)

        happy_parabola = axes.plot(lambda x: 0.5 * x**2, color=GREEN, x_range=[-3, 3])
        happy_label = MathTex(r"a > 0", color=GREEN, font_size=36)
        happy_label.next_to(axes, LEFT, buff=1).shift(UP)

        happy_text = Text("Srećna! 😊", color=GREEN, font_size=32)
        happy_text.next_to(happy_label, DOWN)

        self.play(Create(happy_parabola), Write(happy_label), Write(happy_text))
        self.wait(2)

        # Sad parabola (a < 0)
        sad_parabola = axes.plot(lambda x: -0.5 * x**2, color=RED, x_range=[-3, 3])
        sad_label = MathTex(r"a < 0", color=RED, font_size=36)
        sad_label.next_to(axes, RIGHT, buff=1).shift(UP)

        sad_text = Text("Tužna! 😢", color=RED, font_size=32)
        sad_text.next_to(sad_label, DOWN)

        self.play(Create(sad_parabola), Write(sad_label), Write(sad_text))
        self.wait(2)

        # Clear everything for the next section
        self.play(
            FadeOut(axes),
            FadeOut(axes_labels),
            FadeOut(happy_parabola),
            FadeOut(sad_parabola),
            FadeOut(happy_label),
            FadeOut(sad_label),
            FadeOut(happy_text),
            FadeOut(sad_text),
        )

        qd_equation_spoiler = MathTex(
            r"y = ax^2 + bx + c", substrings_to_isolate=["a", "b", "c"]
        )
        qd_equation_spoiler.font_size = 128.0

        qd_equation_spoiler.set_color_by_tex("a", GREEN)
        qd_equation_spoiler.set_color_by_tex("b", YELLOW)
        qd_equation_spoiler.set_color_by_tex("c", RED)

        self.play(Create(qd_equation_spoiler))
        self.wait(2)

        qd_solution = MathTex(r"\frac{-b \pm \sqrt{b^2 - 4ac}}{2a}")
        qd_solution.font_size = 128.0

        qd_solution.next_to(qd_equation_spoiler, DOWN, 2.5)

        # for part in qd_solution:
        #     self.add(index_labels(part, color=YELLOW))

        # self.add(index_labels(qd_solution, color=RED))

        qd_solution[0][9].set_fill(GREEN)
        qd_solution[0][13].set_fill(GREEN)
        qd_solution[0][1].set_fill(YELLOW)
        qd_solution[0][5].set_fill(YELLOW)
        qd_solution[0][10].set_fill(RED)

        self.play(Create(qd_solution))
        self.wait(2)
        self.play(FadeOut(qd_equation_spoiler), qd_solution.animate.move_to(ORIGIN))
        self.wait(2)

        qd_solution_2 = qd_solution.set_fill(WHITE)
        self.remove(qd_solution)
        self.add(qd_solution_2)

        qd_solution_3 = qd_solution_2
        qd_solution_3[0][5].set_fill(YELLOW)
        qd_solution_3[0][6].set_fill(YELLOW)
        qd_solution_3[0][7].set_fill(YELLOW)
        qd_solution_3[0][8].set_fill(YELLOW)
        qd_solution_3[0][9].set_fill(YELLOW)
        qd_solution_3[0][10].set_fill(YELLOW)

        self.play(Transform(qd_solution_2, qd_solution_3))
        self.wait(2)

        discriminant = MathTex("D = b^2 - 4ac")
        discriminant.font_size = 128.0

        self.play(Transform(qd_solution_2, discriminant))
        self.wait(2)

        discriminant_types = MathTex(r"D > 0 \\ D = 0 \\ D < 0")
        discriminant_types.font_size = 128.0

        self.play(Transform(qd_solution_2, discriminant_types))
        self.wait(2)

        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-11, 10, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE},
            x_axis_config={"numbers_to_include": np.arange(-5, 6, 1)},
            y_axis_config={"numbers_to_include": np.arange(-11, 11, 2)},
        )

        axes_labels = axes.get_axis_labels(x_label="x", y_label="y")

        def create_quadratic(a, b, c):
            return lambda x: a * x**2 + b * x + c

        graph = axes.plot(create_quadratic(4, 4, 1), color=GREEN, x_range=[-7, 7])

        equation_label = MathTex(r"y = 4x^2 + 4x + 1")
        equation_label.next_to(axes, UP, 2)
        equation_label.to_edge()

        calculation = MathTex("D = 4^2 - 4 * 4 * 1 = 16 - 16 = 0")
        calculation.next_to(equation_label, DOWN)
        calculation.font_size = 32.0
        calculation.to_edge()

        self.remove(qd_solution_2)
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(equation_label), Write(calculation))
        self.wait(2)

        graph_2 = axes.plot(create_quadratic(-4, -4, -1), color=RED, x_range=[-7, 7])

        equation_label_2 = MathTex(r"y = -4x^2 - 4x - 1")
        equation_label_2.next_to(axes, DOWN, 2)
        equation_label_2.to_edge()

        calculation_2 = MathTex("D = (-4)^2 - 4 * (-4) * (-1) = 16 - 16 = 0")
        calculation_2.next_to(equation_label_2, DOWN)
        calculation_2.font_size = 32.0
        calculation_2.to_edge()

        self.play(Create(graph_2), Write(equation_label_2), Write(calculation_2))
        self.wait(2)
        self.remove(
            graph, graph_2, equation_label, equation_label_2, calculation, calculation_2
        )

        graph = axes.plot(create_quadratic(1, -4, 3), color=GREEN, x_range=[-3, 7])

        equation_label = MathTex(r"y = x^2 - 4x + 3")
        equation_label.next_to(axes, UP, 2)
        equation_label.to_edge()

        calculation = MathTex("D = (-4)^2 - 4 * 1 * 3 = 16 - 12 = 4")
        calculation.next_to(equation_label, DOWN)
        calculation.font_size = 32.0
        calculation.to_edge()

        self.play(Create(graph), Write(equation_label), Write(calculation))
        self.wait(2)

        graph_2 = axes.plot(create_quadratic(-1, 4, -3), color=RED, x_range=[-3, 7])

        equation_label_2 = MathTex(r"y = -x^2 + 4x - 3")
        equation_label_2.next_to(axes, DOWN, 2)
        equation_label_2.to_edge()

        calculation_2 = MathTex("D = 4^2 - 4 * (-1) * (-3) = 16 - 12 = 4")
        calculation_2.next_to(equation_label_2, DOWN)
        calculation_2.font_size = 32.0
        calculation_2.to_edge()

        self.play(Create(graph_2), Write(equation_label_2), Write(calculation_2))
        self.wait(2)
        self.remove(
            graph, graph_2, equation_label, equation_label_2, calculation, calculation_2
        )

        graph = axes.plot(create_quadratic(3, -6, 4), color=GREEN, x_range=[-3, 7])

        equation_label = MathTex(r"y = 3x^2 - 6x + 4")
        equation_label.next_to(axes, UP, 2)
        equation_label.to_edge()

        calculation = MathTex("D = (-6)^2 - 4 * 3 * 4 = 36 - 48 = -12")
        calculation.next_to(equation_label, DOWN)
        calculation.font_size = 32.0
        calculation.to_edge()

        self.play(Create(graph), Write(equation_label), Write(calculation))
        self.wait(2)

        graph_2 = axes.plot(create_quadratic(-3, 6, -4), color=RED, x_range=[-3, 7])

        equation_label_2 = MathTex(r"y = -3x^2 + 6x - 4")
        equation_label_2.next_to(axes, DOWN, 2)
        equation_label_2.to_edge()

        calculation_2 = MathTex("D = 6^2 - 4 * (-3) * (-4) = 36 - 48 = -12")
        calculation_2.next_to(equation_label_2, DOWN)
        calculation_2.font_size = 32.0
        calculation_2.to_edge()

        self.play(Create(graph_2), Write(equation_label_2), Write(calculation_2))
        self.wait(2)

        self.remove(
            graph_2,
            equation_label_2,
            graph,
            equation_label,
            calculation_2,
            calculation,
            axes,
            axes_labels,
        )

        qd_equation_spoiler = MathTex(
            r"y = ax^2 + bx + c", substrings_to_isolate=["a", "b", "c"]
        )
        qd_equation_spoiler.font_size = 128.0

        qd_equation_spoiler.set_color_by_tex("c", RED)

        self.play(FadeIn(qd_equation_spoiler))
        self.wait(2)

        self.wait(3)
