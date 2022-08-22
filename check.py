import pandas as pd

file_name = "TCB_2022092.xlsx"
df = pd.read_excel(file_name, sheet_name=None)
print(list(df))

for i in range(len(list(df))):
    new_df = pd.read_excel(file_name, sheet_name=i)
    # print("sheet_name: ", i)
    print("RED01: ", new_df["BLUE"].value_counts())