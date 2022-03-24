import pandas as pd

features_file_name = r"features.xlsx"
history_file_name = r"TCB.xlsx"

class FeaturesAnalysis():
    def lianma(self, features_file_name, history_file_name, sheet_name):
        count = 0
        features_data = pd.read_excel(features_file_name, sheet_name=sheet_name)
        history_data = pd.read_excel(history_file_name)
        len_features_data = len(features_data)
        len_history_data = len(history_data)
        red_data = history_data[["red01", "red02", "red03", "red04", "red05", "red06"]]

        for i in range(0, len_history_data):
            red_row_data = red_data.iloc[i]
            for k in range(0, len_features_data):
                features_row_data = features_data.iloc[k]
                if set(features_row_data).issubset(set(red_row_data)) == True:
                    count = count + 1
        return count

    def lianma_check(self, lianma_sheet_name):
        features_data = pd.read_excel(features_file_name, sheet_name=lianma_sheet_name)
        history_data = pd.read_excel(history_file_name)
        len_features_data = len(features_data)
        lianma_comb = [0 for i in range(len_features_data)]

        len_history_data = len(history_data)
        red_data = history_data[["red01", "red02", "red03", "red04", "red05", "red06"]]

        for i in range(0, len_history_data):
            red_row_data = red_data.iloc[i]
            for k in range(0, len_features_data):
                features_row_data = features_data.iloc[k]
                if set(features_row_data).issubset(set(red_row_data)) == True:
                    lianma_comb[k] = lianma_comb[k] + 1
        print("lianma_comb: ", lianma_comb)
        max_comb_index =  lianma_comb.index(max(lianma_comb))
        print("max_comb_index: ", max_comb_index)
        ball_list = features_data.iloc[max_comb_index]
        print("ball_list: ", list(ball_list))
        return list(ball_list)

'''erlian_count = lianma(features_file_name, history_file_name, "二连码")
print("erlian_count: ", erlian_count)'''
'''sanlian_count = lianma(features_file_name, history_file_name, "三连码")
print("sanlian_count: ", sanlian_count)
silian_count = lianma(features_file_name, history_file_name, "四连码")
print("silian_count: ", silian_count)
wulian_count = lianma(features_file_name, history_file_name, "五连码")
print("wulian_count: ", wulian_count)
liulian_count = lianma(features_file_name, history_file_name, "六连码")
print("liulian_count: ", liulian_count)'''
