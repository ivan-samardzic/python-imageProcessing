import cv2
import numpy as np
slika=cv2.imread('rgbPrva.jpg')
slika=cv2.cvtColor(slika,cv2.COLOR_BGR2RGB)
vectorized=slika.reshape((-1,3))
vectorized=np.float32(vectorized)
kriteriji=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,10,1.0)
K=6
pokusaji=10
ret,label,center=cv2.kmeans(vectorized,K,None,kriteriji,pokusaji,cv2.KMEANS_PP_CENTERS)
center=np.uint8(center)
res=center[label.flatten()]
result_Slika=res.reshape((slika.shape))
cv2.imwrite('segmentSlika6zad.jpg',result_Slika)