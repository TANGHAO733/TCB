import pandas as pd

FEATURES_FILE_NAME = r"features.xlsx"
HISTORY_FILE_NAME = r"TCB.xlsx"

class AnalysisTool:
    features_name = None
    features_data = None
    len_features_data = None

    history_data = None
    len_history_data = None
    red_ball_data = None

    red_01_ball_data = None
    red_02_ball_data = None
    red_03_ball_data = None
    red_04_ball_data = None
    red_05_ball_data = None
    red_06_ball_data = None

    def __init__(self):
        self.history_data = pd.read_excel(HISTORY_FILE_NAME)
        self.len_history_data = len(self.history_data)
        self.red_ball_data = self.history_data[["red01", "red02", "red03", "red04", "red05", "red06"]]
        self.red_01_ball_data = self.red_ball_data["red01"]
        self.red_02_ball_data = self.red_ball_data["red02"]
        self.red_03_ball_data = self.red_ball_data["red03"]
        self.red_04_ball_data = self.red_ball_data["red04"]
        self.red_05_ball_data = self.red_ball_data["red05"]
        self.red_06_ball_data = self.red_ball_data["red06"]

    # Returns the number of times a feature was hit - lianma
    def features_statistics(self, features_name):
        self.features_name = features_name
        self.features_data = pd.read_excel(FEATURES_FILE_NAME, sheet_name=self.features_name)
        self.len_features_data = len(self.features_data)

        count = 0
        for i in range(0, self.len_history_data):
            red_row_data = self.red_ball_data.iloc[i]
            for k in range(0, self.len_features_data):
                features_row_data = self.features_data.iloc[k]
                if set(features_row_data).issubset(set(red_row_data)) == True:
                    count = count + 1
        # print(count)
        return count

    def hit_group_statistics(self, features_name):
        self.features_name = features_name
        self.features_data = pd.read_excel(FEATURES_FILE_NAME, sheet_name=self.features_name)
        self.len_features_data = len(self.features_data)

        hit_one_group = 0
        hit_two_group = 0
        for i in range(0, self.len_history_data):
            red_row_data = self.red_ball_data.iloc[i]
            hit_count = 0
            for k in range(0, self.len_features_data):
                features_row_data = self.features_data.iloc[k]
                if set(features_row_data).issubset(set(red_row_data)) == True:
                    hit_count = hit_count + 1

            if hit_count > 1:
                hit_two_group = hit_two_group + 1
            elif (hit_count > 0) and (hit_count <= 1):
                hit_one_group = hit_one_group + 1
        print("hit_one_group: ", hit_one_group)
        print("hit_two_group: ", hit_two_group)

    # Returns the erlian with the highest hit
    def features_hit(self, sheet_name):
        self.features_name = sheet_name
        self.features_data = pd.read_excel(FEATURES_FILE_NAME, sheet_name=self.features_name)
        self.len_features_data = len(self.features_data)
        hit_count = [0 for i in range(self.len_features_data)]
        for i in range(0, self.len_history_data):
            red_row_data = self.red_ball_data.iloc[i]
            for k in range(0, self.len_features_data):
                features_row_data = self.features_data.iloc[k]
                if set(features_row_data).issubset(set(red_row_data)) == True:
                    hit_count[k] = hit_count[k] + 1
        print("lianma_comb: ", hit_count)
        max_comb_index = hit_count.index(max(hit_count))
        print("max_comb_index: ", max_comb_index)
        return max_comb_index

    def big_and_small_statistics(self, red_ball_one):
        print("++++++++++++++++++++++++++++%s++++++++++++++++++++++++++++++++" % red_ball_one)
        if red_ball_one == "red01":
            big_count = self.red_01_ball_data[self.red_01_ball_data > 16].count()
            small_count = self.red_01_ball_data[self.red_01_ball_data <= 16].count()
            print("big_count: ", big_count)
            print("small_count: ", small_count)
        elif red_ball_one == "red02":
            big_count = self.red_02_ball_data[self.red_02_ball_data > 16].count()
            small_count = self.red_02_ball_data[self.red_02_ball_data <= 16].count()
            print("big_count: ", big_count)
            print("small_count: ", small_count)
        elif red_ball_one == "red03":
            big_count = self.red_03_ball_data[self.red_03_ball_data > 16].count()
            small_count = self.red_03_ball_data[self.red_03_ball_data <= 16].count()
            print("big_count: ", big_count)
            print("small_count: ", small_count)
        elif red_ball_one == "red04":
            big_count = self.red_04_ball_data[self.red_04_ball_data > 16].count()
            small_count = self.red_04_ball_data[self.red_04_ball_data <= 16].count()
            print("big_count: ", big_count)
            print("small_count: ", small_count)
        elif red_ball_one == "red05":
            big_count = self.red_05_ball_data[self.red_05_ball_data > 16].count()
            small_count = self.red_05_ball_data[self.red_05_ball_data <= 16].count()
            print("big_count: ", big_count)
            print("small_count: ", small_count)
        elif red_ball_one == "red06":
            big_count = self.red_06_ball_data[self.red_06_ball_data > 16].count()
            small_count = self.red_06_ball_data[self.red_06_ball_data <= 16].count()
            print("big_count: ", big_count)
            print("small_count: ", small_count)
        else:
            print("ERROR: ", red_ball_one)
        print("++++++++++++++++++++++++++++%s++++++++++++++++++++++++++++++++" % red_ball_one)

    def odd_and_even_statistics(self, red_ball_one):
        print("++++++++++++++++++++++++++++%s++++++++++++++++++++++++++++++++" % red_ball_one)
        if red_ball_one == "red01":
            odd_count = self.red_01_ball_data[self.red_01_ball_data % 2 != 0].count()
            even_count = self.red_01_ball_data[self.red_01_ball_data % 2 == 0].count()
            print("odd_count: ", odd_count)
            print("even_count: ", even_count)
        elif red_ball_one == "red02":
            odd_count = self.red_02_ball_data[self.red_02_ball_data % 2 != 0].count()
            even_count = self.red_02_ball_data[self.red_02_ball_data % 2 == 0].count()
            print("odd_count: ", odd_count)
            print("even_count: ", even_count)
        elif red_ball_one == "red03":
            odd_count = self.red_03_ball_data[self.red_03_ball_data % 2 != 0].count()
            even_count = self.red_03_ball_data[self.red_03_ball_data % 2 == 0].count()
            print("odd_count: ", odd_count)
            print("even_count: ", even_count)
        elif red_ball_one == "red04":
            odd_count = self.red_04_ball_data[self.red_04_ball_data % 2 != 0].count()
            even_count = self.red_04_ball_data[self.red_04_ball_data % 2 == 0].count()
            print("odd_count: ", odd_count)
            print("even_count: ", even_count)
        elif red_ball_one == "red05":
            odd_count = self.red_05_ball_data[self.red_05_ball_data % 2 != 0].count()
            even_count = self.red_05_ball_data[self.red_05_ball_data % 2 == 0].count()
            print("odd_count: ", odd_count)
            print("even_count: ", even_count)
        elif red_ball_one == "red06":
            odd_count = self.red_06_ball_data[self.red_06_ball_data % 2 != 0].count()
            even_count = self.red_06_ball_data[self.red_06_ball_data % 2 == 0].count()
            print("odd_count: ", odd_count)
            print("even_count: ", even_count)
        else:
            print("ERROR: ", red_ball_one)
        print("++++++++++++++++++++++++++++%s++++++++++++++++++++++++++++++++" % red_ball_one)

'''at = AnalysisTool()
at.big_and_small_statistics()'''