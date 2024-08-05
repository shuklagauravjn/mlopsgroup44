This is the readme file. Here are the steps that were done for 

**Setting up Version Control:**
<p>
Step 1: For mac, first open a new terminal and then do the following steps:<br>
    Step 1.1: cat ~/.ssh/id_rsa.pub This command will show the public key for my mac terminal<br>
    Step 1.2: copy paste the public key from my local onto a clipboard.<br>
    Step 1.3: now paste the text of step 1.2 at github.com->click on photo->settings->SSH and GPG keys--> New SSH keys--> name it, mine is called "personal mac" and then add the value from clipboard. This entire step will ensure that you can commit from your local mac.<br>
Step 2: Now i downloaded the data from https://www.kaggle.com/datasets/priyamchoksi/adult-census-income-dataset?resource=download into downloads directory.<br>
Step 3: create a local folder on mac and using terminal go to that folder.<br>
Step 4: now fire the following commands:<br>
    Step 4.1: git init<br>
    Step 4.2: git status<br>
    Step 4.3: git add adult.csv<br>
    Step 4.4: git commit -m "initial commit".<br> 
    Step 4.5: git push origin -u feature/v0.1<br>
Step 5: Check the code is committed into feature/v0.1 branch<br>

**Set Up a CI/CD Pipeline:**

Step 1: python3 -m venv myenv<br> 
Step 2: source myenv/bin/activate<br> 
Step 3: pip install -r requirements.txt<br> 

**Steps to create docker container:**

Step 1: create Dockerfile<br> 
Step 2: docker build -t shuklagauravjn/ml-ops-group44-v-01:latest .<br> 
Step 3: docker run -dp 127.0.0.1:7003:7003 ml-ops-group44-v-01 <br> 
Step 4: docker ps <br>
Step 5: docker container ls<br>
Step 6: docker login -u "shuklagauravjn" -p "XSDSDwewe#" docker.io<br>
Step 7: docker push shuklagauravjn/ml-ops-group44-v-01:latest <br>

**Steps to deploy docker container to minikube:**
Step 1: brew install minikube<br> 
Step 2: minikube start <br> 
Step 3: kubectl create deployment ml-ops-group44-v-01 --image=shuklagauravjn/ml-ops-group44-v-01:latest <br> 
Step 4: kubectl expose deployment ml-ops-group44-v-01 --type=NodePort --port=8080 <br>
Step 5: kubectl get services ml-ops-group44-v-01<br>
Step 6: minikube service ml-ops-group44-v-01 <br>
Step 7: <br> 

**Steps to install DVC on local mac and then doing push pull checkout operation:**
Step 1: brew install dvc<br> 
Step 2: dvc init <br> 
Step 3: git status <br> 
Step 4: git commit -m "Initialize DVC" <br>
Step 5: dvc get https://github.com/iterative/dataset-registry \
get-started/data.xml -o data/data.xml <br>
Step 6: dvc add data/data.xml <br>
Step 7: git add data/data.xml.dvc data/.gitignore<br> 
Step 8: git commit -m "Add raw data"<br> 
Step 9: git add data/data.xml.dvc data/.gitignore<br> 
Step 10: mkdir /tmp/dvcstore<br> 
Step 11: dvc remote add -d myremote /tmp/dvcstore<br> 
Step 12: dvc push<br> 
Step 13: dvc pull<br> 
Step 14: cp data/data.xml /tmp/data.xml<br> 
Step 15: cat /tmp/data.xml >> data/data.xml<br> 
Step 16: dvc add data/data.xml
Step 17: dvc push
Step 18: git commit data/data.xml.dvc -m "Dataset updates"