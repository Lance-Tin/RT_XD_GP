import os
import time
import asyncio
import xsensdot_pc_sdk
from PySide6.QtWidgets import QMainWindow, QFileDialog
from GUI.ui_windows import Ui_MainWindow
from PySide6.QtCore import QThread, Signal  # pyside6里面变成了signal
from xd_sdk_read import MeasureCtrl, CallbackHandler
from user_settings import measuremode_dic

class CtrlWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tlis = []
        self.acc_xyzlis = [[],[],[]]
        self.gyr_xyzlis = [[],[],[]]
        self.MeasureCtrl = MeasureCtrl()
        self.allscan_devicelist = None
        self.fpdia = os.getcwd()  # 默认设置为当前路径

        # 工具栏和按钮绑定
        self.action_setpath.triggered.connect(self.mfileopen)
        self.action_stm.triggered.connect(self.measurethread_start)
        self.action_stop.triggered.connect(self.stopmeasure)
        self.pushButton_startscan.clicked.connect(self.scanthread_start)
        self.pushButton_stopscan.clicked.connect(self.stopscan)
        self.pushButton_refresh.clicked.connect(self.refresh)
        self.pushButton_connect.clicked.connect(self.scanthread_start)

        self.scanthread = ScanThread()
        self.scanthread.scanstextSignal.connect(self.logshow)
        self.scanthread.dotsSignal.connect(self.premeasureset)

        # measurement的设置控件绑定
        self.lineEdit_measuretime.inputRejected.connect(lambda :self.lineEdit_measuretime.setText("input measure time (s)"))
        self.lineEdit_measuretime.returnPressed.connect(self.getlineedit)
        self.comboBox_meauremode.currentIndexChanged.connect(self.getmeasuremode)

        # 一些测试的参数会通过这个地方传入给测试线程
        self.measurethread = MeasureThread()
        self.measurethread.measurelogSignal.connect(self.logshow)  # 数据传输至log端显示
        self.measurethread.measuredataSignal.connect(self.getrawdata) # 数据传输出来处理并绘图

    def refresh(self):
        self.MeasureCtrl.callback.clearDetectedDots()
        self.comboBox_dotlist.clear()
        self.graphicsView_acc.refreshclear()
        self.graphicsView_gyr.refreshclear()
        self.scanthread.connectedDOTCount = 0
        self.scanthread.scan_status = True
        if self.MeasureCtrl.manager is not None:
            self.MeasureCtrl.manager.close()

    def getlineedit(self):
        inputtext = self.lineEdit_measuretime.text()
        if inputtext.isdigit():
            self.measurethread.setmeasuretime = int(inputtext)*1000
            print(self.measurethread.setmeasuretime)
            self.textBrowser.append(f'measure time has been set!=={self.measurethread.setmeasuretime/1000}s')
        else:
            print('please input digital!')
            self.textBrowser.append('please input digital!')

    def getmeasuremode(self):
        comboboxmode = self.comboBox_meauremode.currentText()
        self.measurethread.measuremode = measuremode_dic[comboboxmode]
        self.textBrowser.append(f'measuremode change to =#{comboboxmode}#=!')

    def mfileopen(self):
        self.fpdia = QFileDialog.getExistingDirectory(None, "设置文件存储路径", os.path.join(os.getcwd(),'Data/'))  # 起始路径
        self.measurethread.logdirpath = self.fpdia
        # self.measurethread.logdirpath = os.path.join(self.fpdia,'data/')
        # if not os.path.exists(self.measurethread.logdirpath):
        #     os.mkdir(self.measurethread.logdirpath)
        self.textBrowser.append(f'data save path---【{self.measurethread.logdirpath}】 ')

    # 连接到两个信号，进行扫描和连接两种操作，这里需要对传过来的参数进行一个判断
    def scanthread_start(self):
        if self.sender() == self.pushButton_startscan:
            self.scanthread.scan_status = True
            self.scanthread.connect_status = False
        if self.sender() == self.pushButton_connect:
            self.scanthread.connect_status = True
            self.scanthread.scan_status = False
            self.scanthread.choose_dot_addr = [i for i in self.comboBox_dotlist.getCheckItem()]
        self.scanthread.start()


    def stopscan(self):
        self.scanthread.scan_status = False
        print("Stopped scanning for devices.")
        # 结束扫描之后，就将xsens dot的地址给传到logshow框中显示出来

    def logshow(self, message):
        self.textBrowser.append(message)

    def premeasureset(self, dotmessage):
        '''完成dot的初始化的配置，收集dot的一些基本信息，如电量等信息'''
        if isinstance(dotmessage,str):
            if dotmessage not in self.comboBox_dotlist.getCheckItem():
                self.comboBox_dotlist.addItem(dotmessage)
        if isinstance(dotmessage,dict): # {'choosedevicelist':self.choose_devicelist,'chooseDetectedDots':chooseDetectedDots}
            self.measurethread.choose_devicelist = dotmessage['choosedevicelist']
            # 这里需要将callback上面的 m_detectedDots 对象改成和选择的一致，这个是测试之前的准备工作
            self.MeasureCtrl.callback.chooseDetectedDots(dotmessage['chooseDetectedDots'])

    def measurethread_start(self):
        if len(self.scanthread.choose_devicelist) == 0:
            print('please choose dot to connect first!')
            self.textBrowser.append('please choose dot to connect first!')
            self.measurethread.measurestatus = False
        else:
            self.measurethread.measurestatus = True
            print(f"choosed dots: @{[i for i in self.scanthread.choose_dot_addr]}")
            self.textBrowser.append(f"choosed dots: @{[i for i in self.scanthread.choose_dot_addr]}")
            self.measurethread.start()

    def stopmeasure(self):
        self.measurethread.measurestatus = False
        # self.textBrowser.append(f"stop measurement!")

    def getrawdata(self,data_dic):
        # 后面需要考虑将送过来的原始数据进行什么样的处理，然后绘图等这些，目前仅仅绘制了两个plot
        device_addr = list(data_dic.keys())[0]
        # self.legend1.setText(device_addr)
        xs_t = data_dic[device_addr]['time']
        acc_xyz = data_dic[device_addr]['acc']
        gyr_xyz = data_dic[device_addr]['gyr']
        self.tlis.append(xs_t)
        self.acc_xyzlis.append(self.tlis)
        self.gyr_xyzlis.append(self.tlis)

        # 左边图绘制x方向上的加速度数据
        for i in range(3):
            self.acc_xyzlis[i].append(acc_xyz[i])
        self.graphicsView_acc.setTitle(f'RT Acc from {device_addr}')
        self.graphicsView_acc.setLabel("left", "Acc x (g/s2)",**{"color": "k", "font-size": "10px"})
        self.graphicsView_acc.update_ch(self.acc_xyzlis)

        # 右边图绘制x方向上的角速度数据
        for i in range(3):
            self.gyr_xyzlis[i].append(gyr_xyz[i])
        self.graphicsView_gyr.setTitle(f'RT Gyr from {device_addr}')
        self.graphicsView_gyr.setLabel("left", "Gyr x (rad/s)",**{"color": "k", "font-size": "10px"})
        self.graphicsView_gyr.update_ch(self.gyr_xyzlis)

