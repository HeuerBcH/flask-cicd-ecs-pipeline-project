from flask import Flask

# from dotenv import load_dotenv
# import os
# load_dotenv() 
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD with Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
