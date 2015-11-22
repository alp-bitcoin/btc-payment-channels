from flask import Flask

app = Flask(__name__)

import payment_channels.views
