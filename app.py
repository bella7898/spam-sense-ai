from flask import Flask, render_template, request
import spamsense
from flask import redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/demo')
def demo():
  return render_template('demo.html',
                         label1='HAM',
                         score1=0,
                         label2='SPAM',
                         score2=0)

@app.route('/generateclassification', methods=["POST"])
def generateclassification():
  # grab the text from our text box inpupt and store it in variable 'prompt'
  prompt = request.form["message"]
  # define our payload we are sending to the model;
  payload = {
    # set this to the string format of the prompt variable
    "inputs": str(prompt),
    "options": {  # make sure we wait for model to wake up
      "wait_for_model": True
    }
  }
  # use SpamSense to call the query() function on the payload and set the result to a variable 'result'
  result = spamsense.query(payload)

  # figure out how result is formated
  # this is what we have: [[{'label': 'HAM', 'score': 0.9981971383094788}, {'label': 'SPAM', 'score': 0.0018028367776423693}]]

  # what the prediction is
  prediction_1 = result[0][0]
  prediction_2 = result[0][1]

  p1label = str(prediction_1['label']).title()
  p1score = int(prediction_1['score'] * 100)
  p2label = str(prediction_2['label']).title()
  p2score = int(prediction_2['score'] * 100)
  # update the return template but pass in prediction_1 as one variable and predicion_2 as another
  return render_template('demo.html',
                         label1=p1label,
                         score1=p1score,
                         label2=p2label,
                         score2=p2score)

app.run(host='0.0.0.0', port=81)