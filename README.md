# Violence_detection_project

# The project's target

The goal of the project is to detect violence in video, in addition, to identifying objects through computer vision libraries.

# Pipline
1. The input and process 20 video frames in batch with the VGG16 model.
Just prior to the final classification layer of the VGG16 model, the resulting transfer-values saved to a cache file.

2. These transfer values were used as input to the CNN + LSTM neural network. I then trained the second neural network using the classes from the violence dataset (Violence, No-Violence), so the network learns how to classify images based on the transfer-values from the VGG16 model.

# Result




