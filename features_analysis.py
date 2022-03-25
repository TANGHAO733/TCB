from analysis_tools import AnalysisTool

class FeaturesAnalysis:
    analysis_tool = AnalysisTool()

    def lianma_feature_analysis(self):
        # Number of consecutive code hits
        '''erlian_number = analysis_tool.features_statistics("二连码")
        print("erlian_number: ", erlian_number)
        sanlian_number = analysis_tool.features_statistics("三连码")
        print("sanlian_number: ", sanlian_number)
        silian_number = analysis_tool.features_statistics("四连码")
        print("silian_number: ", silian_number)
        wulian_number = analysis_tool.features_statistics("五连码")
        print("wulian_number: ", wulian_number)
        liulian_number = analysis_tool.features_statistics("六连码")
        print("liulian_number: ", liulian_number)'''
        self.analysis_tool.hit_group_statistics("二连码")

    def tongwei_feature_analysis(self):
        # Number of consecutive code hits
        '''erlian_number = analysis_tool.features_statistics("二连码")
        print("erlian_number: ", erlian_number)
        sanlian_number = analysis_tool.features_statistics("三连码")
        print("sanlian_number: ", sanlian_number)
        silian_number = analysis_tool.features_statistics("四连码")
        print("silian_number: ", silian_number)
        wulian_number = analysis_tool.features_statistics("五连码")
        print("wulian_number: ", wulian_number)
        liulian_number = analysis_tool.features_statistics("六连码")
        print("liulian_number: ", liulian_number)'''
        self.analysis_tool.hit_group_statistics("同位码")


    def big_and_small_analysis(self):
        self.analysis_tool.big_and_small_statistics("red01")
        self.analysis_tool.big_and_small_statistics("red02")
        self.analysis_tool.big_and_small_statistics("red03")
        self.analysis_tool.big_and_small_statistics("red04")
        self.analysis_tool.big_and_small_statistics("red05")
        self.analysis_tool.big_and_small_statistics("red06")

    def odd_and_even_analysis(self):
        self.analysis_tool.odd_and_even_statistics("red01")
        self.analysis_tool.odd_and_even_statistics("red02")
        self.analysis_tool.odd_and_even_statistics("red03")
        self.analysis_tool.odd_and_even_statistics("red04")
        self.analysis_tool.odd_and_even_statistics("red05")
        self.analysis_tool.odd_and_even_statistics("red06")

    '''def lianma(self, sheet_name):
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
        max_comb_index = lianma_comb.index(max(lianma_comb))
        print("max_comb_index: ", max_comb_index)
        ball_list = features_data.iloc[max_comb_index]
        print("ball_list: ", list(ball_list))
        return list(ball_list)'''

    '''def high_and_low_tail_number(self, red_ball_index):
        history_data = pd.read_excel(history_file_name)
        red_data = history_data[["red01", "red02", "red03", "red04", "red05", "red06"]]
        red_data_np = np.array(red_data)
        len_red_data = len(red_data_np)
        print(len_red_data)
        h_red_data = (red_data_np % 10) > 4
        h_data = pd.DataFrame(h_red_data)
        h_data_count = len(h_data[h_data[red_ball_index] == True])
        l_data_count = len(h_data[red_ball_index]) - h_data_count
        if h_data_count > l_data_count:
            features_data = pd.read_excel(features_file_name, sheet_name="h_weima")
        else:
            features_data = pd.read_excel(features_file_name, sheet_name="l_weima")
        len_features_data = len(features_data)
        weima_list = [0 for i in range(len_features_data)]
        for i in range(0, len_red_data):
            red_row_data = red_data[red_ball_index].iloc[i]
            for k in range(0, len_features_data):
                features_row_data = features_data.iloc[k]
                if set(features_row_data).issubset(set(red_row_data)) == True:
                    weima_list[k] = weima_list[k] + 1
        print("weima_list: ", weima_list)
        max_weima_index = weima_list.index(max(weima_list))
        print("max_comb_index: ", max_weima_index)
        ball_list = features_data.iloc[max_weima_index]
        print("ball_list: ", list(ball_list))
        return list(ball_list)'''


fa = FeaturesAnalysis()
fa.odd_and_even_analysis()
'''fa.high_and_low_tail_number(1)
fa.high_and_low_tail_number(2)
fa.high_and_low_tail_number(3)
fa.high_and_low_tail_number(4)
fa.high_and_low_tail_number(5)'''


