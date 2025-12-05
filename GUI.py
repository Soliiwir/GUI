import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QMessageBox

class Email(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Email Client")
        self.resize(400, 300)

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Label
        self.label = QLabel("Enter your email info below:")
        layout.addWidget(self.label)

        # To field
        self.to_input = QLineEdit()
        self.to_input.setPlaceholderText("To: someone@example.com")
        layout.addWidget(self.to_input)

        # Subject field
        self.subject_input = QLineEdit()
        self.subject_input.setPlaceholderText("Subject")
        layout.addWidget(self.subject_input)

        # Message field
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Write your message here...")
        layout.addWidget(self.message_input)

        # Send button
        self.send_button = QPushButton("Send Email")
        self.send_button.clicked.connect(self.send_email)
        layout.addWidget(self.send_button)

    def send_email(self):
        to = self.to_input.text()
        subject = self.subject_input.text()
        message = self.message_input.toPlainText()

        if not to or not subject or not message:
            QMessageBox.warning(self, "Warning", "Please fill in all fields!")
            return

        # Show a simple pop-up preview
        preview = f"To: {to}\nSubject: {subject}\n\n{message}"
        QMessageBox.information(self, "Email Sent!", preview)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Email()
    window.show()
    sys.exit(app.exec())
