from flask import Flask, render_template, request
import os
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def calc(num1, num2, operation):
    result = None
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
    return result


@app.route('/', methods=['GET', 'POST'])
async def root():
    num1 = 0
    num2 = 0

    try:
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')

        result = calc(num1, num2, operation)
    except Exception as e:
        return {"result": "No data", "num1": float(num1), "num2": float(num2)}
    return {"result": float(result), "num1": float(num1), "num2": float(num2)}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv('PORT', 3001)))
