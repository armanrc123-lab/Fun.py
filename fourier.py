from manim import *
from numpy import *

class Fourier_s(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-2 * pi, 2 * pi],
            y_range=[-50, 50],
            x_length=10,
            y_length=6,
            axis_config={"include_ticks": False, "include_tip": False},
        )

        graph_e = axes.plot(lambda x: (e ** x) / 10, color=BLUE)

        a_0 = (e ** (2 * pi) - e ** (-2 * pi)) / (4 * pi)

        def fourier_series(x, N=1):
            total = a_0 / 10
            for n in range(1, N + 1):
                a_n = (2 * (-1) ** n / (pi * (4 + n ** 2))) * (e ** (2 * pi) - e ** (-2 * pi))
                b_n = (n * (-1) ** n / (pi * (4 + n ** 2))) * (e ** (-2 * pi) - e ** (2 * pi))
                total += (a_n * cos(n * x / 2) + b_n * sin(n * x / 2)) / 10
            return total

        self.add(axes, graph_e)

        total_steps = 50
        graphs = []

        for N in range(1, total_steps + 1):
            color = interpolate_color(RED, BLUE, N / total_steps)
            graph = axes.plot(lambda x, N=N: fourier_series(x, N), color=color)
            graphs.append(graph)

        current_graph = graphs[0]
        self.play(Create(current_graph), run_time=3)

        for i in range(1, len(graphs)):
            new_graph = graphs[i]
            self.play(ReplacementTransform(current_graph, new_graph), run_time= 1 / sqrt(i))
            current_graph = new_graph

        
        self.play(Transform(current_graph, graph_e))

        

        self.wait(5)





#manim fourier.py Fourier_s -pqm