# WaterMarkPrinter
A PIL based adjustable batch watermark addition command-line tool

## 简介

自用的基于Python PIL库的批量水印添加命令行工具。该工具有以下几个特点：
1. 适用于大批量图片的水印添加。
2. 水印会根据图片的尺寸自动调整大小。
3. 支持调整水印尺寸大小，位置和透明度。

## 开始使用

### 安装依赖
在命令行中运行以下代码，安装依赖
```
pip install pillow
pip install numpy

```

### 如何使用
```
python WaterMarkPrinter.py path watermark [-x {start,center,end}] [-y {start,center,end}] [-i OFFSETX] [-j OFFSETY] [-t TRANSPARENCY] [-s SCALE]
```


**执行该命令行工具需要传入两个必要参数`path`和`watermark`，以下是对相关参数的解释：**

`path`: 传入图片所在的文件夹地址

`watermark`: 传入水印地址

***

**此外，还可以通过传入一些选项来控制水印的表现形式，以下是对相关参数的解释：**

`-x`或`--alignx`: 控制水印在x轴的对齐方式，支持三个参数：`start` 左边，`center` 居中，`end` 右边，默认传入`start`

`-y`或`--aligny`: 控制水印在y轴的对齐方式，支持三个参数：`start` 顶部，`center` 居中，`end` 底部，默认传入`start`

`-i`或`--offsetx`: 控制水印在x轴的偏移量，取值-100-100，与对齐方式可以叠加，默认传入0，它与`-x`或`--alignx`的区别如下:

* `-i 0`或`--offsetx 0`等价于`-x start`或`--alignx start`

* `-i 50`或`--offsetx 50`等价于`-x center`或`--alignx center`

* `-i 100`或`--offsetx 100`等价于`-x end`或`--alignx end`

* `-x end -i -100`或`--alignx end --offsetx -100`等价于`-x start`或`--alignx start`

`-j`或`--offsety`: 控制水印在y轴的偏移量，建议取值-200-200，与对齐方式可以叠加，默认传入0，它与`-y`或`--aligny`的区别如下:

* `-j 0`或`--offsety 0`等价于`-y start`或`--aligny start`

* `-j 50`或`--offsety 50`等价于`-y center`或`--aligny center`

* `-j 100`或`--offsety 100`等价于`-y end`或`--aligny end`

* `-y end -j -100`或`--aligny end --offsety -100`等价于`-y start`或`--aligny start`

`-t`或`--transparency`: 控制水印的透明度，取值0.0-1.0，默认传入1

`-s`或`--scale`: 控制水印的尺寸，取值0.0-1.0，默认传入1

***

**原图**

<div style="display: flex;">
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img1.jpg" width="350" height="234" />
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img2.png" width="350" height="234" />
</div>

<div style="display: flex;">
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img3.jpg" width="250" height="295" />
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img4.jpg" width="400" height="182" />
</div>
<br><br>

**水印**

<img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/mark.jpg" width="128" height="128" />
<br><br>

**例1**

```
python WaterMarkPrinter.py ./ mark.png -x end -y end -s 0.25
```
<br>

**效果图**

<div style="display: flex;">
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark1.jpg" width="350" height="234" />
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark2.png" width="350" height="234" />
</div>

<div style="display: flex;">
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark3.jpg" width="250" height="295" />
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark4.jpg" width="400" height="182" />
</div>
<br>

**例2**

```
python WaterMarkPrinter.py ./ mark.png -x center -j 70 -t 0.6 -s 0.25
```
<br>

**效果图**

<div style="display: flex;">
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark2_1.jpg" width="350" height="234" />
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark2_2.png" width="350" height="234" />
</div>

<div style="display: flex;">
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark2_3.jpg" width="250" height="295" />
  <img src="https://github.com/mockingbird2/WaterMarkPrinter/blob/main/images/img_mark2_4.jpg" width="400" height="182" />
</div>

## 编译EXE

**考虑到使用的便利性，用户可自行通过pyinstaller包编译EXE执行文件并添加到Window系统的环境变量中，方便后续使用。（相关问题请自行搜索，这里不再赘述）**

**下面提供了编译好的，也可以直接下载食用>^<**

通过以下命令自行编译：

1. 安装pyinstaller
   
```
pip install pyinstaller
```

2. 执行编译指令

```
pyinstaller -F -i icon.ico WaterMarkPrinter.py
```

**文件链接**

百度云: [https://pan.baidu.com/s/12_UYVprNm8uW1yWCWi3pfg?pwd=0605](https://pan.baidu.com/s/12_UYVprNm8uW1yWCWi3pfg?pwd=0605)

提取码: ```0605```
