import sys, csv
from PySide.QtGui import *

from PowerSynthGui import *
from PowerSynthAdd import *
from PowerSynthDelete import *
from PowerSynthFind import *
from PowerSynthMain import *

class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):

        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.assignButton()

        self.show()


    def assignButton(self):
        self.FindAndEdt.clicked.connect(self.FindPushed)
        self.AddData.clicked.connect(self.AddPushed)
        self.DeleteData.clicked.connect(self.DeletePushed)

    def FindPushed(self):
        self.nd = FindWindow(self)
        self.nd.show()

    def AddPushed(self):
        self.nd = AddWindow(self)
        self.nd.show()

    def DeletePushed(self):
        self.nd = DeleteWindow(self)
        self.nd.show()


class FindWindow(QDialog, Ui_findDialog):
    def __init__(self, parent=None):
        super(FindWindow, self).__init__(parent)

        self.setupUi(self)

        self.assignButton()

        self.show()

    def assignButton(self):
        self.findButton.clicked.connect(self.buttonPushed)

    def buttonPushed(self):

        with open('input_data.csv', mode = 'rU') as input_data:
            input_reader = csv.reader(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)

            FindWindow.search = self.nameLabel.toPlainText()


            for row in input_reader:
                if (len(row) >= 1):
                    FindWindow.find = row[0]

                    if FindWindow.search==self.find:
                        FindWindow.find1 = row[1]
                        FindWindow.find2 = row[2]
                        self.nd = SetWindow(self)
                        self.nd.show()





class SetWindow(QDialog, Ui_setDialog):
    def __init__(self, parent=FindWindow):


        super(SetWindow, self).__init__(parent)

        self.setupUi(self)

        self.assignButton()

        self.show()

        self.nameEdit.setPlainText(FindWindow.find)
        self.gpaEdit.setPlainText(FindWindow.find1)
        self.schoolEdit.setPlainText(FindWindow.find2)

    def assignButton(self):
        self.setButton.clicked.connect(self.buttonPushed)

    def buttonPushed(self):

        name = self.nameEdit.toPlainText()
        gpa = self.gpaEdit.toPlainText()
        school = self.schoolEdit.toPlainText()

        clean_rows = []

        with open('input_data.csv', mode = 'rU') as input_data:
            input_reader = csv.reader(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)


            for row in input_reader:
                if (len(row) >= 1):
                    find = row[0]

                    if find!=FindWindow.search:

                        clean_rows.append(row)

        with open('input_data.csv', mode='w') as input_data:
            input_writer = csv.writer(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
            input_writer.writerows(clean_rows)

        with open('input_data.csv', mode='a') as input_data:
            input_writer = csv.writer(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
            input_writer.writerow([name, gpa, school])


class AddWindow(QDialog, Ui_Dialog):

    def __init__(self, parent=None):

        super(AddWindow, self).__init__(parent)

        self.setupUi(self)

        self.assignButton()

        self.show()


    def assignButton(self):
        self.addButton.clicked.connect(self.buttonPushed)

    def buttonPushed(self):
        with open('input_data.csv', mode = 'a') as input_data:
            input_writer = csv.writer(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)

            name = self.editName.toPlainText()
            gpa = self.editGPA.toPlainText()
            school = self.editSchool.toPlainText()

            input_writer.writerow([name, gpa, school])

        with open('input_data.csv', mode = 'a') as input_data:
            input_writer = csv.writer(input_data, delimiter=',')

            input_writer.writerow('')



class DeleteWindow(QDialog, Ui_deleteDialog):
    def __init__(self,  parent=None):

        super(DeleteWindow, self).__init__(parent)

        self.setupUi(self)

        self.assignButton()

        self.show()

    def assignButton(self):
        self.deleteButton.clicked.connect(self.buttonPushed)

    def buttonPushed(self):

        remove_word = self.nameLabel.toPlainText()
        clean_rows= []

        with open('input_data.csv', mode = 'rU') as input_data:
            input_reader = csv.reader(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)


            for row in input_reader:
                if (len(row) >= 1):
                    find = row[0]

                    if find!=remove_word:

                        clean_rows.append(row)



        with open('input_data.csv', mode='w') as input_data:
            input_writer = csv.writer(input_data, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, skipinitialspace=True)
            input_writer.writerows(clean_rows)

if __name__ == '__main__':
    app =  QApplication(sys.argv)

    winVar = MainWindow()

    ret=app.exec_()

    sys.exit(ret)