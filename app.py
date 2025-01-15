from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Simulated in-memory database for comments
comments = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', comments=comments)

@app.route('/post', methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        website = request.form.get('website', '')
        comment = request.form.get('comment', '')

        # Store the comment without sanitization - XSS vulnerability.
        comments.append({
            'name': name,
            'email': email,
            'website': website,
            'comment': comment
        })
        return redirect(url_for('blog'))
    return render_template('post.html')

if __name__ == "__main__":
    app.run(debug=True)
