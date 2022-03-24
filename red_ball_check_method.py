from red_ball_tools import RedBallTool


class RedallCheckMethod(RedBallTool):

    def check_red_ball_method_1(self, red_one_lot, red_two_lot, red_three_lot, red_four_lot, red_five_lot, red_ball_list):
        ball_list = self.exclude_overlapping_numbers(red_one_lot, red_ball_list)
        ball_list = self.side_code(red_one_lot, ball_list)
        ball_list = self.empty_gate_number(red_one_lot, red_two_lot, red_three_lot, red_four_lot, red_five_lot, ball_list, red_ball_list)
        lianma_list = self.lianma_check("二连码")
        ball_list = list(set(ball_list + lianma_list))
        return ball_list