# Sentiment-KFP
Sentiment KLP is an open source analysis software used to perform sentiment analysis with Kubeflow Pipelines.

# Running the vanilla KFP version

1. Go to Kubeflow Dashboard and on the left panel click on Volumes.

2. Click on the “+ New Volume” button on the top right and create a volume by giving the name “model-volume”. 

3. Go to Kubeflow Dashboard and on the left panel click on Notebooks.

4. Click on the “+ New Notebook” button on the top right and create a notebook by giving it a name.

5. After the set up is done, click on the Connect button next to the notebook you just created. It will take you to a JupyterLab.

6. In the JupyterLab launcher start a new terminal session to clone the github repo. In the terminal enter the following commands:

 ```
 $ git clone https://github.com/GigliOneiric/Sentiment-KFP.git
 ``` 

7. After succesfully cloning the repo open the notebook named "Main.ipynb" by double-clicking on this name in the left hand directory structure, and to run it click on the "restart the whole kernel and re-reun the whole notebook" button in the top menu of the notebook.

# Optional: Setup Seldon Core

1 . Label the namespace for inference tasks in kubernetes
```
kubectl label namespace kubeflow-user-example-com serving.kubeflow.org/inferenceservice=enabled
```

2. Install s2i
```
# Create a directory
mkdir /tmp/s2i/ && cd /tmp/s2i/

# Download S2I
curl -s https://api.github.com/repos/openshift/source-to-image/releases/latest| grep browser_download_url | grep linux-amd64 | cut -d '"' -f 4  | wget -qi -

# Unpack the tar
tar xvf source-to-image*.gz

# Move it to /usr/local/bin path to be executable
sudo mv s2i /usr/local/bin
rm -rf /tmp/s2i/
```

3. Copy the container folder to any directory on kubernetes

4. Creation of an image within the container directory copied previously
```
s2i build . seldonio/seldon-core-s2i-python38:1.10.0 seldon-sentiment:latest
```

5. Deploying the image in the Docker Registery
```
# Start the registry
docker run -d -p 5000:5000 --restart=always --name registry registry:2

# Tag the image so that it points to the registry
docker tag seldon-sentiment:latest  localhost:5000/seldon-sentiment:latest 

# Push the image
docker push localhost:5000/seldon-sentiment:latest 
```
6. Creation of a SeldonDeployment
```
kubectl apply -f https://raw.githubusercontent.com/GigliOneiric/Sentiment-KFP/main/seldon/SeldonDeployment.yml
```

7. Set up port forwarding
```
tmux new -d -s seldon "kubectl port-forward $(kubectl get pods -l istio=ingressgateway -n istio-system -o jsonpath='{.items[0].metadata.name}') -n istio-system 8050:8080 --address 0.0.0.0"
```

8. Test the SeldonDeployment

 8.1 Read the session cookie from the Kubeflow dashboard in the developer mode of the browser
 ```
 document.cookie
 ```
 8.2 Send a request
 ```
 curl http://localhost:8050/seldon/kubeflow-user-example-com/seldon-sentiment /api/v0.1/predictions --data-urlencode 'json={"data":{"ndarray":[["This is a test"]]}}' -H "Cookie: authservice_session=YOURCOOKIE" -v
 ```

