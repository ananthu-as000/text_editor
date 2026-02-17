# Simple Text Editor

A lightweight, cross-platform text editor built with Python and PyQt5. This editor provides essential text editing functionality with a clean, intuitive interface.

## Features

- **File Operations**
  - Create new files
  - Open existing files (supports .txt, .py, and all file types)
  - Save and Save As functionality
  - Smart unsaved changes detection

- **Text Editing**
  - Standard editing operations (Cut, Copy, Paste, Select All)
  - Monospace font for code editing
  - Real-time cursor position tracking

- **User Interface**
  - Clean menu system with keyboard shortcuts
  - Status bar showing file info and cursor position
  - Intuitive file dialogs

- **Keyboard Shortcuts**
  - `Ctrl+N` - New file
  - `Ctrl+O` - Open file
  - `Ctrl+S` - Save file
  - `Ctrl+Shift+S` - Save As
  - `Ctrl+Q` - Exit
  - `Ctrl+X` - Cut
  - `Ctrl+C` - Copy
  - `Ctrl+V` - Paste
  - `Ctrl+A` - Select All

## Requirements

- Python 3.6+
- PyQt5

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install PyQt5
   ```

## Usage

Run the text editor:
```bash
python main.py
```

The application will open with a clean interface. You can immediately start typing or use the File menu to open existing documents.

## File Structure

```
text_editor/
├── main.py          # Main application file
├── README.md        # This file
└── .gitignore       # Git ignore rules
```

## Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

Created as a simple demonstration of PyQt5 GUI programming capabilities.