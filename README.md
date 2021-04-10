# MIDAS_Internship
CNN Task Work

Added the Colab Jupyter Notebook for the work done. 


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
Since, its a fastai wrapper it's helpful to use their method.
Step1 : learn_inf = load_learner(path/'model_file')
Step2 : pred,pred_idx,probs = learn_inf.predict(img)
This gives our predictions.
