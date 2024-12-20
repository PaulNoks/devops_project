import logging
from logstash_formatter import LogstashFormatterV1
from flask import Flask, jsonify
from flask_cors import CORS
from prometheus_flask_exporter import PrometheusMetrics
metrics = PrometheusMetrics(app)

# Дополнительные настройки метрик можно добавить, например:
metrics.info('app_info', 'Application info', version='1.0.0')


app = Flask(__name__)
CORS(app)  # Включаем CORS для всех маршрутов

logger = logging.getLogger("flask_app")
logger.setLevel(logging.INFO)

logstash_handler = logging.StreamHandler()
logstash_handler.setFormatter(LogstashFormatterV1())
logger.addHandler(logstash_handler)

@app.route('/api/message')
def hello_world():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
