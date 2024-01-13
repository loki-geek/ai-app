# AI App Project
_AI App is a recommendation system which gives suitable answer according to user inputs_

## Requirements
Make sure you have python installed on your system:
- [Python version 3.9.13](https://www.python.org/downloads/release/python-3913/) 

## Project Setup

- Clone the repository in a local folder
    ```sh
    git clone https://github.com/loki-geek/ai-app.git
    ```
- Open terminal and verify python version
  ```sh
    python --version
    ```
- Verify if pip is installed
  ```sh
    pip --version
    ```
## Setup Backend
- Nvaigate to cloned project directory
  ```sh
    cd chatbot_app
    ```
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
