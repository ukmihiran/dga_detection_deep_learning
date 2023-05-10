import tensorflow as tf
import json
import joblib
import pandas as pd
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from keras.models import load_model
from keras.layers import Embedding, LSTM, Dense, Dropout
from keras.models import Sequential
from sklearn.preprocessing import OneHotEncoder

#%%
RANDOM_STATE = 42
MAX_LENGTH = 20

#%%
### Set Paths
binary_tokenizer_path = r'utils_DGA_BINARY/Binary_tokenizer.json'
class_tokenizer_path = r'utils_DGA_Classes/Class_tokenizer.json'

hot_encoder_path = r'utils_DGA_BINARY/hot_encode.sav'
label_encoder_path = r'utils_DGA_Classes/Label_encode.sav'


DGA_model = load_model(r'DGA_Binary_Model.h5')
class_classification = load_model(r'DGA_Class_Final_Model.h5')

#%%
### **Load Data from Trainning**
# Load Tokenizer
with open(class_tokenizer_path) as f:
    data = json.load(f)
    class_tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)

with open(binary_tokenizer_path) as f:
    data = json.load(f)
    binary_tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)
    
#%%
# Load Encoder
hot_encoder = joblib.load(hot_encoder_path)
label_encoder = joblib.load(label_encoder_path)


def preprocess_text(text):
  if text[:3] == "www":
    text = text[4:]
  return text

def text_formation(test_website):
  text = preprocess_text(test_website)
  encode_text = pd.Series(text)

  binary_encode_text = binary_tokenizer.texts_to_sequences(encode_text)
  binary_encode_text = pad_sequences(binary_encode_text, maxlen = MAX_LENGTH , padding='post')

  class_encode_text = class_tokenizer.texts_to_sequences(encode_text)
  class_encode_text = pad_sequences(class_encode_text, maxlen = MAX_LENGTH , padding='post')

  return binary_encode_text,class_encode_text


def binary_prediction(binary_encode_text):
  prediction_binary = DGA_model.predict(binary_encode_text,verbose=0)
  print(prediction_binary)
  binary_pred_acc = np.amax(prediction_binary)
  prediction_binary = hot_encoder.inverse_transform(prediction_binary)[0][0]
  return prediction_binary,binary_pred_acc

def class_prediction(class_encode_text):
  prediction_class = class_classification.predict(class_encode_text,verbose=0)
  class_pred_acc = np.amax(prediction_class)
  prediction_class = np.argmax(prediction_class, axis=1)
  prediction_class = label_encoder.inverse_transform(prediction_class)[0]
  return prediction_class,class_pred_acc

def inferencing(test_website):
    binary_encode_text,class_encode_text = text_formation(test_website)
    
    prediction_binary,binary_pred_acc = binary_prediction(binary_encode_text)
    print(f'The Website : {test_website} is {prediction_binary}')
    binary_prediction_arry = [prediction_binary,binary_pred_acc]
    #print(binary_pred_acc)
    if prediction_binary == 'DGA':
        prediction_class,class_pred_acc = class_prediction(class_encode_text)
        print(f'The Website : {test_website} is {prediction_class}')
        print("ALERT !!!")
        return [binary_prediction_arry,[prediction_class,class_pred_acc]]
    else:
        return [binary_prediction_arry,[None,None]]
        
    
#print(class_pred_acc)
## Enter Custom URL
# test_website = 'www.xkkumnnbpr.com'   'earnestnessbiophysicalohax.com'
# test_website = 'github.com'
# print(inferencing(test_website))

