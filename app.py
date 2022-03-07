import sys

from PyQt5.QtTest import QTest
from PyQt5.QtWidgets import QApplication, QMainWindow

from design import Ui_MainWindow
from gerador_e_validador_cpf import valida_cpf


class CPFGenerator(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.setFixedSize(300, 190)
        self.showCpfGer.setReadOnly(True)

        self.btnGer.clicked.connect(self.generate_cpf)
        self.btnVld.clicked.connect(self.validate_cpf)
        self.btnClear.clicked.connect(self.clear_fields)

    def generate_cpf(self):
        cpf_generated = valida_cpf()
        self.showCpfGer.setText(cpf_generated)
        self.labelValid.setText('CPF GERADO COM SUCESSO!')
        QTest.qWait(5000)
        self.labelValid.setText('')

    def validate_cpf(self):
        cpf_inserted = self.inputCpfVld.text()
        cpf_validated = valida_cpf(cpf_inserted)

        if not cpf_validated:
            self.labelInvalid.setText('CPF INVÁLIDO!')
            QTest.qWait(5000)
            self.labelInvalid.setText('')
        else:
            self.labelValid.setText('CPF VÁLIDO!')
            QTest.qWait(5000)
            self.labelValid.setText('')

    def clear_fields(self):
        self.showCpfGer.setText('')
        self.inputCpfVld.setText('')
        self.labelValid.setText('')
        self.labelInvalid.setText('')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    cpf_generator = CPFGenerator()
    cpf_generator.show()
    qt.exec_()
