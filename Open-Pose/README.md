## Realtime Multiperson Pose Estimation: Keras Model 
This is a keras version of [Realtime Multi-Person Pose Estimation](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation) project  

## Introduction
Code repo for reproducing [2017 CVPR](https://arxiv.org/abs/1611.08050) paper using keras.  

This is a new improved version. The main objective was to remove
dependency on separate c++ server which besides the complexity
of compiling also contained some bugs... and was very slow.

The old version utilizing [rmpe_dataset_server](https://github.com/michalfaber/rmpe_dataset_server) is
still available under the tag [v0.1](https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation/releases/tag/v0.1) if you really would like to take a look.

## Results

#result screenshot for images
<p align="center">
<img src="https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation/blob/master/readme/image_pose_estimation_result1.png", width="720">
</p>
<div align="center">
<img src="https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation/blob/master/readme/image_pose_estimation_result2.png", width="300", height="300">
</p>
<div align="center">
<img src="https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation/blob/master/readme/image_pose_estimation_result3.png", width="300", height="300">


#result screenshot for videos
<img src="https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation/blob/master/readme/sample1.mp4-11-08-21-46-49.mp4", width="300", height="300">
<img src="https://github.com/michalfaber/keras_Realtime_Multi-Person_Pose_Estimation/blob/master/readme/sample2.mp4-11-08-21-40-51.mp4", width="300", height="300">
</div>



## Contents
#converting caffe model to keras model
1. [Converting caffe model](#converting-caffe-model-to-keras-model)
2. [Testing](#testing-steps)
3. [Training](#training-steps)
3. [Changes](#changes)

## Requirements: 
1. [Keras](https://keras.io/)
2. [Caffe - docker](https://hub.docker.com/r/bvlc/caffe/) required if you would like to convert caffe model to keras model. You 
 don't have to compile/install caffe on your local machine.

## Converting Caffe model to Keras model
Authors of [original implementation](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation) released already trained caffe model 
which you can use to extract weights data.   

- Download caffe model `cd model; sh get_caffe_model.sh`
- Dump caffe layers to numpy data `cd ..; docker run -v [absolute path to your keras_Realtime_Multi-Person_Pose_Estimation folder]:/workspace -it bvlc/caffe:cpu python dump_caffe_layers.py`
  Note that docker accepts only absolute paths so you have to set the full path to the folder containing this project.
- Convert caffe model (from numpy data) to keras model `python caffe_to_keras.py`  


## Related repository
- CVPR'16, [Convolutional Pose Machines](https://github.com/shihenw/convolutional-pose-machines-release).
- CVPR'17, [Realtime Multi-Person Pose Estimation](https://github.com/ZheC/Realtime_Multi-Person_Pose_Estimation).

## Citation
Please cite the paper in your publications if it helps your research:    

    @InProceedings{cao2017realtime,
      title = {Realtime Multi-Person 2D Pose Estimation using Part Affinity Fields},
      author = {Zhe Cao and Tomas Simon and Shih-En Wei and Yaser Sheikh},
      booktitle = {The IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
      year = {2017}
      }
	  

