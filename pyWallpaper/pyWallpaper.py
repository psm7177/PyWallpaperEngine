from win32gui import *
from win32con import *
import cv2


desktop = GetDesktopWindow()
workw = 0
shelldll = 0

while True:
    workw = FindWindowEx(desktop, workw, "WorkerW", "")
    print(workw)
    shelldll= FindWindowEx(workw, 0, "SHELLDLL_DefView", "")
    if shelldll != 0:
        break
workw = FindWindowEx(desktop, workw, "WorkerW", "")

hMemDC = 0 
hImage = 0
hOldBitmap = 0


vidcap = cv2.VideoCapture('C:\\Users\\psm71\\source\\repos\\pyWallpaper\\pyWallpaper\\kpop.mp4')
success,hImage = vidcap.read()
count = 0

while success:
  hdc = GetDC(workw)
  hMemDC = CreateCompatibleDC(hdc)

  success,hImage = vidcap.read()
  cv2.imwrite("image.bmp",hImage)

  hImage = LoadImage(0,"image.bmp",IMAGE_BITMAP,1920,1080,LR_LOADFROMFILE)

  hOldBitmap = SelectObject(hMemDC, hImage)

  BitBlt(hdc, 0, 0, 1920, 1080, hMemDC, 0, 0, SRCCOPY)
  SelectObject(hMemDC, hOldBitmap)
   
  DeleteObject(hImage);
  DeleteDC(hMemDC);

  ReleaseDC(workw,hdc)     
  count += 1





