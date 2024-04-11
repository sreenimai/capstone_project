import dlib
import cv2

# Load the shape predictor
try:
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
except FileNotFoundError:
    print("Error: Shape predictor file not found. Make sure it exists in the specified path.")

# Initialize the face detector
detector = dlib.get_frontal_face_detector()

# Define a function to find the area of a face
def find_area(face):
    a = face.left()
    b = face.top()
    c = face.right()
    d = face.bottom()
    return a * b * c * d

# Define a function to get landmarks from an image
def get_landmarks(image):
    try:
        # Convert the image to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale image
        faces = detector(gray)

        # If no faces are detected, return None
        if len(faces) == 0:
            return None
        else:
            # Find the face with the maximum area
            max_area_face = faces[0]
            max_area = find_area(faces[0])
            for face in faces:
                area = find_area(face)
                if area > max_area:
                    max_area = area
                    max_area_face = face

            # Get landmarks for the face with the maximum area
            landmarks = predictor(gray, max_area_face)
            coordinates = [[point.x, point.y] for point in landmarks.parts()]
            return coordinates
    except Exception as e:
        print("Error:", e)
        return None
