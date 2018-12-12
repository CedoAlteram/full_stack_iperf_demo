import os
from subprocess import call
from subprocess import Popen, PIPE
from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def homepage():
    return render_template("index.html")
@app.route('/run-script', methods=['POST'])
def run_script():
    command = "{path}".format(path=os.path.join(os.path.realpath(os.path.dirname(__file__)), 'static', 'iperfTest.sh'))
    p = Popen([command], shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
    output, err = p.communicate()
    rc = p.returncode
    return err if err else output
if __name__ == "__main__":
    app.run()
