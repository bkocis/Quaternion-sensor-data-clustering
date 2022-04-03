Demonstration of data labeling from a [9-axis absolute orientation sensor BNO055](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor).
----------------------------------------------------------------------

This repo showcases a short demo of the experiment of interpreting quaternion data from a giro sensor. In this usecase the sensor was mounted on a dummy-toothbrush in order to experiment with motion clustering in the context of oral health. 

- [Ardunio board](https://www.adafruit.com/product/3010)
- [BNO055 sensor](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor) 

Python code uses sklearn KNN algorithm to cluster the datapoints and for the class label inference of new datapoints.

Demo videos:

[<img src="https://img.youtube.com/vi/9Ww4DPw2Ses/maxresdefault.jpg" width="30%">](https://youtu.be/9Ww4DPw2Ses)


Demo of the problem:

[<img src="https://img.youtube.com/vi/qMMOt3G3qhg/maxresdefault.jpg" width="30%">](https://youtu.be/qMMOt3G3qhg)


