# Leetcode
This repo contains all the leetcode problems I have solved.  
Each problem I solve will have a `Class` containing the solutions as methods, which I will be updating with new solutions as I learn new/different ways to tackle them. Each of these solution classes will have a  
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
The Dockerfile has been set up such that a user is expected to enter a container interactively and explore my solutions/tests in terminal.   
First run:
```bash
docker build -t leetcode_img .
```
To build the image, then run:
```bash
docker run --rm -d --name leetcode_cntnr leetcode_img
```
To open a detached container named leetcode_cntnr. You can then enter this container interactively using:
```bash
docker exec -it leetcode_cntnr bash
```
Alternatively, you run the container interactively after creating the image. To do this, after creating the image run:
```bash
docker run --rm -it --name leetcode_cntnr leetcode_img
```
This will mean that the container will stop as soon as you exit it from the terminal rather than running in the background.
Note that I have included `--rm` flags in the `docker run` commands. This is to set up auto-deletion for the container when it is stopped.
Also Note that once inside the container you will have to run `conda activate leetcode_env` to activate the environment.

### Venv
Run: 
```bash
python3 -m venv venv  
source venv/bin/activate  
```
To create and activate a Venv called venv, now run  
```bash
pip install -r requirements.txt  
```
to install dependancies. Now run  
```bash
pip install .  
```
To install the package to your environment.

## Installation

## Testing
Once package has been downloaded, one can use the:
```bash
pytest
```
command in cli to run the tests in ./tests