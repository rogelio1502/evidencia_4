import sys
from PyQt5 import uic,QtWidgets
from formulario import Ui_RegistroAlumnos,crearBaseDatos,bd

class MyApp:
    def __init__(self):

        self.ventana = QtWidgets.QMainWindow()

        self.ui=Ui_RegistroAlumnos()


        self.ui.setupUi(self.ventana)
        self.ui.fill_table()

        self.ventana.show()

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    # crea una base de datos, hay que configurarla al inicio de formulario
    crearBaseDatos(bd)
    ventana = MyApp()
    app.setStyle("Windows")
    sys.exit(app.exec_())
