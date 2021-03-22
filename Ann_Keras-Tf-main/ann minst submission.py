import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np

#using the mnisnt datset
mnist = tf.keras.datasets.mnist
(x_train, y_train),(x_test, y_test) = mnist.load_data()

x_train = tf.keras.utils.normalize(x_train, axis=1)
x_test = tf.keras.utils.normalize(x_test, axis=1)

model = tf.keras.models.Sequential()#feed froward model
model.add(tf.keras.layers.Flatten())#flatten our input =>28x28 to 1x784

#creating layers of aneural network
#Dense:every node connected
#relu= rectified linear =>activation function
#Loss is a calculation of error. A neural network  attempts to minimize loss.

model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)

print('\nModels loss:')# model's loss (error)
print(format(val_loss,'.5f'))
print('\nModels accuracy:')# model's accuracy
print(format(val_acc,'.5f'))

model.save('Ann_mnist_keras,tensorflow.model')#saving our model


new_model = tf.keras.models.load_model('Ann_mnist_keras,tensorflow.model')#loading our model
predictions=new_model.predict(x_test)

print('\nThe Number is:\n',np.argmax(predictions[0]))#predicts the number
plt.title("Test number is:")
plt.axis('off')

plt.imshow(x_test[0],cmap=plt.cm.binary)#shows a test sample which is recognised as 7
plt.show()



