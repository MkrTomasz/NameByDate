from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog
from PyQt6.QtGui import QIcon
from MainPackage.MetaExtract import MetaProcessor


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.folder_path = "No path selected"

        self.setMinimumSize(400, 150)

        parentLayout = QVBoxLayout()

        self.label = QLabel(self.folder_path)
        self.path_button = QPushButton("Choose folder path")
        self.run_button = QPushButton("Run")

        self.path_button.clicked.connect(self.clickPathButton)
        self.run_button.clicked.connect(self.clickRunButton)

        parentLayout.addWidget(self.label)
        parentLayout.addWidget(self.path_button)
        parentLayout.addWidget(self.run_button)

        centerWidget = QWidget()
        centerWidget.setLayout(parentLayout)
        self.setCentralWidget(centerWidget)
        self.setWindowTitle("NameByDate")
        self.setWindowIcon(QIcon("GUI/Image.png"))


    def clickPathButton(self):
        self.folder_path = str(QFileDialog.getExistingDirectory(self, "Select folders with files to be soreted"))
        if self.folder_path:
            self.label.setText(self.folder_path)
            return self.folder_path
        else:
            self.label.setText("No path selected")
            return self.folder_path


    def clickRunButton(self):
        processor = MetaProcessor(self.folder_path)
        try: 
            processor.renameFiles()
        except OSError:
            pass
