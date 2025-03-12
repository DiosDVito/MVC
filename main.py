import sys
from PyQt5.QtWidgets import QApplication

from Controller.entry_controller import EntryController
from View.entry_view import EntryView

def main():
    app = QApplication(sys.argv)

    # Ventana inicial con botones: Login / Register
    entry_controller = EntryController()
    entry_view = EntryView(entry_controller)
    entry_controller.set_view(entry_view)

    entry_view.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
