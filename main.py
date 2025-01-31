from GUI import MainWindow
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":    
    app = QApplication([])
    window = MainWindow.Window()
    window.show()
    app.exec()