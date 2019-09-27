import apriltag
import cv2
import time

cam = cv2.VideoCapture(1)


options = apriltag.DetectorOptions(families='tag36h11',
                                 border=1,
                                 nthreads=4,
                                 quad_decimate=1.0,
                                 quad_blur=0.0,
                                 refine_edges=True,
                                 refine_decode=False,
                                 refine_pose=True,
                                 debug=False,
                                 quad_contours=True)

detector = apriltag.Detector()

for i in range(40):
    ret, frame = cam.read()
    #cv2.imwrite("her.png", frame)
    #img = cv2.imread('her.png', cv2.IMREAD_GRAYSCALE)
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    '''scale_percent = 30 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)'''
    #img = cv2.resize(img, dim)
    
    result = detector.detect(img)
    if len(result) > 0:
      res = detector.detection_pose(result[0], [352.9612932663888, 353.30552701553773, 328.8698124198212, 225.41004686306474], 17.28)
      #print(result)
      #print()
      print (res[0][:,3], i)
    #time.sleep(0.1)

cam.release()