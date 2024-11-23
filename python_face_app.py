import face_recognition
import json
import sqlite3

def save_face_encoding_to_db(image_path, name):
    # Load the image
    image = face_recognition.load_image_file(image_path)

    # Generate face encodings
    encodings = face_recognition.face_encodings(image)
    if encodings:
        face_encoding = encodings[0].tolist()  # Convert to list for JSON serialization
        encoding_json = json.dumps(face_encoding)  # Convert encoding to JSON

        # Save to database
        print("encoding json: ", encoding_json)

        print(f"Face encoding for '{name}' saved to database.")
    else:
        print("No face detected in the image.")

# Example usage
save_face_encoding_to_db("check.jpg", "John Doe")