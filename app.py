from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>DevOps Task Manager</title>
    </head>
    <body>
        <h1>DevOps Task Manager</h1>
        <p>My first DevOps project is running successfully!</p>
        <p>Version: 1.0</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
