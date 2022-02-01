# Stonks-App

Welcome to the Stonks Financial Solutions App. This project utilizes a Django Framework to manage and handle the basic financial requests for accountants and their managers.

Link to Site: [Stonks Financial Solutions - Project Link](http://stonks-env.eba-p7p3wuag.us-west-2.elasticbeanstalk.com/)

## Project Tracking

### Tasks to complete:

#### Contributors: Jillian Puplampu (JP), Jeremiah Roby (JR), Samir Spraggins (SS), Jalen Springer (JS), Lillivia Taylor (LT), & Raeven Whitfield (RW)

   **Sprint 1 Task List**

   - [x] Email professor about the syllabus and structure of the course. Also ask about email server. - JS
   - [x] Create Initial Project and Publish to Github - JS
   - [x] Place the initial project unto AWS - JS
   - [ ] Create the Database for the project in AWS - JS
   - [ ] Need to figure out how to map DB file to docker container - JS
   - [ ] Create an ER Diagram for Database Design - SS
   - [ ] Finish high fidelity design for the login - RW
   - [ ] Create an App logo - RW
   - [ ] Sprint 1 - Task #1 - #5 (Backend) - JR
   - [ ] Sprint 1 - Task #6 - #8 (Backend) - JP
   - [ ] Sprint 1 - Task #9 - #15 (Backend) - Team
   - [ ] Sprint 1 - Task #16 - #20 (Backend) - JS
   - [ ] Sprint 1 - Task #1 - #5 (Frontend) - RW
   - [ ] Sprint 1 - Task #6 - #8 (Frontend) - LT
   - [ ] Sprint 1 - Task #9 - #15 (Frontend) - SS
   - [ ] Sprint 1 - Task #16 - #20 (Frontend) - Team


## Initial Project Setup

### Project Requirements: (Make sure items are stored to PATH)

  1. [Python Version 3.x](https://www.python.org/downloads/)
  2. Pip - [How to Install Pip](https://pip.pypa.io/en/stable/installation/)


### How to Configure a Python Virtual Environment

#### Install the virtualenv

  - Check if you have virtualenv

    `which virtualenv`

  - Also take note of the packages you already have installed with pip globally by using (This will help to know if your virtualenv has started):

    Windows:

    `pip freeze`

    Unix/Linux:

    `pip3 freeze`

  - If not, enter in the terminal the following to install it.

    Windows:

    `pip install virtualenv`

    Unix/Linux:

    `pip3 install virtualenv`

#### Install & Activate the virtualenv

  - Navigate to the directory for the project. To create a virtual environment in the current directory:

    `virtual env <my_env_name>`

  - Activate virtual env by navigating to the activation file:

    Windows:

    - Command Prompt: `<my_env_name>\Scripts\activate.bat`
    - Powershell:     `<my_env_name>\Scripts\Activate.ps1`

    POSIX:

    - bash/zsh:         `<my_env_name>/bin/activate`
    - fish:             `<my_env_name>/bin/activate.fish`
    - csh/tsch:         `<my_env_name>/bin/activate.csh`
    - Powershell Core:  `<my_env_name>/bin/Activate.ps1`

#### Deactivate virtualenv

  - You can simply deactive the **virtualenv** by either closing the terminal session or running the command  `deactivate`.


### How to Install Dependencies

  - There is a **requirements.txt** file incorporated within this project. After configuring your python virtual environment and activating it. Execute the command:

   `pip install -r requirements.txt --no-index`

### How to Run the Project
  - Execute the following command:

  `python manage.py runserver`

### How to Use Docker Containers

  - Make sure that you have Docker Desktop downloaded from [Docker](https://www.docker.com/get-started).
  - After installing docker on your system, you can execute the following command:

  `docker-compose build --no-cache` - This will pull the docker images and build the docker-compose.yml file in the repo

  - After the containers are built, you can execute the following command:

  `docker-compose up -d` - This will start up the containers that were built, and run them in a detached mode.

  - You will then need to browse over to on your system to [Adminer](http://localhost:8081).
  - After the browsing to the database view in your web browser you will need to enter the following credentials:

  System: MySQL
  Server: stonks-db
  Username: root
  Password: test1234
  Database: Stonks

  - You will now be able to use Adminer to view the contents of the database and make changes locally.

## Resources & Guides

- [Django Project & App Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
- [AWS Django Python Deployment Guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
- [AWS Python Database Configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/#links)

