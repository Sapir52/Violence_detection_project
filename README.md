# Violence_detection_project

# The project's target

The goal of the project is to detect violence in video, in addition, to identifying objects through computer vision libraries.

# Pipline
1. The input and process 20 video frames in batch with the VGG16 model.
Just prior to the final classification layer of the VGG16 model, the resulting transfer-values saved to a cache file.

2. These transfer values were used as input to the CNN + LSTM neural network. I then trained the second neural network using the classes from the violence dataset (Violence, No-Violence), so the network learns how to classify images based on the transfer-values from the VGG16 model.

# Result
![cm](https://user-images.githubusercontent.com/63209732/124356048-ce1af400-dc1c-11eb-8bb4-fad0397c53d5.png)

![accuracy](https://user-images.githubusercontent.com/63209732/124356054-d2471180-dc1c-11eb-8ed9-fcfb0269a3ab.png)

![loss](https://user-images.githubusercontent.com/63209732/124356057-d5420200-dc1c-11eb-99f1-0ab86ae07449.png)

![png1](https://user-images.githubusercontent.com/63209732/124356167-4aadd280-dc1d-11eb-8a5f-f300a3031da5.png)

![png2](https://user-images.githubusercontent.com/63209732/124356173-50a3b380-dc1d-11eb-81ca-ad9555c552e7.png)

![png3](https://user-images.githubusercontent.com/63209732/124356178-5a2d1b80-dc1d-11eb-8be0-f4be3866c1c0.png)





