#############################################################################
#
#  This is used for getting the gender and age range for the uploaded voice.
#
############################################################################
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import pitch

app = Flask(__name__, template_folder='/home/shivani_dynamisers/Hackathon/gender_age')
CORS(app, support_credentials=True)

@app.route('/home')
def index():
   return render_template('home.html')

@app.route('/file', methods=["POST"])
def file_name():
    test_audio = request.form.get("myfile")
    print('File we are getting: ', test_audio)
    classifier_filename = 'classifier_model.sav'
    decision_tree_filename = 'decision_tree_model.sav'

    # load the model from disk
    classifier = pickle.load(open(classifier_filename, 'rb'))
    decision_tree = pickle.load(open(decision_tree_filename, 'rb'))

    gender = classifier.predict([[pitch.find_pitch(test_audio)]][0]
    if gender:
        gen = 'Hey, gorgeous lady!'
    else:
        gen = 'Hey, handsome guy!'
    age = int(decision_tree.predict([[pitch.find_pitch(test_audio),0]])[0])
    print(gen)
    age_state = 'You come under '
    if age in range(13, 20):
        age_state += 'Teenager age (13 - 20)'
    elif age in range(21, 40):
        age_state += 'Adult age (21 - 40)'
    elif age in range(41, 60):
        age_state += 'Middle age (41 - 60)'
    else:
        age_status += 'Old age (60+)'
    print(f'Hey you come under {age_state}: {age}')
    return render_template('home.html', gen=gen, age=age_state)

@app.route('/greeting/<name>')
def give_greeting(name):
    return 'Hello. {0}!'.format(name)

if __name__ == '__main__':
   app.run('0.0.0.0', 5000)
