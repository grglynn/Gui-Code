import sys, csv
from PySide.QtGui import *

from work import Ui_Dialog

with open('input_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
    for row in csv_reader:
        input_name = row[0]
        input_gpa = row[1]
        input_school = row[2]

class MainWindow(QMainWindow, Ui_Dialog):

    def __init__(self):

        super(MainWindow, self).__init__()

        self.setupUi(self)

        self.assignButton()

        self.show()

        self.plainTextEdit.setPlainText(input_name)
        self.plainTextEdit_2.setPlainText(input_gpa)
        self.plainTextEdit_3.setPlainText(input_school)

    def assignButton(self):
        self.pushButton.clicked.connect(self.buttonPushed)

    def buttonPushed(self):
        with open('input_data.csv', mode = 'w') as input_data:
            input_writer = csv.writer(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            name = self.plainTextEdit.toPlainText()
            gpa = self.plainTextEdit_2.toPlainText()
            school = self.plainTextEdit_3.toPlainText()

            input_writer.writerow([name, gpa, school])

if __name__ == '__main__':
    app =  QApplication(sys.argv)

    winVar = MainWindow()

    ret=app.exec_()

    sys.exit(ret)