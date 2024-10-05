from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService
import scipy.special
import numpy.linalg
import itertools

from calculate import *
import math
import scipy

E_SERIESES = g_generate(100)

class Scene(VoiceoverScene):
    def construct_scene1(self):
        f_text = MathTex(r"{{F_{s,t}(n)}} = {{ \min_{ 1\le w\le n-1 } }} \Big\{ { {{w}} \over {{n\phantom{} }} } {{(t+F_{s,t}(w))}} {{+}} { {{n-w}} \over {{n\phantom{} }} } {{(s+F_{s,t}(n - w))}}\Big\}").shift(UP)
        w_text = MathTex(r"w_{s,t}(n) = \{\mbox{The optimal $w$ in $F_{s,t}(n)$}\}").shift(DOWN)
        self.play(FadeIn(f_text), FadeIn(w_text))

        with self.voiceover(text="To find the answer, let's look at the other function F"):
            self.play(FadeOut(w_text), f_text.animate.shift(DOWN))

        with self.voiceover(text="We notice the right-hand side has a common denominator n"):
            [n1, n2] = f_text.get_parts_by_tex(r"n\phantom{}")
            self.play(n1.animate.set_color(YELLOW), n2.animate.set_color(YELLOW))

        with self.voiceover(text="So let's move them to the left"):
            f_text2 = MathTex(
                r"{{n\phantom{} }} {{F_{s,t}(n)}} = {{ \min_{ 1\le w\le n-1 } }} \Big\{ {{w}} {{(t+F_{s,t}(w))}} {{+}} ({{n-w}}) {{(s+F_{s,t}(n - w))}}\Big\}"
            ).move_to(f_text)
            self.play(TransformMatchingTex(f_text, f_text2))
            self.remove(f_text2)
            f_text = MathTex(
                r"n F_{s,t}(n) = {{ \min_{ 1\le w\le n-1 } }} \Big\{ {{w}} ({{t}}+{{F_{s,t}(w)}}) {{+}} {{(n-w)}} ({{s}}+{{F_{s,t}(n - w)}})\Big\}"
            ).move_to(f_text2)
            self.add(f_text)

        with self.voiceover(text="Also expand the right-hand side"):
            f_text2 = MathTex(
                r"n F_{s,t}(n) = {{ \min_{ 1\le w\le n-1 } }} \Big\{ {{w}} {{t}}+ {{w}} {{F_{s,t}(w)}} {{+}} {{(n-w)}} {{s}} + {{(n-w)}} {{F_{s,t}(n - w)}}\Big\}"
            ).scale(0.8).move_to(f_text)
            self.play(TransformMatchingTex(f_text, f_text2))
            self.remove(f_text2)
            f_text = MathTex(
                r"{{n F_{s,t}(n)}} = {{ \min_{ 1\le w\le n-1 } }} \Big\{ {{wt}}+ {{wF_{s,t}(w)}} {{+}} {{(n-w)s}} + {{(n-w)F_{s,t}(n - w)}}\Big\}"
            ).scale(0.8).move_to(f_text2)
            self.add(f_text)

        with self.voiceover(text="We can see that all appearance of F is paired with a multiplier matching the parameter"):
            self.play(f_text.get_part_by_tex("n F_{s,t}(n)").animate.set_color(YELLOW))
            self.play(f_text.get_part_by_tex("wF_{s,t}(w)").animate.set_color(YELLOW))
            self.play(f_text.get_part_by_tex("(n-w)F_{s,t}(n - w)").animate.set_color(YELLOW))

        with self.voiceover(text="This prompts us to introduce another function E, defined as F times n"):
            e_text = MathTex("E_{s,t}(n) = n F_{s,t}(n)").shift(UP*2)
            self.play(Write(e_text))

        with self.voiceover(text="With function E, we can simplify the formula"):
            f_text2 = MathTex(
                 r"{{E_{s,t}(n)}} = {{ \min_{ 1\le w\le n-1 } }} \Big\{ {{wt}}+ {{E_{s,t}(w)}} {{+}} {{(n-w)s}} + {{E_{s,t}(n - w)}}\Big\}"
            ).move_to(f_text)
            self.play(TransformMatchingTex(f_text, f_text2))

        with self.voiceover(text="The advantage of function E is it gets rid of fractions, which will help a lot later"):
            pass
        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def construct_scene2(self):

        with self.voiceover(text="Let's plot the function E for fixed s and t and varying n"):
            sqrt_s = 2
            sqrt_t = 5
            N = 30
            e, wmin, wmax = calc_irr(sqrt_s,sqrt_t, 100)
            necks = [i for i in range(1, len(e)) if wmin[i] == wmax[i]]

            axes = Axes(x_range=[0,35,5], y_range=[0, 300,50], x_length = 10, y_length = 6, axis_config={"include_numbers":True})
            axes_hori = MathTex("n").move_to(axes.get_corner(RIGHT+DOWN), LEFT).shift(RIGHT*0.2)
            axes_vert = MathTex(r"E_{\sqrt{2}, \sqrt{5}}(n)").scale(0.6).move_to(axes.get_corner(LEFT+UP)).shift(LEFT * 0.4)
            self.play(Create(axes), Write(axes_hori), Write(axes_vert))
            pass

        with self.voiceover(text="We will continue using irrational s and t, which will actually be helpful later"):
            dots = VGroup(*[Dot(axes.coords_to_point(n, e[n].value())) for n in range(1, N + 1)])
            self.play(Create(dots))
            pass

        with self.voiceover(text="Again, our plot is a collection of points because the variable n is an integer"):
            pass

        with self.voiceover(text="But let's connect the dots with straight segments to show the shape better"):
            segs = VGroup(*[Line(dots.submobjects[i].get_center(), dots.submobjects[i + 1].get_center(),
                                 color = BLUE
                                 ) for i in range(0, len(dots.submobjects) - 1)])
            self.play(Create(segs))
            pass

        with self.voiceover(text="Starting from this point, be aware that I am going to do things that are not very rigorous."):
            pass

        with self.voiceover(text="And the first wild thing I am going to do... computing and plotting the derivative of E"):
            dE = MathTex(r"\frac{\mathrm{d}E_{s,t}}{\mathrm{d}n}\ ?").shift(UP * 2)
            self.play(Write(dE))

        with self.voiceover(text="To be a bit more precise, this is the derivative of the new function after we connecting the dots"):
            self.play(FadeOut(dots), FadeOut(segs), FadeOut(dE))

            axes2 = Axes(x_range=[0,35,5], y_range=[0, 15], x_length = 10, y_length = 6, x_axis_config={"include_numbers":True}).move_to(axes.get_center())
            axes_vert2 = MathTex(r"E_{\sqrt{2}, \sqrt{5}}'(n)").scale(0.6).move_to(axes_vert.get_center())
            self.play(Transform(axes, axes2), Transform(axes_vert, axes_vert2))
            axes_vert=axes_vert2
            axes=axes2

            derivatives = [e[i + 1] - e[i] for i in range(N)]
            der_plot = VGroup()
            for i in range(1, len(derivatives)):
                d = derivatives[i].value()
                if i != 1:
                    der_plot.add(Line(axes.coords_to_point(i, derivatives[i-1].value()),
                                      axes.coords_to_point(i, d)))
                der_plot.add(Line(axes.coords_to_point(i, d), axes.coords_to_point(i + 1, d)))
            self.play(Create(der_plot))

        with self.voiceover(text="We can see a few flat segments in the plot"):
            pass

        with self.voiceover(text="Let's measure their length"):
            spans = VGroup()
            for i in range(1, len(necks)):
                left = necks[i - 1]
                right = necks[i]
                if left >= len(derivatives) or right >= len(derivatives):
                    break
                height = derivatives[left].value()
                spans.add(MathTex(int(right - left), color=YELLOW).scale(0.8).move_to(axes.coords_to_point((right + left) / 2, height) + DOWN * 0.1, UP))
            self.play(Create(spans))

        with self.voiceover(text="We can see these are the same number sequence we saw from the plot for function w, a particular arrangement of binomial coefficients"):
            pass

        with self.voiceover(text="Let's also label these segments with the value of E prime"):
            spder = VGroup()
            for i in range(1, len(necks)):
                left = necks[i - 1]
                right = necks[i]
                if left >= len(derivatives) or right >= len(derivatives):
                    break
                d = derivatives[left]
                p,q = d.a,d.b
                height = d.value()
                spder.add(MathTex(fr"{p}\sqrt{{ {sqrt_s} }} + {q}\sqrt{{ {sqrt_t} }}", color=BLUE)
                          .rotate(PI/2).scale(0.5).move_to(axes.coords_to_point((right + left) / 2, height) + UP * 0.1, DOWN))
            self.play(Create(spder))

        with self.voiceover(text="which turns out to be some linear combination of s and t"):
            pass

        with self.voiceover(text="By carefully comparing these numbers"):
            pass

        with self.voiceover(text="We can observe a correspondence between the length of segments and E prime"):
            corres = MathTex("(p+1)s + (q+1)t", r"\leftrightarrow", r"\frac{(p+q)!}{p!q!}={p+q\choose p}").shift(DOWN + RIGHT)
            corres.get_part_by_tex("(p+1)s + (q+1)t").set_color(BLUE)
            corres.get_part_by_tex(r"\frac{(p+q)!}{p!q!}={p+q\choose p}").set_color(YELLOW)
            self.play(Write(corres))

            pass

        self.wait(3)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        with self.voiceover(text="Let's show this correspondence using the formula for E"):
            f_text = MathTex(
                 r"{{E_{s,t}(n)}} = {{ \min_{ 1\le w\le n-1 } }} \Big\{ {{wt+ E_{s,t}(w)+(n-w)s+ E_{s,t}(n - w)}} \Big\}"
            ).shift(UP)
            self.play(Write(f_text))

        with self.voiceover(text="We extract the inner expression into its own function D"):
            f_text2 = MathTex(
                 r"{{E_{s,t}(n)}} = {{ \min_{ 1\le w\le n-1 } }} \Big\{ D_{s,t}(n, w) \Big\}"
            ).shift(UP)
            d_text = MathTex(
                r"D_{s,t}(n, w) = {{wt+ E_{s,t}(w)+(n-w)s+ E_{s,t}(n - w)}}"
            )
            self.play(TransformMatchingTex(f_text, VGroup(f_text2, d_text)))

        with self.voiceover(text="and since we are interested in the minimal value of D, let's take its derivative"):
            dd_text = MathTex(
                r"\frac{\partial D_{s,t} }{\partial w} = t+ E_{s,t}'(w) -s - E_{s,t}'(n - w)"
            ).shift(DOWN)
            self.play(FadeIn(dd_text, shift=DOWN))

        with self.voiceover(text="To get the minimal value, we set the derivative to zero"):
            dd_zero = MathTex(
                r"\frac{\partial D_{s,t} }{\partial w} = 0"
            ).shift(DOWN * 2.5 + LEFT * 4)
            self.play(Write(dd_zero))

        with self.voiceover(text="Which gives us this equation"):
            dd_zero_and = MathTex(r"\implies").move_to(dd_zero.get_right() + RIGHT * 0.3, LEFT)
            self.play(Write(dd_zero_and))
            dd_rel = MathTex(r"{{t + E_{s,t}'(w_{s,t})}} = {{s + E_{s,t}'(n - w_{s,t})}}").move_to(dd_zero_and.get_right() + RIGHT * 0.3, LEFT)
            self.play(Write(dd_rel))

        self.wait(2)

        with self.voiceover(text="Meanwhile, if we take the derivative of E"):
            self.play(FadeOut(dd_zero_and), FadeOut(dd_zero), FadeOut(dd_text), FadeOut(d_text))
            self.play(dd_rel.animate.move_to(DOWN * 1.5))
            f_text3 = MathTex(
                 r"{{E_{s,t}(n)}} = {{w_{s,t}t+ E_{s,t}(w_{s,t})+(n-w_{s,t})s+ E_{s,t}(n - w_{s,t})}} "
            ).shift(UP)
            self.play(TransformMatchingTex(f_text2, f_text3))
            de = MathTex(
                 r"{{E_{s,t}'(n)}} =  \frac{\mathrm{d}w_{s,t}}{\mathrm{d}n} ({{t + E_{s,t}'(w_{s,t})}}) + \left(1-\frac{\mathrm{d}w_{s,t}}{\mathrm{d}n}\right)({{s + E_{s,t}'(n - w_{s,t})}})"
            ).scale(0.8)
            de.get_part_by_tex("E_{s,t}'(n)").set_color(RED)
            self.play(FadeIn(de, shift=DOWN))

        with self.voiceover(text="We see the same expressions appearing"):
            ta = dd_rel.get_part_by_tex("t + E_{s,t}'(w_{s,t})")
            sa = dd_rel.get_part_by_tex("s + E_{s,t}'(n - w_{s,t})")
            tb = de.get_part_by_tex("t + E_{s,t}'(w_{s,t})")
            sb = de.get_part_by_tex("s + E_{s,t}'(n - w_{s,t})")
            self.play(ta.animate.set_color(GREEN), tb.animate.set_color(GREEN))
            self.play(sa.animate.set_color(BLUE), sb.animate.set_color(BLUE))

        with self.voiceover(text="This allow us to merge them into a simple relation among E prime"):
            rel = MathTex(
                 r"{{E_{s,t}'(n)}} = {{t + E_{s,t}'(w_{s,t})}} = {{s + E_{s,t}'(n - w_{s,t})}}"
            ).shift(DOWN * 2.5)
            rel.get_part_by_tex("E_{s,t}'(n)").set_color(RED)
            rel.get_part_by_tex("t + E_{s,t}'(w_{s,t})").set_color(GREEN)
            rel.get_part_by_tex("s + E_{s,t}'(n - w_{s,t})").set_color(BLUE)
            self.play(FadeIn(rel, shift=DOWN))

        with self.voiceover(text="Let's move back to the plot of the E prime"):
            self.play(FadeOut(f_text3), FadeOut(de), FadeOut(dd_rel))
            self.play(rel.animate.move_to(UP * 3))
            axes = Axes(x_range=[0,35,5], y_range=[0, 15,5], x_length = 8, y_length = 5).shift(DOWN*0.5+LEFT*1.5)
            axes_vert = MathTex(r"E_{s,t}'(n)").scale(0.7).move_to(axes.get_corner(UP+LEFT),RIGHT)
            axes_hori = MathTex(r"n").move_to(axes.get_corner(DOWN+RIGHT),UP)
            der_plot = VGroup()
            for i in range(1, len(derivatives)):
                d = derivatives[i].value()
                if i != 1:
                    der_plot.add(Line(axes.coords_to_point(i, derivatives[i-1].value()),
                                      axes.coords_to_point(i, d)))
                der_plot.add(Line(axes.coords_to_point(i, d), axes.coords_to_point(i + 1, d)))
            self.play(FadeIn(axes), FadeIn(der_plot), FadeIn(axes_vert), FadeIn(axes_hori))

        dEn = AlgebraicR2(sqrt_s, sqrt_t, 3, 3)
        dEw = dEn - AlgebraicR2(sqrt_s, sqrt_t, 0, 1)
        dEnw = dEn - AlgebraicR2(sqrt_s, sqrt_t, 1, 0)

        def get_plate(dE):
            l = [i for i in range(0, len(derivatives)) if derivatives[i] == dE]
            if len(l) == 0:
                g = [i for i in range(0, len(derivatives)) if derivatives[i] > dE][0]
                return (g, g)
            return (min(l), max(l) + 1)
        EnL, EnR = get_plate(dEn)
        EwL, EwR = get_plate(dEw)
        EnwL, EnwR = get_plate(dEnw)

        with self.voiceover(text="We see that the three terms in the equation correspond to three segments in the plot"):
            EnTL, EnTR = axes.coords_to_point(EnL, dEn.value()), axes.coords_to_point(EnR, dEn.value())
            EwTL, EwTR = axes.coords_to_point(EwL, dEw.value()), axes.coords_to_point(EwR, dEw.value())
            EnwTL, EnwTR = axes.coords_to_point(EnwL, dEnw.value()), axes.coords_to_point(EnwR, dEnw.value())
            LineEn = Line(EnTL, EnTR, color=RED, stroke_width = 6)
            LineEw = Line(EwTL, EwTR, color=GREEN, stroke_width = 6)
            LineEnw = Line(EnwTL, EnwTR, color=BLUE, stroke_width = 6)
            self.play(der_plot.animate.set_color(GREY).set_stroke(width=1))
            self.play(Create(LineEn))
            self.play(Create(LineEw))
            self.play(Create(LineEnw))

        with self.voiceover(text="Their heights satisfies the equation"):
            LineEnEx = DashedLine(EnTL, axes.coords_to_point(2, dEn.value()), color=RED)
            LineEwEx = DashedLine(EwTL, axes.coords_to_point(2, dEw.value()), color=GREEN)
            LineEnwEx = DashedLine(EnwTL, axes.coords_to_point(5, dEnw.value()), color=BLUE)
            self.play(Create(LineEnEx), Create(LineEwEx), Create(LineEnwEx))
            EwDis = DoubleArrow(axes.coords_to_point(2, dEn.value()), axes.coords_to_point(2, dEw.value()), buff=0, color=GREEN)
            EnwDis = DoubleArrow(axes.coords_to_point(5, dEn.value()), axes.coords_to_point(5, dEnw.value()), buff=0, color=BLUE)
            EwDisT = MathTex("t", color=GREEN).move_to(EwDis.get_right()+RIGHT*0.1, LEFT)
            EnwDisT = MathTex("s", color=BLUE).move_to(EnwDis.get_right()+RIGHT*0.1, LEFT)
            self.play(Create(EwDis), Create(EnwDis), Write(EwDisT), Write(EnwDisT))

        with self.voiceover(text="Meanwhile, we can find a point on each segment"):
            j = 0.3
            EnP = (1-j) * EnL + j *EnR
            EwP = (1-j) * EwL + j *EwR
            EnwP = (1-j) * EnwL + j *EnwR
            EnPoint = Dot(axes.coords_to_point(EnP, dEn.value()), color=RED, radius = 0.1)
            EwPoint = Dot(axes.coords_to_point(EwP, dEw.value()), color=GREEN, radius = 0.1)
            EnwPoint = Dot(axes.coords_to_point(EnwP, dEnw.value()), color=BLUE, radius = 0.1)
            self.play(Create(EnPoint), Create(EwPoint), Create(EnwPoint))

        with self.voiceover(text="such that their coordinates are n, w, and n minus w"):
            EnDrop = DashedLine(axes.coords_to_point(EnP, dEn.value()), axes.coords_to_point(EnP, 0), color=RED)
            EwDrop = DashedLine(axes.coords_to_point(EwP, dEw.value()), axes.coords_to_point(EwP, 0), color=GREEN)
            EnwDrop = DashedLine(axes.coords_to_point(EnwP, dEnw.value()), axes.coords_to_point(EnwP, 0), color=BLUE)
            self.play(Create(EnDrop), Create(EwDrop), Create(EnwDrop))
            EnDropText = MathTex("n", color=RED).move_to(axes.coords_to_point(EnP, 0)+DOWN*0.1,UP).scale(0.8)
            EwDropText = MathTex("w", color=GREEN).move_to(axes.coords_to_point(EwP, 0)+DOWN*0.1,UP).scale(0.8)
            EnwDropText = MathTex("n-w", color=BLUE).move_to(axes.coords_to_point(EnwP, 0)+DOWN*0.1,UP).scale(0.8)
            self.play(Write(EnDropText), Write(EwDropText), Write(EnwDropText))

        with self.voiceover(text="If we look at the intervals for coordinates of each segment"):
            EnBL, EnBR = axes.coords_to_point(EnL, 0), axes.coords_to_point(EnR, 0)
            EwBL, EwBR = axes.coords_to_point(EwL, 0), axes.coords_to_point(EwR, 0)
            EnwBL, EnwBR = axes.coords_to_point(EnwL, 0), axes.coords_to_point(EnwR, 0)
            EnRect = Polygon(EnBL, EnBR, EnTR, EnTL, stroke_opacity=0.0, fill_opacity=0.5, fill_color=RED)
            EwRect = Polygon(EwBL, EwBR, EwTR, EwTL, stroke_opacity=0.0, fill_opacity=0.5, fill_color=GREEN)
            EnwRect = Polygon(EnwBL, EnwBR, EnwTR, EnwTL, stroke_opacity=0.0, fill_opacity=0.5, fill_color=BLUE)
            self.play(Create(EnRect), Create(EwRect), Create(EnwRect))
            self.play(Transform(EnDropText, MathTex("[L_n, R_n]", color=RED).scale(0.6).move_to((EnBL+EnBR) / 2 + DOWN * 0.25)),
                      Transform(EwDropText, MathTex("[L_w, R_w]", color=GREEN).scale(0.6).move_to((EwBL+EwBR) / 2 + DOWN * 0.25 + LEFT * 0.25)),
                      Transform(EnwDropText, MathTex("[L_{n-w}, R_{n-w}]", color=BLUE).scale(0.6).move_to((EnwBL+EnwBR) / 2 + DOWN * 0.25 + RIGHT * 0.25)),
                      FadeOut(EnDrop), FadeOut(EwDrop), FadeOut(EnwDrop),
                      FadeOut(EnPoint), FadeOut(EwPoint), FadeOut(EnwPoint),
                      )

        with self.voiceover(text="We can find a relation between them"):
            int_rel = MathTex("{{[L_w, R_w]}} + {{[L_{n-w}, R_{n-w}]}} = {{[L_n, R_n]}}").move_to(RIGHT*3.5 + UP *1.5).scale(0.8)
            int_rel.get_part_by_tex("[L_n, R_n]").set_color(RED)
            int_rel.get_part_by_tex("[L_w, R_w]").set_color(GREEN)
            int_rel.get_part_by_tex("[L_{n-w}, R_{n-w}]").set_color(BLUE)
            self.play(Write(int_rel))

        with self.voiceover(text="Which implies the same relation between their left and right end points"):
            int_relL = MathTex("{{L_w}} + {{L_{n-w} }} = {{L_n}}").move_to(RIGHT*4.5 + UP*0.5).scale(0.8)
            int_relL.get_part_by_tex("L_n").set_color(RED)
            int_relL.get_part_by_tex("L_w").set_color(GREEN)
            int_relL.get_part_by_tex("L_{n-w} ").set_color(BLUE)
            int_relR = MathTex("{{R_w}} + {{R_{n-w} }} = {{R_n}}").move_to(RIGHT*4.5).scale(0.8)
            int_relR.get_part_by_tex("R_n").set_color(RED)
            int_relR.get_part_by_tex("R_w").set_color(GREEN)
            int_relR.get_part_by_tex("R_{n-w} ").set_color(BLUE)
            self.play(Write(int_relL), Write(int_relR))

        with self.voiceover(text="If we take the difference between the two equation"):
            int_relDiff = MathTex("{{R_w-L_w}} + {{R_{n-w}-L_{n-w} }} = {{R_n-L_n}}").move_to(RIGHT*4 + UP*0.25).scale(0.7)
            int_relDiff.get_part_by_tex("R_n-L_n").set_color(RED)
            int_relDiff.get_part_by_tex("R_w-L_w").set_color(GREEN)
            int_relDiff.get_part_by_tex("R_{n-w}-L_{n-w} ").set_color(BLUE)
            self.play(TransformMatchingTex(VGroup(int_relL, int_relR), int_relDiff))

        with self.voiceover(text="We get the relation between the spans"):
            int_relSpan = MathTex(r"{{\mathrm{Span}_w}} + {{\mathrm{Span}_{n-w} }} = {{\mathrm{Span}_n}}").move_to(int_rel.get_center())
            int_relSpan.get_part_by_tex(r"\mathrm{Span}_n").set_color(RED)
            int_relSpan.get_part_by_tex(r"\mathrm{Span}_w").set_color(GREEN)
            int_relSpan.get_part_by_tex(r"\mathrm{Span}_{n-w} ").set_color(BLUE)

            self.play(Transform(EnDropText, MathTex(r"\mathrm{Span}_n", color=RED).scale(0.6).move_to((EnBL+EnBR) / 2 + DOWN * 0.25)),
                      Transform(EwDropText, MathTex(r"\mathrm{Span}_w", color=GREEN).scale(0.6).move_to((EwBL+EwBR) / 2 + DOWN * 0.25)),
                      Transform(EnwDropText, MathTex(r"\mathrm{Span}_{n-w}", color=BLUE).scale(0.6).move_to((EnwBL+EnwBR) / 2 + DOWN * 0.25 + RIGHT * 0.25))
                      )

            self.play(FadeOut(int_rel), TransformMatchingTex(int_relDiff, int_relSpan))

        with self.voiceover(text="Let's look at another triplet of segments"):
            self.play(FadeOut(LineEn, LineEw, LineEnw, LineEnEx, LineEwEx, LineEnwEx, EwDis, EnwDis, EwDisT, EnwDisT,
                              EnRect, EwRect, EnwRect, EnDropText, EwDropText, EnwDropText))

            dEn2 = AlgebraicR2(sqrt_s, sqrt_t, 6, 1)
            dEw2 = dEn2 - AlgebraicR2(sqrt_s, sqrt_t, 0, 1)
            dEnw2 = dEn2 - AlgebraicR2(sqrt_s, sqrt_t, 1, 0)
            EnL2, EnR2 = get_plate(dEn2)
            EwL2, EwR2 = get_plate(dEw2)
            EnwL2, EnwR2 = get_plate(dEnw2)

            EnTL2, EnTR2 = axes.coords_to_point(EnL2, dEn2.value()), axes.coords_to_point(EnR2, dEn2.value())
            EwTL2, EwTR2 = axes.coords_to_point(EwL2, dEw2.value()), axes.coords_to_point(EwR2, dEw2.value())
            EnwTL2, EnwTR2 = axes.coords_to_point(EnwL2, dEnw2.value()), axes.coords_to_point(EnwR2, dEnw2.value())
            LineEn2 = Line(EnTL2, EnTR2, color=RED, stroke_width = 6)
            LineEw2 = Dot(EwTL2, color=GREEN, radius= 0.05)
            LineEnw2 = Line(EnwTL2, EnwTR2, color=BLUE, stroke_width = 6)
            self.play(Create(LineEn2))
            self.play(Create(LineEw2))
            self.play(Create(LineEnw2))

            LineEnEx2 = DashedLine(EnTL2, axes.coords_to_point(2, dEn2.value()), color=RED)
            LineEwEx2 = DashedLine(EwTL2, axes.coords_to_point(2, dEw2.value()), color=GREEN)
            LineEnwEx2 = DashedLine(EnwTL2, axes.coords_to_point(5, dEnw2.value()), color=BLUE)
            self.play(Create(LineEnEx2), Create(LineEwEx2), Create(LineEnwEx2))
            EwDis2 = DoubleArrow(axes.coords_to_point(2, dEn2.value()), axes.coords_to_point(2, dEw2.value()), buff=0, color=GREEN)
            EnwDis2 = DoubleArrow(axes.coords_to_point(5, dEn2.value()), axes.coords_to_point(5, dEnw2.value()), buff=0, color=BLUE)
            EwDisT2 = MathTex("t", color=GREEN).move_to(EwDis2.get_right()+RIGHT*0.1, LEFT)
            EnwDisT2 = MathTex("s", color=BLUE).move_to(EnwDis2.get_right()+RIGHT*0.1, LEFT)
            self.play(Create(EwDis2), Create(EnwDis2), Write(EwDisT2), Write(EnwDisT2))

            EnBL2, EnBR2 = axes.coords_to_point(EnL2, 0), axes.coords_to_point(EnR2, 0)
            EwBL2, EwBR2 = axes.coords_to_point(EwL2, 0), axes.coords_to_point(EwR2, 0)
            EnwBL2, EnwBR2 = axes.coords_to_point(EnwL2, 0), axes.coords_to_point(EnwR2, 0)

            EnRect2 = Polygon(EnBL2, EnBR2, EnTR2, EnTL2, stroke_opacity=0.0, fill_opacity=0.5, fill_color=RED)
            EwRect2 = DashedLine(EwTR2, EwBR2, color=GREEN)
            EnwRect2 = Polygon(EnwBL2, EnwBR2, EnwTR2, EnwTL2, stroke_opacity=0.0, fill_opacity=0.5, fill_color=BLUE)
            self.play(Create(EnRect2), Create(EwRect2), Create(EnwRect2))

            EnDropText2 = MathTex(r"\mathrm{Span}_n", color=RED).scale(0.6).move_to((EnBL2+EnBR2) / 2 + DOWN * 0.25)
            EwDropText2 = MathTex(r"\mathrm{Span}_w", color=GREEN).scale(0.6).move_to((EwBL2+EwBR2) / 2 + DOWN * 0.25)
            EnwDropText2 = MathTex(r"\mathrm{Span}_{n-w}", color=BLUE).scale(0.6).move_to((EnwBL2+EnwBR2) / 2 + DOWN * 0.25+ RIGHT * 0.25)
            self.play(Write(EnDropText2), Write(EwDropText2), Write(EnwDropText2))

        with self.voiceover(text="This time, one of the span is zero, as there is no corresponding segment for the desired E prime"):
            self.play(Circumscribe(LineEw2))

        with self.voiceover(text="We can work out that this happens when the E prime is a multiple of s or t, whose detail I unfortunately can't cover in this video"):
            zero_cond = MathTex(
                r"E_{s,t}' \in \mathbb{Z}^{\ge 2} s \cup \mathbb{Z}^{\ge 2} t \implies \mathrm{Span} = 0",
                color=PURPLE
                ).scale(0.8).move_to(RIGHT * 3.5 + DOWN)
            self.play(Write(zero_cond))

        with self.voiceover(text="Lastly, we notice the very first segment"):
            self.play(FadeOut(LineEn2, LineEw2, LineEnw2, LineEnEx2, LineEwEx2, LineEnwEx2, EwDis2, EnwDis2, EwDisT2, EnwDisT2,
                              EnRect2, EwRect2, EnwRect2, EnDropText2, EwDropText2, EnwDropText2))
            dEn2 = AlgebraicR2(sqrt_s, sqrt_t, 1, 1)
            EnL2, EnR2 = get_plate(dEn2)
            EnTL2, EnTR2 = axes.coords_to_point(EnL2, dEn2.value()), axes.coords_to_point(EnR2, dEn2.value())
            LineEn2 = Line(EnTL2, EnTR2, color=YELLOW, stroke_width = 6)
            self.play(Create(LineEn2))

            EnBL2, EnBR2 = axes.coords_to_point(EnL2, 0), axes.coords_to_point(EnR2, 0)
            EnRect2 = Polygon(EnBL2, EnBR2, EnTR2, EnTL2, stroke_opacity=0.0, fill_opacity=0.5, fill_color=YELLOW)
            self.play(Create(EnRect2))

        with self.voiceover(text="Has a span of one and E prime equal to s plus t"):
            EnDropText2 = MathTex(r"1", color=YELLOW).scale(0.6).move_to((EnBL2+EnBR2) / 2 + DOWN * 0.25)
            EnDText = MathTex(r"s + t", color=YELLOW).scale(0.8).move_to(EnTL2 + LEFT * 0.7)
            self.play(Write(EnDropText2), Write(EnDText))

        with self.voiceover(text="Which gives us the starting point for induction"):
            one_cond = MathTex(
                r"E_{s,t}' = s + t \implies \mathrm{Span} = 1", color=YELLOW
                ).scale(0.8).move_to(RIGHT * 3.5 + DOWN * 1.7)
            self.play(Write(one_cond))

        with self.voiceover(text="We have all our building blocks ready to show the correspondence"):
            self.play(FadeOut(axes, axes_hori, axes_vert, LineEn2, EnRect2, EnDropText2, EnDText, der_plot))
            self.play(rel.animate.move_to(UP * 3.5 + LEFT * 3).scale(0.8),
                      int_relSpan.animate.move_to(UP * 3.5 + RIGHT * 4).scale(0.8),
                      zero_cond.animate.move_to(UP * 3),
                      one_cond.animate.move_to(UP * 2.5))
            line_hori = Line(UP * 2.2 + LEFT * 7, UP * 2.3 + RIGHT * 7)
            line_vert = Line(UP * 2.2, DOWN * 4)
            self.play(FadeIn(line_hori, line_vert))

        def tri_pos(p, q):
            row = p + q - 2
            col = p - q
            return (row * DOWN * 0.6 + UP * 1 + col * RIGHT * 0.55)

        latD = 3.5

        trigL = [[None for _ in range(10)] for _ in range(10)]
        trigR = [[None for _ in range(10)] for _ in range(10)]

        with self.voiceover(text="We start with the initial span of one"):
            trigL[1][1] = MathTex("s + t", color=YELLOW).scale(0.6).move_to(tri_pos(1, 1) + latD * LEFT)
            trigR[1][1] = MathTex("1", color=YELLOW).scale(0.8).move_to(tri_pos(1, 1) + latD * RIGHT)
            self.play(Write(trigL[1][1]), Write(trigR[1][1]))

        with self.voiceover(text="and add those zero spans on the sides"):
            for k in range(2, 7):
                trigL[0][k] = MathTex(f"{k}t", color=PURPLE).scale(0.6).move_to(tri_pos(0, k) + latD * LEFT)
                trigR[0][k] = MathTex("0", color=PURPLE).scale(0.8).move_to(tri_pos(0, k) + latD * RIGHT)
                trigL[k][0] = MathTex(f"{k}s", color=PURPLE).scale(0.6).move_to(tri_pos(k, 0) + latD * LEFT)
                trigR[k][0] = MathTex("0", color=PURPLE).scale(0.8).move_to(tri_pos(k, 0) + latD * RIGHT)
                self.play(Write(trigL[0][k]), Write(trigR[0][k]), Write(trigL[k][0]), Write(trigR[k][0]), run_time=0.1)

        with self.voiceover(text="We can recursively construct two triangles"):
            for k in range(3, 8):
                for p in range(1, k):
                    q = k - p
                    trigL[p][q] = MathTex(f"{p}s + {q}t").scale(0.6).move_to(tri_pos(p, q) + latD * LEFT)
                    trigR[p][q] = MathTex(f"{int(scipy.special.comb(p+q-2,p-1))}").scale(0.8).move_to(tri_pos(p, q) + latD * RIGHT)
                    self.play(Write(trigL[p][q]), Write(trigR[p][q]), run_time=0.1)

        with self.voiceover(text="On the left side, we run through linear combinations of s and t"):
            allL = MathTex("(p+1)s + (q+1)t").move_to(LEFT* 3.5 + DOWN *3)
            self.play(Write(allL))


        with self.voiceover(text="On the right side, we get Pascal's triangle that runs through binomial coefficients"):
            allL = MathTex(r"p+q\choose p").move_to(RIGHT* 3.5 + DOWN *3)
            self.play(Write(allL))

        with self.voiceover(text="Since the recurrence formula for each side are based on the same n"):
            pass

        with self.voiceover(text="This establishes a one-to-one correspondence between the two triangles"):
            corr = DoubleArrow(DOWN * 3 + LEFT, DOWN*3 + RIGHT)
            self.play(Create(corr))

        with self.voiceover(text="Except this only works when s over t is irrational"):
            pass

        with self.voiceover(text="If we have rational configuration, say s equals one and t equals 2"):
            st_exa = MathTex("s = 1, t = 2").scale(0.8).move_to(UP * 1.9 + LEFT * 5.7)
            s = 1
            t = 2
            self.play(Write(st_exa))

            for p in range(len(trigL)):
                for q in range(len(trigL[p])):
                    tl = trigL[p][q]
                    if tl is None:
                        continue
                    self.play(Transform(tl, MathTex(int(p * s + q * t), color=tl.get_color())
                                        .scale(0.8).move_to(tl.get_center())), run_time = 0.1)

        with self.voiceover(text="We see a lot of repeating numbers on the left"):
            for leftv in range(1, 20):
                pqs = [(p,q) for p in range(len(trigL)) for q in range(len(trigL[p]))
                       if trigL[p][q] is not None and p * s + q * t == leftv]
                if len(pqs) == 0 or len(pqs) == 1:
                    continue
                pq0 = tri_pos(*min(pqs, key=lambda pq: pq[0])) + latD * LEFT
                pq1 = tri_pos(*min(pqs, key=lambda pq: pq[1])) + latD * LEFT
                pq0b = pq0 + (pq0 - pq1) / numpy.linalg.norm(pq0 - pq1) * 0.2
                pq1b = pq1 + (pq1 - pq0) / numpy.linalg.norm(pq0 - pq1) * 0.2
                pqLine = Line(pq0b, pq1b, stroke_width = 30, stroke_opacity=0.4, color=RED)
                self.play(Create(pqLine), run_time = 0.3)

        with self.voiceover(text="If we group numbers in the same way on the right"):
            for leftv in range(1, 20):
                pqs = [(p,q) for p in range(len(trigL)) for q in range(len(trigL[p]))
                       if trigL[p][q] is not None and p * s + q * t == leftv]
                if len(pqs) == 0 or len(pqs) == 1:
                    continue
                pq0 = tri_pos(*min(pqs, key=lambda pq: pq[0])) + latD * RIGHT
                pq1 = tri_pos(*min(pqs, key=lambda pq: pq[1])) + latD * RIGHT
                pq0b = pq0 + (pq0 - pq1) / numpy.linalg.norm(pq0 - pq1) * 0.2
                pq1b = pq1 + (pq1 - pq0) / numpy.linalg.norm(pq0 - pq1) * 0.2
                pqLine = Line(pq0b, pq1b, stroke_width = 30, stroke_opacity=0.4, color=ORANGE)
                self.play(Create(pqLine), run_time = 0.3)

        with self.voiceover(text="And take the sum of each group"):
            self.play(Create(MathTex("1", color=BLUE).move_to(trigR[1][1].get_center()+LEFT*0.3 + UP * 0.2)), run_time=0.5)
            self.play(Create(MathTex("1", color=BLUE).move_to(trigR[0][2].get_center()+LEFT*0.3 + UP * 0.2)), run_time=0.5)
            self.play(Create(MathTex("2", color=BLUE).move_to(trigR[1][2].get_center()+LEFT*0.3 + UP * 0.2)), run_time=0.5)
            self.play(Create(MathTex("3", color=BLUE).move_to(trigR[0][3].get_center()+LEFT*0.3 + UP * 0.2)), run_time=0.5)
            self.play(Create(MathTex("5", color=BLUE).move_to(trigR[1][3].get_center()+LEFT*0.3 + UP * 0.2)), run_time=0.5)
            self.play(Create(MathTex("8", color=BLUE).move_to(trigR[0][4].get_center()+LEFT*0.3 + UP * 0.2)), run_time=0.5)

            pass

        with self.voiceover(text="We see these are numbers in Fibonacci sequence"):
            pass

        with self.voiceover(text="In fact, one can prove that taking sums along a certain direction in Pascal's triangle will always produce a Fibonacci-like sequence"):
            pass

        with self.voiceover(text="This explains why we see them for rational s over t"):
            pass

        with self.voiceover(text="With function E now understood, now let's look at the w function again"):
            self.play(
                *[FadeOut(mob)for mob in self.mobjects]
            )

            pass

        with self.voiceover(text="Let's bring back the triplet of segments from E prime"):
            EnL, EnR = 2 * UP + LEFT * 6, 2 * UP + LEFT * 1
            EwL, EwR = LEFT * 5, LEFT * 2
            EnwL, EnwR = 2 * DOWN + LEFT * 4.5, 2 * DOWN + LEFT * 2.5

            EnSpan = 5
            EwSpan = 3
            EnwSpan = 2

            LineEn = Line(EnL, EnR, stroke_width = 6, color=RED)
            LineEw = Line(EwL, EwR, stroke_width = 6, color=GREEN)
            LineEnw = Line(EnwL, EnwR, stroke_width = 6, color=BLUE)
            TextEn = MathTex("n", color=RED).move_to(2 * UP + LEFT * 6.7, LEFT)
            TextEw = MathTex("w_{s,t}", color=GREEN).move_to(LEFT * 6.7, LEFT)
            TextEnw = MathTex("n - w_{s,t}", color=BLUE).move_to(2 * DOWN + LEFT * 6.7, LEFT)

            self.play(Create(LineEn), Create(LineEw), Create(LineEnw),
                      Write(TextEn), Write(TextEw), Write(TextEnw))

        def lerp(a, b, x):
            return a * (1-x) + b * x

        with self.voiceover(text="We pick one point on each span that satisfy the constraint"):
            EnX = EnSpan * 0.3
            EwX = EwSpan * 0.3
            EnwX = EnwSpan * 0.3
            EnP = Dot(lerp(EnL, EnR, EnX/EnSpan), color=RED, radius=0.1)
            EwP = Dot(lerp(EwL, EwR, EwX/EwSpan), color=GREEN, radius=0.1)
            EnwP = Dot(lerp(EnwL, EnwR, EnwX/EnwSpan), color=BLUE, radius=0.1)
            self.play(Create(EnP), Create(EwP), Create(EnwP))

        with self.voiceover(text="Let's also track the value of n and w in a plane"):
            EnOff = 1
            EwOff = 1
            axes = Axes([0, 7], [0, 5], 6, 6/7*5).move_to(RIGHT * 3)
            axes_hori = MathTex("n", color=RED).move_to(axes.get_corner(RIGHT+DOWN), LEFT)
            axes_vert = MathTex("w_{s,t}", color=GREEN).move_to(axes.get_corner(LEFT+UP), DOWN)
            slideEn = Line(axes.coords_to_point(EnOff, 0), axes.coords_to_point(EnSpan + EnOff, 0), stroke_width = 5, color=RED)
            slideEw = Line(axes.coords_to_point(0, EwOff), axes.coords_to_point(0, EwOff + EwSpan), stroke_width = 5, color=GREEN)
            self.play(Create(axes), Create(axes_hori), Create(axes_vert), Create(slideEn), Create(slideEw))

            trackEn = DashedLine(axes.coords_to_point(EnX + EnOff, 0), axes.coords_to_point(EnX + EnOff, EwX + EwOff), color=RED)
            trackEw = DashedLine(axes.coords_to_point(0, EwX + EwOff), axes.coords_to_point(EnX + EnOff, EwX + EwOff), color=GREEN)
            self.play(Create(trackEn), Create(trackEw))
            trackP = Dot(axes.coords_to_point(EnX + EnOff, EwX + EwOff))
            self.play(Create(trackP))

        def ani_move(toEnX, toEwX):
            nonlocal EnX, EwX, EnwX, EnP, EwP, EnwP, trackEn, trackEw, trackP
            EnX = toEnX
            EwX = toEwX
            EnwX = EnX - EwX
            return [EnP.animate.move_to(lerp(EnL, EnR, EnX/EnSpan)),
                    EwP.animate.move_to(lerp(EwL, EwR, EwX/EwSpan)),
                    EnwP.animate.move_to(lerp(EnwL, EnwR, EnwX/EnwSpan)),
                    Transform(trackEn, DashedLine(axes.coords_to_point(EnX + EnOff, 0), axes.coords_to_point(EnX + EnOff, EwX + EwOff), color=RED)),
                    Transform(trackEw, DashedLine(axes.coords_to_point(0, EwX + EwOff), axes.coords_to_point(EnX + EnOff, EwX + EwOff), color=GREEN)),
                    trackP.animate.move_to(axes.coords_to_point(EnX + EnOff, EwX + EwOff))
                    ]

        with self.voiceover(text="We first move all three points to the left end"):
            self.play(*ani_move(0, 0))

        with self.voiceover(text="and let them slide to the right end"):
            toEnX = EnSpan
            toEwX = EwSpan
            para_diag=Line(axes.coords_to_point(EnX + EnOff, EwX + EwOff), axes.coords_to_point(toEnX + EnOff, toEwX + EwOff))
            self.play(*ani_move(toEnX, toEwX), Create(para_diag), run_time=3)

        with self.voiceover(text="This gives us a line of possible n and w values"):
            pass

        with self.voiceover(text="However, this is not the only possible configuration"):
            pass

        with self.voiceover(text="We can keep the w at the right end, and slide n leftwards"):
            toEnX = EwSpan
            toEwX = EwSpan
            para_up=Line(axes.coords_to_point(EnX + EnOff, EwX + EwOff), axes.coords_to_point(toEnX + EnOff, toEwX + EwOff))
            self.play(*ani_move(toEnX, toEwX), Create(para_up), run_time=3)

        with self.voiceover(text="We can do this till n minus w hits the left end"):
            pass

        with self.voiceover(text="Then we can slide both n and w leftwards till all of them hits the end"):
            toEnX = 0
            toEwX = 0
            para_left=Line(axes.coords_to_point(EnX + EnOff, EwX + EwOff), axes.coords_to_point(toEnX + EnOff, toEwX + EwOff))
            self.play(*ani_move(toEnX, toEwX), Create(para_left), run_time=3)

        with self.voiceover(text="Similarly, we can keep w at the left end while sliding n rightwards"):
            toEnX = EnwSpan
            toEwX = 0
            para_down=Line(axes.coords_to_point(EnX + EnOff, EwX + EwOff), axes.coords_to_point(toEnX + EnOff, toEwX + EwOff))
            self.play(*ani_move(toEnX, toEwX), Create(para_down), run_time=3)

        with self.voiceover(text="till n minus w hits the right end"):
            pass

        with self.voiceover(text="and then we slide all of them to the right end"):
            toEnX = EnSpan
            toEwX = EwSpan
            para_right=Line(axes.coords_to_point(EnX + EnOff, EwX + EwOff), axes.coords_to_point(toEnX + EnOff, toEwX + EwOff))
            self.play(*ani_move(toEnX, toEwX), Create(para_right), run_time=3)

        with self.voiceover(text="We have tracked the boundary of a parallelogram"):
            pass

        with self.voiceover(text="It is not hard to see that all intermediate configurations are also valid"):
            pass

        with self.voiceover(text="Hence the entire solid parallelogram represents possible value of w"):
            para = Polygon(axes.coords_to_point(EnOff, EwOff),
                           axes.coords_to_point(EnOff + EwSpan, EwOff + EwSpan),
                           axes.coords_to_point(EnOff + EnSpan, EwOff + EwSpan),
                           axes.coords_to_point(EnOff - EwSpan + EnSpan, EwOff),
                           fill_color=DARK_GREY,fill_opacity=1.0,color=GREY)
            self.play(Create(para))

        with self.voiceover(text="Or to be precise, all integral points in the parallelogram"):
            para_dots = VGroup()
            for n in range(EnSpan + 1):
                for w in range(max(0, EwSpan + 1)):
                    nw = n - w
                    if nw < 0 or nw > EnwSpan:
                        continue
                    para_dots.add(Dot(axes.coords_to_point(EnOff + n, EwOff + w)))
            self.play(Create(para_dots))

        with self.voiceover(text="This explains why the plot for w consists of a series of parallelogram"):
            pass


        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def construct_scene2_5(self):
        with self.voiceover(text="As I said before, the explanation here is not rigorous"):
            pass

        with self.voiceover(text="A lot more care needs to be taken when we talk about the derivative of an otherwise discrete function"):
            der = MathTex(r"\frac{\mathrm{d}E_{s,t}(n)}{\mathrm{d} n}")
            self.play(Write(der))

        with self.voiceover(text="In this case, it is better to talk about the discrete differential instead"):
            self.play(der.animate.shift(LEFT * 5))
            self.play(Create(Cross(der)))
            disder = MathTex(r"\Delta_n E_{s,t}(n) = E_{s,t}(n + 1) - E_{s,t}(n)")
            self.play(Write(disder))

        with self.voiceover(text="We also missed another important piece:"):
            pass

        with self.voiceover(text="E is a convex function, or its second differential is non-negative"):
            disderc = MathTex(r"\Delta_n^2 E_{s,t}(n) \geq 0").shift(DOWN)
            self.play(Write(disderc))

        with self.voiceover(text="which needs some extra care to proof as well"):
            pass

        with self.voiceover(text="This makes it rigorous to link the sign of the differential and the optimal strategy"):
            disdercc = MathTex(r"\Delta_w D_{s,t}(n, w) \mbox{ changes sign} \Leftrightarrow w \mbox{ is optimal}").shift(DOWN * 2)
            self.play(Write(disdercc))

        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )


    def construct_scene3(self):
        with self.voiceover(text="Let's recap with a way to compute function E and w"):
            pass

        max_row = 13
        pasc = [[None for _ in range(max_row + 1)] for _ in range(max_row + 1)]
        tagd = [[None for _ in range(max_row + 1)] for _ in range(max_row + 1)]
        tagw = [[None for _ in range(max_row + 1)] for _ in range(max_row + 1)]

        with self.voiceover(text="We first list binomial coefficients with Pascal's triangle"):
            for row in range(0, max_row + 1):
                for k in reversed(range(0, row + 1)):
                    p, q, = k, row - k
                    content = str(int(scipy.special.comb(row, k)))
                    scale = 1.0 if len(content) < 3 else 0.8
                    pasc[p][q] = MathTex(content).scale(scale).move_to((k - row / 2) * LEFT + UP * 3.5 + DOWN * row)
                    self.play(Write(pasc[p][q]), run_time = 0.1 if row < 8 else 0.01)

        with self.voiceover(text="We then add a yellow tag to each binomial coefficients in a specific way"):
            pass

        TAGD_OFF = DOWN * 0.35
        TAGW_OFF = UP * 0.35

        with self.voiceover(text="We tag the one on the top with s plus t"):
            tagd[0][0] = MathTex("1s + 1t", color=YELLOW).scale(0.5).move_to(pasc[0][0].get_center() + TAGD_OFF)
            self.play(Write(tagd[0][0]))

        with self.voiceover(text="And when we move one number towards bottom left, we add another s; when we move one number toward bottom right, we add another t"):
            arrow_s = Arrow(pasc[0][0].get_center() + LEFT, pasc[6][0].get_center() + LEFT, color=YELLOW)
            arrow_t = Arrow(pasc[0][0].get_center() + RIGHT, pasc[0][6].get_center() + RIGHT, color=YELLOW)
            self.play(Create(arrow_s), Create(arrow_t))
            text_s = MathTex("+s", color=YELLOW).move_to(arrow_s.get_center() + LEFT)
            text_t = MathTex("+t", color=YELLOW).move_to(arrow_t.get_center() + RIGHT)
            self.play(Write(text_s), Write(text_t))
            for row in range(1, max_row + 1):
                for k in reversed(range(0, row + 1)):
                    p, q, = k, row - k
                    tagd[p][q] = MathTex(f"{p+1}s + {q+1}t", color=YELLOW).scale(0.5).move_to(pasc[p][q].get_center() + TAGD_OFF)
                    self.play(Write(tagd[p][q]), run_time = 0.2 if row < 8 else 0.01)

        with self.voiceover(text="To give a more concrete example"):
            pass

        with self.voiceover(text="Let's say s and t are 2 and 3 respectively"):
            s, t = 2,3
            st = MathTex(f"s = {s}, t = {t}", color=YELLOW).move_to(LEFT * 5.5 + UP * 3.5)
            self.play(Write(st))

        with self.voiceover(text="and calculate the values of all tags"):
            for row in range(0, max_row + 1):
                for k in reversed(range(0, row + 1)):
                    p, q, = k, row - k
                    new_tagd = MathTex(str(s * (p + 1) +t * (q + 1)), color=YELLOW).scale(0.6).move_to(tagd[p][q].get_center())
                    self.play(Transform(tagd[p][q], new_tagd), run_time = 0.2 if row < 8 else 0.01)

        with self.voiceover(text="We also add a blue tag to each number"):
            pass

        with self.voiceover(text="by copying the number from its left shoulder"):
            for row in range(1, max_row + 1):
                for k in reversed(range(0, row)):
                    p, q, = k, row - k
                    tagw[p][q] = pasc[p][q - 1].copy()
                    target = MathTex(str(int(scipy.special.comb(row-1, k))), color=BLUE).scale(0.6).move_to(pasc[p][q].get_center() + TAGW_OFF)
                    self.play(Transform(tagw[p][q], target), run_time = 0.2 if row < 8 else 0.01)

        with self.voiceover(text="By the convention of extended Pascal's triangle, we tag all numbers on the left side with zeros"):
            for row in range(1, max_row + 1):
                k = row
                p, q, = k, row - k
                tagw[p][q] =  MathTex("0", color=BLUE).scale(0.6).move_to(pasc[p][q].get_center() + TAGW_OFF)
                self.play(Write(tagw[p][q]), run_time = 0.3)

        with self.voiceover(text="The only exception is the one on the top, whose blue tag we will leave as undefined"):
            tagw[0][0] = MathTex(r"\mathrm{undef}", color=BLUE).scale(0.6).move_to(pasc[0][0].get_center() + TAGW_OFF)
            self.play(Write(tagw[0][0]))

        internal = []
        external = []
        for row in range(0, max_row + 1):
            for k in reversed(range(0, row + 1)):
                p, q, = k, row - k
                white = int(scipy.special.comb(row, k))
                yellow = s * (p + 1) +t * (q + 1)
                blue = int(scipy.special.comb(row-1, k)) if (p, q) != (0, 0) else 0
                internal.append([p, q, white, yellow, blue])

        internal.sort(key = lambda i: (i[3], i[0]))

        el_between = 0.6
        el_start = 6.5
        with self.voiceover(text="Next, we sort them by the yellow tag in ascending order"):
            self.play(FadeOut(arrow_s, arrow_t, text_s, text_t))
            anime = []
            for i, (p, q, white, yellow, blue) in enumerate(internal):
                pos = i * RIGHT * el_between + LEFT * el_start
                anime += [pasc[p][q].animate.move_to(pos),
                          tagw[p][q].animate.move_to(pos + TAGW_OFF),
                          tagd[p][q].animate.move_to(pos + TAGD_OFF)]
                external.append((pasc[p][q], tagd[p][q], tagw[p][q]))
            self.play(*anime)
            asc_arrow = Arrow(DOWN + LEFT * 6, DOWN + RIGHT * 6, color=YELLOW)
            self.play(Create(asc_arrow))

        with self.voiceover(text="For elements with equal yellow tags"):
            equal_rects = []
            for _, g in itertools.groupby(enumerate(internal), lambda i: i[1][3]):
                g = list(g)
                if len(g) == 1:
                    continue
                left = g[0][0]
                right = g[-1][0]
                equal_rect = Polygon(external[left][1].get_corner(LEFT + UP) + LEFT * 0.1 + UP * 0.1,
                                     external[left][1].get_corner(LEFT + DOWN) + LEFT * 0.1 + DOWN * 0.1,
                                     external[right][1].get_corner(RIGHT + DOWN) + RIGHT * 0.1 + DOWN * 0.1,
                                     external[right][1].get_corner(RIGHT + UP) + RIGHT * 0.1 + UP * 0.1,
                                     color=RED)
                equal_rects.append((left, right, equal_rect))
            self.play(*[Create(e[2]) for e in equal_rects])

        with self.voiceover(text="We merge them by summing up white and blue numbers"):
            anime = []
            for left, right, rect in equal_rects:
                internal[left][4] = int(sum(internal[i][4] for i in range(left, right + 1)))
                internal[left][2] = int(sum(internal[i][2] for i in range(left, right + 1)))
                white_content = str(internal[left][2])
                white_scale = 1.0 if len(white_content) < 3 else 0.6
                anime += [Transform(external[left][0], MathTex(white_content).scale(white_scale).move_to(external[left][0].get_center())),
                          Transform(external[left][2], MathTex(str(internal[left][4]), color=BLUE).scale(0.6).move_to(external[left][2].get_center())),
                          Transform(rect, Polygon(external[left][1].get_corner(LEFT + UP) + LEFT * 0.1 + UP * 0.1,
                                     external[left][1].get_corner(LEFT + DOWN) + LEFT * 0.1 + DOWN * 0.1,
                                     external[left][1].get_corner(RIGHT + DOWN) + RIGHT * 0.1 + DOWN * 0.1,
                                     external[left][1].get_corner(RIGHT + UP) + RIGHT * 0.1 + UP * 0.1,
                                     color=RED))
                ] + \
                [FadeOut(external[i][0], shift = LEFT * (i - left ) * el_between) for i in range(left + 1, right + 1)] + \
                [FadeOut(external[i][1], shift = LEFT * (i - left ) * el_between) for i in range(left + 1, right + 1)] + \
                [FadeOut(external[i][2], shift = LEFT * (i - left ) * el_between) for i in range(left + 1, right + 1)]

            self.play(*anime)

            self.play(FadeOut(*[rect for _, _, rect in equal_rects]))
            for left, right, _ in reversed(equal_rects):
                del internal[left+1:right+1]
                del external[left+1:right+1]

            anime = []
            for i, (white, yellow, blue) in enumerate(external):
                pos = i * RIGHT * el_between + LEFT * el_start
                anime += [
                    white.animate.move_to(pos),
                    blue.animate.move_to(pos + TAGW_OFF),
                    yellow.animate.move_to(pos + TAGD_OFF)
                ]
            self.play(*anime)

        with self.voiceover(text="We can then use these numbers to construct E and w functions"):
            self.play(FadeOut(asc_arrow))
            anime = []
            for white, yellow, blue in external:
                anime += [white.animate.shift(DOWN*3),
                        yellow.animate.shift(DOWN*3),
                        blue.animate.shift(DOWN*3)]
            self.play(*anime)


        with self.voiceover(text="We first focus on white and yellow numbers"):
            cursor = SurroundingRectangle(VGroup(external[0][0], external[0][1]))
            axes = Axes([0, 10, 1], [0, 80, 10], 9, 5).shift(UP * 0.5)
            self.play(Create(cursor), Create(axes))

        with self.voiceover(text=f"The first pair of them is {internal[0][2]} and {internal[0][3]}"):
            pass

        segments = []
        segments_text = []
        epoints = []
        i = 0
        with self.voiceover(text=f"So starting from point one, zero, we draw a vector of horizontal span {internal[i][2]} and slop {internal[i][3]}"):
            pointxy = numpy.array([1, 0])
            point = Dot(axes.coords_to_point(*pointxy))
            start_text = MathTex("(1, 0)").scale(0.6).move_to(point.get_center(), RIGHT+UP)
            self.play(Create(point), Write(start_text))

            pointxy2 = pointxy + numpy.array([internal[i][2], internal[i][2] * internal[i][3]])
            segments.append(Arrow(axes.coords_to_point(*pointxy), axes.coords_to_point(*pointxy2), buff=0))
            stext = MathTex("+(", str(internal[i][2]) , ",", str(internal[i][2]), r"\cdot", str(internal[i][3]) , ")", color=RED).scale(0.6).move_to(segments[-1].get_center(), RIGHT+DOWN)
            stext.submobjects[1].set_color(WHITE)
            stext.submobjects[3].set_color(WHITE)
            stext.submobjects[5].set_color(YELLOW)
            segments_text.append(stext)
            self.play(Create(segments[-1]), Write(segments_text[-1]))
            for n in range(pointxy[0] + 1, pointxy2[0] + 1):
                l = (n - pointxy[0]) / (pointxy2[0] - pointxy[0])
                p = (1-l ) * pointxy + l * pointxy2
                epoints.append(Dot(axes.coords_to_point(*p)))
            pointxy = pointxy2

        with self.voiceover(text="Similarly, for each pair of white and yellow numbers"):
            pass

        with self.voiceover(text="We add a new vector with horizontal span equal to the white number, and slope equal to the yellow number"):
            for i in range(1, 6):
                self.play(Transform(cursor, SurroundingRectangle(VGroup(external[i][0], external[i][1]))))

                pointxy2 = pointxy + numpy.array([internal[i][2], internal[i][2] * internal[i][3]])
                segments.append(Arrow(axes.coords_to_point(*pointxy), axes.coords_to_point(*pointxy2), buff=0))
                stext = MathTex("+(", str(internal[i][2]) , ",", str(internal[i][2]), r"\cdot", str(internal[i][3]) , ")", color=RED).scale(0.6).move_to(segments[-1].get_center(), RIGHT+DOWN)
                stext.submobjects[1].set_color(WHITE)
                stext.submobjects[3].set_color(WHITE)
                stext.submobjects[5].set_color(YELLOW)
                segments_text.append(stext)
                self.play(Create(segments[-1]), Write(segments_text[-1]))
                for n in range(pointxy[0] + 1, pointxy2[0] + 1):
                    l = (n - pointxy[0]) / (pointxy2[0] - pointxy[0])
                    p = (1-l ) * pointxy + l * pointxy2
                    epoints.append(Dot(axes.coords_to_point(*p)))
                pointxy = pointxy2

        with self.voiceover(text="This is the plot of function E"):
            self.play(*[s.animate.set_color(GRAY_E) for s in segments])
            self.play(*[Create(d) for d in epoints])
            hori = MathTex("n").move_to(axes.get_corner(RIGHT + DOWN), LEFT)
            vert = MathTex("E_{s,t}(n)").move_to(axes.get_corner(UP + LEFT), RIGHT)
            self.play(Create(hori), Create(vert))

            self.wait(3)

        self.play(FadeOut(hori, vert, point, axes, start_text), FadeOut(*segments), FadeOut(*epoints), FadeOut(*segments_text))

        with self.voiceover(text="Now we move our focus to white and blue numbers"):
            i = 0
            self.play(Transform(cursor, SurroundingRectangle(VGroup(external[i][0], external[i][2]))))
            axes = Axes([0, 30, 1], [0, 15, 1], 10, 5).shift(UP * 0.5)
            self.play(Create(axes))

        with self.voiceover(text="The first blue number is undefined, so we skip it. This corresponding to the fact that w one is also undefined"):
            pass

        with self.voiceover(text="We start from the point two one"):
            pointxy = numpy.array([2, 1])
            point = Dot(axes.coords_to_point(*pointxy))
            start_text = MathTex("(2, 1)").scale(0.6).move_to(point.get_center(), RIGHT+UP)
            self.play(Create(point), Write(start_text))

        paras = []
        paradots = VGroup()
        with self.voiceover(text="For each pair of white and blue numbers, we draw a parallelogram with horizontal span equal to the white number, and height equal to the yellow number"):
            for i in range(1, 10):
                self.play(Transform(cursor, SurroundingRectangle(VGroup(external[i][0], external[i][2]))))
                pointxy2 = pointxy + numpy.array([internal[i][2], internal[i][4]])
                u = pointxy + numpy.array([internal[i][4], internal[i][4]])
                v = pointxy2 - numpy.array([internal[i][4], internal[i][4]])

                for dx in range(1, internal[i][2] + 1):
                    low = max(0, internal[i][4] - (internal[i][2] - dx))
                    high = min(internal[i][4], dx)
                    for dy in range(low, high + 1):
                        paradots.add(Dot(axes.coords_to_point(dx + pointxy[0], dy + pointxy[1])))

                paras.append(Polygon(axes.coords_to_point(*pointxy),
                                     axes.coords_to_point(*u),
                                     axes.coords_to_point(*pointxy2),
                                     axes.coords_to_point(*v),fill_opacity=0.5, fill_color=GREY, stroke_color=WHITE))
                self.play(Create(paras[-1]))
                pointxy = pointxy2

        with self.voiceover(text="This becomes the plot of the w function"):
            self.play(Create(paradots))

            hori = MathTex("n").move_to(axes.get_corner(RIGHT + DOWN), LEFT)
            vert = MathTex("w_{s,t}(n)").move_to(axes.get_corner(UP + LEFT), RIGHT)
            self.play(Create(hori), Create(vert))

        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

    def construct_scene4(self):
        with self.voiceover("It's time to conclude this video"):
            conclude = Tex("Conclusion").scale(1.5)
            self.play(Write(conclude))

        with self.voiceover("From the binary search problem with a crashing computer"):
            pass

        with self.voiceover("We defined function F and w to represent the time cost and optimal strategy"):
            f_conclude = MathTex("F_{s,t}(n)").shift(DOWN + LEFT * 2)
            self.play(Write(f_conclude))
            w_conclude = MathTex("w_{s,t}(n)").shift(DOWN + RIGHT * 2)
            self.play(Write(w_conclude))

        with self.voiceover("We also defined an auxiliary function E to understand the time cost better"):
            self.play(Transform(f_conclude, MathTex("E_{s,t}(n)").move_to(f_conclude.get_center())))

        with self.voiceover("We found the pattern behind these functions, and a way to compute them"):
            pass

        with self.voiceover("There are still a lot to discover"):
            random1 = MathTex(r"f_{s,t}(x) = \sum_{r}\frac{e^{rx}}{r(se^{tr}+te^{sr})}", color=BLUE).scale(0.8).rotate(PI * 0.1).shift(UP * 2 + LEFT * 4)
            random2 = MathTex(
                r"w_{s,t}^{\mathrm{I}} = \bigg[ \bigg\lceil \sqrt{2\bigg(n - \frac{t}{s}\bigg) + \frac{9}{4}} - \frac{3}{2} \bigg\rceil, \bigg\lfloor \sqrt{2\bigg(n - \frac{t}{s}\bigg) - \frac{7}{4}} + \frac{1}{2} \bigg\rfloor \bigg]"
                , color=BLUE).scale(0.5).rotate(-PI * 0.1).shift(DOWN * 2.5 + RIGHT * 2)
            random3 = MathTex(r"e^{-sr} + e^{-tr} = 1", color=BLUE).scale(0.8).rotate(PI*0.05).shift(DOWN * 2 + LEFT * 3.5)
            random4 = MathTex(r"n_{k|k+1}\sim \frac{(t/s)^{k+1}}{(k+1)!}", color=BLUE).scale(0.8).rotate(-PI*0.15).shift(UP * 1.4 + RIGHT * 3.8)

            self.play(Write(random1))
            self.play(Write(random2))
            self.play(Write(random3))
            self.play(Write(random4))

        with self.voiceover("Perhaps I'll make a second video later."):
            pass

        self.wait(3)
        #self.play(
        #    *[FadeOut(mob)for mob in self.mobjects]
        #)


    def construct(self):

        #self.set_speech_service(AzureService())
        self.set_speech_service(GTTSService())
        self.construct_scene1()
        self.construct_scene2()
        self.construct_scene2_5()
        self.construct_scene3()
        self.construct_scene4()
