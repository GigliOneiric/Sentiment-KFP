# Sentiment-KFP
Sentiment KLP is an open source analysis software used to perform sentiment analysis with Kubeflow Pipelines.

# Running the vanilla KFP version

1. Go to Kubeflow Dashboard and on the left panel click on Volumes.

2. Click on the “+ New Volume” button on the top right and create a volume by giving the name “model-volume”. 

3. Go to Kubeflow Dashboard and on the left panel click on Notebooks.

4. Click on the “+ New Notebook” button on the top right and create a notebook by giving it a name.

5. After the set up is done, click on the Connect button next to the notebook you just created. It will take you to a JupyterLab.

6. In the JupyterLab launcher start a new terminal session to clone the github repo. In the terminal enter the following commands:

 ```$ git clone https://github.com/GigliOneiric/Sentiment-KFP.git``` 

7. After succesfully cloning the repo open the notebook named "Main.ipynb" by double-clicking on this name in the left hand directory structure, and to run it click on the "restart the whole kernel and re-reun the whole notebook" button in the top menu of the notebook.
