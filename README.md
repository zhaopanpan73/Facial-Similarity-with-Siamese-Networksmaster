# 用孪生网络检测人脸相似性（in Pytorch）
**
Attention:
**
**
1.写这个代码的主要目的是想学习一下用孪生网络来区分给定的一对图片
2.这个项目是用pytorch写的
**


**
1.数据集的格式和 PyTorch自己的数据集格式一样，不同类别的图片放在不同的文件夹中，同一类别的图片放在一个同一个文件夹中。
**

** Converting pgm files (if you decide to use the AT&T dataset) to png
1. Install imagemagick 
2. Go to root directory of the images
3. Run `find -name "*pgm" | xargs -I {} convert {} {}.png`**


**2.代码所需要的依赖包在 requirements.txt 中详细说明**

**3.这个项目使用的python版本是python3.6**
