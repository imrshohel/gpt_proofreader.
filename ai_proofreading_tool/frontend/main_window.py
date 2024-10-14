from PySide6.QtWidgets import QMainWindow, QStackedWidget
from qfluentwidgets import (FluentIcon, NavigationInterface, NavigationItemPosition,
                            NavigationWidget, Theme, setTheme)
from ai_proofreading_tool.frontend.components.document_manager import DocumentManager
from ai_proofreading_tool.frontend.components.text_editor import TextEditor
from ai_proofreading_tool.frontend.components.suggestions_panel import SuggestionsPanel
from ai_proofreading_tool.frontend.components.settings_panel import SettingsPanel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Proofreading Tool")
        self.resize(1000, 650)
        setTheme(Theme.DARK)

        # Create main widget and layout
        self.navigation_interface = NavigationInterface(
            self, showMenuButton=True, showReturnButton=True)
        self.stackWidget = QStackedWidget(self)

        # Create and add widgets
        self.document_manager = DocumentManager()
        self.text_editor = TextEditor()
        self.suggestions_panel = SuggestionsPanel()
        self.settings_panel = SettingsPanel()

        self.stackWidget.addWidget(self.document_manager)
        self.stackWidget.addWidget(self.text_editor)
        self.stackWidget.addWidget(self.suggestions_panel)
        self.stackWidget.addWidget(self.settings_panel)

        # Set up navigation
        self.navigation_interface.addItem(
            routeKey='document_manager',
            icon=FluentIcon.DOCUMENT,
            text='Documents',
            onClick=lambda: self.stackWidget.setCurrentWidget(self.document_manager)
        )
        self.navigation_interface.addItem(
            routeKey='text_editor',
            icon=FluentIcon.EDIT,
            text='Editor',
            onClick=lambda: self.stackWidget.setCurrentWidget(self.text_editor)
        )
        self.navigation_interface.addItem(
            routeKey='suggestions',
            icon=FluentIcon.RECOMMEND,
            text='Suggestions',
            onClick=lambda: self.stackWidget.setCurrentWidget(self.suggestions_panel)
        )
        self.navigation_interface.addItem(
            routeKey='settings',
            icon=FluentIcon.SETTING,
            text='Settings',
            onClick=lambda: self.stackWidget.setCurrentWidget(self.settings_panel)
        )

        # Set the central widget
        self.setCentralWidget(self.stackWidget)