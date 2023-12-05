# -*- coding: utf-8 -*-
"""
Created on Sat Dec 2 00:11:50 2023

@author: Omobolaji
"""

import cv2
import face_recognition
import time

# Function to get location
def get_location():
    # For testing purposes, return a predefined location
    return {
        'address': "123 Test Street, Test City, Test Country",
        'latitude': 0.0,
        'longitude': 0.0
    }

# Function to authenticate location
def authenticate_location(expected_location):
    obtained_location = get_location()

    # Check if the obtained location matches the expected location
    return (
        expected_location['address'].lower() in obtained_location['address'].lower() and
        expected_location['latitude'] == obtained_location['latitude'] and
        expected_location['longitude'] == obtained_location['longitude']
    )

# Function to load known faces from a secure storage (e.g., database)
def load_known_faces():
    # Replace this with your implementation to load known faces and their names
    # For simplicity, using a hardcoded list as an example
    known_faces = []
    known_names = []
    # known_faces should contain face encodings, and known_names should contain corresponding names
    return known_faces, known_names

# Function to recognize a face against known faces
def recognize_face(captured_encoding, known_faces, known_names):
    matches = face_recognition.compare_faces(known_faces, captured_encoding)

    for i, match in enumerate(matches):
        if match:
            return known_names[i]

    return None

# Function to capture picture and perform facial recognition
def capture_and_recognize_face(file_path="captured_picture.jpg"):
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return False
    
    ret, frame = cap.read()
    
    if ret:
        cv2.imwrite(file_path, frame)
        print(f"Picture captured and saved as {file_path}")
        
        # Load known faces
        known_faces, known_names = load_known_faces()

        # Load the captured image for facial recognition
        captured_image = face_recognition.load_image_file(file_path)
        captured_face_encodings = face_recognition.face_encodings(captured_image)

        if captured_face_encodings:
            # Check against known faces
            for captured_encoding in captured_face_encodings:
                recognized_name = recognize_face(captured_encoding, known_faces, known_names)
                if recognized_name:
                    print(f"User recognized: {recognized_name}")
                else:
                    # Override: If not found, print a message
                    print("User not found in the system.")
        else:
            print("No face detected. Facial recognition failed.")
    else:
        print("Error: Could not capture picture.")
    
    cap.release()  # Release the camera

# Main function
def main():
    # Your information
    your_name = "Oadeyan"
    employee_id = "YourEmployeeID"  # Replace with your actual employee ID
    
    # Expected location for authentication
    expected_location = {
        'address': "123 Test Street, Test City, Test Country",
        'latitude': 0.0,
        'longitude': 0.0
    }
    
    # Authenticate location
    if not authenticate_location(expected_location):
        print("Authentication failed. Location does not match.")
        return
    
    # Capture picture and perform facial recognition
    capture_and_recognize_face()
    
    # Record the current time
    current_time = time.strftime("%Y-%m-%d %H:%M:%S")
    
    # Display organized results with credit
    print("Name:", your_name)
    print("Employee ID:", employee_id)
    print("Location Address:", expected_location['address'])
    print("Location Latitude:", expected_location['latitude'])
    print("Location Longitude:", expected_location['longitude'])
    print("Time stamped:", current_time)
    
    # Credit information
    print("\nScript customized by Oadeyan")
    print("Powered by FreNiMi")

if __name__ == "__main__":
    main()
