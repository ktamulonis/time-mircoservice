from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def get_current_time():
    return str(datetime.now())

if __name__ == "__main__":
    app.run()
