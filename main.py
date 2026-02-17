import sys
import os
from PyQt5.QtWidgets import (QApplication, QMainWindow, QTextEdit, QVBoxLayout, 
                             QWidget, QMenuBar, QAction, QFileDialog, QMessageBox,
                             QHBoxLayout, QLabel)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QKeySequence

class SimpleTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.current_file = None
        self.is_modified = False
        self.initUI()
        
    def initUI(self):
        # Set up the main window
        self.setWindowTitle('Simple Text Editor')
        self.setGeometry(100, 100, 800, 600)
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Create the text editor
        self.text_edit = QTextEdit()
        self.text_edit.setFont(QFont("Monospace", 11))
        self.text_edit.textChanged.connect(self.text_changed)
        
        # Create status bar
        self.status_bar = self.statusBar()
        self.update_status()
        
        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        central_widget.setLayout(layout)
        
        # Create menu bar
        self.create_menu_bar()
        
    def create_menu_bar(self):
        menubar = self.menuBar()
        
        # File Menu
        file_menu = menubar.addMenu('File')
        
        new_action = QAction('New', self)
        new_action.setShortcut(QKeySequence.New)
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)
        
        open_action = QAction('Open', self)
        open_action.setShortcut(QKeySequence.Open)
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)
        
        file_menu.addSeparator()
        
        save_action = QAction('Save', self)
        save_action.setShortcut(QKeySequence.Save)
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)
        
        save_as_action = QAction('Save As...', self)
        save_as_action.setShortcut(QKeySequence.SaveAs)
        save_as_action.triggered.connect(self.save_file_as)
        file_menu.addAction(save_as_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction('Exit', self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close_application)
        file_menu.addAction(exit_action)
        
        # Edit Menu
        edit_menu = menubar.addMenu('Edit')
        
        cut_action = QAction('Cut', self)
        cut_action.setShortcut(QKeySequence.Cut)
        cut_action.triggered.connect(self.text_edit.cut)
        edit_menu.addAction(cut_action)
        
        copy_action = QAction('Copy', self)
        copy_action.setShortcut(QKeySequence.Copy)
        copy_action.triggered.connect(self.text_edit.copy)
        edit_menu.addAction(copy_action)
        
        paste_action = QAction('Paste', self)
        paste_action.setShortcut(QKeySequence.Paste)
        paste_action.triggered.connect(self.text_edit.paste)
        edit_menu.addAction(paste_action)
        
        edit_menu.addSeparator()
        
        select_all_action = QAction('Select All', self)
        select_all_action.setShortcut(QKeySequence.SelectAll)
        select_all_action.triggered.connect(self.text_edit.selectAll)
        edit_menu.addAction(select_all_action)
        
    def new_file(self):
        if self.check_unsaved_changes():
            self.text_edit.clear()
            self.current_file = None
            self.is_modified = False
            self.update_status()
            self.update_window_title()
    
    def open_file(self):
        if self.check_unsaved_changes():
            file_path, _ = QFileDialog.getOpenFileName(
                self, 'Open File', '', 
                'Text Files (*.txt);;Python Files (*.py);;All Files (*)'
            )
            
            if file_path:
                try:
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        self.text_edit.setPlainText(content)
                        self.current_file = file_path
                        self.is_modified = False
                        self.update_status()
                        self.update_window_title()
                except Exception as e:
                    QMessageBox.critical(self, 'Error', f'Could not open file:\n{str(e)}')
    
    def save_file(self):
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_file_as()
    
    def save_file_as(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, 'Save File As', '', 
            'Text Files (*.txt);;Python Files (*.py);;All Files (*)'
        )
        
        if file_path:
            self.save_to_file(file_path)
    
    def save_to_file(self, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(self.text_edit.toPlainText())
                self.current_file = file_path
                self.is_modified = False
                self.update_status()
                self.update_window_title()
                self.status_bar.showMessage(f'File saved: {os.path.basename(file_path)}', 2000)
        except Exception as e:
            QMessageBox.critical(self, 'Error', f'Could not save file:\n{str(e)}')
    
    def text_changed(self):
        self.is_modified = True
        self.update_window_title()
    
    def update_window_title(self):
        if self.current_file:
            filename = os.path.basename(self.current_file)
            title = f'{filename}{"*" if self.is_modified else ""} - Simple Text Editor'
        else:
            title = f'Untitled{"*" if self.is_modified else ""} - Simple Text Editor'
        self.setWindowTitle(title)
    
    def update_status(self):
        cursor = self.text_edit.textCursor()
        line = cursor.blockNumber() + 1
        column = cursor.columnNumber() + 1
        
        if self.current_file:
            filename = os.path.basename(self.current_file)
            status_text = f'{filename} | Line: {line}, Column: {column}'
        else:
            status_text = f'Untitled | Line: {line}, Column: {column}'
            
        self.status_bar.showMessage(status_text)
    
    def check_unsaved_changes(self):
        if self.is_modified:
            reply = QMessageBox.question(
                self, 'Unsaved Changes', 
                'You have unsaved changes. Do you want to save them?',
                QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel
            )
            
            if reply == QMessageBox.Yes:
                self.save_file()
                return not self.is_modified  # Return False if save was cancelled
            elif reply == QMessageBox.Cancel:
                return False
                
        return True
    
    def close_application(self):
        if self.check_unsaved_changes():
            self.close()
    
    def closeEvent(self, event):
        if self.check_unsaved_changes():
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    
    # Set application properties
    app.setApplicationName('Simple Text Editor')
    app.setApplicationVersion('1.0')
    
    # Create and show the main window
    editor = SimpleTextEditor()
    editor.show()
    
    # Update cursor position when cursor moves
    editor.text_edit.cursorPositionChanged.connect(editor.update_status)
    
    # Start the application
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()