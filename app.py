import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return ('<p>CHARLES CHRISTIAN BONAO'
            'BSIT-III'
            'SYSTEM INTEGRATION'
            'SEMI-FINALS EXAM</p>')
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)