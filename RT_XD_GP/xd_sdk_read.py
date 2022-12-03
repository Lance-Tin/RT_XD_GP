#
# Example Read shows how to do following things:
# Scan for Xsens DOT Devices
# Use Callbacks to receive found Devices
# "Open the port" Connect to Xsens DOT Device
# Read TagName and Firmware Version from a Connected Xsens DOT Device
# Receive battery notifications on change in Charging state and Level
# Print received error notifications onInternalError
# Read the incoming data from Xsens DOT Device
# Do a Heading Reset
# Clean up
# Example write shows how to do following things:
# Scan for Xsens DOT Devices
# Use Callbacks to receive found Devices
# "Open the port" Connect to Xsens DOT Device
# Read TagName from a Connected Xsens DOT Device
# Write a new tagname to the device using setTagName
# Print received error notifications onInternalError
# Clean up

import time
import os
import asyncio
from threading import Lock
import xsensdot_pc_sdk
from user_settings import *
from collections import defaultdict
from GUI.ui_windows import Ui_MainWindow

class CallbackHandler(xsensdot_pc_sdk.XsDotCallback):
    def __init__(self, max_buffer_size=5):
        # xsensdot_pc_sdk.XsDotCallback.__init__(self)
        super().__init__()
        self.m_detectedDots = list() # 连接列表dot数目
        self.m_errorReceived = False # 接受错误排除
        self.m_maxNumberOfPacketsInBuffer = max_buffer_size # 设置dot最大连接个数，windows为5个
        self.m_packetBuffer = defaultdict(list) # 将xsens dot的名称变成字典key
        self.m_lock = Lock() # 设置线程锁，避免多个线程对同一资源请求修改数据

    def clearDetectedDots(self): # 重置dot
        self.m_detectedDots = list()
        return self.m_detectedDots

    def chooseDetectedDots(self,choose_dots): # 这里进行一些处理，将连接的设备给断开处理（从列表中将未选择的dot remove
        self.m_detectedDots = choose_dots
        return True

    def getDetectedDots(self): # 该方法会连接设备，当设备与后面写的程序中的设备超过一定数量之后，就会报错
        return self.m_detectedDots

    def errorReceived(self):
        return self.m_errorReceived

    def packetsAvailable(self):
        for dev in self.m_detectedDots:
            if self.packetAvailable(dev.bluetoothAddress()) == 0:
                return False
        return True

    def packetAvailable(self, bluetoothAddress):
        self.m_lock.acquire()
        res = len(self.m_packetBuffer[bluetoothAddress]) > 0
        self.m_lock.release()
        return res

    def getNextPacket(self, bluetoothAddress):
        if len(self.m_packetBuffer[bluetoothAddress]) == 0:
            return None
        self.m_lock.acquire()
        oldest_packet = xsensdot_pc_sdk.XsDataPacket(self.m_packetBuffer[bluetoothAddress].pop(0))
        self.m_lock.release()
        return oldest_packet

    def onAdvertisementFound(self, port_info):
        if not whitelist or port_info.bluetoothAddress() in whitelist:
            self.m_detectedDots.append(port_info)
        else:
            print(f"Ignoring {port_info.bluetoothAddress()}")

    def onBatteryUpdated(self, dev, batteryLevel, chargingStatus):
        print(dev.deviceTagName() + f" BatteryLevel: {batteryLevel} Charging status: {chargingStatus}")

    def onError(self, errorString):
        print(f"Error received: {errorString}")
        self.m_errorReceived = True

    def onLiveDataAvailable(self, dev, pack):
        self.m_lock.acquire()
        while len(self.m_packetBuffer[dev.portInfo().bluetoothAddress()]) >= self.m_maxNumberOfPacketsInBuffer:
            self.m_packetBuffer[dev.portInfo().bluetoothAddress()].pop()
        self.m_packetBuffer[dev.portInfo().bluetoothAddress()].append(xsensdot_pc_sdk.XsDataPacket(pack))
        self.m_lock.release()



