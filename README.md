## Scheduling process simulator

Made by:
Esteban Durango
Miguel Angel Alvarez
Saray Cubillos García

# README

## Project Overview

This project is a simulator process that emulates the performance of different scheduling algorithms on a list of randomized job parameters. The application compares the Shortest Job First (SJF), Multi-Level Queue (MLQ), and Round Robin (RR) algorithms based on metrics like response time, turnaround time, and wait time. It identifies the best algorithm for a group of jobs and generates a dataset with the job list and the best algorithm for each group.

## System Requirements

- Python 3.8 or higher
- Poetry package manager

## Installation Steps

1. **Install Poetry**

   Poetry is a dependency manager for Python projects. If you don't have Poetry installed, you can install it using the following command:

   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

   Alternatively, you can follow the installation instructions from the official [Poetry documentation](https://python-poetry.org/docs/#installation).

2. **Clone the Repository**

   Clone the project repository to your local machine:

   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
   ```

3. **Install Dependencies**

   Navigate to the project directory and install the required dependencies using Poetry:

   ```bash
   poetry install
   ```

4. **Activate the Poetry Shell**

   Enter the Poetry shell environment to ensure that all dependencies are correctly configured:

   ```bash
   poetry shell
   ```

## Running the Application

1. **Run the Main Script**

   Execute the main script to run the simulator process. This will generate a CSV file containing the dataset with the randomized job lists and the best scheduling algorithm for each list:

   ```bash
   python main.py
   ```

2. **Output**

   After running the script, you will get a CSV file named `dataset.csv` in the project directory. This file will contain the job parameters and the corresponding best scheduling algorithm based on the defined metrics.

## Example

To give you an idea of the output, here is an example of what the `dataset.csv` file might look like:

```
job_id,job_duration,best_algorithm
1,5,SJF
2,3,RR
3,8,MLQ
...
```

## Additional Information

- **Metrics Used for Comparison:**
  - **Response Time:** The time from submission of a request until the first response is produced.
  - **Turnaround Time:** The total time taken to execute a particular job.
  - **Wait Time:** The total time a job spends waiting in the queue before it gets executed.

- **Algorithms Implemented:**
  - **Shortest Job First (SJF)**
  - **Multi-Level Queue (MLQ)**
  - **Round Robin (RR)**

Feel free to explore and modify the project to fit your needs. If you encounter any issues or have any questions, please refer to the project's [issues page](https://github.com/your-username/your-repo-name/issues) on GitHub. 

Happy coding!
