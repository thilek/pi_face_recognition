from flask import Flask, jsonify, request, redirect
import face_recognition as recognition


app = Flask(__name__)
recognition.load_faces()

@app.route('/status', methods=['GET'])
def handle_service():
    
    action = request.args.get('action')

    if action == "start":
        return recognition.start_recognition()
        
    elif action == "stop":
        return recognition.stop_recognition()
    else:
        return "unknown action"


    return "unknown action"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)
