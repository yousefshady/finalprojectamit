# E-commerce website template
This is an e-commerce website template made with Django & React.js

This template includes functions like:

User side:
1. Cart
2. Wishlist
3. Orders
4. Register
5. Login
6. Forgot password
7. Update user
8. View user profile

Admin side:
1. View and manage users
2. View and manage orders
3. Add, edit, and delete products

## How to setup database
1. Open a terminal like Bash or CMD
    1. Activate the virtual enviroment, to activate the virtual enviroment type this in your terminal
        1. If you don't have one just type
            ```cmd
            python -m venv env
            ```

        2. For bash:
            ```bash
            source env/scripts/activate
            ```
        3. For CMD & PowerShell:
            ```cmd
            env/scripts/activate
            ```
            If CMD and PowerShell won't work try typing this command first
            ```cmd
            Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process -Force
            ```
            Then type this to go to the project folder
            ```cmd
            cd ecommerce
            ```
    2. Downloading the requirements:

        To download the required files type this command into the terminal
        ```cmd
        pip install ../requirements.txt
        ```
    3. Setting up the database:

        To setup the database type in these 2 commands
        ```cmd
        py manage.py makemigrations
        ```
        ```cmd
        py manage.py migrate
        ```
    4. Running the server:

        To run the server type this command
        ```cmd
        py manage.py runserver
        ```
        To stop the server just enter the terminal and click Ctrl + C on Windows or Cmd + C on Mac
    5. Using the admin panel:
        
        To open the admin panel go to localhost:8000/admin or your website domain /admin and login to access the admin panel
        
        If you don't have a superuser account just use this command
        ```cmd
        py manage.py createsuperuser
        ```

    6. Setting up the email system:

        1. Go to settings.py located in the ecommerce folder and scroll to the bottom
        2. Fill in the required details
        3. To enter the password go to the .env file in the same folder as the settings.py file and enter your password in the EMAILPASSWORD variable
            1. Note: If you're using Gmail SMTP you can't use your account password you have to create an app password, to do that go to [your account](https://myaccount.google.com/) and turn on 2 step verification, then go to [app passwords](https://myaccount.google.com/apppasswords) and set the select app field as other and enter a name for the app and click generate, then take the 16 digit code and put it in the .env file in the EMAILPASSWORD variable
        4. Now go to views.py file in the orders folder and change the Company name here in `company_name='Company name here'` to your company/website name in the views: checkout, cancelorder, and uncancelorder

## How to customize the CSS of the page
Go to `reactapp/build/static/css/style.css` and edit what you want there and even add more styling if you want

If you want to edit the page title go to `reactapp/build/base.html` and edit the text after the title block which is this `{% block title %}{% endblock title %}`
***
## That's the end of the README. Thank you for choosing this template!
