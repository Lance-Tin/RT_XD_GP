# 额外自定义添加的pyqt界面配置
from PySide6 import QtCharts
from PySide6.QtCore import Qt, QEvent, QPointF
from PySide6.QtWidgets import QComboBox, QWidget, QGraphicsWidget
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
import pyqtgraph as pg


# UI window 创建之后加载 # from GUI.ui_windows_extr import CheckComBox,CustomPlot

class CustomPlot(pg.PlotWidget):

    def __init__(self, parent=None, plotItem=None, **kargs):
        super().__init__(parent=parent, background="w", plotItem=plotItem, **kargs)

        styles = {"color": "k", "font-size": "10px"}
        # self.legend1 = pg.LabelItem(justify='right') # default center
        # self.setLabel("left", "Acc (g/s2)", **styles)
        self.setLabel("bottom", "Time", **styles)
        self.showGrid(x=True, y=True)
        self.setXRange(0, 600, padding=0.5)
        self.setYRange(0, 10, padding=0.1)
        
        self.pen_ch1 = pg.mkPen(color="b", width=1)
        self.pen_ch2 = pg.mkPen(color="g", width=1)
        self.pen_ch3 = pg.mkPen(color="r", width=1)

        self.plot_ch([[0, 0], [0, 0], [0, 0], [0, 600]])

    def plot_ch(self, dataarray, ch=3):
        y1 = dataarray[0]
        y2 = dataarray[1]
        y3 = dataarray[2]
        x = dataarray[3]
        self.addLegend((5,5))
        self.data_line_ch1 = self.plot(x, y1, pen=self.pen_ch1, name='x')
        self.data_line_ch2 = self.plot(x, y2, pen=self.pen_ch2, name='y')
        self.data_line_ch3 = self.plot(x, y3, pen=self.pen_ch3, name='z')


    def update_ch(self, dataarray, ch=3):
        y1 = dataarray[0]# y1 = dataarray[0], y2 = dataarray[1], y3 = dataarray[2], x = dataarray[3]
        y2 = dataarray[1]
        y3 = dataarray[2]
        x = dataarray[3]
        self.data_line_ch1.setData(x, y1)
        self.data_line_ch2.setData(x, y2)
        self.data_line_ch3.setData(x, y3)

    def refreshclear(self):
        self.clear()
        self.plot_ch([[0, 0], [0, 0], [0, 0], [0, 600]])

class CheckComBox(QComboBox):
    def __init__(self, parent):
        super(CheckComBox, self).__init__(parent)

    def addItem(self, item):
        super(CheckComBox, self).addItem(item)
        item = self.model().item(self.count() - 1, 0)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)

    def itemChecked(self, index):
        item = self.model().item(i, 0)
        return item.checkState() == Qt.Checked

    def getCheckItem(self):
        # getCheckItem可以获得选择的项目text
        checkedItems = []
        for index in range(self.count()):
            item = self.model().item(index)
            if item.checkState() == Qt.Checked:
                checkedItems.append(item.text())
        return checkedItems

    def wheelEvent(self, e):
        if e.type() == QEvent.Wheel:
            e.ignore()
