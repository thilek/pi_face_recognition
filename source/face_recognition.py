# This module loads face encodings and handles face recognition
# The recognition is done in a separate process

# To run this, you need a Raspberry Pi 2 (or greater) with face_recognition and
# the picamera[array] module installed.
# You can follow this installation instructions to get your RPi set up:
# https://gist.github.com/ageitgey/1ac8dbe8572f3f533df6269dab35df65

import face_recognition
import picamera
import numpy as np
from multiprocessing import Process

# Initialize some variables
face_locations = []
face_encodings = []
known_face_encodings = []
names = []
recognition_process = None


# Starts face recognition in a process
def start_recognition():
    global recognition_process
    if recognition_process != None and recognition_process.is_alive():
         return "Face recognition is already running"
    else:
        recognition_process = Process(name='face_recognition', target=run_recognition)
        recognition_process.start()
        return "Face recognition started"

# Stops face recognition process if it was running
def stop_recognition():
    global recognition_process
    if recognition_process is None :
        return "Face recognition was not running"
    elif recognition_process.is_alive():
        print("Stopping face recognition")
        recognition_process.terminate()
        recognition_process = None
        return "Face recognition stopped"
    else:
        return "Unknown Status"


# Load face assets from image files.
def load_faces():
    print("Loading known face asset(s)")
    load_face_encoding("Thilek", "images/thilek/thilek.jpg")

# Creates and appends face encodings
def load_face_encoding(name, file_name):
    image = face_recognition.load_image_file(file_name)
    face_encoding = face_recognition.face_encodings(image)[0]
    known_face_encodings.append(face_encoding)
    names.append(name)

# Runs face recognition. Best to run this in a separate process/thread
def run_recognition():
    # Get a reference to the Raspberry Pi camera.
    # If this fails, make sure you have a camera connected to the RPi and that you
    # enabled your camera in raspi-config and rebooted first.
    camera = picamera.PiCamera()
    camera.resolution = (320, 240)
    output = np.empty((240, 320, 3), dtype=np.uint8)
  
    while True:
        # Grab a single frame of video from the RPi camera as a numpy array
        camera.capture(output, format="rgb")

        # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(output)
        print("{} faces detected".format(len(face_locations)))
        face_encodings = face_recognition.face_encodings(output, face_locations)

        # Loop over each face found in the frame to see if it's someone we know.
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            matches = face_recognition.face_distance(known_face_encodings, face_encoding)
            name = "Recognized <Unknown Person>"
            
            min_distance = min(matches)
            if min_distance < 0.6:
                i = matches.argmin()
                name = names[i]
                
            print("Recognized {}!".format(name))
