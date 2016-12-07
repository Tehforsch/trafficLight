import tensorflow as tf
import numpy as np
from constants import STDDEV, LEARNING_PARAMETER

class MLP(object):
    def __init__(self, shape, inputLayer, nonlinearities, cost):
        self.shape = shape
        self.numLayers = len(shape)
        self.nonlinearities = nonlinearities
        self.biases = [self.getBias(m) for m in self.shape[1:]]
        self.weights = [self.getWeights(m, n) for (m, n) in zip(self.shape, self.shape[1:])]
        self.inputLayer = inputLayer
        self.layers = []
        self.setupModel()
        self.trainingData = tf.placeholder("float", self.outputLayer.get_shape())
        self.cost = cost(self.trainingData, self.outputLayer)
        self.training = tf.train.GradientDescentOptimizer(LEARNING_PARAMETER).minimize(self.cost)
        self.session = tf.Session()
        tf.initialize_all_variables().run(session=self.session)

    def getBias(self, m):
        return tf.Variable(tf.random_normal([m], stddev = STDDEV))

    def getWeights(self, m, n):
        return tf.Variable(tf.random_normal([m, n], stddev = STDDEV))

    def setupModel(self):
        layer = self.inputLayer
        for i in range(self.numLayers - 1):
            self.layers.append(layer)
            # feed forward one layer
            layer = self.nonlinearities[i](self.biases[i] + tf.matmul(layer, self.weights[i]))
        self.outputLayer = layer
        self.layers.append(self.outputLayer)

    def train(self, trainingData):
        trainingIn, trainingOut = trainingData
        self.session.run(self.training, feed_dict={
            self.inputLayer: trainingIn, 
            self.trainingData: trainingOut
        })
        print("Accuracy: ", self.session.run(self.cost, feed_dict={
            self.inputLayer: trainingIn, 
            self.trainingData: trainingOut
        }))

    def printWeightValues():
        for i in range(len(self.weights)):
            print(self.session.run(self.weights[i].value()))

    def printBiasValues():
        for i in range(len(self.biases)):
            print(self.session.run(self.biases[i].value()))
