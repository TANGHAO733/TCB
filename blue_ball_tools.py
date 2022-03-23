import pandas as pd

class BlueBallTool:
    file_name = r"TCB.xlsx"
    datas = pd.read_excel(file_name)

    def big_and_small(self, ball_list):
        # print("big_and_small_datas: ", datas)
        big_number = len(self.datas[self.datas["blue"] > 8])
        print("big_number: ", big_number)
        small_number = len(self.datas[self.datas["blue"] <= 8])
        print("small_number: ", small_number)
        big_number_list = []
        small_number_list = []
        for i in range(len(ball_list)):
            ball = ball_list[i]
            if ball > 8:
                big_number_list.append(ball)
            else:
                small_number_list.append(ball)

        if big_number > small_number:
            return big_number_list
        else:
            return small_number_list

    def odd_and_even(self, ball_list):
        odd_number = len(self.datas[self.datas["blue"] % 2 != 0])
        even_number = len(self.datas[self.datas["blue"] % 2 == 0])
        odd_number_list = []
        even_number_list = []
        for i in range(len(ball_list)):
            ball = ball_list[i]
            if ball % 2 != 0:
                odd_number_list.append(ball)
            else:
                even_number_list.append(ball)

        if odd_number > even_number:
            return odd_number_list
        else:
            return even_number_list

    def range_ball(self, ball_list):
        temp_list = []
        range_1_ball = []
        range_2_ball = []
        range_3_ball = []
        range_4_ball = []
        for i in range(len(ball_list)):
            ball = ball_list[i]
            # 1-4/5-8/9-12/13-16
            if ball <= 4:
                range_1_ball.append(ball)
            elif (ball > 4) and (ball <= 8):
                range_2_ball.append(ball)
            elif (ball > 8) and (ball <= 12):
                range_3_ball.append(ball)
            else:
                range_4_ball.append(ball)

        max = 0
        range_1_number = len(self.datas[self.datas["blue"] <= 4])
        print("range_1_number: ", range_1_number)
        range_2_number = len(self.datas[(self.datas["blue"] > 4) & (self.datas["blue"] <= 8)])
        print("range_2_number: ", range_2_number)
        range_3_number = len(self.datas[(self.datas["blue"] > 8) & (self.datas["blue"] <= 12)])
        print("range_3_number: ", range_3_number)
        range_4_number = len((self.datas[self.datas["blue"] > 12]))
        print("range_4_number: ", range_4_number)
        if range_1_number > range_2_number:
            max = range_1_number
            temp_list = range_1_ball
        if range_3_number > max:
            max = range_3_number
            temp_list = range_3_ball
        if range_4_number > max:
            max = range_4_number
            temp_list = range_4_ball
        return temp_list

    def rem_method_3(self, ball_list):
        temp_list = []
        rem_0_ball = []
        rem_1_ball = []
        rem_2_ball = []
        for i in range(len(ball_list)):
            ball = ball_list[i]
            # 1-4/5-8/9-12/13-16
            if ball % 3 == 0:
                rem_0_ball.append(ball)
            elif ball % 3 == 1:
                rem_1_ball.append(ball)
            else:
                rem_2_ball.append(ball)

        max = 0
        rem_0_number = len(self.datas[self.datas["blue"] % 3 == 0])
        rem_1_number = len(self.datas[self.datas["blue"] % 3 == 1])
        rem_2_number = len(self.datas[self.datas["blue"] % 3 == 2])
        if rem_0_number > rem_1_number:
            max = rem_0_number
            temp_list = rem_0_ball
        if rem_2_number > max:
            max = rem_2_number
            temp_list = rem_2_ball
        return temp_list

'''ball_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
blue_ball_tool = BlueBallTool()
ball_list = blue_ball_tool.big_and_small(ball_list)
print(ball_list)
ball_list = blue_ball_tool.odd_and_even(ball_list)
print(ball_list)
ball_list = blue_ball_tool.rem_method_3(ball_list)
print(ball_list)
ball_list = blue_ball_tool.range_ball(ball_list)
print(ball_list)'''

