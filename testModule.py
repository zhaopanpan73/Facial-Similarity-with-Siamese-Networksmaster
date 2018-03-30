import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
def imshow(img,text,should_save=False):
    npimg = img.numpy()
    plt.axis("off")
    if text:
        plt.text(75, 8, text, style='italic',fontweight='bold',
            bbox={'facecolor':'white', 'alpha':0.8, 'pad':10})
    plt.imshow(np.transpose(npimg, (1, 2, 0)))
    plt.show()

img = Image.open("F:\DataSet\CASIADataSet\90Degree/1_17.png")
img.show()
arr = np.asarray(img, dtype="uint8")
concatenated =arr
imshow(concatenated, 'Dissimilarity: {:.2f}'.format(2))
