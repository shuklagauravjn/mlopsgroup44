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
Step 5: docker container ls
Step 6: docker login -u "shuklagauravjn" -p "XSDSDwewe#" docker.io
Step 6: docker push shuklagauravjn/ml-ops-group44-v-01:latest 