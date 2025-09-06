# Handwritten Digit Recognition (MNIST)

This is a simple project for handwritten digit recognition using the MNIST 
dataset and a fully-connected neural network built with **PyTorch**.

## Requirements

You need to install the following Python libraries:

```bash
pip install numpy torch torchvision matplotlib
```

## How to Run

Run the following command in your terminal:

```bash
python test.py
```

On the first run, the MNIST dataset will be downloaded automatically. Please make sure you have a stable internet connection.


## Project Description

Dataset: MNIST (70,000 images of handwritten digits, 28x28 grayscale).

Model: A feed-forward neural network with 3 hidden layers (64 units each) and ReLU activations.

Training: Uses Adam optimizer and negative log-likelihood loss.

Output: Prints training accuracy and shows sample predictions with matplotlib.

## Notes

The dataset will be cached locally (about 20 MB).

If you re-run the program, the dataset will be loaded from your local cache (no need to re-download).

