from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import ListWidget, PushButton
from ai_proofreading_tool.backend.suggestion_service import SuggestionService

class SuggestionsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.suggestion_service = SuggestionService()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.suggestions_list = ListWidget()
        self.refresh_button = PushButton('Refresh Suggestions')
        self.refresh_button.clicked.connect(self.refresh_suggestions)
        
        layout.addWidget(self.suggestions_list)
        layout.addWidget(self.refresh_button)
        
        self.setLayout(layout)

    def refresh_suggestions(self):
        self.suggestions_list.clear()
        # Assuming we have a way to know which document is currently open
        current_document_id = self.get_current_document_id()
        if current_document_id:
            suggestions = self.suggestion_service.get_suggestions(current_document_id)
            for suggestion in suggestions:
                self.suggestions_list.addItem(suggestion)

    def get_current_document_id(self):
        # This method should be implemented to return the ID of the currently open document
        pass