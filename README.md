# MIDAS_Internship
CNN Task Work

Added the Colab Jupyter Notebook for the work done. 

Task 2 : 
* Use this dataset (https://www.dropbox.com/s/pan6mutc5xj5kj0/trainPart1.zip) to train a CNN. Use no other data source or pretrained networks, and explain your design choices during preprocessing, model building and training. Also, cite the sources you used to borrow techniques. A test set will be provided later to judge the performance of your classifier. Please save your model checkpoints.
* Next, select only 0-9 training images from the above dataset, and use the pretrained network to train on MNIST dataset. Use the standard MNIST train and test splits (http://yann.lecun.com/exdb/mnist/). How does this pretrained network perform in comparison to a randomly initialized network in terms of convergence time, final accuracy and other possible training quality metrics? Do a thorough analysis. Please save your model checkpoints.
* Finally, take the following dataset (https://www.dropbox.com/s/otc12z2w7f7xm8z/mnistTask3.zip), train on this dataset and provide test accuracy on the MNIST test set, using the same test split from part 2. Train using scratch random initialization and using the pretrained network part 1. Do the same analysis as 2 and report what happens this time. Try and do qualitative analysis of what's different in this dataset. Please save your model checkpoints.


Requiremets/Dependencies:

1. fastbook 
You can use fastai without any installation by using Google Colab. In fact, every page of this documentation is also available as an interactive notebook - click "Open in colab" at the top of any page to open it (be sure to change the Colab runtime to "GPU" to have it run fast!) See the fast.ai documentation on Using Colab for more information.

conda install -c fastai -c pytorch -c anaconda fastai gh anaconda
miniconda : conda install -c fastai -c pytorch fastai
pip install fastai

2. python 3.35+




TRAINED MODELS:
1. https://drive.google.com/file/d/1-NeyT_BRyjRfDHl4wFT-h3RVYY5dJci0/view?usp=sharing
2. https://drive.google.com/file/d/1-EfsDTiJv3rF2oS8i9ANv9O6POZ9L2q3/view?usp=sharing

TO LOAD THE MODELS FOR TESTING:

* Since, its a fastai wrapper it's helpful to use their method.
* Step1 : learn_inf = load_learner(path/'model_file')
* Step2 : pred,pred_idx,probs = learn_inf.predict(img)
* This gives our predictions.
