import os
import subprocess
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QWidget,
)


class GradeUpdaterWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.student_ids = []
        self.original_grades = []
        self.corrected_grades = []
        self.selected_file = ''

        self.setWindowTitle("Grade Updater")
        self.resize(820, 600)

        central_widget = QWidget(self)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(24, 24, 24, 24)
        main_layout.setSpacing(16)
        self.setCentralWidget(central_widget)

        title = QLabel("Grade Updater", central_widget)
        title.setObjectName("title")
        main_layout.addWidget(title)

        file_row = QHBoxLayout()
        self.load_button = QPushButton("Load Grades File", central_widget)
        self.load_button.clicked.connect(self.load_file_dialog)
        file_row.addWidget(self.load_button)
        file_row.addStretch()
        main_layout.addLayout(file_row)

        self.table = QTableWidget(50, 3, central_widget)
        self.table.setHorizontalHeaderLabels(
            ["ID", "Original Grades", "Corrected Grades"]
        )
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            self.table.horizontalHeader().ResizeMode.Stretch
        )
        self.table.verticalHeader().setVisible(False)
        self.table.setAlternatingRowColors(True)
        main_layout.addWidget(self.table)

        bonus_row = QHBoxLayout()
        bonus_label = QLabel("Bonus points:", central_widget)
        self.bonus_input = QSpinBox(central_widget)
        self.bonus_input.setRange(0, 1000)
        self.bonus_input.setValue(0)
        self.bonus_input.setKeyboardTracking(False)
        self.bonus_input.editingFinished.connect(self.calculate_corrected_grades)
        bonus_row.addWidget(bonus_label)
        bonus_row.addWidget(self.bonus_input)
        bonus_row.addStretch()
        main_layout.addLayout(bonus_row)

        button_row = QHBoxLayout()
        button_row.addStretch()
        self.about_button = QPushButton("About", central_widget)
        self.about_button.clicked.connect(self.show_about_dialog)
        self.update_button = QPushButton("Update File", central_widget)
        self.update_button.setObjectName("primaryButton")
        self.update_button.clicked.connect(self.update_csv_file)
        button_row.addWidget(self.about_button)
        button_row.addWidget(self.update_button)
        main_layout.addLayout(button_row)

    def load_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Load Grades File",
            "",
            "CSV Files (*.csv)",
        )
        if file_path:
            self.selected_file = file_path
            self.read_csv_data()

    def read_csv_data(self):
        # TODO: Parse the selected CSV and populate the grade data lists.
        pass

    def update_table(self):
        grade_lists = (self.student_ids, self.original_grades, self.corrected_grades)
        row_count = max(50, *(len(values) for values in grade_lists))
        self.table.clearContents()
        self.table.setRowCount(row_count)

        for column, values in enumerate(grade_lists):
            for row, value in enumerate(values):
                self.table.setItem(row, column, QTableWidgetItem(str(value)))

    def calculate_corrected_grades(self):
        # TODO: Apply the bonus points to the original grades.
        pass

    def update_csv_file(self):
        # TODO: Write the corrected grades to the selected CSV file.
        pass

    def show_about_dialog(self):
        dialog = QMessageBox(self)
        dialog.setWindowTitle("About Grade Updater")
        dialog.setTextFormat(Qt.TextFormat.RichText)
        dialog.setTextInteractionFlags(Qt.TextInteractionFlag.TextBrowserInteraction)
        dialog.setText(
            "Jonathan Freedman<br>"
            "Introduction to Mechatronics<br>"
            '<a href="https://github.com/JonathanVuut/mechatronics-hw4-ex1">'
            "GitHub repository</a>"
        )
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()

    def open_file_os(self, file_path):
        if sys.platform == "win32":
            os.startfile(file_path)
        elif sys.platform == "darwin":
            subprocess.run(["open", file_path], check=True)
        else:
            subprocess.run(["xdg-open", file_path], check=True)


def main():
    app = QApplication(sys.argv)
    style_path = os.path.join(os.path.dirname(__file__), "style.qss")
    with open(style_path, encoding="utf-8") as style_file:
        app.setStyleSheet(style_file.read())

    window = GradeUpdaterWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
