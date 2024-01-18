from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('page1.html') 

# @app.route("/") # Render the index.html template

if __name__ == '__main__':
    app.run(debug=True)
