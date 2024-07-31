This is the readme file. Here are the steps that were done for setting up git.
Step 1: For mac, first open a new terminal and then do the following steps:
    Step 1.1: cat ~/.ssh/id_rsa.pub This command will show the public key for my mac terminal
    Step 1.2: copy paste the public key from my local onto a clipboard.
    Step 1.3: now paste the text of step 1.2 at github.com->click on photo->settings->SSH and GPG keys--> New SSH keys--> name it, mine is called "personal mac" and then add the value from clipboard. This entire step will ensure that you can commit from your local mac.
Step 2: Now i downloaded the data from https://www.kaggle.com/datasets/priyamchoksi/adult-census-income-dataset?resource=download into downloads directory.
Step 3: create a local folder on mac and using terminal go to that folder.
Step 4: now fire the following commands:
    Step 4.1: git init
    Step 4.2: git status
    Step 4.3: git add adult.csv
    Step 4.4: git commit -m "initial commit". 
    Step 4.5: git push origin -u feature/v0.1
Step 5: Check the code is committed into feature/v0.1 branch 
