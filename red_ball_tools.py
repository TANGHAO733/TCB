import numpy as np
from features_analysis import FeaturesAnalysis


class RedBallTool(FeaturesAnalysis):

    def exclude_overlapping_numbers(self, latest_red_lottery, red_ball_list):
        latest_red_lottery_set = set(latest_red_lottery)
        red_ball_list_set = set(red_ball_list)
        result_set = red_ball_list_set - latest_red_lottery_set
        return list(result_set)

    def side_code(self, latest_red_lottery, red_ball_list):
        red_ball_np = np.array(latest_red_lottery)
        ones = np.ones(len(latest_red_lottery))
        red_ball_np_add_ones = red_ball_np + ones
        print("red_ball_np_add_ones: ", list(red_ball_np_add_ones))
        red_ball_np_sub_ones = red_ball_np - ones
        print("red_ball_np_sub_ones: ", list(red_ball_np_sub_ones))
        red_ball_np_add_list_int = []
        red_ball_np_sub_list_int = []
        for i in range(len(list(red_ball_np_add_ones))):
            red_ball_np_add = int(red_ball_np_add_ones[i])
            if (red_ball_np_add > 0) and (red_ball_np_add <= 33):
                red_ball_np_add_list_int.append(red_ball_np_add)
        for i in range(len(list(red_ball_np_sub_ones))):
            red_ball_np_sub = int(red_ball_np_sub_ones[i])
            if (red_ball_np_sub > 0) and (red_ball_np_sub <= 33):
                red_ball_np_sub_list_int.append(red_ball_np_sub)
        print("red_ball_np_add_list_int: ", red_ball_np_add_list_int)
        print("red_ball_np_sub_list_int: ", red_ball_np_sub_list_int)
        result = list(set(red_ball_np_add_list_int) | set(red_ball_np_sub_list_int))
        print("result: ", result)
        red_ball = list(set(red_ball_list) & set(result))
        return red_ball

    def empty_gate_number(self, red_one_lot, red_two_lot, red_three_lot, red_four_lot, red_five_lot, ball_list, ball_full_list):
        red_lot_result = set(red_one_lot) | set(red_two_lot) | set(red_three_lot) | set(red_four_lot) | set(red_five_lot)
        result = set(ball_full_list) - red_lot_result
        result = list(result | set(ball_list))
        return result
