import sys
from PyQt5 import QtWidgets
from functools import partial

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    def cl(n):
            print(n)
    tw = QtWidgets.QTableWidget()
    tw.setColumnCount(3)

    for row in range(3):
        rowPosition = tw.rowCount()
        tw.insertRow(rowPosition)
        tw.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem("col #0"))

        pb = QtWidgets.QPushButton()
        pb.setText("Pushbutton")
        pb.clicked.connect(partial(cl, n=row))
        tw.setCellWidget(rowPosition, 1, pb)
        
        tw.setItem(rowPosition, 2, QtWidgets.QTableWidgetItem("col #2"))
        
    tw.show()
    

    
    
    
    sys.exit(app.exec_())