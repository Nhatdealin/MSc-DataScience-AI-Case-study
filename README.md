# MSc-DataScience-AI-Case-study

***MSc1 Data Science and AI - Case-study class***


## Artificial intelligence for animal bone classification


**Aim**: Based on a database of 2D images taken from meshed 3D models of bones, this study intends
to distinguish four morphologically close mammalian species.


The methods used by archaeozoologists to identify animal species from bones recovered from archaeological sites are based on a combination of several anatomical and osteometric criteria. However, many species have very similar morphological characteristics that limit the identification of animals at the species level, especially when the bones are not well preserved, broken or fragmentary. Thus, this prospective study proposes to develop a new methodological approach based on Machine Learning methods to distinguish morphologically close species by means of specific skeletal part: the astragalus bone.

The four species currently studied belong to the Caprinae subfamily: sheep, goat, mouflon and chamois. For each of these species, between 10 and 20 specimens have been modelled in 3D. These models are the objects of this project.

The main steps of the analytical procedure will be the following:

    1) The student will have to generate multiple 2D images from all sides of meshed 3D modelled astragali. The 2D images can be generated from the MeshLab software. The number of images is to be defined by the student in discussion with the supervisors.

    2) Based on this image dataset, the student will investigate supervised and unsupervised Machine Learning (i.e., Support-Vector Machines and Convolutional Neural Network) in order to correctly assign the images to the corresponding species.

    3) Machine Learning methods for 3D data processing could also be investigated for classification.


## Abstract
In recent years, deep learning has achieved great success in many fields, such as computer vision and natural language processing. However, this kind of techniques hasn’t been widely explored in archaeology and specifically, in the classification of animals from bones collected from archaeological sites. As we know, archaeological research is a very specific discipline in its approach to specimens as well as data. The methods used by archaeozoologists to identify animals from bones recovered from archaeological sites are based on a combination of several anatomical and bone measurement criteria. However, many species with very similar morphological characteristics limit the identification of animals at the species level, especially when bones are not well preserved, broken, or fragmented. Therefore, this potential study proposes the development of a new methodological approach based on Deep Learning methods to distinguish morphologically closely related species by specific skeleton parts: Astragalus. Transfern Learning is used with a Resnet18 arquitecture to train 2D images rendered from a 3D astragalus model, achieving accuracy of 0.6 for the classification between 4 classes of the bone.


## Summary result

<div id="tab:table-name">

**Model result**
| Dataset name | Train accuracy | Validation accuracy | Test accuracy |
|:-------------|:---------------|:--------------------|:--------------|
| Dataset 1    | 0.788          | 0.449               | 0.45          |
| Dataset 2    | 0.865          | 0.667               | 0.40          |
| Dataset 3    | 0.860          | 0.724               | 0.5964        |

<span id="tab:table-name"
label="tab:table-name">\[tab:table-name\]</span>Table comparing result
from each datasets.

</div>


## Training result
![History accuracy]() <img src="https://github.com/Nhatdealin/MSc-DataScience-AI-Case-study/blob/master/img/accurancy.png" width="100" height="100">

![History loss]()<img src="https://github.com/Nhatdealin/MSc-DataScience-AI-Case-study/blob/master/img/accurancy.png" width="100" height="100">
