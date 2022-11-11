from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='/home/shivani_dynamisers/Hackathon/gender_age')
@app.route('/home')
def index():
    fileName()
   return render_template('home.html')

def fileName():
    # fname = request.form.get("fname")
    fname = 'ren2'
    classifier_filename = 'classifier_model.sav'
    DecisionTree_filename = 'decision_tree_model.sav'

    # load the model from disk
    classifier = pickle.load(open(classifier_filename, 'rb'))
    Decision_Tree = pickle.load(open(DecisionTree_filename, 'rb'))

    test_audio = fname + '.wav'
    print('for sound test audio is ',classifier.predict([[pitch.find_pitch(test_audio)]]))
    print('age prediction is',Decision_Tree.predict([[pitch.find_pitch(test_audio),0]]))

if __name__ == '__main__':
   app.run('0.0.0.0', 5000)