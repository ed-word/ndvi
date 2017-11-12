import pandas as pd
import numpy as np
from sklearn.svm import SVR


df = pd.read_csv('merge.csv')

xtrain = []
ytrain = []
xtest = []
ytest = []

x = df['LATITUDE'][0]
lalolist = [[df['AIR_TEMPERATURE'][0], df['SOIL_TEMPERATURE'][0], df['SOIL_MOISTURE'][0], df['RAINFALL'][0]]]
ylist = [df['VALUE'][0]] 
for index, row in df.iterrows():
	if x != row['LATITUDE']:
		templist = np.array(lalolist)
		
		a = templist[:-3]
		xtrain.extend(a)

		ytrain.extend(ylist[:-3])
		
		xtest.extend(templist[-3:])
		
		ytest.extend(ylist[-3:])
		
		lalolist = []
		ylist = []
		x = row['LATITUDE']
	else:
		temp = []
		temp.append(row['AIR_TEMPERATURE'])
		temp.append(row['SOIL_TEMPERATURE'])
		temp.append(row['SOIL_MOISTURE'])
		temp.append(row['RAINFALL'])
		ylist.append(row['VALUE'])
		lalolist.append(temp)


templist = np.array(lalolist)
a = templist[:-3]
xtrain.extend(a)
ytrain.extend(ylist[:-3])
xtest.extend(templist[-3:])
ytest.extend(ylist[-3:])

print(np.array(xtrain).shape)
print(np.array(ytrain).shape)
print(np.array(xtest).shape)
print(np.array(ytest).shape)




import tensorflow as tf

# Parameters
learning_rate = 0.00001
epoch = 10000
batch_size = 20
display_step = 10

# Network Parameters
n_hidden_1 = 64 # 1st layer number of neurons
n_hidden_2 = 64
n_hidden_3 = 64 
num_input = 4

# tf Graph input
X = tf.placeholder("float", [None, num_input])
Y = tf.placeholder("float", [None, 1])

weights = {
    'h1': tf.Variable(tf.random_normal([num_input, n_hidden_1])),
    'h2': tf.Variable(tf.random_normal([n_hidden_1, n_hidden_2])),
    'h3': tf.Variable(tf.random_normal([n_hidden_2, n_hidden_3])),
    'out': tf.Variable(tf.random_normal([n_hidden_3, 1]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'b2': tf.Variable(tf.random_normal([n_hidden_2])),
    'b3': tf.Variable(tf.random_normal([n_hidden_3])),
    'out': tf.Variable(tf.random_normal([1]))
}

# Construct a linear model
layer_1 = tf.add(tf.matmul(X, weights['h1']), biases['b1'])
layer_1 = tf.nn.relu(layer_1)

layer_2 = tf.add(tf.matmul(layer_1, weights['h2']), biases['b2'])
layer_2 = tf.nn.relu(layer_2)

layer_3 = tf.add(tf.matmul(layer_2, weights['h3']), biases['b3'])
layer_3 = tf.nn.relu(layer_3)

pred = tf.matmul(layer_3, weights['out']) + biases['out']

# Mean squared error
cost = tf.reduce_mean(tf.squared_difference(pred, Y))
# Gradient descent
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)


def generate_batch(x, y, start, end):
    x = x[start:end]
    y = y[start:end]

    bx = []
    by = []
    for i, j in zip(x,y):
    	bx.append(i)
    	by.append(j)

    bx = np.array(bx)
    by = np.array(by)
    by = by.reshape(-1,1)
    return (bx, by)	

no_of_batches = int(len(xtrain) / batch_size)

init = tf.global_variables_initializer()
with tf.Session() as sess:
	# Run the initializer
	sess.run(init)
	for step in range(1, epoch+1):
		try:
			loss = 0
			for j in range(no_of_batches):
				batch_x, batch_y = generate_batch(xtrain, ytrain, start=j*batch_size, end=(j+1)*batch_size)
				_, l, p = sess.run([optimizer,cost,pred], feed_dict={X: batch_x, Y: batch_y})
				loss += l
			if(step%display_step==0 or step==1):
				loss = float(loss/no_of_batches)
				print("Step ",str(step),", Minibatch Loss= ", str(loss))
		except KeyboardInterrupt:
			break
	print("Optimization Finished!")

	batch_x, batch_y = generate_batch(xtest, ytest, start=0, end=len(ytest))
	loss,p = sess.run([cost,pred], feed_dict={X: batch_x, Y: batch_y})
	loss /= len(xtest)
	for i, j in zip(batch_y,p):
		print("Actual: ",i," Pred: ",j)
	print("Test loss: ",loss)
