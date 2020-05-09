# TheOneWithYolo
Using you only look once technique by employing TF version of DarkNet. This is learning material for me/those who wants to grasp pre-existing technologies and build on top of it for maximum usability of open-source projects.





<b>here is my demo</b> for this [video](https://youtu.be/NyLF8nHIquM) from youtube (FYI: I don't claim ownership of this video)

<p align="center"> <img src="demo.gif" width="800" height="300" /> </p>

### Pre-Trained Weights

For getting pretrained weights, click [here](https://drive.google.com/drive/folders/0B1tW_VtY7onidEwyQ2FtQVplWEU).<br>
You can also download weights from [pjreddie](https://pjreddie.com/darknet/yolo/), but some weight are not compatible with DarkFlow.

## Dependencies

* Cython (as original library was written in C)
* OpenCV
* TensorFlow
* Numpy
* MatplotLib

_note_: I have used Python 3.6 for this, and Python & pip are already configured in my system. You can also use Anaconda for this project.

```bash
pip install cython
pip install tensorflow
pip install numpy
pip install matplotlib
```
As <b>OpenCV</b> is not directly packaged for Windows, So we need use a [Unofficial Binary Distribution](https://www.lfd.uci.edu/~gohlke/pythonlibs/) of OpenCV.<vr><br>
If you are not using windows, please go ahead and install it like rest.
