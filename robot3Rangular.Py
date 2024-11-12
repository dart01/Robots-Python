
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not cap.isOpened():
    print("Unable to read camera feed")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    if ret:
        # Display the resulting frame
        cv2.imshow('Video', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()