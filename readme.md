The original paper is available under: https://arxiv.org/abs/2101.03541


## Objective

The ability to detect and track fast-moving objects is crucial for various applications of Artificial Intelligence like autonomous driving, ball tracking in sports, robotics or object counting. The goal of this project was to develop the Fully Convolutional Neural Network "CueNet", whose task is to detect and track a cueball on a labyrinth game robustly and reliably. It's the first step to make an autonomous system that can play the labyrinth game on its own.

## CueNet

To tackle this problem we developed two models, CueNet V1 which has a single 240 x 180-pixel input image and CueNet V2 whose approach was to take three consecutive 240 x 180-pixel images as an input and transform them into a probability heatmap for the cueball's location. The network was tested with a separate video that contained all sorts of distractions to test its robustness. When confronted with our testing data, CueNet V1 predicted the correct cueball location in 99.6% of all frames, while CueNet V2 had 99.8% accuracy.

#### Demo of CueNet(Output in red) with our dataset "HeavyTest":

![](labyrinth.gif)
