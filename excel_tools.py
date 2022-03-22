import xlwings as xw

file_name = r"TCB.xlsx"
sheet_name = "TCB"
app = xw.App(visible=False)


class ExcelTools:

    @staticmethod
    def create_workbook():
        workbook = app.books.add()
        worksheet = workbook.sheets.add("TCB")
        row_a = ["red01", "red02", "red03", "red04", "red05", "red06", "blue"]
        worksheet.range("A1:G1").value = row_a
        ExcelTools.close_workbook(workbook)

    def additional_data(self, data_list, rows):
        a = "A" + str(rows + 1)
        g = "G" + str(rows + 1)
        worksheet_range = "%s:%s" % (a, g)
        workbook = app.books.open(file_name)
        worksheet = workbook.sheets[sheet_name]
        row_data = data_list
        worksheet.range(worksheet_range).value = row_data
        self.close_workbook(workbook)

    @staticmethod
    def close_workbook(workbook):
        workbook.save(file_name)
        workbook.close()

    @staticmethod
    def get_rows():
        workbook = app.books.open(file_name)
        info = workbook.sheets[sheet_name].used_range
        rows = info.last_cell.row
        return rows

    @staticmethod
    def close_app():
        app.quit()


'''datas = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]]
create_workbook(app, file_name)
for i in range(len(datas)):
    rows = get_rows("TCB")
    data = datas[i]
    additional_data("TCB", data, rows)
app.quit()'''
