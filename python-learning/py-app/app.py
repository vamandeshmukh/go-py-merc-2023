from flask import Flask, render_template
from flask_bootstrap import Bootstrap

print('start')
app = Flask(__name__)
bootstrap = Bootstrap(app)

emp_data = {
    'firstName': 'Sonu',
    'phone': '+91-98765-43210',
    'skillset': ['NodeJS', 'Angular', 'ReactJS', 'Springboot', 'Microservices', 'DevOps'],
}


@app.route('/')
def home():
    print('home')
    return render_template('home.html')

@app.route('/about')
def about():
    print('about')
    return render_template('about.html', emp=emp_data)

@app.route('/contact')
def contact():
    print('contact')
    return render_template('contact.html')

@app.errorhandler(404)
def not_found_error(error):
    print('404')
    return render_template('page404.html'), 404

if __name__ == '__main__':
    print('started')
    app.run(host='localhost', port=9999)


    print('end')
