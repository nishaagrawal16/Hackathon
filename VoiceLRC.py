import pitch
from pydub import AudioSegment
import os
import wave
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
import pickle

##############################################################
#
#  This is for creating the trained Data from the sample files.
#
##############################################################
def trained_data():
    pitch = [] # Data creation
    gender = [] # Stores the gender
    age = [] # Stores the age
    for (root, dirs, files) in os.walk('../gender_age/manual_data/'):
        for file in files:
            print(file)
            audio = os.path.join(root, file)
            wav_obj = wave.open(audio, 'rb')
            if (wav_obj.getnchannels() == 2): #converting to single channel
                sound = AudioSegment.from_wav(audio)
                sound = sound.set_channels(1)
                sound.export(audio, format="wav")
            pit = pitch.find_pitch(audio)
            print(pit)
            splitted_file_name = file.split('_')
            if(splitted_file_name[0] == 'M'):
                gender.append([0])
            else:
                gender.append([1])
                
            pitch.append([pit])

            age.append([splitted_file_name[1]])

    classifier = LogisticRegression(random_state = 0)
    classifier.fit(pitch, gender)

    depX = []
    for i in range(0, len(gender)):
        depX.append([pitch[i][0], gender[i][0]])
    decision_tree = DecisionTreeClassifier(criterion = 'entropy' , random_state = 0, max_depth = 2, min_samples_split = 3)
    decision_tree.fit(depX, age)
    
    # Saves the model to disk.
    classifier_filename = 'classifier_model.sav'
    decision_tree_filename = 'decision_tree_model.sav'

    pickle.dump(classifier, open(classifier_filename, 'wb'))
    pickle.dump(decision_tree, open(decision_tree_filename, 'wb'))
            

if __name__ == '__main__':
    trained_data()
