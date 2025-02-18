from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask!"

# Required for Vercel Deployment
def handler(event, context):
    return app(event, context)

if __name__ == '__main__':
    app.run(debug=True)
