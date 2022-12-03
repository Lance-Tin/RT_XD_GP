import sys
from PySide6.QtWidgets import QApplication
from GUI.control_windows import CtrlWindow
# 扫描搜索，选择，连接，设置，测试，关闭

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = CtrlWindow()
    main_window.show()
    sys.exit(app.exec())
