#Upon reviewing the dataset, I noticed that it captures four distinct scenes of a parking lot at various times throughout the day over a specific period. Additionally, I observed that the cameras were positioned close to the ceiling, resulting in the roof occupying a significant portion of the image space and causing objects to appear out of focus. Furthermore, I noticed that the outer edges of the images exhibit curvature, indicative of barrel distortion. This distortion is likely a result of the wide field of view provided by the camera.


#The code world like this: It takes in the directory that contains the images and makes a list out of it. Then the images were read using cv2.imread() before preprocessing. 
