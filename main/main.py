from PyQt6 import QtCore, QtWidgets, QtGui
import sys
from ui.create import Ui_MainWindow
import random

def button_on_off():
    mas_music = ['EMIL BULLS - Survivor', 'Skillet - Psycho in my Head', ' Король и шут - Лесник', 'RIOT - Overkill', 'Че-то - йоу', 'Валерка - LOVE_R6.']

    if ui.listWidget.count() == 0:
        for el in mas_music:
            ui.listWidget.addItem(el)
    else:
        ui.listWidget.clear()

def button_random():
        items = []
        for i in range(ui.listWidget.count()):
            items.append(ui.listWidget.item(i).text())

        random.shuffle(items)  # random
        ui.listWidget.clear()
        for i in items: 
            ui.listWidget.addItem(i)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv) # Создание приложение

    MainWindow = QtWidgets.QMainWindow() # UI
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    ui.toolButton.clicked.connect(button_on_off)
    ui.button_rand.clicked.connect(button_random)

    sys.exit(app.exec())