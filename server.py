from flask import *
from summary import *

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize',methods=['POST'])
def other():
    body = request.form['textbox']
    length = request.form['length']
    print(length)
    res = get_summary(body,length) 
    data = {'body':body,'len':length,'res':res}   
    return render_template('other.html',data = data)


if __name__ == '__main__':
    app.run(debug=True)