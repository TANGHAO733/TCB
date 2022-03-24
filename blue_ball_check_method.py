import pandas as pd
from blue_ball_tools import BlueBallTool


class BlueBallCheckMethod(BlueBallTool):

    def check_blue_ball_method_1(self, ball_list):
        # print("datas: ", datas)
        ball_list =self.big_and_small(ball_list)
        print(ball_list)
        ball_list = self.odd_and_even(ball_list)
        print(ball_list)
        ball_list = self.rem_method_3(ball_list)
        print(ball_list)
        ball_list = self.range_ball(ball_list)
        print(ball_list)
        return ball_list

