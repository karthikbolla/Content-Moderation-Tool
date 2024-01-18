from flask import *
from distutils.log import debug
from fileinput import filename
from video import video_write
import os

app=Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/success',methods=['POST'])
def success():
    if request.method == 'POST':
        f=request.files['file']
        f.save(f.filename)
        video_write(f.filename)
        os.rename('output.webm','static/output.webm')
        return render_template("index.html")
    
if __name__=='__main__':
    app.run(debug=True)
