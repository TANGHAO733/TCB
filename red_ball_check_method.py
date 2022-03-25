from red_ball_tools import RedBallTool


class RedallCheckMethod(RedBallTool):

    def check_red_ball_method_1(self, red_one_lot, red_two_lot, red_three_lot, red_four_lot, red_five_lot, red_ball_list,
                                small_red_ball_list, big_red_ball_list):
        ball_list = self.exclude_overlapping_numbers(red_one_lot, red_ball_list)
        ball_list = self.side_code(red_one_lot, ball_list)
        ball_list = self.empty_gate_number(red_one_lot, red_two_lot, red_three_lot, red_four_lot, red_five_lot, ball_list, red_ball_list)
        erlian_number = self.erlian()
        print("erlian_number: ", erlian_number)
        tongwei_number = self.tongwei()
        print("tongwei_number: ", tongwei_number)
        ball_list = list(set(ball_list + erlian_number + tongwei_number))
        h_number = []
        l_number = []
        for i in range(len(ball_list)):
            ball = ball_list[i]
            if ball % 10 > 4:
                h_number.append(ball)
            else:
                l_number.append(ball)
        red01 = red04 = red06 = l_number
        red02 = red03 = red05 = h_number
        odd_number = []
        even_number = []
        for i in range(len(ball_list)):
            ball = ball_list[i]
            if ball % 2 == 0:
                even_number.append(ball)
            else:
                odd_number.append(ball)
        print("odd_number: ", odd_number)
        print("even_number: ", even_number)


        red_01 = list(set(red01) & set(small_red_ball_list) & set(odd_number))
        red_02 = list(set(red02) & set(small_red_ball_list))
        red_03 = list(set(red03) & set(small_red_ball_list))
        red_04 = list(set(red04) & set(big_red_ball_list))
        red_05 = list(set(red05) & set(big_red_ball_list))
        red_06 = list(set(red06) & set(big_red_ball_list) & set(odd_number))
        print("red01: ", red_01)
        print("red02: ", red_02)
        print("red03: ", red_03)
        print("red04: ", red_04)
        print("red05: ", red_05)
        print("red06: ", red_06)
        '''lianma_list = self.lianma_check("二连码")
        ball_list = list(set(ball_list + lianma_list))
        parity_code = self.lianma_check("同位码")'''
        ball_list = list(set(red_01 + red_02 + red_03 + red_04 + red_05 + red_06))
        return ball_list