from PySide6.QtWidgets import QWidget, QVBoxLayout
from qfluentwidgets import ComboBox, PushButton, LineEdit
from ai_proofreading_tool.utils.prompt_factory import PromptFactory
from ai_proofreading_tool.backend.user_service import UserService

class SettingsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.prompt_factory = PromptFactory()
        self.user_service = UserService()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()
        
        self.ai_service_combo = ComboBox()
        self.ai_service_combo.addItems(['OpenAI', 'Claude AI', 'Google AI', 'Groq', 'Ollama'])
        self.ai_service_combo.currentIndexChanged.connect(self.update_ai_service)
        
        self.api_key_input = LineEdit()
        self.api_key_input.setPlaceholderText('Enter API Key')
        self.save_api_key_button = PushButton('Save API Key')
        self.save_api_key_button.clicked.connect(self.save_api_key)
        
        self.prompt_combo = ComboBox()
        self.prompt_combo.addItems(self.prompt_factory.get_all_prompts().keys())
        self.prompt_combo.currentIndexChanged.connect(self.load_prompt)
        
        self.prompt_edit = LineEdit()
        self.save_prompt_button = PushButton('Save Prompt')
        self.save_prompt_button.clicked.connect(self.save_prompt)
        self.reset_prompt_button = PushButton('Reset Prompt')
        self.reset_prompt_button.clicked.connect(self.reset_prompt)
        
        layout.addWidget(self.ai_service_combo)
        layout.addWidget(self.api_key_input)
        layout.addWidget(self.save_api_key_button)
        layout.addWidget(self.prompt_combo)
        layout.addWidget(self.prompt_edit)
        layout.addWidget(self.save_prompt_button)
        layout.addWidget(self.reset_prompt_button)
        
        self.setLayout(layout)

    def update_ai_service(self):
        selected_service = self.ai_service_combo.currentText()
        self.user_service.update_ai_service(selected_service)

    def save_api_key(self):
        api_key = self.api_key_input.text()
        self.user_service.save_api_key(api_key)

    def load_prompt(self):
        prompt_name = self.prompt_combo.currentText()
        prompt_content = self.prompt_factory.get_prompt(prompt_name)
        self.prompt_edit.setText(prompt_content)

    def save_prompt(self):
        prompt_name = self.prompt_combo.currentText()
        prompt_content = self.prompt_edit.text()
        self.prompt_factory.save_user_prompt(prompt_name, prompt_content)

    def reset_prompt(self):
        prompt_name = self.prompt_combo.currentText()
        self.prompt_factory.reset_prompt(prompt_name)
        self.load_prompt()