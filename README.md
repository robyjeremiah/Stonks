# Stonks-App

Welcome to the Stonks Financial Solutions App. This project utilizes a Django Framework to manage and handle the basic financial requests for accountants and their managers.

Link to Site: [Stonks Financial Solutions - Project Link](http://stonks-env.eba-p7p3wuag.us-west-2.elasticbeanstalk.com/)
Link to Sprint #1: [Sprint List](https://kennesawedu.sharepoint.com/:w:/r/sites/Team-Group6SWE-4713AppDomain/_layouts/15/doc2.aspx?sourcedoc=%7B2811871A-3662-47A8-8703-3DB4D9BFF3A7%7D&file=SWE4713%20-%20Application%20Domain%20-%20Sprint%201%20-%20Feature%20for%20User%20Interface%20Module.docx&action=default&mobileredirect=true&DefaultItemOpen=1&ct=1643793612811&wdOrigin=OFFICECOM-WEB.MAIN.OTHER&cid=74f90ef7-ed49-4ef0-b2a7-c1d3885e0556)

## Project Tracking

### Tasks to complete:

#### Contributors: Jillian Puplampu (JP), Jeremiah Roby (JR), Samir Spraggins (SS), Jalen Springer (JS), Lillivia Taylor (LT), & Raeven Whitfield (RW)

   **Sprint 1 Task List**

   - [x] Email professor about the syllabus and structure of the course. Also ask about email server. - JS
   - [x] Create Initial Project and Publish to Github - JS
   - [x] Place the initial project unto AWS - JS
   - [x] Create the Database for the project in AWS - JS
   - [x] Need to figure out how to map DB file to docker container - JS
   - [x] Create an ER Diagram for Database Design - SS
   - [ ] Finish high fidelity design for the login - RW
   - [ ] Create an App logo - RW
   - [ ] Sprint 1 - Task #1 - #5 (Backend) - JR
   - [ ] Sprint 1 - Task #6 - #8 (Backend) - JP
   - [ ] Sprint 1 - Task #9 - #15 (Backend) - Team
   - [ ] Sprint 1 - Task #16 - #20 (Backend) - JS
   - [ ] Sprint 1 - Task #1 - #5 (Frontend) - RW
   - [x] Sprint 1 - Task #6 - #8 (Frontend) - LT
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

### How to Use Docker Containers (Windows Only) --> Working on MacOS soon

  #### Setting Up Environment Variables for Docker
  - In the directory, you should see a .env.example file. Open that file, and change the following:
    
    MY_USER='your-username'
    MY_PASSWORD='password_of_your_choice'
  
  - The remaining items can remain the same. After saving the file, rename the file to be '.env' instead of '.env.example'
  - You have successfully created your environment variables!
  #### Running Docker
  - Make sure that you have Docker Desktop downloaded from [Docker](https://www.docker.com/get-started).
  - After installing docker on your system, you can execute the following command:

  `docker-compose build --no-cache` - This will pull the docker images and build the docker-compose.yml file in the repo

  - After the containers are built, you can execute the following command:

  `docker-compose up -d` - This will start up the containers that were built, and run them in a detached mode.
  
  - After the containers are running, you can browse to view the project at [Stonks-App](http://localhost:9000)
  - The last thing left to do is connect to the database!
  #### Installing MySQL Workbench (Temporary until I can configure the web version)

  - Trying to still configure the database connection through the browser, however, temporarily install [MySQL Workbench](https://dev.mysql.com/downloads/workbench/). We will use it to connect to the database.
  - After the installation is completed, add a new connection. Enter the information as follows:

    Connection Name: 'Whatever Name You Would Like, I Went With Stonks'
    Port: 3307
    Username: 'The Username You Created in .env'
    Password: 'The Password You Created in .env'
  
  - Make sure to test your connection at the bottom. If successful, you can close out the window and connect. You should see all the tables for the database!

  #### Using Docker to Run the environment

  - To get the latest migrations for the project run the following command in your terminal:
    `docker-compose run web python manage.py migrate`
## Resources & Guides

- [Django Project & App Tutorial](https://docs.djangoproject.com/en/4.0/intro/tutorial01/)
- [AWS Django Python Deployment Guide](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-django.html)
- [AWS Python Database Configuration](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-rds.html)
- [Markdown Guide](https://www.markdownguide.org/basic-syntax/#links)

