import cv2 as cv
import os

# Argument 0 is given to use the default camera of the laptop
camera = cv.VideoCapture(0)

# Now check if the camera object is created successfully
if not camera.isOpened():
    print("The Camera is not Opened....Exiting")
    exit()

# Prompt user to enter the folder name
folder_name = input("Enter the name of the folder: ")

# Create folder to store images
folder_path = 'C:/Users/hisha/Desktop/Python/OpenCV/Multipleimages/' + folder_name
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

# Clicking 200 images per folder
count = 0
while count < 200:
    # Read frame from camera
    status, frame = camera.read()

    # Check if frame is captured
    if not status:
        print("Frame is not been captured..Exiting...")
        break

    # Resize the image to 1400x700 pixels
    resized_frame = cv.resize(frame, (1280, 900))

    # Display window with resized image
    cv.imshow("Video Window", resized_frame)

    # Store the image to specific folder
    cv.imwrite(folder_path + '/img' + str(count) + '.png', resized_frame)

    count += 1

    # Press 'q' to quit the display window
    if cv.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
camera.release()
cv.destroyAllWindows()
