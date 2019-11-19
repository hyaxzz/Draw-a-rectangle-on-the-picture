import numpy as np
import cv2 as cv
import csv
drawing = False # true if mouse is pressed
mode = False # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
px,py=-1,-1
# mouse callback function
def draw_line(event,x,y,flags,param):
 global ix,iy,px,py,drawing,mode

 def create_csv():
     path = "result.csv"
     with open(path, 'a') as f:
         csv_write = csv.writer(f)
         data_row = [x, y]
         csv_write.writerow(data_row)
 if event == cv.EVENT_LBUTTONDOWN:#点击左键事件
  drawing = True
  ix,iy = x,y #获取坐标
  print(x,y)
  create_csv()
 elif event == cv.EVENT_MOUSEMOVE:  # 鼠标移动事件
     drawing=False
     # if drawing == True:
     #     cv.line(img,(ix,iy),(x,y),(0,0,255),3)
     #     px, py = x, y

 elif event == cv.EVENT_LBUTTONUP:#左键释放事件
   drawing = True
   cv.line(img, (ix, iy), (x, y), (0, 0, 255), 3)
   px,py=-1,-1

img  = cv.imread('test.jpg',1)
cv.namedWindow('image')
cv.setMouseCallback('image',draw_line)
def create_csv():
    path = "result.csv"
    with open(path, 'w') as f:
        csv_write = csv.writer(f)
        csv_head = ['x','y']
        csv_write.writerow(csv_head)
        data_row = [ix, iy]
        csv_write.writerow(data_row)


create_csv()
while(1):
 cv.imshow('image',img)
 k=cv.waitKey(1)& 0xFF

 if k == 27:
     cv.imwrite('result.jpg', img)
     break
