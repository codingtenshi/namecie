## General Information and Features:

This web application allows users to create sports groups such as running and nordic walking. 
The application was built using the Django framework. 
As a user, you have the following capabilities:

- Registration
- Creating or joining a sports group
- Sending invitations to friends to join the group
- Tracking your own sports events as well as the group's sports events
- Adding sports events you wish to participate in
- Generating a public page for the sports group.

## Table of Contens:

<!-- toc -->

- [Project is created with:](#project-is-created-with)
- [Installation process:](#installation-process)
- [Additional information](#additional-information)

<!-- tocstop -->

## Project is created with:
- Python version 3.11.4
- Django version 4.2.3
- Django-tailwind version 3.6.0
- HTML version 5



## Project installation:

1. Clone the repository to your local computer:
    ```
    $ git clone https://github.com/codingtenshi/namecie
    ```
1. Enter the cloned repozytory:
    ```
    $ cd namecie/namecieProject
    ```
1. (Optional) Create and activate a virtual environment:
    ```
    For macOS:
    - python -m venv venv
    - source venv/bin/activate

    For Windows:
    - python -m venv venv
    - venv/Scripts/activate
    ```
1. Install dependencies:
    ```
    $ pip install -r requirements.txt
    ```
1. Install Tailwind:
    ```
    $ python manage.py tailwind install
    ```
1. Build CSS file to one:
    ```
    $ python manage.py tailwind build 
    ```
1. Run the application server:
    ```
    $ python manage.py migrate
    ```
1. Run the application server:
    ```
    $ python manage.py runserver
    ```

## Development:

> You need to have two active terminal sessions.

1. In first terminal session start application:
    ```bash
    export ORY_SDK_URL=http://localhost:4000/.ory
    export ORY_UI_URL=http://localhost:4000/.ory/ui
    export LOGIN_URL=http://localhost:4000/.ory/ui/login
    python manage.py runserver
    ```
1. In second terminal session start Ory proxy (you need to install Ory CLI to do it):
    ```bash
    # SDK address is what you get from Ory Console when you create a project
    export ORY_SDK_URL=https://angry-brattain-gtfy93w28k.projects.oryapis.com
    ory proxy http://localhost:8000
    ```
1. In browser open `http://localhost:4000/`

## Additional information:


While creating the project I learned how to:
- manage time,
- work with the Django framework,
- use Github