from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton
from qfluentwidgets import LineEdit, PushButton

class CreateDocumentPopup(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Create New Document")
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.title_input = LineEdit()
        self.title_input.setPlaceholderText("Enter document title")
        
        self.create_button = PushButton("Create")
        self.create_button.clicked.connect(self.accept)
        
        layout.addWidget(self.title_input)
        layout.addWidget(self.create_button)
        
        self.setLayout(layout)

    def get_title(self):
        return self.title_input.text()