# 添加一个搜索线程类，用于处理各种耗时的阻塞工作
class ScanThread(QThread):
    scanstextSignal = Signal(str)
    dotsSignal = Signal(object)  # 传递信号的种类

    def __init__(self):
        super().__init__()
        self.connectedDOTCount = 0 # 连接的xensdot数目
        self.scan_status = False
        self.connect_status = False
        self.MesureCtrl = MeasureCtrl()
        self.choose_dot_addr = None
        self.choose_devicelist = []

    def connectchoosedot(self):
        if len(self.choose_dot_addr) == 0:
            self.scanstextSignal.emit('please choose dots first!')
            print('please choose dots first!')
        else:
            st = time.perf_counter()
            self.scanstextSignal.emit('start connect...')
            chooseDetectedDots = []
            getDetectedDots = self.MesureCtrl.callback.getDetectedDots()
            for portInfo in getDetectedDots:
                address = portInfo.bluetoothAddress()
                if address in self.choose_dot_addr:
                    chooseDetectedDots.append(portInfo)
            # devicelist = self.MesureCtrl.getdevicelist(chooseDetectedDots) # 总共时间消耗： 15.603464700000002
            devicelist = asyncio.run(self.MesureCtrl.gdmain(chooseDetectedDots)) # 总共时间消耗： 总共时间消耗： 15.419088600000002
            self.choose_devicelist = devicelist
            # 把选择的原始chooseDetectedDots递上，以及处理过的devicelist递上；准备后续测试
            self.dotsSignal.emit({'choosedevicelist':self.choose_devicelist,'chooseDetectedDots':chooseDetectedDots})
            et = time.perf_counter()
            print('总共时间消耗：',et-st)
            self.scanstextSignal.emit(f"All choosed dots have been connected! you can start measurement!")

    # 开启一个线程用于搜索dots，默认搜索20s（20000）；并且进行处理dot的连接
    def run(self):
        if self.connect_status:
            self.connectchoosedot()
        if self.scan_status:
            print("Scanning for devices...")
            self.MesureCtrl.manager.enableDeviceDetection()
            # xsensdot_pc_sdk.XsTimeStamp_nowMs() - self.MesureCtrl.startTime <= 20000:
            scanstartTime = xsensdot_pc_sdk.XsTimeStamp_nowMs()
            while not self.MesureCtrl.callback.errorReceived() and self.scan_status:
                if not self.scan_status:
                    self.scan_status = False
                    self.MesureCtrl.manager.disableDeviceDetection()
                    break
                time.sleep(0.1)
                scan_time = (xsensdot_pc_sdk.XsTimeStamp_nowMs() - scanstartTime) / 1000
                print(f"\r scan time {scan_time} s...", end="")
                # self.scanstextSignal.emit(f"scan time {scan_time} s...")
                getDetectedDots = self.MesureCtrl.callback.getDetectedDots() # 注意这个一次while循环只能调用一次
                nextCount = len(getDetectedDots)
                if nextCount != self.connectedDOTCount:
                    deviceadress = getDetectedDots[nextCount - 1].bluetoothAddress()
                    print(f"Number of connected DOTs: {nextCount}---@{deviceadress}")
                    self.connectedDOTCount = nextCount
                    self.scanstextSignal.emit(
                        f"scan time {scan_time} s...Number of connected DOTs: {nextCount}---@{deviceadress}")  # 将扫描状态传过去
                    self.scanstextSignal.emit(f'DOT-{nextCount}--{deviceadress}')
            for d in self.MesureCtrl.callback.m_detectedDots:
                self.dotsSignal.emit(d.bluetoothAddress()) # 没有选择的dot递到bombobox里面
            self.scanstextSignal.emit(f'scan complete!')

        return True

