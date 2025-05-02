from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# قائمة لتخزين الفيديوهات
videos = []

@app.route('/')
def index():
    return render_template('index.html', videos=videos)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/why')
def why():
    return render_template('why.html')

@app.route('/goal')
def goal():
    return render_template('goal.html')

@app.route('/support')
def support():
    return render_template('support.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        title = request.form['title']
        video_id = request.form['video_id']
        description = request.form['description']
        videos.append({'title': title, 'video_id': video_id, 'description': description})
        return redirect(url_for('index'))
    return render_template('admin.html')

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))

