1)Upon reviewing the dataset, I noticed that it captures four distinct scenes of a parking lot at various times throughout the day over a specific period. Additionally, I observed that the cameras were positioned close to the ceiling, resulting in the roof occupying a significant portion of the image space and causing objects to appear out of focus. Furthermore, I noticed that the outer edges of the images exhibit curvature, indicative of barrel distortion. This distortion is likely a result of the wide field of view provided by the camera.


2)The code works like this: It takes in the directory that contains the images and makes a list out of it. Then the images were read using cv2.imread() before preprocessing. Before passing the images to compare_frames_change_detection fucntion the images were resized to the same size as there are of different sizes and the cv2.absdiff() only takes images of same type.
Before applying artithmetic operations on the images, in an attempt to reduce the effect of light, Histogram equalization is utilized to improve contrast and ensure consistent brightness levels across images, thereby facilitating more accurate comparison results.and i have also made some changes to the compare_frames_change_fucntion.
A threshold is applied to the computed similarity scores to distinguish between similar and dissimilar image pairs. Images with similarity scores below the threshold are classified as similar, while those exceeding the threshold are considered different.


3) In my solution, I used the score obtained from the comparison function to assess the similarities between images. Through numerous test runs, I've noted that this score, representing the contour area, the area of the contours within the arithmetic difference of the compared images. This observation suggests that the contour area serves as the most suitable metric for this task.


4)To enhance the collection of unique images, consider the following:
Space out the intervals between image captures to ensure a diverse range of scenes and conditions are captured. This allows for greater variation in environmental factors such as lighting, weather, and activity levels.
Prioritize capturing images during peak traffic periods when there is a higher influx of vehicles or pedestrians. This increases the likelihood of capturing unique scenarios and interactions, providing a more comprehensive dataset.
Avoid taking more images at evenings and early in the mornings.
Ensure that cameras are not positioned against the direction of light sources, as this can result in backlighting and cause images to appear washed out or poorly illuminated. Optimal lighting conditions enhance image clarity and facilitate accurate analysis.


5)To ensure thorough comparison, the code employs a secondary loop to compare each image with every other image in the dataset. This approach guards against overlooking subtle similarities between images, especially in cases where consecutive images may exhibit slight variations but still depict the same scene.
The threshold was set slightly higher in the second loop to account for highly illuminated images, which tend to produce larger differences when compared. While this approach may result in the loss of some information, it effectively filters out most of the unnecessary data, ensuring that only significant differences between images are considered. This adjustment helps prioritize the detection of meaningful variations while mitigating the impact of lighting conditions on the comparison process.
The decision to utilize two loops for comparison strikes a balance between comprehensive evaluation and computational efficiency. By initially comparing adjacent images and subsequently conducting a broader comparison across the entire dataset, the code delivers accurate and exhaustive analysis of image similarities.
