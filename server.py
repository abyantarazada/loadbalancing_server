from flask import Flask, send_file, render_template

app = Flask(__name__)

@app.route('/')
def downloadFile():
    path = "/video.mp4"
    return send_file(path, as_attachment = True)

if __name__ == "__main__":
    app.run(debug = True)
