from flask import flask

app=Flask(__name__)

app.route('/')
app.route('/home')
def index():
    return "<p>hello</P>"

if __name__=="__main__":
    app.run()