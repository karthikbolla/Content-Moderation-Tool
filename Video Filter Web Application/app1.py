from flask import Flask, request, jsonify,render_template
from video import video_write

app1 = Flask(__name__)

def content_moderation(video):
    # Perform content moderation analysis here
    # Replace this with your actual analysis logic
    # Assume 'result' is the category determined by the analysis
    result = "U/A"
    return result

@app1.route('/', methods=['POST'])
def analyze():
    video_file = request.files.get('file')
    video_url = request.form.get('url')

    if video_file:
        # Perform analysis for uploaded file
        category = video_write(video_file)
    elif video_url:
        # Perform analysis for video URL
        category = video_write(video_url)
    else:
        return render_template('page1.html')

    return render_template('page1.html')

if __name__ == '__main__':
    app1.run(debug=True)
