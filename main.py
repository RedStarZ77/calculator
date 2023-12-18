from flask import Flask, render_template, request
import os
from flask_cors import CORS

from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.trace.export import ConsoleSpanExporter
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

provider = TracerProvider()
processor = BatchSpanProcessor(ConsoleSpanExporter())
provider.add_span_processor(processor)
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "calculator"}))
)
jaeger_exporter = JaegerExporter(
    agent_host_name=os.getenv("JAGER_HOSTNAME", "localhost"),
    agent_port=6831,
)
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(jaeger_exporter))

tracer = trace.get_tracer("calculator")

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


def calc(num1, num2, operation):
    with tracer.start_as_current_span("calculate"):
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
    with tracer.start_as_current_span("calculatedata"):
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
