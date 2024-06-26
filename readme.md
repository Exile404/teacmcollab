Certainly! Here's the full content in a Markdown file:

markdown
# Project Management API Documentation

## Project Setup Instructions

### Prerequisites:
- Python 3.8+
- Django 3.2+
- Django REST Framework
- SQLite3 (or any preferred database)
- pip (Python package installer)

### Steps to set up the project locally:

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Exile404/teamcollab.git
   cd teamcollab
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run Migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser:**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the Admin Panel:**
   - Go to `http://127.0.0.1:8000/admin`
   - Log in with your superuser credentials.

8. **Access the Swagger UI:**
   - Go to `http://127.0.0.1:8000/swagger/` to view the API documentation.

**Additional Notes:**
- Ensure you have set up the `ALLOWED_HOSTS` in `settings.py` if you're deploying to a server.
- It's good practice to use environment variables for sensitive settings like `SECRET_KEY`, `DATABASES`, etc.

## API Documentation

**API Endpoints:**

### Users:
1. **Register User**
   - **Endpoint:** `POST /api/users/register/`
   - **Description:** Create a new user.
   - **Request Body:**
     ```json
     {
       "username": "string",
       "email": "string",
       "password": "string",
       "first_name": "string",
       "last_name": "string"
     }
     ```
   - **Response:**
     ```json
     {
       "id": "integer",
       "username": "string",
       "email": "string",
       "first_name": "string",
       "last_name": "string",
       "date_joined": "datetime"
     }
     ```

2. **Login User**
   - **Endpoint:** `POST /api/users/login/`
   - **Description:** Authenticate a user and return a token.
   - **Request Body:**
     ```json
     {
       "username": "string",
       "password": "string"
     }
     ```
   - **Response:**
     ```json
     {
       "refresh": "string",
       "access": "string"
     }
     ```

3. **Get User Details**
   - **Endpoint:** `GET /api/users/{id}/`
   - **Description:** Retrieve details of a specific user.
   - **Response:**
     ```json
     {
       "id": "integer",
       "username": "string",
       "email": "string",
       "first_name": "string",
       "last_name": "string",
       "date_joined": "datetime"
     }
     ```

4. **Update User**
   - **Endpoint:** `PUT/PATCH /api/users/{id}/`
   - **Description:** Update user details.
   - **Request Body:**
     ```json
     {
       "username": "string",
       "email": "string",
       "first_name": "string",
       "last_name": "string"
     }
     ```
   - **Response:** Same as Get User Details.

5. **Delete User**
   - **Endpoint:** `DELETE /api/users/{id}/`
   - **Description:** Delete a user account.
   - **Response:** HTTP 204 No Content

### Projects:
1. **List Projects**
   - **Endpoint:** `GET /api/projects/`
   - **Description:** Retrieve a list of all projects.
   - **Response:**
     ```json
     [
       {
         "id": "integer",
         "name": "string",
         "description": "string",
         "owner": "integer",
         "created_at": "datetime"
       }
     ]
     ```

2. **Create Project**
   - **Endpoint:** `POST /api/projects/`
   - **Description:** Create a new project.
   - **Request Body:**
     ```json
     {
       "name": "string",
       "description": "string",
       "owner": "integer"
     }
     ```
   - **Response:** Same as List Projects.

3. **Retrieve Project**
   - **Endpoint:** `GET /api/projects/{id}/`
   - **Description:** Retrieve details of a specific project.
   - **Response:** Same as List Projects.

4. **Update Project**
   - **Endpoint:** `PUT/PATCH /api/projects/{id}/`
   - **Description:** Update project details.
   - **Request Body:** Same as Create Project.
   - **Response:** Same as List Projects.

5. **Delete Project**
   - **Endpoint:** `DELETE /api/projects/{id}/`
   - **Description:** Delete a project.
   - **Response:** HTTP 204 No Content

### Tasks:
1. **List Tasks**
   - **Endpoint:** `GET /api/projects/{project_id}/tasks/`
   - **Description:** Retrieve a list of all tasks in a project.
   - **Response:**
     ```json
     [
       {
         "id": "integer",
         "title": "string",
         "description": "string",
         "status": "string",
         "priority": "string",
         "assigned_to": "integer",
         "project": "integer",
         "created_at": "datetime",
         "due_date": "datetime"
       }
     ]
     ```

2. **Create Task**
   - **Endpoint:** `POST /api/projects/{project_id}/tasks/`
   - **Description:** Create a new task in a project.
   - **Request Body:**
     ```json
     {
       "title": "string",
       "description": "string",
       "status": "string",
       "priority": "string",
       "assigned_to": "integer",
       "due_date": "datetime"
     }
     ```
   - **Response:** Same as List Tasks.

3. **Retrieve Task**
   - **Endpoint:** `GET /api/tasks/{id}/`
   - **Description:** Retrieve details of a specific task.
   - **Response:** Same as List Tasks.

4. **Update Task**
   - **Endpoint:** `PUT/PATCH /api/tasks/{id}/`
   - **Description:** Update task details.
   - **Request Body:** Same as Create Task.
   - **Response:** Same as List Tasks.

5. **Delete Task**
   - **Endpoint:** `DELETE /api/tasks/{id}/`
   - **Description:** Delete a task.
   - **Response:** HTTP 204 No Content

### Comments:
1. **List Comments**
   - **Endpoint:** `GET /api/tasks/{task_id}/comments/`
   - **Description:** Retrieve a list of all comments on a task.
   - **Response:**
     ```json
     [
       {
         "id": "integer",
         "content": "string",
         "user": "integer",
         "task": "integer",
         "created_at": "datetime"
       }
     ]
     ```

2. **Create Comment**
   - **Endpoint:** `POST /api/tasks/{task_id}/comments/`
   - **Description:** Create a new comment on a task.
   - **Request Body:**
     ```json
     {
       "content": "string",
       "user": "integer"
     }
     ```
   - **Response:** Same as List Comments.

3. **Retrieve Comment**
   - **Endpoint:** `GET /api/comments/{id}/`
   - **Description:** Retrieve details of a specific comment.
   - **Response:** Same as List Comments.

4. **Update Comment**
   - **Endpoint:** `PUT/PATCH /api/comments/{id}/`
   - **Description:** Update comment details.
   - **Request Body:** Same as Create Comment.
   - **Response:** Same as List Comments.

5. **Delete Comment**
   - **Endpoint:** `DELETE /api/comments/{id}/`
   - **Description:** Delete a comment.
   - **Response:** HTTP 204 No Content

## If you are using postman for api testing, after login place the access part in headers like this: Key: Authorization; value: access token
