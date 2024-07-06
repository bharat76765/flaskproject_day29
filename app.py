from flask import Flask, render_template, request, redirect, url_for
import roadmap_api

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/roadmap', methods=['POST'])
def roadmap():
    role = request.form.get('role')
    roadmap_data = roadmap_api.get_roadmap(role)
    return render_template('roadmap.html', role=role, roadmap=roadmap_data)

if __name__ == '__main__':
    app.run(debug=True)
