from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "This app is running perfectly" 

if __name__ == '__main__':
    app.run(debug=True)