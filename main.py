from flask import (
    Flask,
    render_template,
    # Request,
    request
)
import util.network
import util.params
import logging
import functools
import json

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(name)-15s | %(funcName)15s() | %(message)s'
)

app = Flask(__name__)


def log_decorator(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        logger.info(f"calling {fn.__name__}({util.params.params2str(*args, **kwargs)})")
        retval = fn(*args, **kwargs)
        logger.info(f"return value: {retval}")
        return retval

    return wrapper


@app.route("/")
@log_decorator
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
@log_decorator
def login():
    # print(request.form)
    # print(request.form['username'])
    # print(request.form['password'])
    # for k, v in request.form.items():
    #     print(k, v)
    print(type(request.form))
    print(request.form)
    username = request.form['username']
    password = request.form['password']
    print(username, password)
    return render_template("index.html", username=username, password=password)


if __name__ == '__main__':
    app.run(host=util.network.get_ipaddress(), debug=True)
