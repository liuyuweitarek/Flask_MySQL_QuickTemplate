# Flask_MySQL_QuickTemplate
This is a quick template which help you build up backend with Flask + MySQL and handle config and API functions clearly. 

## Installation

1. Clone the project

    ```bash
    $ git clone https://github.com/liuyuweitarek/Flask_MySQL_QuickTemplate.git
    $ cd Flask_MySQL_QuickTemplate
    ```

2. Build Project Python Environment

    Python Version > 3
    
    * Set up/Start up virtual env
      ```bash
      $ python3 -m venv env
      $ source env/bin/activate
      ```
    * Install Dependencies
      ```bash
      $ python -m pip install --upgrade pip
      $ pip install -r requirements.txt 
      ```

3. Set up MySQL Environment
     * [MySQL Installation Guideline:](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/) Follow the instructions based on your OS system. 
     * Create the database for this project
       ```bash
        $ mysql -u root -p
          (input password)
        $ mysql> CREATE DATABASE {DATABASENAME}_dev ;
        $ mysql> CREATE DATABASE {DATABASENAME}_prod ;
       ```
        
       If you are not root, you could ask your admin for creating databases and granting the privileges to you with adding the commands below.
       ```bash
        (In root account)
        $ mysql> GRANT ALL PRIVILEGES ON {DATABASENAME}_dev.* TO '{ACCOUNT}'@'%';
        $ mysql> GRANT ALL PRIVILEGES ON {DATABASENAME}_prod.* TO '{ACCOUNT}'@'%';
       ```
       P.S. If the error shows that it can't find the user, using the code down below to check your account identity
       ```bash
        $ SELECT User FROM mysql.user;
        
        # It shows like:
        +------------------+--------------+--------------+
        | user             | host         | password     |
        +------------------+--------------+--------------+
        | {ACCOUNT}        | localhost    | 37as%#8123fs |
        | Other_user       | %            | slclk2j393   |
        +------------------+--------------+--------------+
        1 rows in set (0.01 sec)
       ```
       Based on the columns, "user" and "host", on User table, you might need to change the commands to :
       ```bash
        (In root account)
        $ mysql> GRANT ALL PRIVILEGES ON {DATABASENAME}_dev.* TO '{ACCOUNT}'@'localhost';
        $ mysql> GRANT ALL PRIVILEGES ON {DATABASENAME}_prod.* TO '{ACCOUNT}'@'localhost';
       ```
 4. Modify cfg.py's config
    ```python
    class ProductionConfig:
      ...
      HOST = {YOUR IP ADDRESS}                                                              <= Edit              
      PORT = {PORT which is available on your machine}                                      <= Edit
      ...

      # SQL
      SQLALCHEMY_DATABASE_URI= "mysql://{ACCOUNT}:{PASSWORD}@127.0.0.1/{DATABASENAME}_prod" <= Edit
      ...

    class DevelopmentConfig:
      ...
      HOST = {YOUR IP ADDRESS}                                                              <= Edit
      PORT = {PORT which is available on your machine}                                      <= Edit
      ...

      # SQL
      SQLALCHEMY_DATABASE_URI= "mysql://{ACCOUNT}:{PASSWORD}@127.0.0.1/{DATABASE_NAME}_dev" <= Edit
      ...
    
    ```
 ## Usage
 1. Make sure that MySQL Service active correctly
    ```bash
    $ service mysql status
    ```
    <p align="center">
      <img src="https://github.com/liuyuweitarek/Flask_MySQL_QuickTemplate/blob/main/wiki/mysql_service_check.jpg">
    </p>
 2. Activate project python environment 
     ```bash
     $ cd ~/Flask_MySQL_QuickTemplate
     $ source env/bin/activate
     ```
 3. Run
    ```bash
     $ python run.py --config [dev, prod]
    ```
    
       


