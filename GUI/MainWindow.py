from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 150)

        parentLayout = QVBoxLayout()

        self.label = QLabel("Test")
        self.button = QPushButton("Click me")

        self.button.clicked.connect(self.clickButton)

        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)


    def clickButton(self):
        folder_path = str(QFileDialog.getExistingDirectory(self, "Select folders with files to be soreted"))
        self.label.setText(folder_path)
    

app = QApplication([])

window = Window()

window.show()
app.exec()