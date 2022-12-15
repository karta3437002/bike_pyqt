import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from form import *
from YouBike_json import *
url = "https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json"
json = get_json(url)


class MyMainWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.insert_stage()
        self.show_data()

    def insert_stage(self):
        stage_list = get_stage(json)

        for i, item in enumerate(stage_list):
            self.comboBox_stage.insertItem(i, item)

    def show_data(self):
        stage_name = self.comboBox_stage.currentText()
        data = [x for x in json if x["sna"] == stage_name][0]
        print(data)
        data_time = f'{data["mday"][:4]}-{data["mday"][4:6]}-{data["mday"][6:8]} {data["mday"][8:10]}:{data["mday"][10:12]}:{data["mday"][12:14]}'
        self.label_refresh_time_data.setText(data_time)
        self.label_sno_data.setText(data["sno"])
        self.label_sna_data.setText(data["sna"])
        self.label_ar_data.setText(data["ar"])
        self.label_tot_data.setText(data["tot"])
        self.label_sbi_data.setText(data["sbi"])
        self.label_bemp_data.setText(data["bemp"])









if __name__ == "__main__":


    app = qtw.QApplication(sys.argv)
    myWin = MyMainWindow()

    myWin.show()
    sys.exit(app.exec_())