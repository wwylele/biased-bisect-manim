from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
from manim_voiceover.services.azure import AzureService
import scipy.special

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

        with self.voiceover(text="Starting from this point, I am not going to explain very rigorously, because I don't want the video to be too long."):
            pass

        with self.voiceover(text="And I will start doing that by... computing and plotting the derivative of E"):
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

        with self.voiceover(text="We can see a few flat lines in the plot"):
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

        with self.voiceover(text="Let's also label these flat lines with the value of E prime"):
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

        with self.voiceover(text="We can observe a correspondence between the length of flat lines and the derivatives"):
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

        with self.voiceover(text="We see that the three terms in the equation correspond to three flat lines in the plot"):
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

        with self.voiceover(text="Meanwhile, we can find a point on each line"):
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

        with self.voiceover(text="If we look at the intervals for coordinates of each line"):
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

        with self.voiceover(text="Let's look at another triplet of flat lines"):
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

        with self.voiceover(text="This time, one of the span is zero, as there is no corresponding flat line for the desired E prime"):
            self.play(Circumscribe(LineEw2))

        with self.voiceover(text="We can work out that this happens when the E prime is a multiple of s or t, whose detail I unfortunately can't cover in this video"):
            zero_cond = MathTex(
                r"E_{s,t}' \in \mathbb{Z}^{\ge 2} s \cup \mathbb{Z}^{\ge 2} t \implies \mathrm{Span} = 0",
                color=PURPLE
                ).scale(0.8).move_to(RIGHT * 3.5 + DOWN)
            self.play(Write(zero_cond))

        with self.voiceover(text="Lastly, we notice the very first flat line"):
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
            for k in range(3, 7):
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

        self.wait(3)
        pass


    def construct(self):

        #self.set_speech_service(AzureService())
        self.set_speech_service(GTTSService())
        #self.construct_scene1()
        self.construct_scene2()