class MeasureCtrl():
    manager = xsensdot_pc_sdk.XsDotConnectionManager()
    callback = CallbackHandler()
    if manager is None:
        print("Manager could not be constructed, exiting.")
        exit(-1)
    manager.addXsDotCallbackHandler(callback)
    def __init__(self):
        pass
        # self.manager = xsensdot_pc_sdk.XsDotConnectionManager()
        # self.callback = CallbackHandler()
        # if self.manager is None:
        #     print("Manager could not be constructed, exiting.")
        #     exit(-1)
        # self.manager.addXsDotCallbackHandler(self.callback)

    async def asyncgetdevicelist(self,portInfo):
        address = portInfo.bluetoothAddress()
        print(f"Opening DOT with address: @ {address}")
        if not self.manager.openPort(portInfo):  # 与dot建立连接的地方，该操作是耗时的操作
            print(f"Connection to Device {address} failed, retrying...")
            print(f"Device {address} retry connected:")
            if not self.manager.openPort(portInfo):
                print(f"Could not open DOT. Reason: {self.manager.lastResultText()}")

        device = self.manager.device(portInfo.deviceId())
        if device is not None:
            print(f"Found a device with Tag: {device.deviceTagName()} @ address: {address}")
            return device

    async def gdmain(self,cgetDetectedDots):
        tasks = []
        for portInfo in cgetDetectedDots:
            tasks.append(self.asyncgetdevicelist(portInfo))
        results = await asyncio.gather(*tasks)
        return results


    def getdevicelist(self,cgetDetectedDots):
        # Set the device tag name of a device
        deviceList = list()
        sequence_number = 0
        for portInfo in cgetDetectedDots:
            address = portInfo.bluetoothAddress()
            print(f"Opening DOT with address: @ {address}")
            if not self.manager.openPort(portInfo): # 与dot建立连接的地方，该操作是耗时的操作
                print(f"Connection to Device {address} failed, retrying...")
                print(f"Device {address} retry connected:")
                if not self.manager.openPort(portInfo):
                    print(f"Could not open DOT. Reason: {self.manager.lastResultText()}")
                    continue

            device = self.manager.device(portInfo.deviceId())
            if device is None:
                continue

            deviceList.append(device) # 将连接好的devices类添加到列表中
            print(f"Found a device with Tag: {device.deviceTagName()} @ address: {address}")

        return deviceList


    # log记录如果有反向的数据，默认记录为欧拉角模式
    def startrelog(self,device,logdirpath,logoption=xsensdot_pc_sdk.XsLogOptions_Euler):
        # 进行设备数据log记录
        filterProfiles = device.getAvailableFilterProfiles()
        print("Available filter profiles:")
        for f in filterProfiles:
            print(f.label())

        print(f"Current profile: {device.onboardFilterProfile().label()}")
        if device.setOnboardFilterProfile("General"):
            print("Successfully set profile to General")
        else:
            print("Setting filter profile failed!")

        print("Setting log CSV output")
        device.setLogOptions(logoption)  # 设置log数据模式
        logfilename = "logfile_" + device.portInfo().bluetoothAddress().replace(':', '-') + ".csv"
        logfilepath = os.path.join(logdirpath,logfilename)
        print(f"Enable logging to: {logfilepath}")
        if not device.enableLogging(logfilepath):  # 开始数据记录
            print(f"Failed to enable logging. Reason: {self.manager.lastResultText()}")

    # 进行一个异步的开始测试设置，减少log记录文件下的不对齐数据
    async def measurementset(self,device,measuremode=xsensdot_pc_sdk.XsPayloadMode_RateQuantities):
        # 进行实时数据采集
        print("Putting device into measurement mode.")
        if not device.startMeasurement(measuremode):  # 设置数据实时数据采集的模式
            print(f"Could not put device into measurement mode. Reason: {self.manager.lastResultText()}")

    # 控制上面异步的开始测试
    async def msmain(self,deviceList,measuremode):
        tasks = []
        for device in deviceList:
            tasks.append(self.measurementset(device,measuremode))
        await asyncio.gather(*tasks)