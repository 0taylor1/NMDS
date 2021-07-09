# NMDS
Non-metric Multidimensional Scaling

## Files
* `.ipynb_checkpoints`  
  - contains ipynb checkpoints from initial commit. will be removed 
* `figures`  
  - contains relevant plots/figures. to be expanded
* `Notes.ipynb`  
  - latex write-ups of governing mathematical expressions
  - small snippets of code for testing 
* `cvxpy.ipynb`  
  - code for solving problem using cvxpy. draft version
* `cvxpy_examples.ipynb`
  - examples from cvxpy.org to help understand package syntax

## To-do
### 7/8
1. try different regularization parameter (lambda) 
2. try adding more ordered quadruples (closer to full order)
3. try doing comparing the gram matrix (K and K_) directly instead of the decomposed positions (X and X_)
4. try problem with different data  
  i) more interesting generated data (s fold, swiss roll, etc)  
  ii) simple real world data
  
## Setup
Get a copy of this repository  
`git clone https://github.com/0taylor1/NMDS <folder_name>`  
`cd <folder_name>`  
Create a new branch  
`git checkout -b <your_branch_name>`  

To commit your work (on the new branch)  
`git checkout <your_branch_name>`  
`git add <file_to_contribute>`  
`git commit -am "<describe_change>"`  
push  
`git push origin <your_branch_name>`

To merge  
`git checkout master`  
`git merge <your_branch_name>`  
(solve conflicts, push changes)    
`git push origin master`  

To pull  
(go to a safe branch to pull on)  
`git pull origin <branch_to_pull>`  