# 添加一个数据采集和接受的线程
class MeasureThread(QThread):
    measurestatusSignal = Signal(str)
    measurelogSignal = Signal(str)
    measuredataSignal = Signal(dict)  # 传递信号的种类

    def __init__(self):
        super().__init__()
        self.choose_devicelist = []
        # self.logoption = kwargs['logoption']
        self.setmeasuretime = 7200000
        self.logdirpath = None
        self.measurestatus = False
        self.MesureCtrl = MeasureCtrl()
        self.measuremode = xsensdot_pc_sdk.XsPayloadMode_RateQuantities


    # 判断是否要打开log记录存储（默认存储），设置measure模式，进行测试
    def run(self):
        for device in self.choose_devicelist:
            self.MesureCtrl.startrelog(device, self.logdirpath)
        asyncio.run(self.MesureCtrl.msmain(self.choose_devicelist,measuremode=self.measuremode))  # 设置开始测试模式

        # 设置log头部
        s = ""
        for device in self.choose_devicelist:
            s += f"{device.portInfo().bluetoothAddress():42}"
        print("%s" % s, flush=True)
        self.measurelogSignal.emit(s)  # 将数据头传到log界面
        # 开始测试模块
        orientationResetDone = False
        measuretartTime = xsensdot_pc_sdk.XsTimeStamp_nowMs()
        while xsensdot_pc_sdk.XsTimeStamp_nowMs() - measuretartTime <= self.setmeasuretime:
            if not self.measurestatus:
                # 结束前需要进行一个方向重置
                for device in self.choose_devicelist:
                    print(f"\nResetting heading to default for device {device.portInfo().bluetoothAddress()}: ", end="",
                          flush=True)
                    self.measurelogSignal.emit(
                        f"\nResetting heading to default for device {device.portInfo().bluetoothAddress()}: ")
                    if device.resetOrientation(xsensdot_pc_sdk.XRM_DefaultAlignment):
                        print("OK", end="", flush=True)
                        self.measurelogSignal.emit("OK")
                    else:
                        print(f"NOK: {device.lastResultText()}", end="", flush=True)
                        self.measurelogSignal.emit(f"NOK: {device.lastResultText()}")
                print("\n", end="", flush=True)

                print("\nStopping measurement...")
                self.measurelogSignal.emit("\nStopping measurement...")
                for device in self.choose_devicelist:
                    if not device.stopMeasurement():
                        print("Failed to stop measurement.")
                        self.measurelogSignal.emit("Failed to stop measurement.")
                    if not device.disableLogging():
                        print("Failed to disable logging.")
                        self.measurelogSignal.emit("Failed to disable logging.")
                print("Closing ports...")
                self.measurelogSignal.emit("Closing ports...")
                self.MesureCtrl.manager.close()
                break

            if self.MesureCtrl.callback.packetsAvailable():
                datas = ""
                for device in self.choose_devicelist:
                    # Retrieve a packet
                    device_addr = device.portInfo().bluetoothAddress()
                    data_dic = {device_addr:{}}
                    packet = self.MesureCtrl.callback.getNextPacket(device_addr)
                    # containsRawAcceleration rawAcceleration
                    xs_time = xsensdot_pc_sdk.XsTimeStamp_nowMs() - measuretartTime
                    data_dic[device_addr]['time'] = xs_time
                    # 这里设置数据输入和输出的接口
                    if packet.containsCalibratedAcceleration():
                        acc = packet.calibratedAcceleration() # array
                        datas += f"Acc_x:{acc[0]:7.2f}, Acc_y:{acc[1]:7.2f}, Acc_z:{acc[2]:7.2f}| "
                        data_dic[device_addr]['acc'] = list(acc)
                    if packet.containsCalibratedGyroscopeData():
                        gyr = packet.calibratedGyroscopeData() # array
                        datas += f"Gyr_x:{gyr[0]:7.2f}, Gyr_y:{gyr[1]:7.2f}, Gyr_z:{gyr[2]:7.2f}| "
                        data_dic[device_addr]['gyr'] = list(gyr)
                    # if packet.containsOrientation(): # 目前只设定接受两种数据
                    #     euler = packet.orientationEuler() # array
                    #     datas += f"Roll:{euler[0]:7.2f}, Pitch:{euler[1]:7.2f}, Yaw:{euler[2]:7.2f}| "
                    #     data_dic[device_addr]['euler'] = list(euler)
                print("%s\r" % datas, end="", flush=True)
                self.measurelogSignal.emit(datas)
                self.measuredataSignal.emit(data_dic)


                # 在开始的前5秒进行一个方向重置
                if not orientationResetDone and xsensdot_pc_sdk.XsTimeStamp_nowMs() - measuretartTime >= 5000:
                    for device in self.choose_devicelist:
                        print(f"\nResetting heading for device {device.portInfo().bluetoothAddress()}: ", end="",
                              flush=True)
                        self.measurelogSignal.emit(
                            f"\nResetting heading for device {device.portInfo().bluetoothAddress()}: ")
                        if device.resetOrientation(xsensdot_pc_sdk.XRM_Heading):
                            print("OK", end="", flush=True)
                            self.measurelogSignal.emit("OK")
                        else:
                            print(f"NOK: {device.lastResultText()}", end="", flush=True)
                            self.measurelogSignal.emit(f"NOK: {device.lastResultText()}")
                    print("\n", end="", flush=True)
                    self.measurelogSignal.emit("\n")
                    orientationResetDone = True
        print("\n----------------------over!-------------------", end="", flush=True)
        self.measurelogSignal.emit("\n---------------------over!--------------------")
        return True