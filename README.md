<p align="center">
  <img src="https://user-images.githubusercontent.com/54715463/155894839-e6a05c2e-aa95-4b53-bb4d-c4cbc1a964b9.png" alt="Material Bread logo">
</p>

***

# RoboMedicinae1 - Segmentation models CNN
<a href="https://github.com/Steigner/RM1_ROS/blob/main/LICENSE"><img alt="License: MIT" src="https://black.readthedocs.io/en/stable/_static/license.svg"></a>
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

**Open-source, copy and modify what you need!**

**Open-source, kopírujte a upravujte co potřebujete!**

## About
RM1 is an experimental robotic platform created to automate antigen testing. This project was developed as part of a master's thesis. The aim was to create a functional and modular prototype that is easily modifiable and deployable after debugging. The basic idea is to create a web-based server that communicates with ROS. ROS was used in the work as a simulation and debugging environment, mainly for robot control. The thesis is divided into four main parts:

+ [<=](https://github.com/Steigner/Robo_Medicinae_I) Robo Medicinae I
+ [<=](https://github.com/Steigner/RM1_server) RM1 - Server
+ [<=](https://github.com/Steigner/RM1_ROS) RM1 - ROS         
+ [<=](https://github.com/Steigner/RM1_Gripper) RM1 - Gripper
+ [<=](https://github.com/Steigner/RM1_SegCNN) RM1 - SegCNN

Scripts used to train convolutional neural networks to segment images for nostril detection are integrated in this repository. The Make-Sense tool was used for the labeling process. Then a custom script was implemented for subsequent masking. Subsequently, the actual augmentation and training process is stored in the .ipynb notebook. For interest, a script was also added to demonstrate the minimum search using the Adagrad algorithm. The trained models are also included in .onnx format. However, the dataset was not included due to GDPR.

## Screenshots and videos

<p align="center"> <b>Click to full resolution</b> </p>

![plot](Unet.png)
![plot](ASPOCRNet.png)

## Authors

* Author: Martin Juricek
* Supervisor: Roman Parak

## Citation
If you want to quote please check the header repository. 

github.com/Steigner/Robo_Medicinae_I [=>](https://github.com/Steigner/Robo_Medicinae_I) 

## References

[Faculty of Mechanical Engineering BUT](https://www.fme.vutbr.cz/en)
