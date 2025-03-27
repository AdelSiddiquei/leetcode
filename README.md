# Leetcode
This repo contains a collection of leetcode problems that I have solved. 
All solutions live inside the [leetcode_solutions](./leetcode_solutions) folder, which is structured as a package, with the associated tests in the [tests](./tests) folder.  
  
Each question and the relevant solution is written within it's own file, named appropriately. Each file contains a class called `Solution` containing all implemented solutions as methods of the class. Some classes have multiple solutions, and are regularly updateed as and when I discover new algorithms to make more efficient solutions.

Each of these solution classes will have a  `self.solution_count` attribute where I will be keeping track of the number of solutions I have coded for that problem.

## File structure
The solved problems will go in the [leetcode_solutions](./leetcode_solutions) directory, with the file named as the question number from [Leetcode](https://leetcode.com/).
The corresponding test goes within the tests folder, named the same.

### Table of Solutions
| Question      | Solution      | Algorithms Used |
| ------------- | ------------- | -------------   | 
| [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)  | [q121.py](./leetcode_solutions/q121.py)  |                 |
| [27. Remove Element](https://leetcode.com/problems/remove-element)|  [q27.py](./leetcode_solutions/q27.py)  | |
| [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array)  |  [q88.py](./leetcode_solutions/q88.py)  | |
| Content cell| | |


## Usage
Below are instructions on how to run the solutions, and tests with different package managers: Conda, Python venv and Docker.

### Conda
1. Run the below command to create the environment and activate it.
     ```bash
     conda env create -f environment.yaml  
     conda activate leetcode_env  
     ```
2. Now install the `leetcode_solutions` package into the conda environment.
     ```bash
     pip install -e .
     ```

### Docker
1. Build the Docker image.
     ```bash
     docker build -t leetcode_img .
     ```
2. Run the Docker container.
     ```bash
     docker run --rm -d --name leetcode_cntnr leetcode_img
     ```
3. Enter the container. 
     ```bash
     docker exec -it leetcode_cntnr bash
     ```
4. Activate the conda env `leetcode_env`. You will now have a working terminal, inside the container.
     ```bash 
     conda activate leetcode_env
     ```

**Note:** `--rm` option in the `docker run` commands ensure that the container is deleted after it stops.

### Python `venv`
1. Create a Venv.
     ```bash
     python3 -m venv venv  
     ```
2. Activate venv.
     ```bash
     source venv/bin/activate  
     ```
3. Install dependancies.
     ```bash
     pip install -r requirements.txt  
     ```
4.  To install the package to your environment.
     ```bash
     pip install -e .  
     ```

## Testing
Once you are within a a working environment (see above), run the tests with `pytest`.
```bash
pytest
```