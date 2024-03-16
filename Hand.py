import mediapipe as mp
import cv2

# Create a MediaPipe Hands object.
hands = mp.solutions.hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5)

# Create a drawing utils object.
drawing_utils = mp.solutions.drawing_utils

# Capture video from the webcam.
cap = cv2.VideoCapture(1)

# Process each frame.
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert the frame to RGB.
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image.flags.writeable = False

    # Run the MediaPipe Hands model on the frame.
    results = hands.process(image)

    # Display the frame.
    cv2.imshow('MediaPipe Hands', frame)

    # Press 'q' to quit.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam.
cap.release()

# Close all windows.
cv2.destroyAllWindows()