from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import TextEdit, PushButton
from ai_proofreading_tool.backend.document_service import DocumentService

class TextEditor(QWidget):
    def __init__(self):
        super().__init__()
        self.document_service = DocumentService()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.editor = TextEdit()
        self.save_button = PushButton('Save')
        self.save_button.clicked.connect(self.save_document)
        
        layout.addWidget(self.editor)
        layout.addWidget(self.save_button)
        
        self.setLayout(layout)

    def load_document(self, document_id):
        document = self.document_service.get_document(document_id)
        if document:
            self.editor.setPlainText(document.content)

    def save_document(self):
        content = self.editor.toPlainText()
        # Assuming we have a way to know which document is currently open
        current_document_id = self.get_current_document_id()
        if current_document_id:
            self.document_service.update_document(current_document_id, content)

    def get_current_document_id(self):
        # This method should be implemented to return the ID of the currently open document
        pass