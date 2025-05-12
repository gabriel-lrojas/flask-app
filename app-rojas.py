from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
     return """
      <h3>Gabriel</h3>
      <h1>Hello, DevOps and friend and crusaders !</h1>
      <h3>Trang</h3>
      <h2 style="color:blue;">Contribution Trang – Module DevOps !</h2>
      <h3>Thomas</h3>
      <h3>Men are brave !</h3>
    """


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

