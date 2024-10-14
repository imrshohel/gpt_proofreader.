from PySide6.QtWidgets import QPushButton
from qfluentwidgets import PushButton, FluentIcon

class NewDocumentButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("New Document")
        self.setIcon(FluentIcon.ADD)

class DeleteDocumentButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Delete Document")
        self.setIcon(FluentIcon.DELETE)

class SaveDocumentButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Save")
        self.setIcon(FluentIcon.SAVE)

class RefreshSuggestionsButton(PushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Refresh Suggestions")
        self.setIcon(FluentIcon.REFRESH)