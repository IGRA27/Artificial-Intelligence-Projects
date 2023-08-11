from flask import Flask, jsonify, request
import numpy as np
from PIL import Image
import tensorflow as tf

app = Flask(_name_)
app.config['ENV'] = 'production'

model = tf.keras.models.load_model('modelo.h5')

@app.route('/predict', methods=['POST'])
def predict():
    # Procesa la imagen recibida
    img = Image.open(request.files['image']).resize((256, 256))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Realiza la predicción utilizando el modelo cargado
    prediction = model.predict(img)[0]
    #Obtiene la etiqueta de la predicción
    label = 'gauss' if prediction[0] > prediction[1] and prediction[0] > prediction[2] else \
            'movimiento' if prediction[1] > prediction[0] and prediction[1] > prediction[2] else \
            'nitida'
    
    # Devuelve la respuesta en formato JSON
    return jsonify({'prediction': label})

if _name_ == '_main_':
    app.run()