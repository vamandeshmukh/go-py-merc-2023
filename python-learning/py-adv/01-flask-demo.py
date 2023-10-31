
from flask import Flask

print('start')

app = Flask(__name__)

@app.route('/')
def hello_world():
    print('helllo')
    return 'Hello, World!'

if __name__ == '__main__':
    print('started')
    app.run()

print('end')

# install flask from CMD
# # pip install flask
  