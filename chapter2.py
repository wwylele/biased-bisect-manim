from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService

from calculate import *
import math


E_SERIESES = g_generate(1000)

class Scene(VoiceoverScene):
    def construct_scene1(self):

        f_text = MathTex(r"F_{s,t}(n) = \min_{ 1\le w\le n-1 }\Big\{\frac{w}{n}(t+F_{s,t}(w)) + \frac{n-w}{n}(s+F_{s,t}(n - w))\Big\}").shift(UP)
        w_text = MathTex(r"w_{s,t}(n) = \{\mbox{The optimal $w$ in $F_{s,t}(n)$}\}").shift(DOWN)
        self.play(Write(f_text))
        self.play(Write(w_text))

        with self.voiceover(text="One intuitive way to study functions is to plot them."):
            pass

        with self.voiceover(text="There are a few problems we probably should address before doing that"):
            p1 = Tex("Domain?", color = YELLOW).scale(0.8).move_to((4, 3, 0))
            p2 = Tex("Codomain?", color = YELLOW).scale(0.8).move_to((-3.6, -1.8, 0))
            p3 = Tex("Continuity?", color = YELLOW).scale(0.8).move_to((4.6, -2.3, 0))
            p4 = Tex("Dimensions?", color = YELLOW).scale(0.8).move_to((-4.8, 3.4, 0))
            self.play(Write(p1))
            self.play(Write(p2))
            self.play(Write(p3))
            self.play(Write(p4))

        with self.voiceover(text="but maybe it is a better idea to jump right into it and resolve problems when we encounter them"):
            self.play(Unwrite(p1))
            self.play(Unwrite(p2))
            self.play(Unwrite(p3))
            self.play(Unwrite(p4))

        with self.voiceover(text="We are interested in how the strategy, represented by the function w, is affected by different time cost"):
            self.play(w_text.animate.set_color(YELLOW).scale(1.1))

        with self.voiceover(text="so here it goes, the plot of function w."):
            self.play(Unwrite(f_text))
            self.play(Unwrite(w_text))

        N = 29
        axes = Axes(x_range=[-1,1], y_range=[0, N, 1], x_length = 10, y_length = 5, axis_config={"include_tip": False})
        axes_hori = MathTex("s:t").move_to(axes.get_corner(RIGHT+DOWN),LEFT).shift(RIGHT* 0.2 + UP * 0.2)
        axes_vert = MathTex("w_{s,t}(", str(N), ")").move_to(axes.get_top(), DOWN).shift(UP * 0.2)
        self.play(Create(axes), Create(axes_hori), Create(axes_vert))


        def plot_w(axes, N):
            vgroup_line = VGroup()
            vgroup_aux = VGroup()
            vgroup_label = VGroup()
            aux_dict = {}
            def add_aux_dict(st, w):
                nonlocal aux_dict
                x = abs(st.get_x())
                if x > 0.8 and x < 1:
                    return

                if st not in aux_dict or aux_dict[st] < w:
                    aux_dict[st] = w

            for w in range(1, N):
                next_search = 0
                while next_search < len(E_SERIESES):

                    try:
                        begin = next(filter(lambda i: E_SERIESES[i].wmin[N] <= w and E_SERIESES[i].wmax[N] >= w,
                                       range(next_search, len(E_SERIESES))))
                    except StopIteration:
                        break
                    try:
                        end = next(filter(lambda i: not(E_SERIESES[i].wmin[N] <= w and E_SERIESES[i].wmax[N] >= w),
                                       range(begin, len(E_SERIESES)))) - 1
                    except StopIteration:
                        end = len(E_SERIESES) - 1
                    next_search = end + 1

                    ebegin, eend = E_SERIESES[begin], E_SERIESES[end]
                    pbegin = axes.coords_to_point(ebegin.get_x(), w)
                    pend = axes.coords_to_point(eend.get_x(), w)
                    vgroup_line.add(Line(pbegin, pend, color=BLUE))
                    dot_radius = 0.04
                    vgroup_line.add(Dot(pbegin, color=BLUE, radius=dot_radius), Dot(pend, color=BLUE, radius=dot_radius))
                    add_aux_dict(ebegin.st, w)
                    add_aux_dict(eend.st, w)

            for st, w in aux_dict.items():
                a = axes.coords_to_point(st.get_x(), 0)
                b = axes.coords_to_point(st.get_x(), w)
                vgroup_label.add(MathTex(f"{st.s}:{st.t}").scale(0.5).move_to(a + DOWN * 0.3).rotate(PI/4))

                if st == ST(1, 1):
                    continue
                vgroup_aux.add(DashedLine(a, b, z_index = -1, color=GREY))

            return vgroup_line, vgroup_aux, vgroup_label

        w_line, w_aux, w_label = plot_w(axes, N)
        self.play(Create(w_line), Create(w_aux), Create(w_label))

        with self.voiceover(text="Ok, this is a very interesting graph, but there are also a lot to address"):
            pass
        with self.voiceover(text="For starters, the function w has three inputs and one out put, how is our graph only two-dimensional?"):
            pass
        with self.voiceover(text="One reason is that I fixed n here to be " + str(N)):
            axes_vert_n = axes_vert.get_part_by_tex(str(N))
            self.play(Circumscribe(axes_vert_n))

        with self.voiceover(text="We can change n to other values, and the graph will change accordingly."):
            axes_vert_prev = axes_vert
            w_line_prev, w_aux_prev, w_label_prev = w_line, w_aux, w_label
            for N_new in list(reversed(range(N - 5, N))) + [N]:
                axes_vert_new = MathTex("w_{s,t}(", str(N_new), ")").move_to(axes_vert.get_center())
                w_line_new, w_aux_new, w_label_new = plot_w(axes, N_new)
                self.play(ReplacementTransform(axes_vert_prev, axes_vert_new),
                          ReplacementTransform(w_line_prev, w_line_new),
                          ReplacementTransform(w_aux_prev, w_aux_new),
                          ReplacementTransform(w_label_prev, w_label_new))
                axes_vert_prev = axes_vert_new
                w_line_prev, w_aux_prev, w_label_prev = w_line_new, w_aux_new, w_label_new
                self.wait(1)

            axes_vert = axes_vert_prev
            w_line, w_aux, w_label = w_line_prev, w_aux_prev, w_label_prev

        with self.voiceover(text="As for s and t, we represent them using a single variable"):
            pass
        with self.voiceover(text="namely the ratio of s to t"):
            self.play(axes_hori.animate.set_color(YELLOW).scale(1.1))

        with self.voiceover(text="This is because it is only the ratio that matters for the optimal strategy"):
            pass
        with self.voiceover(text="In other words, we can show that multiplying s and t by a common factor k will not change the value of function w"):
            w_k = MathTex("w_{ks,kt}(n) = w_{s,t}(n)").move_to((-4, 2, 0))
            self.play(Write(w_k))

        with self.voiceover(text="meanwhile, it will multiply the function F by the same factor k"):
            f_k = MathTex("F_{ks,kt}(n) = kF_{s,t}(n)").move_to(w_k.get_bottom(), UP).shift(DOWN * 0.2)
            self.play(Write(f_k))
        with self.voiceover(text="These can be proven by induction, but we will omit the detail here."):
            pass
        with self.voiceover(text="But even though I said the variable is the ratio of s to t, you can see the horizontal axis is not scaled linearly"):
            self.play(Unwrite(w_k), Unwrite(f_k))

        with self.voiceover(text="In fact, I scaled it using a specific formula"):
            x_axis_left = axes.coords_to_point(-1, 0) + DOWN * 0.7
            x_axis_right = axes.coords_to_point(1, 0) + DOWN * 0.7
            x_axis = Line(x_axis_left, x_axis_right)
            x_form = MathTex(r"x_{s,t}=\frac{s-t}{s+t}", color=YELLOW).scale(0.6).move_to(x_axis.get_right()+RIGHT * 0.2,LEFT)
            x_th = 0.1
            x_th0 = Line(x_axis.get_left() + UP *x_th, x_axis.get_left() + DOWN *x_th)
            x_th1 = Line(x_axis.get_center() + UP *x_th, x_axis.get_center() + DOWN *x_th)
            x_th2 = Line(x_axis.get_right() + UP *x_th, x_axis.get_right() + DOWN *x_th)
            x_th0_t = MathTex("-1").move_to(x_th0.get_center() + DOWN * 0.4)
            x_th1_t = MathTex("0").move_to(x_th1.get_center() + DOWN * 0.4)
            x_th2_t = MathTex("1").move_to(x_th2.get_center() + DOWN * 0.4)
            x_group = VGroup(x_axis, x_th0, x_th1, x_th2, x_form, x_th0_t, x_th1_t, x_th2_t)
            self.play(FadeIn(x_group, shift=DOWN))

        with self.voiceover(text="This formula for x restricts the range of the variable to minus one to one, and is symmetric for s and t"):
            pass

        with self.voiceover(text="if we swap s and t, x takes its inverse value"):
            x_swap = MathTex("x_{t,s} = -x_{s,t}").move_to((-4, 2, 0))
            self.play(Write(x_swap))

        with self.voiceover(text="The reason I do this is because the function w and F are also symmetric for s and t."):
            w_swap = MathTex("w_{t,s}(n) = n-w_{s,t}(n)").move_to(x_swap.get_bottom(), UP).shift(DOWN * 0.2)
            f_swap = MathTex("F_{t,s}(n) = F_{s,t}(n)").move_to(w_swap.get_bottom(), UP).shift(DOWN * 0.2)
            self.play(Write(w_swap))
            self.play(Write(f_swap))

        with self.voiceover(text="This again can be proven by induction, but can also be seen in the graph"):
            pass

        with self.voiceover(text="The plot of w is symmetric about the center point"):
            w_line_clone = w_line.copy()
            self.play(Rotate(w_line_clone, angle=PI, about_point=axes.coords_to_point(0, N/2)), run_time=3)
            self.remove(w_line_clone)

        with self.voiceover(text="The next thing we can notice"):
            self.play(Unwrite(x_swap), Unwrite(w_swap), Unwrite(f_swap), Uncreate(x_group),
                      axes_hori.animate.set_color(WHITE).scale(1 / 1.1))

        with self.voiceover(text="is that for one specific ratio of s to t"):
            ex_s, ex_t = 20, 9
            x = ST(ex_s, ex_t).get_x()
            x_dot = Dot(axes.coords_to_point(x, 0), color = RED)
            self.play(Create(x_dot))
            x_line = DashedLine(axes.coords_to_point(x, 0), axes.coords_to_point(x, N), color = RED)
            self.play(Create(x_line))

        with self.voiceover(text="we can find multiple w value on the graph"):
            ex_e = get_series_at(E_SERIESES, ST(ex_s, ex_t))
            x_wdots = [Dot(axes.coords_to_point(x, w), color = RED) for w in range(ex_e.wmin[N], ex_e.wmax[N] + 1)]
            self.play(*[Create(dot) for dot in x_wdots])
            self.play(*[Flash(dot) for dot in x_wdots])

        with self.voiceover(text="This reveals an inaccurate assumption we implicitly made previously"):
            w_range = MathTex("w_{s,t}(n)", r"\in\mathbb{N}").move_to((-4, 2, 0))
            self.play(Write(w_range))
            pass

        with self.voiceover(text="for a given configuration of n, s and t, the optimal strategy is not necessarily unique."):
            slash_part = w_range.get_part_by_tex(r"\in\mathbb{N}")
            w_range_slash = Line(slash_part.get_corner(LEFT + DOWN), slash_part.get_corner(RIGHT + UP), color = RED)
            self.play(Create(w_range_slash))
            pass

        with self.voiceover(text="To make this precise, we should define w as a function that outputs not a single number, but a set of natural numbers"):
            w_range_new = MathTex("w_{s,t}(n)", r"\subseteq\mathbb{N}").move_to(w_range.get_center())
            self.play(FadeOut(w_range_slash), TransformMatchingTex(w_range, w_range_new))

        with self.voiceover(text="At this point, everything about this plot is well-defined, and it's time to see if we can learn anything new from the plot"):
            self.play(Unwrite(w_range_new), Uncreate(x_dot), Uncreate(x_line), *[Uncreate(dot) for dot in x_wdots])

        with self.voiceover(text="It can be seen that the function w is generally rising with respect to increasing s to t ratio."):
            arrow = Arrow(axes.coords_to_point(-0.8, 10), axes.coords_to_point(0.8, N), color=YELLOW)
            self.play(Create(arrow))

        with self.voiceover(text="A larger s means we spend less time on a failed test, and we want to test newer changes to get more failed tests, so this does match our intuition."):
            pass

        with self.voiceover(text="But we also notice that there are a few outliers that breaks the monotonicity."):
            outliers = []
            for i in range(3, len(E_SERIESES) - 2):
                center = E_SERIESES[i]
                left = E_SERIESES[i - 1]
                right = E_SERIESES[i + 1]
                for w in range(center.wmin[N], center.wmax[N] + 1):
                    if not left.wmin[N] <= w <= left.wmax[N] and not right.wmin[N] <= w <= right.wmax[N]:
                        outliers.append(Circle(0.3).move_to(axes.coords_to_point(center.get_x(), w)))
            self.play(*[Create(o) for o in outliers])
            outlier_text = Text("Outliers", color=RED).move_to((2, -0.5, 0))
            self.play(Write(outlier_text))

        with self.voiceover(text="This hints more complicated structure behind this problem."):
            pass

        with self.voiceover(text="We also see the plot is segmented by some simple ratio of s to t,"):
            self.play(FadeOut(arrow), FadeOut(outlier_text), *[FadeOut(o) for o in outliers])
            self.play(*[l.animate.set_color(YELLOW).scale(1.1) for l in w_label])

        with self.voiceover(text="but there aren't any obvious pattern that can be seen in these numbers."):
            pass

        with self.voiceover(text="This seems to be all we can learn from the plot for now. To see more patterns, perhaps we should change our perspective."):
            self.play(*[l.animate.set_color(WHITE).scale(1/1.1) for l in w_label])
            pass

        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        pass

    def plot_w_dot(self, axes, N, e):
        plots = VGroup()
        for n in range(2, N + 1):
            for w in range(e.wmin[n], e.wmax[n] + 1):
                dot = Dot(axes.coords_to_point(n, w), color=BLUE, radius=0.04)
                plots.add(dot)
        return plots

    def plot_w_para(self, axes, N, e):
        necks = [neck for neck in e.necks if neck < N]
        para_plot = VGroup()
        measures = VGroup()
        measures_n = VGroup()
        measures_w = VGroup()
        n_sequence = [r"\mbox{Span}_n = "]
        w_sequence = [r"\mbox{Height}_w = "]
        for i in range(len(necks) - 1):
            nl = necks[i]
            nr = necks[i + 1]
            wl = e.wmin[nl]
            wr = e.wmax[nr]
            a = axes.coords_to_point(nl, wl)
            b = axes.coords_to_point(nr - (wr- wl), wl)
            c = axes.coords_to_point(nr, wr)
            d = axes.coords_to_point(nl + (wr- wl), wr)
            para_plot.add(Polygon(a,b,c,d,fill_color=DARK_GREY,fill_opacity=1.0,color=GREY))

            measure_stroke = 1.0
            measure_dash = 0.04
            if i == 0:
                measures.add(DashedLine(axes.coords_to_point(nl, wl), axes.coords_to_point(nl, 0) + DOWN * 0.5, stroke_width=measure_stroke, dash_length=measure_dash))
                measures.add(DashedLine(axes.coords_to_point(nl, wl), axes.coords_to_point(0, wl) + LEFT * 0.5, stroke_width=measure_stroke, dash_length=measure_dash))
            measures.add(DashedLine(axes.coords_to_point(nr, wr), axes.coords_to_point(nr, 0) + DOWN * 0.5, stroke_width=measure_stroke, dash_length=measure_dash))
            measures.add(DashedLine(axes.coords_to_point(nl + (wr-wl), wr), axes.coords_to_point(0, wr) + LEFT * 0.5, stroke_width=measure_stroke, dash_length=measure_dash))

            n_span = str(nr-nl)
            measures_n.add(MathTex(n_span).move_to((axes.coords_to_point(nl, 0) + axes.coords_to_point(nr, 0))/2 + DOWN * 0.2, UP).scale(0.6))

            w_height = str(wr-wl)
            shift = LEFT * 0.2
            if wr-wl < 2:
                shift = LEFT * (0.6 + 0.3 *(i % 2))
            measures_w.add(MathTex(w_height).move_to((axes.coords_to_point(0, wl) + axes.coords_to_point(0, wr))/2 + shift, RIGHT).scale(0.6))

            n_sequence += [n_span, ","]
            w_sequence += [w_height, ","]

        n_sequence.append(r"\cdots")
        w_sequence.append(r"\cdots")

        return para_plot, measures, measures_n, measures_w, MathTex(*n_sequence), MathTex(*w_sequence)

    def construct_scene2(self):
        s,t = 1,2
        N = 57
        e = get_series_at(E_SERIESES, ST(s, t))

        with self.voiceover(text="This time, we fix s and t, and let n vary"):
            axes = Axes(x_range=[0,N,5], y_range=[0, N / 2,5], x_length = 10, y_length = 5).shift(DOWN * 0.5)
            axes_hori = MathTex("n").move_to(axes.get_corner(RIGHT+DOWN), LEFT).shift(RIGHT*0.2)
            axes_vert = MathTex(f"w_{{ {s},{t} }}(n)").move_to(axes.get_corner(LEFT+UP), DOWN).shift(UP * 0.2)
            self.play(Create(axes), Write(axes_hori), Write(axes_vert))

        with self.voiceover(text="We plot the function w versus n with s-t ratio of 1 to 2."):
            plots = self.plot_w_dot(axes, N, e)
            self.play(Create(plots), run_time = 4)

        with self.voiceover(text="Because both n and w are integers, our plot is a collection of discrete points."):
            pass

        with self.voiceover(text="But we notice that they form a series of parallelograms."):
            para_plot, measures, measures_n, measures_w, n_sequence, w_sequence = self.plot_w_para(axes, N, e)
            self.play(Create(para_plot))

        with self.voiceover(text="These parallelograms all have vertices of 45 degrees, and are connected with each other at those vertices."):
            n_a = [neck for neck in e.necks if neck < N][-2]
            w_a = e.wmin[n_a]
            neck = axes.coords_to_point(n_a, w_a)
            l1 = Line(neck + LEFT, neck + RIGHT, color = RED)
            l2 = l1.copy().rotate(PI/4,about_point=neck)
            angle = Angle(l1, l2, color=RED)
            value = MathTex(r"45^{\circ}", color=RED).next_to(angle, DOWN)
            self.play(Create(l1), Create(l2), Create(angle), Write(value))

        with self.voiceover(text="Let's measure the span and the hight of these parallelograms"):
            self.play(FadeOut(l1), FadeOut(l2), FadeOut(angle), FadeOut(value))
            self.play(Create(measures), Create(measures_n), Create(measures_w))

        with self.voiceover(text="and collect them together into two sequences."):
            n_sequence.shift(UP * 3)
            w_sequence.shift(UP * 2)
            self.play(TransformMatchingTex(measures_n, n_sequence))
            self.play(TransformMatchingTex(measures_w, w_sequence))

        with self.voiceover(text="Hold on, this looks very familiar. Isn't this the Fibonacci sequence?"):
            pass

        with self.voiceover(text="In this sequence, each number is the sum of two previous numbers."):
            rec = MathTex(r"a_{k} = a_{k-1} + a_{k-2}").shift(UP)
            self.play(Write(rec))
            numbers = [n_sequence.get_part_by_tex(str(n)) for n in [1,2,3,5,8,13,21]]
            prev = None
            for i in range(len(numbers) - 2):
                summer = VGroup()
                brace = Brace(VGroup(numbers[i], numbers[i + 1]), direction= UP, color=YELLOW)
                lb = brace.get_top()
                rb = numbers[i + 2].get_top() + UP * 0.2
                lt = lb + UP * 0.1
                rt = (rb[0], lt[1], 0)
                arrow = VMobject(color=YELLOW).set_points_as_corners([
                    lb, lt, rt, rb
                ])
                tip = VMobject(color=YELLOW).set_points_as_corners([
                    rb + (-0.1, 0.1, 0.0), rb, rb + (0.1, 0.1, 0.0)
                ])
                #arrow.add_tip()
                summer.add(brace)
                summer.add(arrow)
                summer.add(tip)
                if prev is None:
                    self.play(FadeIn(summer), run_time = 0.1)
                else:
                    self.play(FadeOut(prev), FadeIn(summer), run_time = 0.1)
                prev = summer
                self.wait(0.5)
            pass

        with self.voiceover(text="Could this be a coincidence?"):
            self.play(FadeOut(prev))

        with self.voiceover(text="Let's try a different configuration of s and t and see if it has similar patterns"):
            self.play(FadeOut(rec), FadeOut(w_sequence), FadeOut(n_sequence), FadeOut(para_plot), FadeOut(measures))

        with self.voiceover(text="Let's try 2 to 3 as the s-t ratio"):
            s,t = 2,3
            e = get_series_at(E_SERIESES, ST(s, t))
            axes_vert_2 = MathTex(f"w_{{ {s} , {t} }}(n)").move_to(axes_vert.get_center())
            self.play(TransformMatchingTex(axes_vert, axes_vert_2, transform_mismatches=True))
            old_plots = plots
            plots = self.plot_w_dot(axes, N, e)
            self.play(Transform(old_plots, plots))

        with self.voiceover(text="Similarly, we recognize the series of parallelograms"):
            para_plot, measures, measures_n, measures_w, n_sequence, w_sequence = self.plot_w_para(axes, N, e)
            self.play(Create(para_plot))

        with self.voiceover(text="Again, we measure the span and the height of these parallelograms"):
            self.play(Create(measures), Create(measures_n), Create(measures_w))

        with self.voiceover(text="and collect them into sequences"):
            n_sequence.shift(UP * 3)
            w_sequence.shift(UP * 2)
            self.play(TransformMatchingTex(measures_n, n_sequence))
            self.play(TransformMatchingTex(measures_w, w_sequence))

        with self.voiceover(text="This time, it is less obvious what the sequence is. But if we look carefully"):
            pass

        with self.voiceover(text="We'll notice that each number is still the sum of two other numbers"):
            pass

        with self.voiceover(text="But now they are two or three slots a part."):
            rec = MathTex(r"a_{k} = a_{k-2 } + a_{k- 3 }").shift(UP)
            self.play(Write(rec))
            numbers = n_sequence.submobjects
            numbers = [numbers[i] for i in range(len(numbers) - 1) if i % 2 == 1] # HACK
            prev = None
            for i in range(len(numbers) - 3):
                summer = VGroup()
                brace = Brace(VGroup(numbers[i], numbers[i + 1]), direction= UP, color=YELLOW)
                lb = brace.get_top()
                rb = numbers[i + 3].get_top() + UP * 0.2
                lt = lb + UP * 0.1
                rt = (rb[0], lt[1], 0)
                arrow = VMobject(color=YELLOW).set_points_as_corners([
                    lb, lt, rt, rb
                ])
                tip = VMobject(color=YELLOW).set_points_as_corners([
                    rb + (-0.1, 0.1, 0.0), rb, rb + (0.1, 0.1, 0.0)
                ])
                summer.add(brace)
                summer.add(arrow)
                summer.add(tip)
                if prev is None:
                    self.play(FadeIn(summer), run_time = 0.1)
                else:
                    self.play(FadeOut(prev), FadeIn(summer), run_time = 0.1)
                prev = summer
                self.wait(0.5)
            self.play(FadeOut(prev))

        with self.voiceover("We also notice how the number 2 and 3 likely come from the value of s and t"):
            self.play(Transform(axes_vert_2.copy(), rec))
            pass

        with self.voiceover("This hints how different s t configuration affects the strategy w."):
            pass

        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        pass

    def construct_scene3(self):
        with self.voiceover("Based on our observation so far, we can formulate our hypothesis about the optimal strategy"):
            pass

        with self.voiceover("The function w is segmented by some nodes n1, n2, n3, and so on"):
            n1 = MathTex("w_{s,t}(n_1) = ").shift(UP * 3 + LEFT)
            n2 = MathTex("w_{s,t}(n_2) = ").shift(UP * 2 + LEFT)
            n3 = MathTex("w_{s,t}(n_3) = ").shift(UP + LEFT)
            n4 = MathTex(r"\cdots")
            self.play(Write(n1))
            self.play(Write(n2))
            self.play(Write(n3))
            self.play(Write(n4))

        with self.voiceover("Right at each node, the optimal strategy is a single value w1, w2, w3 and so on."):
            w1 = MathTex(r"\{w_1\}").move_to(n1.get_right() + RIGHT * 0.3, LEFT)
            w2 = MathTex(r"\{w_2\}").move_to(n2.get_right() + RIGHT * 0.3, LEFT)
            w3 = MathTex(r"\{w_3\}").move_to(n3.get_right() + RIGHT * 0.3, LEFT)
            self.play(Write(w1))
            self.play(Write(w2))
            self.play(Write(w3))

        with self.voiceover("In each segment between two nodes, a parallelogram forms"):
            wn1 = Tex(r"For $n_i \le n \le n_j$").shift(DOWN)
            wn2 = MathTex(r"w_{s,t}(n) = \{w\in\mathbb{Z} \mid w_i\le w \le w_i + (n-n_i) \land w_j -(n_j - n)\le w\le w_j \}").shift(DOWN * 2).scale(0.8)
            self.play(Write(wn1))
            self.play(Write(wn2))

        with self.voiceover("And lastly, the length and the height of segments form sequences that satisfies a recurrence relation that generalizes Fibonacci sequence"):
            self.play(FadeOut(wn1), FadeOut(wn2))
            a1 = MathTex(r"a_j = n_{j+1} - n_j").shift(DOWN + LEFT * 3)
            b1 = MathTex(r"b_j = w_{j+1} - w_j").shift(DOWN + RIGHT * 3)
            self.play(Write(a1), Write(b1))
            a2 = MathTex(r"a_j = {{a_{j - s} }} + {{a_{j - t} }}").shift(DOWN * 2 + LEFT * 3)
            b2 = MathTex(r"b_j = {{b_{j - s} }} + {{b_{j - t} }}").shift(DOWN * 2 + RIGHT * 3)
            self.play(Write(a2), Write(b2))

        with self.voiceover("But this formula only makes sense for integer s and t"):
            st_int = MathTex(r"{{s, t}}\in\mathbb{Z}", color = YELLOW).shift(DOWN*3)
            self.play(Write(st_int))

        with self.voiceover("We can relax this a bit because we are free to scale s and t by a common factor"):
            st_int2 = MathTex(r"{{ks, kt}}\in\mathbb{Z}", color = YELLOW).shift(DOWN*3)
            self.play(Transform(st_int, st_int2))
            a3 = MathTex(r"a_j = {{a_{j - ks} }} + {{a_{j - kt} }}").shift(DOWN * 2 + LEFT * 3)
            b3 = MathTex(r"b_j = {{b_{j - ks} }} + {{b_{j - kt} }}").shift(DOWN * 2 + RIGHT * 3)
            self.play(Transform(a2, a3), Transform(b2, b3))

        with self.voiceover("And this works out as long as s over t is rational"):
            st_int3 = MathTex(r"s/t\in\mathbb{Q}", color = YELLOW).shift(DOWN*3)
            self.play(Transform(st_int, st_int3))

        with self.voiceover("So what happens if we are given irratonal s and t?"):
            pass

        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def construct_scene4(self):

        s,t = math.sqrt(2),math.sqrt(5)
        k = 10000000000
        s,t = int(k * s), int(k * t)
        N = 57
        e = get_series_at(E_SERIESES, ST(s, t))

        with self.voiceover(text="Let's crank up the irrationality, and use square root of 2 and 5 for s and t"):
            axes = Axes(x_range=[0,N,5], y_range=[0, N / 2,5], x_length = 10, y_length = 5).shift(DOWN * 0.5)
            axes_hori = MathTex("n").move_to(axes.get_corner(RIGHT+DOWN), LEFT).shift(RIGHT*0.2)
            axes_vert = MathTex(r"w_{ \sqrt{2},\sqrt{5} }(n)").move_to(axes.get_corner(LEFT+UP), DOWN).shift(UP * 0.2)
            self.play(Create(axes), Write(axes_hori), Write(axes_vert))

        with self.voiceover(text="We plot the function w like before"):
            plots = self.plot_w_dot(axes, N, e)
            self.play(Create(plots), run_time = 4)

        with self.voiceover(text="It is a little bit harder to see, but we can still find a series of parallelograms"):
            para_plot, measures, measures_n, measures_w, n_sequence, w_sequence = self.plot_w_para(axes, N, e)
            self.play(Create(para_plot))

        with self.voiceover(text="Then we measure their spans and heights"):
            self.play(Create(measures), Create(measures_n), Create(measures_w))

        with self.voiceover(text="and collect them into sequences"):
            n_sequence.shift(UP * 3).scale(0.6)
            w_sequence.shift(UP * 2).scale(0.6)
            self.play(TransformMatchingTex(measures_n, n_sequence))
            self.play(TransformMatchingTex(measures_w, w_sequence))

        with self.voiceover(text="These are just some random looking number without apparent pattern"):
            pass

        with self.voiceover(text="Let's computer more terms for one of them and see if we can find anything"):
            pass

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


        neck_start = MathTex(r"\mbox{Span}_n = ").shift(UP * 3 + LEFT * 5.5)
        self.play(Write(neck_start))
        line_cursor = neck_start.get_right() + RIGHT
        cursor = line_cursor.copy()

        necks = [neck for neck in e.necks if neck < 900]
        neck_all = VGroup()
        for i in range(len(necks) - 1):
            nl = necks[i]
            nr = necks[i + 1]
            neck_all.add(MathTex(int(nr - nl), ",").move_to(cursor, LEFT))
            if i % 10 == 9:
                line_cursor += DOWN * 0.5
                cursor = line_cursor.copy()
            else:
                cursor += RIGHT
        self.play(Write(neck_all, run_time=8))

        with self.voiceover(text="Can you see the pattern?"):
            pass
        self.wait(3)

        with self.voiceover(text="Let's rearrange these numbers a little bit"):
            binos = [(k, n- k) for n in range(1, 12) for k in range(n + 1)]
            binos.sort(key=lambda b: b[0] * s + b[1] * t)
            ani = []
            for i in reversed(range(len(neck_all.submobjects))):
                neck = neck_all.submobjects[i]
                k, nk = binos[i]
                n = k + nk
                ani.append(neck.animate.move_to(UP * 3 + DOWN * n * 0.55 + LEFT * (k - n / 2)))
            self.play(Succession(*ani), run_time=15)

        with self.voiceover(text="We see these are numbers from binomial coefficients, arranged in an unusual way"):
            pass

        with self.voiceover(text="But why is it? How is the binary search problem connected to binomial coefficients, as well as the Fibonacci sequence we previously saw?"):
            pass

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


    def construct(self):

        #self.set_speech_service(AzureService())
        self.set_speech_service(GTTSService())
        self.construct_scene1()
        self.construct_scene2()
        self.construct_scene3()
        self.construct_scene4()

