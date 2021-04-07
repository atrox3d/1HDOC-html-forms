from flask import Flask, render_template
import util.network
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(host=util.network.get_ipaddress(), debug=True)
