# NMDS
Non-metric Multidimensional Scaling
![SURP2021 Poster](poster.pdf)

## To-do 7/21
* clean up code   
* more test problems  
* implement in matlab?   

## Files
* `data`
  - contains datafiles used for testing 
* `examples`
  - contains example code from references  
      + cvxpy tutorial  
      + sklearn  
      + ADMM example source code  
* `figures`  
  - contains relevant plots/figures. to be expanded
* `utils`
  - contains scripts used for generating data, etc.
* `Notes.ipynb`  
  - latex write-ups of governing mathematical expressions
  - small snippets of code for testing 
* `cvxpy.ipynb`  
  - code for solving problem using cvxpy. draft
  
## Setup
#### Get a copy of this repository  
`git clone https://github.com/0taylor1/NMDS <folder_name>`  
`cd <folder_name>`  
#### Create a new branch  
`git checkout -b <your_branch_name>`  

#### To commit your work (on the new branch)  
`git checkout <your_branch_name>`  
`git add <file_to_contribute>`  
`git commit -am "<describe_change>"`  
#### push  
`git push origin <your_branch_name>`

#### To merge  
`git checkout master`  
`git merge <your_branch_name>`  
(solve conflicts, push changes)    
`git push origin master`  

#### To pull  
(go to a safe branch to pull on)  
`git pull origin <branch_to_pull>`  
