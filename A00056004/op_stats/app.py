from flask import Flask
import json

import sys

sys.path.append('/home/flaskdev/so-exam3/A00056004/')

from op_stats.stats import Stats

app = Flask(__name__)


@app.route('/getStats/cpu')
def get_cpuinfo():
    cpu_percent = Stats.get_cpu_percent()
    return json.dumps({'Cpu usage': cpu_percent})


@app.route('/getStats/ram')
def get_raminfo():
    ram = Stats.get_ram()
    return json.dumps({'Ram available': ram})


@app.route('/getStats/disk')
def get_diskinfo():
    free_disk = Stats.get_free_disk()
    return json.dumps({'Free disk': free_disk})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
