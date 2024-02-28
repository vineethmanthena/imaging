
import cv2
import os
import imutils
from imaging_interview import preprocess_image_change_detection

def compare_frames_change_detection(prev_frame, next_frame, min_contour_area):
    equalized_prev_frame = cv2.equalizeHist(prev_frame)
    equalized_next_frame = cv2.equalizeHist(next_frame)
    frame_delta = cv2.absdiff(equalized_prev_frame, equalized_next_frame)
    thresh = cv2.threshold(frame_delta, 85, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)
    cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    score = 0
    res_cnts = []
    for c in cnts:
        if cv2.contourArea(c) >= min_contour_area:
            res_cnts.append(c)
            score += cv2.contourArea(c)

    return score, res_cnts, thresh

if __name__ == "__main__":
    dir = r"C:\dataset_directory"
    file_paths = [os.path.join(dir, file) for file in os.listdir(dir) if file.lower().endswith((".jpg", ".png"))]

    images = []
    images_processed = []
    for file_path in file_paths:
        img = cv2.imread(file_path)
        if img is not None:
            images.append(img)
            
            processed = preprocess_image_change_detection(img)
            resized = cv2.resize(processed, (300, 300))
            images_processed.append(resized)
    unique = [images[0]]
    unique_processed = [images_processed[0]]
    for i in range(len(images) - 1):
        score, _, _ = compare_frames_change_detection(images_processed[i], images_processed[i + 1], 250)
        if score >= 2000:
            unique_processed.append(images_processed[i + 1])
            unique.append(images[i+1])
        
             
    unique_1 = unique_processed.copy()
    i = 0
    while i < len(unique_1):
        j = i + 1
        while j < len(unique_1):
            score, _, _ = compare_frames_change_detection(unique_1[i], unique_1[j], 100)
            if score <= 17000:
                del unique_1[j]
            else:
                j += 1
        i += 1

    print(len(unique))
    print(len(unique_processed))
    print(len(unique_1))
   

