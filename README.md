# Face recognition for Raspberry PI with Web Service to Start/Stop

Was developed and tested with Raspberry Pi 4 (4Gb) model B and Raspberry Pi Camera Module v2.
You can try with different configurations. You can refer to [https://github.com/ageitgey/face_recognition/tree/master/examples](Adam Geitgey examples) for webcams and and other data sources.

I wanted to start and stop the service remotely, therefore created a web service to handle the face detection.
The idea was to use it with my home automation, when the door is opened or motion detected i would like to start the face recognition. Based on the recognition, I would like to to trigger some automation.

## TODO
    * If unknown face is recognized, take a photo and add a tag to the face. So that can be added later.
    * Add triggers for recognized faces.
    * Dockerize the solution. I tried to do it, but building and running was taking ages. 

## Inspirations and Reference
[https://github.com/ageitgey/face_recognition](https://github.com/ageitgey/face_recognition)
[https://github.com/denverdino/face_recognition_pi](https://github.com/denverdino/face_recognition_pi)
