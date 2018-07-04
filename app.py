from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
Bootstrap(app)

web_name = 'Northeastern University Ma He Group'

@app.route('/')
def index():
    return render_template('home.html', title_name=web_name)


@app.route('/home/')
def home():
    return render_template('home.html', title_name=web_name)


@app.route('/leader/')
def leader():
    return render_template('leader.html', title_name=web_name)


@app.route('/leader/more')
def leader_more():
    return render_template('mahe/publications.html', title_name=web_name)


if __name__ == '__main__':
    app.run("0.0.0.0", debug=True, port=30000)
