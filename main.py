import json

from flask import Flask, request
import flask_cors

import floor

app = Flask(__name__)

@app.route('/', methods=['POST','OPTIONS'])
@flask_cors.cross_origin()
def index():
    request_message = json.loads(request.get_data())

    text, tts = floor.get()

    derived_session_fields = ['session_id', 'user_id', 'message_id']
    response_message = {
        "response": {
            "text": text,
            "tts": tts,
            "card":{},
            "end_session": True
        },
        "session": {derived_key: request_message['session'][derived_key] for derived_key in derived_session_fields},
        "version": request_message['version']
    }
    return json.dumps(response_message)

if __name__ == "__main__":
    app.run(port=8003)