# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'AddSuspect.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

from Classes.CriminalRecord import CriminalRecord
from Classes.Involved import Involved

curr_dir = os.path.dirname('systemdb\Classes\Suspect.py')
parent_dir = os.path.dirname(curr_dir)
sys.path.insert(0, parent_dir)
from Classes.Case import Case
from Classes.Suspect import Suspect



class AddSuspect(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("AddSuspect")
        self.resize(1007, 678)
        self.gridLayout_2 = QtWidgets.QGridLayout(self)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.SuspectFirstNameField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectFirstNameField.setFont(font)
        self.SuspectFirstNameField.setObjectName("SuspectFirstNameField")
        self.gridLayout.addWidget(self.SuspectFirstNameField, 6, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 6, 1, 1, 1)
        self.SuspectCriminalRecordField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectCriminalRecordField.setFont(font)
        self.SuspectCriminalRecordField.setObjectName("SuspectCriminalRecordField")
        self.gridLayout.addWidget(self.SuspectCriminalRecordField, 14, 2, 1, 1)
        self.SuspectLastNameField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectLastNameField.setFont(font)
        self.SuspectLastNameField.setObjectName("SuspectLastNameField")
        self.gridLayout.addWidget(self.SuspectLastNameField, 7, 2, 1, 1)
        self.SuspectIDField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectIDField.setFont(font)
        self.SuspectIDField.setObjectName("SuspectIDField")
        self.gridLayout.addWidget(self.SuspectIDField, 3, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 12, 0, 1, 1)
        self.SuspectDOBField = QtWidgets.QDateEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectDOBField.setFont(font)
        self.SuspectDOBField.setObjectName("SuspectDOBField")
        self.gridLayout.addWidget(self.SuspectDOBField, 8, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 16, 2, 1, 1)
        self.SuspectPhoneRecordField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectPhoneRecordField.setFont(font)
        self.SuspectPhoneRecordField.setObjectName("SuspectPhoneRecordField")
        self.gridLayout.addWidget(self.SuspectPhoneRecordField, 10, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 2, 2, 1, 1)
        self.label = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 8, 0, 1, 1)
        self.SuspectAddrZIPField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectAddrZIPField.setFont(font)
        self.SuspectAddrZIPField.setObjectName("SuspectAddrZIPField")
        self.gridLayout.addWidget(self.SuspectAddrZIPField, 13, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        self.SuspectAddrStreetField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectAddrStreetField.setFont(font)
        self.SuspectAddrStreetField.setObjectName("SuspectAddrStreetField")
        self.gridLayout.addWidget(self.SuspectAddrStreetField, 11, 2, 1, 1)
        self.SuspectGenderFIeld = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectGenderFIeld.setFont(font)
        self.SuspectGenderFIeld.setObjectName("SuspectGenderFIeld")
        self.gridLayout.addWidget(self.SuspectGenderFIeld, 9, 2, 1, 1)
        self.SuspectAddrGovField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectAddrGovField.setFont(font)
        self.SuspectAddrGovField.setObjectName("SuspectAddrGovField")
        self.gridLayout.addWidget(self.SuspectAddrGovField, 12, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.AddSuspectDataBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.AddSuspectDataBtn.setFont(font)
        self.AddSuspectDataBtn.setObjectName("AddSuspectDataBtn")
        self.gridLayout.addWidget(self.AddSuspectDataBtn, 17, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 11, 0, 1, 1)
        self.BackBtn = QtWidgets.QPushButton(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.BackBtn.setFont(font)
        self.BackBtn.setObjectName("BackBtn")
        self.gridLayout.addWidget(self.BackBtn, 17, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 13, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 6, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 6, 0, 1, 1)
        self.SuspectCaseIDField = QtWidgets.QLineEdit(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuspectCaseIDField.setFont(font)
        self.SuspectCaseIDField.setObjectName("SuspectCaseIDField")
        self.gridLayout.addWidget(self.SuspectCaseIDField, 15, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 14, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 15, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 3, 3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 0, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 1, 4, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 4, 1, 1, 1)

        self.AddSuspectDataBtn.clicked.connect(self.add_suspect)

        self.retranslateUi()


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "self"))
        self.label_10.setText(_translate("self", "Phone Record"))
        self.label_9.setText(_translate("self", "Gender"))
        self.label_2.setText(_translate("self", "Suspect ID"))
        self.label_7.setText(_translate("self", "Address Gov"))
        self.label_5.setText(_translate("self", "First Name"))
        self.label_4.setText(_translate("self", "Address Street"))
        self.label_3.setText(_translate("self", "DOB"))
        self.label_6.setText(_translate("self", "Last Name"))
        self.BackBtn.setText(_translate("self", "Back"))
        self.label.setText(_translate("self", "Add Suspect"))
        self.AddSuspectDataBtn.setText(_translate("self", "Add"))
        self.label_8.setText(_translate("self", "Address ZIP"))
        self.label_11.setText(_translate("self", "Criminal Record"))
        self.label_12.setText(_translate("self", "Case ID"))
    
    def add_suspect(self):
        suspect_id = self.SuspectIDField.text()
        first_name = self.SuspectFirstNameField.text()
        last_name = self.SuspectLastNameField.text()
        gender = self.SuspectGenderFIeld.text()
        dob = self.SuspectDOBField.text()
        phone_record = self.SuspectPhoneRecordField.text()
        street = self.SuspectAddrStreetField.text()
        government = self.SuspectAddrGovField.text()
        zip = self.SuspectAddrZIPField.text()
        criminal_record = self.SuspectCriminalRecordField.text()
        case_id = self.SuspectCaseIDField.text()
        
        if suspect_id == '' or first_name == '' or last_name == '' or gender == '' or dob == '' or phone_record == '' or street == '' or government == '' or zip == '':
            QtWidgets.QMessageBox.warning(self, 'Error', 'Please enter all fields')
            return 
        try:
            suspect_id = int(suspect_id)
        except:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Suspect ID must be an integer')
            return
        
        try:
            case_id = int(case_id)
        except:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Case ID must be an integer')
            return
        tmp = Suspect.get_all()
        tmp = [x[0] for x in tmp]

        tmpCases = Case.get_all()
        tmpCases = [x[0] for x in tmpCases]
        
        if case_id not in tmpCases:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Case ID does not exist')
            return

        if suspect_id in tmp:
            QtWidgets.QMessageBox.warning(self, 'Error', 'Suspect ID already exists')
            return
        
        suspect = Suspect(suspect_id, first_name, last_name, gender, dob, phone_record, street, government, zip)
        criminal_record = CriminalRecord(suspect_id,criminal_record)
        involved_in = Involved(suspect_id, case_id)
        involved_in.insert_into_database()
        suspect.insert_into_database()
        criminal_record.insert_into_database()
        QtWidgets.QMessageBox.warning(self, 'Sucess', 'Suspect is Added Successfully')
        self.SuspectIDField.clear()
        self.SuspectFirstNameField.clear()
        self.SuspectLastNameField.clear()
        self.SuspectGenderFIeld.clear()
        self.SuspectDOBField.clear()
        self.SuspectPhoneRecordField.clear()
        self.SuspectAddrStreetField.clear()
        self.SuspectAddrGovField.clear()
        self.SuspectAddrZIPField.clear()


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     self = QtWidgets.QWidget()
#     ui = Ui_self()
#     ui.setupUi(self)
#     self.show()
#     sys.exit(app.exec_())
