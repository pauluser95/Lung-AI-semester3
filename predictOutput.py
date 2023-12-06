import sys
import tensorflow as tf
import numpy as np
from tensorflow.python.keras.layers import Dense, Flatten
import cv2

data_to_js="this is from python"

input = sys.argv[1]
# input="00cfd1c1.png"

dataset_url = "./uploads/"+input
img_height=180
img_width=180

class_names = ['ARDS', 'Bacterial Pneumonia', 'COVID-19', 'Chlamydophila', 'E.Coli', 'Fungal Pneumonia', 'Influenza', 'Klebsiella', 'Legionella', 'Lipoid pneumonia', 'Mycoplasma', 'No Finding', 'No Pneumonia (healthy)', 'Pneumocystis', 'Pneumonia', 'SARS', 'Streptococcus', 'Undefined Pneumonia', 'Varicella', 'Viral Pneumonia']

resnet_model = tf.keras.models.Sequential()

pretrained_model= tf.keras.applications.ResNet50(include_top=False,
                   input_shape=(180,180,3),
                   pooling='avg',classes=20,
                   weights='imagenet')
for layer in pretrained_model.layers:#dont know what, should comment later if not commented train time is shorter
        layer.trainable=False

resnet_model.add(pretrained_model)
resnet_model.add(Flatten())
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(20, activation='softmax'))
resnet_model.load_weights('w-ori-resnet.h5')




image=cv2.imread(dataset_url)
image_resized=cv2.resize(image,(180,180))
image=np.expand_dims(image_resized,axis=0)

pred=resnet_model.predict(image,verbose=0)
for i in range(len(pred[0])):
  pred[0][i]=pred[0][i]*100
  pred[0][i]=round(pred[0][i],2)
output_class=class_names[np.argmax(pred)]
print("The predicted result is",output_class,"</p><p>",pred[0][np.argmax(pred)],"%</p>")

sys.stdout.flush()
