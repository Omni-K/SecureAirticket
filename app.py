from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    #fulldoc = int(request.args.get('fulldoc'))
    slide = int(request.args.get('slide'))
    print(slide)
    #if fulldoc == 1:
    #    return render_template('fulldoc1.html')
    #if fulldoc == 2:
    #    return render_template('fulldoc2.html')
    if 1 <= slide <= 8:
        return render_template(f'slide_{slide}.html')

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
