from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService


class Scene1(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))


        with self.voiceover(text="Let's start with a story, inspired by some real experience I had.") as tracker:
            pass

        game_window = Square()

        with self.voiceover(text="One day, I found a cool video game someone made.") as tracker:
            self.play(Create(game_window))

        with self.voiceover(text="I enjoyed it at first, but after a while, the game felt incomplete, and I wanted to add something new to it.") as tracker:
            pass

        with self.voiceover(text=" Thankfully, the game is open sourced, meaning I can download its source code, and recompile it with my modification.") as tracker:
            self.play(game_window.animate.shift(DOWN * 2))
            source_file = Square()
            source_file.shift(UP)
            source_link = Line(source_file.get_bottom(), game_window.get_top())
            self.play(Create(source_file), Create(source_link))

        with self.voiceover(text="I immediately grabbed the source code, made a tiny change to improve it, and I was really happy about it.") as tracker:
            day_zero_group = Group(source_file, source_link, game_window)
            self.remove(source_file, source_link, game_window)
            self.add(day_zero_group)
            self.play(day_zero_group.animate.shift(LEFT * 3))

            source_file1 = Square()
            source_file1.shift(UP)
            change_link1 = Line(source_file.get_right(), source_file1.get_left())
            self.play(Create(source_file1), Create(change_link1))

            game_window1 = Square()
            game_window1.shift(DOWN * 2)
            source_link1 = Line(source_file1.get_bottom(), game_window1.get_top())
            self.play(Create(source_link1), Create(game_window1))

        with self.voiceover(text="The next day, I came up with another little idea, and again made a change to the game.") as tracker:
            source_file2 = Square()
            source_file2.shift(UP + RIGHT * 3)
            change_link2 = Line(source_file1.get_right(), source_file2.get_left())
            self.play(Create(source_file2), Create(change_link2))

            game_window2 = Square()
            game_window2.shift(DOWN * 2 + RIGHT * 3)
            source_link2 = Line(source_file2.get_bottom(), game_window2.get_top())
            self.play(Create(source_link2), Create(game_window2))

        scale_factor = 0.4
        with self.voiceover(text="I continued doing this every day, for a hundred days, and accumulated one hundred little changes to the source code.") as tracker:
            self.remove(day_zero_group,
                        source_file1, change_link1, source_link1, game_window1,
                        source_file2, change_link2, source_link2, game_window2)
            day_012_group = Group(source_file, source_link, game_window,
                                  source_file1, change_link1, source_link1, game_window1,
                                   source_file2, change_link2, source_link2, game_window2)
            self.add(day_012_group)
            self.play(day_012_group.animate.scale(scale_factor).shift(LEFT * 3))

            source_file3 = Square()
            source_file3.scale(scale_factor)
            source_file3.move_to(source_file2.get_center() + RIGHT * scale_factor * 3)

            game_window3 = Square()
            game_window3.scale(scale_factor)
            game_window3.move_to(source_file3.get_center() + DOWN * scale_factor * 3)

            source_link3 = Line(source_file3.get_bottom(), game_window3.get_top())
            change_link3 = Line(source_file2.get_right(), source_file3.get_left())

            self.play(Create(source_file3), Create(game_window3), Create(source_link3), Create(change_link3))

            source_file4 = Square()
            source_file4.scale(scale_factor)
            source_file4.move_to(source_file3.get_center() + RIGHT * scale_factor * 3)

            game_window4 = Square()
            game_window4.scale(scale_factor)
            game_window4.move_to(source_file4.get_center() + DOWN * scale_factor * 3)

            source_link4 = Line(source_file4.get_bottom(), game_window4.get_top())
            change_link4 = Line(source_file3.get_right(), source_file4.get_left())

            self.play(Create(source_file4), Create(game_window4), Create(source_link4), Create(change_link4))

            source_file5 = Text("…", width = 2)
            source_file5.scale(scale_factor)
            source_file5.move_to(source_file4.get_center() + RIGHT * scale_factor * 3)
            change_link5 = Line(source_file4.get_right(), source_file5.get_left() + LEFT * 0.2)

            self.play(Create(source_file5), Create(change_link5))

            source_file6 = Square()
            source_file6.scale(scale_factor)
            source_file6.move_to(source_file5.get_center() + RIGHT * scale_factor * 3)

            game_window6 = Square()
            game_window6.scale(scale_factor)
            game_window6.move_to(source_file6.get_center() + DOWN * scale_factor * 3)

            source_link6 = Line(source_file6.get_bottom(), game_window6.get_top())
            change_link6 = Line(source_file5.get_right() + RIGHT * 0.2, source_file6.get_left())

            self.play(Create(source_file6), Create(game_window6), Create(source_link6), Create(change_link6))

        with self.voiceover(text="Then, someone told me that the game had an easter egg that I never discovered.") as tracker:
            pass

        with self.voiceover(text="I guess I shouldn't be too surprised, as I didn't really explore every corner in the game, nor in the source code.") as tracker:
            pass

        with self.voiceover(text="So I followed a guide to find the easter egg"):
            pass

        with self.voiceover(text="only to find that, for some reason, the game crashed."):
            error = SVGMobject("icon-error.svg", stroke_color=RED, stroke_width = 8)
            error.scale(scale_factor * 0.8).move_to(game_window6.get_center())
            self.play(Create(error))

        with self.voiceover(text="What's made it worse is that it caused a blue screen of death to my computer due to some graphic driver shenanigans."):
            pass

        with self.voiceover(text="I quickly confirmed that the vanilla game did not crash"):
            correct = Text("✓", color=GREEN)
            correct.scale(scale_factor * 3).move_to(game_window.get_center())
            self.play(Create(correct))

        with self.voiceover(text="so the culprit is one of the hundred changes I made"):
            self.play(Indicate(source_file1), Indicate(source_file2), Indicate(source_file3),
                      Indicate(source_file4), Indicate(source_file5), Indicate(source_file6))

        with self.voiceover(text="Unfortunately, I couldn't identify which piece of the code caused the crash, so the most feasible way forward to fix it, was to find the culprit first."):
            question1 = MathTex("?", color=YELLOW)
            question1.scale(scale_factor * 3).move_to(source_file1.get_center())
            question2 = question1.copy().move_to(source_file2.get_center())
            question3 = question1.copy().move_to(source_file3.get_center())
            question4 = question1.copy().move_to(source_file4.get_center())
            question6 = question1.copy().move_to(source_file6.get_center())
            self.play(Create(question1), Create(question2), Create(question3),
                      Create(question4), Create(question6))

        self.wait()


