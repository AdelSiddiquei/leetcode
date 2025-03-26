# Leetcode
This repo contains a collection of leetcode problems that I have solved. 
All solutions live inside the leetcode_solutions folder, which is structured as a package, with the associated tests in the tests folder.  
  
Each question and the relevant solution is written within it's own file, named appropriately. Each file contains a class containing all implemented solutions as methods of the class. Some classes have multiple solutions, and are regularly updateed as and when I discover new algorithms to make more efficient solutions.

Each of these solution classes will have a  
`self.solution_count` attribute where I will be keeping track of the number of solutions I have coded for that problem.

## File structure
The solved problems will go in the solved_problems directory, with naming convention as follows:
    - The letter q followed by the question number for the problem from leetcode.com/studyplan/top-interview-150/
    - This will be followed by the name of the problem from the same source.
For example, "q121_best_time_to_buy_and_sell_stock.py".

Corresponding testing for each script will go into the .tests/ folder, where each test will follow the the simple naming convention of "test_" followed by the corresponding question number.
For example, "test_q121.py"

## Usage
I will be adding instructions for using this repo with Conda, Venv and Docker once they are implemented. Currently only implemented Conda environment, instrctions to come.
The first step is to clone this repo, and then use the appropriate method to install the package. Instructions using Conda, Venv and Docker are below:

### Conda
Run  
```bash
conda env create -f environment.yaml  
conda activate leetcode_env  
```
This will create the environment and activate it. Now run  
```bash
pip install .
```
to install the package to your environment.

### Docker
To run the solutions in an isolated container:

1. Build the Docker image:
```bash
docker build -t leetcode_img .
```
2. To start an interactive container session:
```bash
docker run --rm -it --name leetcode_cntnr leetcode_img
```
OR
To create a detached container:
```bash
docker run --rm -d --name leetcode_cntnr leetcode_img
```
Which can be entered by running:
```bash
docker exec -it leetcode_cntnr bash
```
Note that the use of `--rm` flags in the `docker run` commands. This is to set up auto-deletion for the container when it is stopped.
3. Once inside the container activate the envrionment:
```bash
conda activate leetcode_env
```

### Venv
1. Create a Venv:
```bash
python3 -m venv venv  
```
2. Activate venv:
```bash
source venv/bin/activate  
```
3. Install dependancies:
```bash
pip install -r requirements.txt  
```
4.  To install the package to your environment.
```bash
pip install .  
```


## Installation

## Testing
Once package has been downloaded, and environment activated one can use the:
```bash
pytest
```
command in cli to run the tests in `./tests`