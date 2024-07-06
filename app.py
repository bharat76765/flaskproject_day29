from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = 'http://127.0.0.1:5050/api/roadmap/'

@app.route('/')
def index():
    roles = ["Data science", "Web Developer", "DevOps Engineer","Database Administrator","Analyst","Information technology management","Application Developer","Software Architect","Data Engineer","Java Developer","Network administrator","Software engineer","Full stack developer","IT Security Specialist","Product Management","Cloud Engineer","Blockchain Engineer"]  # List all roles here
    return render_template('index.html', roles=roles)

@app.route('/roadmap', methods=['GET'])
def roadmap():
    role = request.args.get('role')
    response = requests.get(API_URL + role)
    if response.status_code == 200:
        data = response.json()
        return render_template('roadmap.html', role=data['role'], image_url=data['image_url'])
    else:
        return "Role not found", 404

if __name__ == '__main__':
    app.run(debug=True, port=5001)
