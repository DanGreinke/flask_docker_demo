
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
    return "welcome to the flask tutorials"

#curl http://localhost:5001/addition -F "data=1,2,3"
@app.route('/addition', methods=['POST','GET'])
def addition():
    try:
        request.method == 'POST'
        input_data = request.form['data'].split(',')
        int_list = [eval(i) for i in input_data]
        return str(sum(int_list))
    except:
        return "Please input a comma separated list of integers (e.g. 1,2,3)"

if __name__ == "__main__": 
    app.run(host ='0.0.0.0', port = 5001, debug = True)


# Based on tutorial here: https://www.geeksforgeeks.org/dockerize-your-flask-app/