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
            question1 = Tex("$?$", color=YELLOW)
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
            log_text = Tex(r"$\#(\mbox{test}) = \log(\#(\mbox{changes})$)").shift(DOWN * 2)
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
