# AI App Project
_AI App is a recommendation system which gives suitable answer according to user inputs_

## Requirements
Make sure you have python installed on your system:
- [Python version 3.9.13](https://www.python.org/downloads/release/python-3913/) 

## Project Setup

- Update the dependencies
    ```sh
    #For Amazon Linux 2023
    sudo yum update && sudo yum upgrade
    #For Ubuntu, use 'apt' instead of 'yum'.
    ```
- Install Python and pip
  ```sh
    sudo yum install python
    python --version
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    pip --version
    ```
- Create a new directory and Clone the repository in a local folder
    ```sh
    mkdir ai-app
    cd ai-app
    git clone https://github.com/loki-geek/ai-app.git
    ```
    
## Setup Backend

- Create a python virtual environment for backend
  ```sh
    python3 -m venv chatenv
    ```
- Activate the virtual environment
  ```sh
  # For winodws
    chatenv\Scripts\activate
  # For linux
    source chatenv/bin/activate
    ```
- Install python libraries
  ```sh
   cd chatbot_app
   pip install -r requirements.txt
    ```
- Start Django server
  ```sh
   python manage.py runserver
    ```
- Django backend server will start on http://localhost:8000/
  
- Stop the server by pressing CTRL+C
  
- Deactivate the venv
  ```sh
   deactivate
    ```
