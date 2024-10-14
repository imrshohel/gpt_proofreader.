from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import ListWidget
from ai_proofreading_tool.backend.document_service import DocumentService
from .buttons.action_buttons import NewDocumentButton, DeleteDocumentButton
from .popup_windows.create_document_popup import CreateDocumentPopup
from .dialogues.message_box import ConfirmationDialog

class DocumentManager(QWidget):
    def __init__(self):
        super().__init__()
        self.document_service = DocumentService()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.document_list = ListWidget()
        self.refresh_document_list()
        
        self.new_doc_button = NewDocumentButton()
        self.new_doc_button.clicked.connect(self.create_new_document)
        
        self.delete_doc_button = DeleteDocumentButton()
        self.delete_doc_button.clicked.connect(self.delete_document)
        
        layout.addWidget(self.document_list)
        layout.addWidget(self.new_doc_button)
        layout.addWidget(self.delete_doc_button)
        
        self.setLayout(layout)

    def refresh_document_list(self):
        self.document_list.clear()
        documents = self.document_service.get_all_documents()
        for doc in documents:
            self.document_list.addItem(doc.title)

    def create_new_document(self):
        popup = CreateDocumentPopup(self)
        if popup.exec():
            title = popup.get_title()
            if title:
                self.document_service.create_document(title)
                self.refresh_document_list()

    def delete_document(self):
        current_item = self.document_list.currentItem()
        if current_item:
            title = current_item.text()
            confirm = ConfirmationDialog('Confirm Deletion', f'Are you sure you want to delete "{title}"?', self)
            if confirm.exec() == ConfirmationDialog.DialogCode.Accepted:
                self.document_service.delete_document(title)
                self.refresh_document_list()