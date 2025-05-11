from PyQt5 import QtWidgets, QtCore

class CalculatorWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setup_ui()
        
    def setup_ui(self):
        self.layout = QtWidgets.QVBoxLayout(self)
        
        form_layout = QtWidgets.QFormLayout()
        
        self.num1_input = QtWidgets.QLineEdit()
        self.num1_input.setPlaceholderText("enter first number")
        self.num2_input = QtWidgets.QLineEdit()
        self.num2_input.setPlaceholderText("enter second number")
        
        form_layout.addRow("first Number:", self.num1_input)
        form_layout.addRow("second Number:", self.num2_input)
        
        self.calculate_btn = QtWidgets.QPushButton("Calculate Sum")
        self.calculate_btn.clicked.connect(self.calculate_sum)
        
        self.result_label = QtWidgets.QLabel("result: ")
        self.result_label.setAlignment(QtCore.Qt.AlignCenter)
        font = self.result_label.font()
        font.setPointSize(12)
        font.setBold(True)
        self.result_label.setFont(font)
        
        self.layout.addLayout(form_layout)
        self.layout.addWidget(self.calculate_btn)
        self.layout.addWidget(self.result_label)
        
        self.setMinimumSize(300, 200)
    
    def calculate_sum(self):
        try:
            num1 = float(self.num1_input.text())
            num2 = float(self.num2_input.text())
            result = num1 + num2
            self.result_label.setText(f"Result: {result}")
        except ValueError:
            self.result_label.setText("Error: Please enter valid numbers")

class SimpleCalculatorPlugin:
    def __init__(self):
        self.name = 'Calculator'
        self.version = '1.0.0'
        self.description = 'calculator plugin'
        self.author = 'Aathithya Sharan'
        self.widget = None
    
    def register(self):
        self.widget = CalculatorWidget()
        self.widget.show()
        return {
            'name': self.name,
            'version': self.version,
            'description': self.description,
            'author': self.author
        }
    
    def deactivate(self):
        if self.widget:
            self.widget.close()
            self.widget = None

plugin_class = SimpleCalculatorPlugin
