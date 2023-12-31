"""
Learning how to create a neural network from scratch -> possibly to create a naive model
of the C. elegans connectome
"""

import numpy as np

class NeuralNetwork:
    def __init__(self, neurons):
        self.layer = neurons

    def forward(self, inputs):
        outputs = []
        for neuron in self.layer:
            weighted_sum = sum(neuron.weights[i][1] * inputs[i] for i in range(len(inputs))) + neuron.bias
            neuron.output = self.activation_function(weighted_sum)
            outputs.append(neuron.output)
        return outputs

    def activation_function(self, x):
        # You can use different activation functions here, e.g., sigmoid, relu, etc.
        return 1 / (1 + np.exp(-x))
