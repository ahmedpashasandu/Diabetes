# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 17:07:36 2025

@author: chotu s
"""

import numpy as np
import pickle


loaded_model=pickle.load(open("C:/Users/chotu s/Desktop/deoloy ml project/trained_model.sav","rb"))

input_data=(5,166,72,19,175,25.8,0.587,51)
input_data_as_numpy_array=np.asarray(input_data)
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)

if (prediction[0]==0):
    print("the person is deabetics")
else:
    print("the person is not deabetics")