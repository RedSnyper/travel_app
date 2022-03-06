# Travel App RESTAPI for Elective

Steps before running the app:

### 1. Clone the project  

project structure:
- travel_app (root)
    - alembic
    - travel_app
        - *packages and modules*
        - main.py
    - requirements.txt

### 2. Create and activate virtual environment on root directory terminal:

    python -m venv env
    env\Scripts\activate

### 3. Install required packages:  
    In  root terminal, after activating venv type:
        pip install -r requirements.txt

### 4. Create a .env file.  

The .env file should contain:

- DATABASE_HOSTNAME = 
- DATABASE_PORT = 
- DATABASE_PASSWORD = 
- DATABASE_NAME = 
- DATABASE_USERNAME = 
- SECRET_KEY = *alphanumeric charaters*
- ALGORITHM = *jwt token algorithm (e.g. HS256)*
- ACCESS_TOKEN_EXPIRE_MINUTES = *time in minutes*  

### 5. Edit the db.py **SQLALCHEMY_DATABASE_URL** 

    f{"postgresql://"} to the database driver of your choice. Rest remains unchanged

### 6. Run the app:

- cd into the root project folder
- on terminal type  
    ### **uvicorn: travel_app.main:app**  

    (if for development purpose:)
    
    ### **uvicorn travel_app.main:app --reload**
