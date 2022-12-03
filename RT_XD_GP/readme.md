Xsens_DOT实时数据采集分析软件
==

(Xsens DOT real time data collection for PC)



 ![GPlogo](E:\FlFile\LSTM-GRF\PRE-GUI\XSENS_DOT_RS\Resources\GPlogo.png)RT XD GP
==

Support system：

* windows 10+
* environment: python3.9+

Installation
--

Download this repositories, and ```pip install -r requirements.txt```

Also, you need go to [XSENS Software Downloads ](https://www.xsens.com/software-downloads) to download the xsens dot SDK for python 



Quick Start
--

* Enter the main path

* Clicke the ```main.py``` run or using the command```python main.py```

* Then follow the following steps to collect data

* > ```set path``` 
  >
  > ```scan devices```
  >
  > ``` stop scan```
  >
  > Choose specific dots ```connect```
  >
  > ```input measure time```
  >
  > ```start measurement```

![scan](./Resources/scan.gif)

![choose_dots](./Resources/choose_dots.gif)

![connect](./Resources/connect.gif)

![measure](./Resources/measure.gif)



To Do
--

* Add different data collection modes
* Add ground reaction forces prediction module
* Improve drawing function

