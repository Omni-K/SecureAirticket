from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    slide = None
    slide = request.args.get('slide')

    if slide is not None:
        slide = int(slide)
        if 1 <= slide <= 8:
            return render_template(f'slide_{slide}.html')

    return render_template('main.html')


@app.route('/index')
def main():
    return render_template('main.html')


if __name__ == '__main__':
    app.run()
