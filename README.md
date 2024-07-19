# Hackaton-Finkargo

ERD (Entity-Relationship Diagram) for the PostgreSQL database. We'll include the following tables:
users - To store user information.
support_cases - To store the details of each support case.
ERD
Users Table
user_id (Primary Key)
username
email
password_hash
created_at
updated_at
Support Cases Table
case_id (Primary Key)
title
description
status
created_at
updated_at
user_id (Foreign Key referencing users)


Base de datos: 
DATABASE_URL = "postgresql://support_user:yourpassword@localhost/support_case_db"

URLS front: 
http://localhost:3000/track-case
http://localhost:3000/create-case

URL back: 
http://localhost:8000/



