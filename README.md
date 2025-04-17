# NPCI MLOps Assignment-11
## CI/CD Pipeline using GitLab-CI for Customer Churn Prediction

### Problem Statement
In this assignment, you will build a complete CI/CD pipeline for a machine learning model that predicts customer churn using the customer-dataset with customer demographics and activity history. It includes data preprocessing, model training, running test cases, dockerizing application, and deployment. For this project you need to setup a CI/CD workflow using GitLab-CI.

### Objective
To implement a automated workflow in GitLab-CI with the following jobs:
- model training
- testing
- build and push docker image
- deploy


### Project Structure

   ```
   root
   ├── SubmissionImages/
   ├── dataset/
   |   └── churn_modeling.csv
   ├── requirements/
   |   ├── requirements.txt
   |   ├── test_requirements.txt
   |   └── api_requirements.txt
   ├── tests/
   |   └── test_prediction.py
   ├── trained_model/
   |   ├── __init__.py
   |   └── .gitignore
   ├── data_preprocessing.py
   ├── train_model.py
   ├── predict.py
   ├── app.py
   ├── Dockerfile
   ├── .gitignore
   └── README.md
   ```


### Starter Code Files
Starter code files for below functionalities have been provided:
1. Data Preprocessing (data_preprocessing.py)
2. Model Training (train_model.py)
3. Prediction (predict.py)
4. Testing (tests/test_prediction.py)
5. Dockerize application (Dockerfile)


### Steps to Follow for Setting up GitLab CI/CD Pipeline

1. Create a blank GitLab Project.
2. Add a Self-hosted Runner (Configure a GitHub Codespace as a runner).
3. Add your DockerHub credentials as GitLab variables.
4. Clone this GitLab project on to your system and add the files given in this assignment repo.
5. Create a `.gitlab-ci.yml` file (at the root location) and **add your CI/CD jobs to it**.
6. Push the project files and the `.gitlab-ci.yml` file to GitLab server.
7. Once pushed the pipline will be started, check it by visualizing pipeline.
8. Debug if any issue persist while running the pipeline jobs.


### Requirements:

1. **Train job:**
   - Install training requirements
   - Loads the dataset & preprocess it
   - Train a ML model and save it

2. **Test job:**
   - Install testing requirements
   - Run test cases

3. **Push Docker Image job:**
   - Do docker login
   - Create a docker image
   - Push the docker image on DockerHub
   - Visit your DockerHub account → verify if the image is uploaded

5. **Deploy job:**
   - Pull the latest image
   - Delete the old container if its running
   - Start a new container using the latest updated iamge
   - Check the runner if the application is running


### Submission Requirements:
Implement the required CI/CD pipeline on GitLab.

Add the required execution screenshots in the `SubmissionImages` folder, such as screenshots showing the successfull pipeline axecution, docker image pushed on DockerHub, application running in browser, etc.

After completing the assignment and developing the solution code on your GitLab project, commit and push the `.gitlab-ci.yml` file & screenshots to this repository as well. 
  - Stage your changes and commit the files:
    ```
    git add .
    git commit -m "GitLab-CI workflow file added"
    ```
  - Push your changes to the GitHub repository:
    ```
    git push
    ```

### Grading Criteria:
- To implement below pipeline jobs correctly
  - Train job [2 Mark]
  - Test job [2 Marks]
  - Push docker image job [3 Mark]
  - Deploy job [3 Marks]


Good luck, and happy coding!
