from flask import Flask
import json
from op_stats.stats import Stats

app = Flask(__name__)

@app.route('/v1/stats/cpu')
def get_cpuinfo():
    cpu_percent = Stats.get_cpu_percent()
    return json.dumps({'cpu_percent': cpu_percent})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8080)
