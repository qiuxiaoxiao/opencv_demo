# demo1
## 读写像素
* 对RGB图像来说，在Python中的第一个维度表示高度，第二个维度表示宽度，第三个维度是通道数目，可以通过下面的代码获取图像三个维度的大小
* image.shape
* image.size
* image.dtype

## 循环读取图像方法一：
直接从图像中读取，缺点是每次都需要访问imread之后的Mat对象，进行native操作，速度是个问题，代码实现如下：
* height = image.shape[0]
* width = image.shape[1]
* channels = image.shape[2]
* print(image.shape)
* for row in range(height):
*   for col in range(width):
*       for c in range(channels):
*           level = image[row, col, c]
*           pv = level + 30
*           image[row, col, c] = (255 if pv > 255 else pv)

## 循环读取图像方法二：
首先通过numpy把像素数据读到内存中，在内存中进行高效循环访问每个像素，修改之后，再赋值回去即可，代码如下：
* #read once
* pixel_data = numpy.array(image,dtype = numpy.uint8)
* # loop pixel by pixel
* for row in range(height):
*   for col in range(width):
*       for c in range(channels):
*           level = pixel_data[row, col, c]
*           pixel_data[row, col, c] = 255 -level
* #write once
* image[ : : ] = pixel_data

## 案例演示 在Python语言中完成图像的属性读取、像素读取与操作、实现了图像的颜色取反、亮度提升、灰度值、梯度化、操作。