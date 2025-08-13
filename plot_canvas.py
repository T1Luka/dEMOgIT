from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

class PlotCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        self.ax = fig.add_subplot(111)
        super().__init__(fig)
        self.setParent(parent)

    def plot(self, X, y, w=None, b=None):
        self.ax.clear()
        if len(X) == 0:
            self.ax.text(0.5,0.5,"Chưa có dữ liệu để hiển thị", ha='center')
            self.draw()
            return

        self.ax.scatter(X[y==1,0], X[y==1,1], c='blue', label='Lớp +1')
        self.ax.scatter(X[y==-1,0], X[y==-1,1], c='red', label='Lớp -1')

        if w is not None and b is not None:
            x_min, x_max = self.ax.get_xlim()
            xs = np.linspace(x_min, x_max, 200)
            ys = -(w[0]*xs + b)/w[1]
            self.ax.plot(xs, ys, 'g-', label='Đường phân tách')

        self.ax.legend()
        self.ax.grid(True)
        self.draw()