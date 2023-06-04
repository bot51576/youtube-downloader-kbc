from __future__ import print_function
from flask import Flask, render_template, request
from youtube_dl import youtube_downloader

app = Flask(__name__)
save_path = ''

@app.route("/",  methods=['GET', 'POST'])
def index():
    global save_path
    if request.method == 'GET':
        return render_template('index.html', p=save_path)
    
    url = request.form.get('url')
    path = request.form.get('path')
    save_path = path
    youtube_downloader(url, save_path)
    return render_template('index.html',  p=save_path)

    

if __name__ == "__main__": 
    app.run(host="localhost", port=5000)