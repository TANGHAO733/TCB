from blue_ball_check_method import BlueBallCheckMethod
from red_ball_check_method import RedallCheckMethod

check_blue_method = BlueBallCheckMethod()
check_red_method = RedallCheckMethod()

latest_one_lottery = [[4, 10, 11, 14, 23, 32], [7]]
latest_two_lottery = [[1, 10, 11, 22, 26, 32], [7]]
latest_three_lottery = [[12, 23, 24, 26, 27, 30], [5]]
latest_four_lottery = [[3, 8, 10, 13, 26, 32], [8]]
latest_five_lottery = [[5, 11, 20, 22, 23, 29], [9]]
'''
# 旧
latest_one_lottery = [[1, 10, 11, 22, 26, 32], [7]]
latest_two_lottery = [[12, 23, 24, 26, 27, 30], [5]]
latest_three_lottery = [[3, 8, 10, 13, 26, 32], [8]]
latest_four_lottery = [[5, 11, 20, 22, 23, 29], [9]]
latest_five_lottery = [[14, 15, 18, 19, 26, 32], [9]]'''


blue_ball_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
red_ball_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
small_red_ball_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
big_red_ball_list = [17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
check_blue_ball_list = check_blue_method.check_blue_ball_method_1(blue_ball_list)
print("check_blue_ball_list: ", check_blue_ball_list)
red_one_lot = latest_one_lottery[0]
red_two_lot = latest_two_lottery[0]
red_three_lot = latest_three_lottery[0]
red_four_lot = latest_four_lottery[0]
red_five_lot = latest_five_lottery[0]


blue_lot = latest_one_lottery[1]
check_red_ball_list = check_red_method.check_red_ball_method_1(red_one_lot, red_two_lot, red_three_lot, red_four_lot,
                                                               red_five_lot, red_ball_list, small_red_ball_list,
                                                               big_red_ball_list)
print("check_red_ball_list: ", check_red_ball_list)
print(set([3, 13, 33, 21, 31, 6, 26, 32, 33]))
