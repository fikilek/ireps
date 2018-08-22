from flask import Flask, render_template
app = Flask(__name__)
app.secret_key = '1q2w3e4r5t56y76u78i9o'


@app.route('/')
def base():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)