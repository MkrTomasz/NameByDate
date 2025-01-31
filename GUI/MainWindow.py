from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog

class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(400, 150)

        parentLayout = QVBoxLayout()

        self.label = QLabel("No path selected")
        self.button = QPushButton("Choose folder path")

        self.button.clicked.connect(self.clickButton)

        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)


    def clickButton(self):
        folder_path = str(QFileDialog.getExistingDirectory(self, "Select folders with files to be soreted"))
        if folder_path != "":
            self.label.setText(folder_path)
        else:
            self.label.setText("No path selected")