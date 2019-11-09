app = Flask(__name__)

@app.route("/")
def index():
    return render_template('main.py')

app.run()
