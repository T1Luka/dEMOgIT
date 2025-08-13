import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QRadioButton, QMessageBox
from plot_canvas import PlotCanvas
from data_handler import DataHandler
from svm_model import SVMModel
import numpy as np

class SVMApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ứng dụng Phân loại SVM')
        self.setGeometry(200, 200, 700, 600)

        self.data_handler = DataHandler()
        self.svm_model = SVMModel()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.plot_canvas = PlotCanvas(self)
        self.layout.addWidget(self.plot_canvas)

        control_layout = QHBoxLayout()

        self.label_pos = QRadioButton("Lớp +1")
        self.label_pos.setChecked(True)
        self.label_neg = QRadioButton("Lớp -1")

        control_layout.addWidget(self.label_pos)
        control_layout.addWidget(self.label_neg)

        self.train_button = QPushButton("Huấn luyện SVM")
        self.clear_button = QPushButton("Xóa dữ liệu")

        control_layout.addWidget(self.train_button)
        control_layout.addWidget(self.clear_button)

        self.layout.addLayout(control_layout)

        self.info_label = QLabel("Nhấp vào đồ thị để thêm điểm.")
        self.layout.addWidget(self.info_label)

        self.plot_canvas.mpl_connect('button_press_event', self.on_plot_click)
        self.train_button.clicked.connect(self.train_svm)
        self.clear_button.clicked.connect(self.clear_data)

        self.plot_canvas.plot(self.data_handler.X, self.data_handler.y)

    def on_plot_click(self, event):
        if event.xdata is None or event.ydata is None:
            return
        label = 1 if self.label_pos.isChecked() else -1
        point = np.array([[event.xdata, event.ydata]])
        self.data_handler.add_point(point, label)
        self.plot_canvas.plot(self.data_handler.X, self.data_handler.y)
        self.info_label.setText(f"Đã thêm điểm: ({event.xdata:.2f}, {event.ydata:.2f}) - Lớp {label}")

    def train_svm(self):
        if len(self.data_handler.y) == 0:
            QMessageBox.warning(self, "Lỗi", "Chưa có dữ liệu để huấn luyện!")
            return
        self.svm_model.train(self.data_handler.X, self.data_handler.y)
        w, b = self.svm_model.get_params()
        self.plot_canvas.plot(self.data_handler.X, self.data_handler.y, w, b)
        self.info_label.setText("Huấn luyện xong. Đường phân tách đã được vẽ.")

    def clear_data(self):
        self.data_handler.clear()
        self.plot_canvas.plot(self.data_handler.X, self.data_handler.y)
        self.info_label.setText("Dữ liệu đã được xóa.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SVMApp()
    window.show()
    sys.exit(app.exec_())