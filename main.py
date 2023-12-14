from flask import Flask, render_template, request
import os
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET','POST'])
def root():
    result = None

    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')
    except Exception as e:
        result = f"Error: {str(e)}"
    try:
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
    except Exception as e:
        result = f"Error: {str(e)}"
    return {"result":float(result),"num1":float(num1),"num2":float(num2)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port= int(os.getenv('PORT', 3001)))
