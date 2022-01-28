import cv2 as cv
import numpy as np
import os,traceback

from matplotlib import pyplot as plt
def listdir(path):  #传入存储的list
    file_list = []
    for file in os.listdir(path):
        file_list.append(file)

    return file_list

def contours_demo_1(image,p_image):

    contours,heriachy = cv.findContours(image, cv.RETR_EXTERNAL , cv.CHAIN_APPROX_SIMPLE)
    for i,contour in enumerate(contours):
        cv.drawContours(image, contours, i, (0, 0, 255), 2)

    cv.imshow("detect contours", image)
    color = [255]
    stencil = np.zeros(image.shape).astype(image.dtype)
    stencil_1 = cv.fillPoly(stencil, contour, color)
    image_2 = p_image
    mask_3 = cv.merge([stencil_1, stencil_1, stencil_1])
    result = cv.bitwise_and(image_2, mask_3)
    # cv.imshow("da", result)
    return result

def edge_demo(image):
    # blurred = cv.GaussianBlur(image, (3,3 ), 0)
    # gray = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    xgrad = cv.Sobel(image, cv.CV_16SC1, 1, 0)
    ygrad = cv.Sobel(image, cv.CV_16SC1, 0, 1)
    #edge_output = cv.Canny(xgrad, ygrad, 10, 100)
    edge_output = cv.Canny(image, 50, 150)
    # cv.imshow("Canny Edge", edge_output)
    dst = cv.bitwise_and(image, image, mask=edge_output)
    # cv.imshow("Color Edge", dst)
    return edge_output
def threshold_demo(image):
    ret, binary = cv.threshold(image,0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    return binary
def contours_demo(image,p_image):
    ii=0
    image_2=p_image
    area_1=[]
    mask_3=[]
    contour_1=[]
    heriachy=[]
    contours,heriachy = cv.findContours(image, cv.RETR_TREE , cv.CHAIN_APPROX_SIMPLE)

    for i,contour in enumerate(contours):
        # cv.drawContours(p_image, contours, i, (0, 0, 255), 1)
        # cv.drawContours(p_image, contours, i, (0, 0,255), 1)
        area=cv.contourArea(contour)
        area_1.append(area)

    area_index=area_1.index(max(area_1))
    try:
        for abc in heriachy:
            for i in range(len(abc)):
                if abc[i][3] ==-1 and i==area_index:
                    contour_1.append(contours[i])
    except TypeError:
        traceback.format_exc()
        return [[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    color = [255]
    stencil = np.zeros(image.shape).astype(image.dtype)
    stencil_1 = cv.fillPoly(stencil, contour_1, color)
    mask_3 = cv.merge([stencil_1, stencil_1, stencil_1])
    result = cv.bitwise_and(image_2, mask_3)
    # result =cv.drawContours(result, contour_1, 0, (0, 0, 255), 15)
    # cv.imshow("da", result)
    return result

def dilate_demo(image):
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (10, 10))
    dst = cv.dilate(image, kernel)
    # cv.imshow("erode_demo", dst)
    return dst
def edge(image):
    abc = np.zeros((80, 4096, 3))
    image[0:80] = abc
    return image
def close_demo(image):
    # print(image.shape)
    # gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    # ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    # cv.imshow("binary", binary)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))
    binary = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
    return binary
def pre_treatment(image):
    blurred = cv.bilateralFilter(image, 1, 100, 15)  #双边滤波
    # b = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
    b, g, r = cv.split(blurred)       #灰度化
    b_bin = threshold_demo(b)
    close_d = close_demo(b_bin)
    # edge111 = edge_demo(close_d)
    # dilate = dilate_demo(edge111)
    result = contours_demo(close_d, image)
    return result
if __name__=="__main__":
    file_list = listdir("../test_JPEGImages")
    for file in file_list:
        src = cv.imread("../test_JPEGImages/"+file)
        result = pre_treatment(src)
        cv.imshow("da", result)
        cv.waitKey()
        # src = cv.imread("../test_JPEGImages/"+file )
        # blurred = cv.bilateralFilter(src, 1,100, 15)
        # # b = cv.cvtColor(blurred, cv.COLOR_BGR2GRAY)
        # b, g, r=cv.split(blurred)
        # cv.imwrite("000.jpg",b)
        # b_ray=threshold_demo(b)
        # # cv.imshow("da", b_ray)
        # cv.imwrite(str(file)+"111.jpg", b_ray)
        # close_d=close_demo(b_ray)
        # cv.imwrite(str(file)+"222.jpg", close_d)
        # # edge111=edge_demo(close_d)
        # # cv.imwrite("333.jpg", edge111)
        # # dilate=dilate_demo(edge111)
        # # cv.imwrite("444.jpg", dilate)
        # # cv.imshow("2", edge111)
        # # cv.imwrite("./"+file,b)
        # result=contours_demo(close_d,src)
        # cv.imwrite(str(file)+"555.jpg", result)
        # cv.imshow("3", result)
        # cv.waitKey()
