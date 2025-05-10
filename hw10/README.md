# Homework 10: Calling an AI Model – Basic Example

## 📘 Overview

This assignment demonstrates how to define and call a simple AI model using PyTorch. The example shows a basic neural network performing a forward pass on some random input data.

## 🧠 Objective

- Create a simple neural network model using `torch.nn.Module`.
- Pass input data to the model to obtain an output.
- Understand how forward propagation works in a basic setting.

## ✅ Implementation Summary

1. **Model Definition**  
   A neural network with:
   - Input layer: 10 features
   - Hidden layer: 5 neurons with ReLU activation
   - Output layer: 1 neuron (for regression or binary classification style output)

2. **Input Generation**  
   Randomly generated input tensor of shape `[1, 10]`.

3. **Model Call**  
   The model is called with the input tensor, and the output is printed.