class Scene2(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        N = 20

        with self.voiceover(text="My fellow programmers probably have guessed I was using git, the famous tool to manage source code history,"):
            git_logo = ImageMobject("Git-Logo-White.png")
            git_logo.shift(UP * 3 + LEFT * 3).scale(0.3)
            self.play(FadeIn(git_logo))

            commits = [Circle(0.1, color=WHITE).shift(LEFT * 4)]
            links = []
            self.play(Create(commits[0]), run_time = 0.1)
            for _ in range(N):
                commit = commits[-1].copy().shift(RIGHT * 0.4)
                link = Line(commits[-1].get_right(), commit.get_left())
                self.play(Create(commit), Create(link), run_time = 0.1)
                links.append(link)
                commits.append(commit)

        bug = 13
        markers = []
        with self.voiceover(text="and I was trying to find the first bad commit that introduced the bug"):
            for i in range(N + 1):
                if i < bug:
                    marker = Text("✓", color = GREEN)
                else:
                    marker = Text("✗", color = RED)
                marker.move_to(commits[i].get_center())
                self.play(Create(marker), run_time = 0.1)
                markers.append(marker)

            bug_icon = SVGMobject("bug.svg", stroke_color=WHITE).scale(0.2).move_to(commits[bug].get_bottom() + DOWN * 1)
            bug_arrow = Arrow(bug_icon.get_top(), commits[bug].get_bottom())
            self.play(Create(bug_icon), Create(bug_arrow), Indicate(commits[bug]), Indicate(markers[bug]))

        with self.voiceover(text="There is a tool in git, called git bisect, which allows you quickly find the bad commit."):
            pass

        with self.voiceover(text="If you are not familiar with git, your first reaction might be, just test all versions from the beginning one by one, and you will hit the bad change at some point."):
            self.play(*[FadeOut(marker) for marker in markers[1:-1]])
            self.play(FadeOut(bug_icon), FadeOut(bug_arrow))

            magni = SVGMobject("magnifying.svg", stroke_color=WHITE, stroke_width=2).scale(0.2).move_to(commits[1].get_top() + UP * 1)
            magni_arrow = Arrow(commits[1].get_top() + UP, commits[1].get_top())
            self.play(Create(magni), Create(magni_arrow))
            self.play(Create(markers[1]))

            for i in range(2, bug + 1):
                magni_arrow.target = Arrow(commits[i].get_top() + UP, commits[i].get_top())
                self.play(MoveToTarget(magni_arrow), magni.animate.move_to(commits[i].get_top() + UP * 1), run_time = 0.2)
                self.play(Create(markers[i]), run_time = 0.1)

            self.play(FadeIn(bug_icon), FadeIn(bug_arrow), play_time=0.1)
            self.play(Flash(bug_icon))

        with self.voiceover(text="But if you think a little bit, and recall the algorithm called binary search, you will come up with a better strategy"):
            self.play(*[FadeOut(marker) for marker in markers[1:bug + 1]])
            self.play(FadeOut(bug_icon), FadeOut(bug_arrow), FadeOut(magni_arrow), FadeOut(magni))

        tested_markers = []
        tester = N // 2
        with self.voiceover(text="we first test the change made in the middle"):
            magni_arrow = Arrow(commits[tester].get_top() + UP, commits[tester].get_top())
            magni.move_to(commits[tester].get_top() + UP * 1)
            self.play(Create(magni), Create(magni_arrow))
            self.play(Create(markers[tester]))
            tested_markers.append(markers[tester])

        begin, end = 0, N

        range_rect_h = 0.2
        range_rect = Polygon(commits[begin].get_center() + UP * range_rect_h,
                             commits[begin].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + UP * range_rect_h).set_z_index(-1)

        with self.voiceover(text="and depending on the result, we narrow down our searching range and repeat the process."):
            self.play(FadeIn(range_rect))
            while True:
                if tester >= bug:
                    end = tester
                else:
                    begin = tester
                range_rect.target = Polygon(commits[begin].get_center() + UP * range_rect_h,
                             commits[begin].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + UP * range_rect_h).set_z_index(-1)
                self.play(MoveToTarget(range_rect))
                if end - begin == 1:
                    break

                tester = (begin + end) // 2
                magni_arrow.target = Arrow(commits[tester].get_top() + UP, commits[tester].get_top())
                self.play(MoveToTarget(magni_arrow), magni.animate.move_to(commits[tester].get_top() + UP * 1), run_time = 1.0)
                self.play(Create(markers[tester]))
                tested_markers.append(markers[tester])

        with self.voiceover(text="Eventually, we will narrow down the range to a single change, which is the culprit."):
            self.play(FadeIn(bug_icon), FadeIn(bug_arrow), play_time=0.1)
            self.play(Flash(bug_icon))

        with self.voiceover(text="With binary search, the number of tests we need to perform is logarithmic to the number of total changes"):
            log_text = MathTex(r"\#(\mbox{test}) = \log(\#(\mbox{changes}))").shift(DOWN * 2)
            self.play(Write(log_text))

        with self.voiceover(text="But here is the twist"):
            self.play(*[FadeOut(marker) for marker in tested_markers])
            self.play(FadeOut(log_text), FadeOut(bug_icon), FadeOut(bug_arrow),
                      FadeOut(magni_arrow), FadeOut(magni), FadeOut(range_rect))

        tested_markers = []
        tester = N // 2
        begin, end = 0, N
        range_rect = Polygon(commits[begin].get_center() + UP * range_rect_h,
                             commits[begin].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + UP * range_rect_h).set_z_index(-1)
        with self.voiceover(text="for the particular problem I have, the bug would crash my entire system, and it takes like 10 minutes to reboot and set everything up again. Meanwhile, if a version of the game doesn't crash, it takes only 1 minute to verify it works fine."):
            self.play(FadeIn(range_rect))
            magni_arrow = Arrow(commits[tester].get_top() + UP, commits[tester].get_top())
            magni.move_to(commits[tester].get_top() + UP * 1)
            self.play(Create(magni), Create(magni_arrow))
            self.play(Create(markers[tester]))
            tested_markers.append(markers[tester])

            while True:
                if tester >= bug:
                    end = tester
                else:
                    begin = tester
                range_rect.target = Polygon(commits[begin].get_center() + UP * range_rect_h,
                             commits[begin].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + UP * range_rect_h).set_z_index(-1)
                self.play(MoveToTarget(range_rect))
                if end - begin == 1:
                    break

                tester = (begin + end) // 2
                magni_arrow.target = Arrow(commits[tester].get_top() + UP, commits[tester].get_top())
                self.play(MoveToTarget(magni_arrow), magni.animate.move_to(commits[tester].get_top() + UP * 1), run_time = 1.0)
                self.play(Create(markers[tester]))
                tested_markers.append(markers[tester])
                if tester >= bug:
                    sand_clock = SVGMobject("sand-clock.svg", stroke_color=WHITE, fill_color=WHITE).scale(0.3).move_to(magni.get_right() + RIGHT * 0.5)
                    self.play(FadeIn(sand_clock), run_time = 0.2)
                    for _ in range(3):
                        self.wait(0.5)
                        self.play(Rotate(sand_clock, PI))
                    self.play(FadeOut(sand_clock), run_time = 0.2)

        with self.voiceover(text="There is a significant asymmetry between a successful test and a failed test."):
            self.play(FadeIn(bug_icon), FadeIn(bug_arrow), play_time=0.1)
            self.play(Flash(bug_icon))

        with self.voiceover(text="With this information, do I still want to follow the classical binary search and test the middle point?"):
            self.play(*[FadeOut(marker) for marker in tested_markers])
            self.play(FadeOut(bug_icon), FadeOut(bug_arrow),
                      FadeOut(magni_arrow), FadeOut(magni), FadeOut(range_rect))

        tested_markers = []
        tester = N // 4
        begin, end = 0, N
        range_rect = Polygon(commits[begin].get_center() + UP * range_rect_h,
                             commits[begin].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + UP * range_rect_h).set_z_index(-1)
        with self.voiceover(text="Intuitively, the answer is no, and I'd like to do more tests that are likely successful, so I spend less time rebooting my computer. I want to test an earlier change somewhere off the center, because it is less likely that the bad change made it in early on."):
            self.play(FadeIn(range_rect))
            magni_arrow = Arrow(commits[tester].get_top() + UP, commits[tester].get_top())
            magni.move_to(commits[tester].get_top() + UP * 1)
            self.play(Create(magni), Create(magni_arrow))
            self.play(Create(markers[tester]))
            tested_markers.append(markers[tester])

            while True:
                if tester >= bug:
                    end = tester
                else:
                    begin = tester
                range_rect.target = Polygon(commits[begin].get_center() + UP * range_rect_h,
                             commits[begin].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + DOWN * range_rect_h,
                             commits[end].get_center() + UP * range_rect_h).set_z_index(-1)
                self.play(MoveToTarget(range_rect))
                if end - begin == 1:
                    break

                tester = max((end - begin) // 4 + begin, begin + 1)
                magni_arrow.target = Arrow(commits[tester].get_top() + UP, commits[tester].get_top())
                self.play(MoveToTarget(magni_arrow), magni.animate.move_to(commits[tester].get_top() + UP * 1), run_time = 1.0)
                self.play(Create(markers[tester]))
                tested_markers.append(markers[tester])
                if tester >= bug:
                    sand_clock = SVGMobject("sand-clock.svg", stroke_color=WHITE, fill_color=WHITE).scale(0.3).move_to(magni.get_right() + RIGHT * 0.5)
                    self.play(FadeIn(sand_clock), run_time = 0.2)
                    for _ in range(1):
                        self.wait(0.5)
                        self.play(Rotate(sand_clock, PI))
                    self.play(FadeOut(sand_clock), run_time = 0.2)

            self.play(FadeIn(bug_icon), FadeIn(bug_arrow), play_time=0.1)
            self.play(Flash(bug_icon))

        with self.voiceover(text="Now the question to ask is: what my strategy should be to minimize my total time?"):
            question = Text("What's the optimal strategy?").shift(DOWN * 2)
            self.play(Write(question))


        self.wait()

class Scene3(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        with self.voiceover(text="We want to minimize the total time, so let's see how to calculate it first."):
            pass

        with self.voiceover(text="We use F to represent the expected total time"):
            f_text = MathTex("F")
            self.play(Write(f_text))

        with self.voiceover(text="F is a function of three inputs"):
            f_text2 = MathTex("F", "(", "n", ",", "s", ",", "t", ")")
            self.play(TransformMatchingTex(f_text, f_text2))

        with self.voiceover(text="n, the total number of changes made to the program"):
            self.play(Indicate(f_text2.get_part_by_tex("n")))

        with self.voiceover(text="s, the time taken by a successful test"):
            self.play(Indicate(f_text2.get_part_by_tex("s")))

        with self.voiceover(text="and t, the time taken by a failed test"):
            self.play(Indicate(f_text2.get_part_by_tex("t")))

        with self.voiceover(text="Here I'd like to use a notation where I put s and t as subscripts of F"):
            f_text3 = MathTex("{{F}}_{ {{s}},{{t}} }", "(", "n", ")")
            self.play(TransformMatchingTex(f_text2, f_text3))

        with self.voiceover(text="This is just to signify they play a different role from the input n, but mathematically they are still inputs of the function F"):
            pass

        with self.voiceover(text="It's often a good idea to start with small cases. "):
            self.play(f_text3.animate.shift(UP * 3))

        with self.voiceover(text="What is the value of F when n is one?"):
            f_n1 = MathTex("{{F}}_{ {{s}},{{t}} }", "(", "1", ")", "=", "?")
            f_n1.get_part_by_tex("?").set_color(YELLOW)
            self.play(TransformMatchingTex(f_text3.copy(), f_n1, transform_mismatches=True))


        commits = []
        commits_desc = []
        markers = []
        links = []

        good = Text("✓", color = GREEN)
        bad = Text("✗", color = RED)

        commit_down = DOWN * 0.5

        desc_right = RIGHT * 1

        with self.voiceover(text="Well, this is very easy, as n equal to one means I have made only one change to the code, "):
            self.play(f_n1.animate.shift(RIGHT * 3))
            commits.append(Circle(0.1, color=WHITE).shift(LEFT * 5 + UP))
            commits_desc.append(Tex("Original", font_size=36).move_to(commits[-1].get_right() + desc_right, LEFT))
            self.play(Create(commits[-1]), Write(commits_desc[-1]), run_time=0.2)

            commits.append(commits[-1].copy().shift(commit_down))
            commits_desc.append(Tex("Change $1$", font_size=36).move_to(commits[-1].get_right() + desc_right, LEFT))
            links.append(Line(commits[-2].get_bottom(), commits[-1].get_top()))
            self.play(Create(links[-1]), run_time=0.2)
            self.play(Create(commits[-1]), Write(commits_desc[-1]), run_time=0.2)

            markers = [good.copy().move_to(commits[0]), bad.copy().move_to(commits[1])]
            self.play(Create(markers[0]), run_time=0.2)
            self.play(Create(markers[1]), run_time=0.2)

        with self.voiceover(text="which is the only possible culprit"):
            bug_icon = SVGMobject("bug.svg", stroke_color=WHITE).scale(0.2).move_to(commits[-1].get_left(), RIGHT)
            self.play(FadeIn(bug_icon), Flash(bug_icon))

        with self.voiceover(text="Hence F equals zero, as I didn't need to do any test"):
            f_n1_2 = MathTex("{{F}}_{ {{s}},{{t}} }", "(", "1", ")", "=", "0").move_to(f_n1)
            self.play(TransformMatchingTex(f_n1, f_n1_2, transform_mismatches=True))

        with self.voiceover(text="What about when n equals two?"):
            self.play(FadeOut(commits[0]), FadeOut(commits[1]),
                      FadeOut(commits_desc[0]), FadeOut(commits_desc[1]),
                      FadeOut(markers[0]), FadeOut(markers[1]),
                      FadeOut(bug_icon), FadeOut(links[0]), run_time = 0.5)
            self.play(f_n1_2.animate.shift(UP * 2))
            f_n2 = MathTex("{{F}}_{ {{s}},{{t}} }", "(", "2", ")", "=", "?")
            f_n2.get_part_by_tex("?").set_color(YELLOW)
            self.play(TransformMatchingTex(f_text3.copy(), f_n2, transform_mismatches=True))

        with self.voiceover(text="Now I have made two code changes"):
            self.play(f_n2.animate.shift(RIGHT * 3))
            commits.append(commits[-1].copy().shift(commit_down))
            commits_desc.append(Tex("Change $2$", font_size=36).move_to(commits[-1].get_right() + desc_right, LEFT))
            links.append(Line(commits[-2].get_bottom(), commits[-1].get_top()))

            self.play(Create(commits[0]), Write(commits_desc[0]), run_time=0.2)
            self.play(Create(links[0]), run_time=0.2)
            self.play(Create(commits[1]), Write(commits_desc[1]), run_time=0.2)
            self.play(Create(links[1]), run_time=0.2)
            self.play(Create(commits[2]), Write(commits_desc[2]), run_time=0.2)

            markers = [good.copy().move_to(commits[0]),
                       bad.copy().move_to(commits[2])]
            self.play(Create(markers[0]), run_time=0.2)
            self.play(Create(markers[1]), run_time=0.2)
            pass

        with self.voiceover(text=" and I want to know which of them introduced the bug."):
            bug_icon_left = LEFT
            bug_icon_question_left = LEFT * 0.5
            bug_icon.move_to(commits[1].get_left() + bug_icon_left, RIGHT)
            bug_icon_question = MathTex('?')
            bug_icon_question.move_to(commits[1].get_left() + bug_icon_question_left, RIGHT)
            self.play(FadeIn(bug_icon), FadeIn(bug_icon_question))
            current = 1
            for _ in range(4):
                current = 3 - current
                self.play(bug_icon.animate.move_to(commits[current].get_left() + bug_icon_left, RIGHT),
                          bug_icon_question.animate.move_to(commits[current].get_left() + bug_icon_question_left, RIGHT),
                          play_time = 0.3)

            pass

        with self.voiceover(text="Or perhaps both of them introduced some bugs?"):
            current = 3 - current
            self.wait(2)
            bug_icon2 = bug_icon.copy()
            bug_icon_question2 = bug_icon_question.copy()
            self.play(bug_icon2.animate.move_to(commits[current].get_left() + bug_icon_left, RIGHT),
                      bug_icon_question2.animate.move_to(commits[current].get_left() + bug_icon_question_left, RIGHT),
                      play_time = 0.3)
            pass

        with self.voiceover(text="OK, this can soon get out of hand, so let's clarify an assumption"):
            self.play(FadeOut(bug_icon), FadeOut(bug_icon_question),
                      FadeOut(bug_icon2), FadeOut(bug_icon_question2))

        with self.voiceover(text="there will always be exactly one bug introduced by one code change, and every changes I made are equally possible to be the culprit"):
            pass


        commits_b = [x.copy() for x in commits]
        markers_b = [x.copy() for x in markers]
        links_b = [x.copy() for x in links]
        with self.voiceover(text="So in this case, either the first or the second change is the culprit,"):
            right = RIGHT * 4
            self.play(*[x.animate.shift(right) for x in commits_b],
                      *[x.animate.shift(right) for x in markers_b],
                      *[x.animate.shift(right) for x in links_b])
            markers.append(bad.copy().move_to(commits[1]))
            markers_b.append(good.copy().move_to(commits_b[1]))
            bug_icon.move_to(commits[1].get_left(), RIGHT)
            bug_icon2.move_to(commits_b[2].get_right(), LEFT)
            self.play(FadeIn(bug_icon), FadeIn(bug_icon2))
            self.play(Create(markers[2]), run_time=0.2)
            self.play(Create(markers_b[2]), run_time=0.2)

        with self.voiceover(text='And their probability are both fifty percent'):
            p1 = MathTex(r"P = ", r"\frac{1}{2}\phantom{}")
            p2 = MathTex(r"P = ", r"\frac{1}{2}")
            p1.move_to(commits[2].get_bottom() + DOWN * 2)
            p2.move_to(commits_b[2].get_bottom() + DOWN * 2)
            self.play(Write(p1), Write(p2))

        with self.voiceover(text='To determine which case it is, we only need to test the first change'):
            test_rect = Rectangle(height = 0.5, width = 6.5, color=YELLOW).move_to((commits[1].get_center() + commits_b[1].get_center()) / 2)
            magni = SVGMobject("magnifying.svg", stroke_color=YELLOW, stroke_width=2).scale(0.2).move_to(test_rect.get_left() + LEFT * 0.2, RIGHT)
            self.play(Create(test_rect), Create(magni))

        with self.voiceover(text='If this test crashes my computer, the time cost will be t'):
            cost = MathTex(r"\mbox{cost} = ", "t").move_to(commits[2].get_center() + DOWN)
            self.play(FadeIn(cost, shift=DOWN))

        with self.voiceover(text='Otherwise, the time cost will be s'):
            cost2 = MathTex(r"\mbox{cost} = ", "s").move_to(commits_b[2].get_center() + DOWN)
            self.play(FadeIn(cost2, shift=DOWN))

        with self.voiceover(text='But you might say, wait, there should be no cost at all.'):
            pass

        with self.voiceover(text="since we immediately get the result from the testing, we don't need to wait for computer reboot or anything"):
            overlap = LEFT * 0.15
            cost_zero = MathTex(r"⁄  0?",color=YELLOW).move_to(cost.get_right() + overlap, LEFT)
            cost2_zero = MathTex(r"⁄  0?",color=YELLOW).move_to(cost2.get_right() + overlap, LEFT)
            self.play(Write(cost_zero), Write(cost2_zero))

        with self.voiceover(text="I'd say, that's reasonable, but I still need to wait for it to continue my other work on the computer, "):
            pass

        with self.voiceover(text='so we always count the cost here.'):
            self.play(Unwrite(cost_zero), Unwrite(cost2_zero))

        with self.voiceover(text='The final answer to the total expected cost will be the sum of cost in each case multiplied by the probability.'):
            pass

        with self.voiceover(text='which, for n equals two, is half of s plus half of t'):
            f_n2_2 = MathTex("{{F}}_{ {{s}},{{t}} }", "(", "2", ")", "=", r"\frac{1}{2}", "s", "+", r"\frac{1}{2}\phantom{}", "t")
            f_n2_2.move_to(f_n2.get_left(), LEFT)
            self.play(TransformMatchingTex(Group(f_n2, p1, p2, cost, cost2), f_n2_2))

        with self.voiceover(text='When n is larger than two, there are multiple versions I can test, and the optimal strategy becomes important'):
            self.play(FadeOut(magni), FadeOut(test_rect), *[FadeOut(x) for x in markers + markers_b],
                      FadeOut(commits_desc[1]), FadeOut(commits_desc[2]),
                      FadeOut(bug_icon), FadeOut(bug_icon2))
            commits_desc = [commits_desc[0]]
            self.play(*[x.animate.shift(UP * 1.4) for x in commits + commits_b + links + links_b + commits_desc])
            for _ in range(4):
                commits.append(commits[-1].copy().shift(commit_down))
                commits_b.append(commits_b[-1].copy().shift(commit_down))
                links.append(Line(commits[-2].get_bottom(), commits[-1].get_top()))
                links_b.append(Line(commits_b[-2].get_bottom(), commits_b[-1].get_top()))
                self.play(Create(links[-1]), Create(links_b[-1]), run_time=0.2)
                self.play(Create(commits[-1]), Create(commits_b[-1]), run_time=0.2)
            commits_desc.append(Tex("Change $n$", font_size=36).move_to(commits[-1].get_right() + desc_right, LEFT))
            self.play(Write(commits_desc[-1]))

            markers = [good.copy().move_to(commits[0]), bad.copy().move_to(commits[-1])]
            markers_b = [good.copy().move_to(commits_b[0]), bad.copy().move_to(commits_b[-1])]
            self.play(Create(markers[0]), Create(markers[1]), Create(markers_b[0]), Create(markers_b[1]), run_time=0.2)

        with self.voiceover(text='Oh by the way, I should mention that my computer is not capable of running multiple tests in parallel, so I must perform tests sequentially'):
            pass

        w = 3
        with self.voiceover(text="Let's say I start with testing the version after w changes."):
            commits_desc.append(Tex("Change $w$", font_size=36).move_to(commits[w].get_right() + desc_right, LEFT))
            self.play(Write(commits_desc[-1]))
            test_rect = Rectangle(height = 0.5, width = 6.5, color=YELLOW).move_to((commits[w].get_center() + commits_b[w].get_center()) / 2)
            magni = SVGMobject("magnifying.svg", stroke_color=YELLOW, stroke_width=2).scale(0.2).move_to(test_rect.get_left() + LEFT * 0.2, RIGHT)
            self.play(Create(test_rect), Create(magni))

        with self.voiceover(text='The outcome is either failure or success'):
            markers.append(bad.copy().move_to(commits[w]))
            markers_b.append(good.copy().move_to(commits_b[w]))
            self.play(Create(markers[-1]))
            self.play(Create(markers_b[-1]))

        with self.voiceover(text='Indicating the first bad change is either among the first w changes'):
            brace = Brace(Group(*commits[1:w + 1]), LEFT)
            bug_icon.move_to(brace.get_left(), RIGHT)
            self.play(Create(brace), FadeIn(bug_icon))

        with self.voiceover(text='or among the rest n minus w changes.'):
            brace_b = Brace(Group(*commits_b[w + 1:]), RIGHT)
            bug_icon2.move_to(brace_b.get_right(), LEFT)
            self.play(Create(brace_b), FadeIn(bug_icon2))

        with self.voiceover(text='Therefore, the probability for each case'):
            pass

        with self.voiceover(text='is w over n'):
            p1 = MathTex(r"P = ", r"\frac{w}{n}")
            p1.move_to(commits[-1].get_bottom() + DOWN * 2)
            self.play(Write(p1))

        with self.voiceover(text='or n minus w over n, respectively'):
            p2 = MathTex(r"P = ", r"\frac{n-w}{n}")
            p2.move_to(commits_b[-1].get_bottom() + DOWN * 2)
            self.play(Write(p2))

        with self.voiceover(text="As for the cost, we again spend t or s time on each case"):
            cost = MathTex(r"\mbox{cost} = ", "t").move_to(commits[-1].get_center() + DOWN)
            self.play(FadeIn(cost, shift=DOWN))

            cost2 = MathTex(r"\mbox{cost} = ", "s").move_to(commits_b[-1].get_center() + DOWN)
            self.play(FadeIn(cost2, shift=DOWN))

        with self.voiceover(text="But remember, this is only for the first test. "):
            pass

        with self.voiceover("We need to continue searching after narrowing down the range"):
            self.play(Indicate(brace), Indicate(brace_b))
            pass

        with self.voiceover(text="The time cost for the rest of tests can again be expressed by the function F"):
            self.play(Indicate(f_text3))

        with self.voiceover(text="Specifically, we will add F of w, and F of n minus w, to each case respectively"):
            cost_new = MathTex(r"\mbox{cost} = ", "t", r"+F_{s,t}(w)").move_to(cost.get_center()).scale(0.8)
            cost2_new = MathTex(r"\mbox{cost} = ", "s", r"+F_{s,t}(n - w)").move_to(cost2.get_center()).scale(0.8)
            self.play(TransformMatchingTex(cost, cost_new))
            self.play(TransformMatchingTex(cost2, cost2_new))

        with self.voiceover(text="Combining both cases, we get the expected cost for starting with testing change w"):
            total_cost = MathTex(r"\frac{w}{n}", "(", "t", r"+F_{s,t}(w)", ") + ", r"\frac{n-w}{n}",  "(", "s", r"+F_{s,t}(n - w)", ")")
            total_cost.shift(DOWN * 3)
            self.play(TransformMatchingTex(Group(p1, p2, cost_new, cost2_new), total_cost))

        with self.voiceover(text="The value of F of n, is therefore the minimal value of this expected cost among all possible choice of w"):
            total_f = MathTex(r"F_{s,t}(n) = ", r"\min_{ {{1\le w\le n-1}} }\Big\{", r"\frac{w}{n}", "(", "t", r"+F_{s,t}(w)", ") + ", r"\frac{n-w}{n}",  "(", "s", r"+F_{s,t}(n - w)", ")", r"\Big\}")
            total_f.move_to(total_cost.get_center())
            self.play(TransformMatchingTex(total_cost, total_f))


        with self.voiceover(text="Here the range for w is all n changes except for the last one, because we already know the last version is broken"):
            self.play(Indicate(total_f.get_part_by_tex(r"1\le w<n")))

        with self.voiceover(text="We also notice the n equal to 2 case can be merged with the general formula"):
            self.play(Indicate(f_n2_2))
            self.play(FadeOut(f_n2_2, target_position = total_f.get_center()))

        with self.voiceover(text="Putting these together, we get a recurrence relation that fully defines the function F"):
            self.play(*[FadeOut(x) for x in commits + commits_b + links + links_b + commits_desc + markers + markers_b],
                      FadeOut(test_rect), FadeOut(magni), FadeOut(brace), FadeOut(brace_b), FadeOut(bug_icon), FadeOut(bug_icon2))

            total_f_new = MathTex(r"F_{s,t}(n) = ", r"\min_{ 1\le w\le n-1 }\Big\{\frac{w}{n}(t+F_{s,t}(w)) + \frac{n-w}{n}(s+F_{s,t}(n - w))\Big\}")
            total_f_new.move_to(total_f.get_center())
            self.remove(total_f)
            self.add(total_f_new)

            final_f2 = MathTex(r"\min_{ 1\le w\le n-1 }\Big\{\frac{w}{n}(t+F_{s,t}(w)) + \frac{n-w}{n}(s+F_{s,t}(n - w))\Big\}").scale(0.8)
            final_f2.shift(RIGHT * 0.2 + UP)
            final_f2_c = MathTex(r"(n \ge 2)").move_to(final_f2.get_right() + RIGHT * 0.5, LEFT)
            final_f1 = MathTex(r"0").move_to(final_f2.get_top() + UP * 0.2, DOWN).align_to(final_f2, LEFT)
            final_f1_c = MathTex(r"(n = 1)").move_to(final_f2_c.get_top() + UP * 0.2, DOWN)
            final_brace = Brace(Group(final_f1, final_f2), LEFT)
            final_left = MathTex(r"F_{s,t}(n) = ").move_to(final_brace.get_left(), RIGHT)
            self.play(TransformMatchingTex(Group(f_text3, f_n1_2, total_f_new),
                                           Group(final_left, final_f1, final_f2, final_f1_c, final_f2_c)),
                    Create(final_brace))

        with self.voiceover(text="And since our goal is to find the best strategy, let's also define a function w, which is the value w we choose when finding the minimal value in F"):
            final_w = MathTex(r"w_{s,t}(n) = \{\mbox{The optimal $w$ in the $F_{s,t}(n)$ formula}\}").shift(DOWN)
            self.play(Write(final_w))

        with self.voiceover(text="In the next section, we will study the properties of these functions, and see if the formula can be simplified."):
            pass
