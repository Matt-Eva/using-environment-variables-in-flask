from flask import Flask
import os

app = Flask(__name__)

print(os.environ)

for key, value in os.environ.items():
    print(key, value)

print(os.environ.get('TEST'))

@app.route("/")
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run()