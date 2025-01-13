#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

# Print route
@app.route('/print/<string:text>')
def print_string(text):
    print(text)  
    return text  

# Count route
@app.route('/count/<int:number>')
def count(number):
    numbers_list = "\n".join(str(i) for i in range(number)) + '\n' 
    return numbers_list  

# Math route
@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/' or operation == 'div':  
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        result = num1 / num2
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation"
    
    return str(result)  


if __name__ == '__main__':
    app.run(port=5555, debug=True)
