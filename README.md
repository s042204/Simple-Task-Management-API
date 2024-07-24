# Simple Task Management API

This is a simple task management API built using Flask.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Create a virtual environment:
   ```sh
   python -m venv env
   ```
4. Activate the virtual environment:
   ```sh
   source env/bin/activate
   ```
   or for Windows:
   ```sh
   .\env\Scripts\activate
   ```
5. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```
6. Run the application:
   ```sh
   python run.py
   ```

## API Endpoints

- `GET /tasks` - Get all tasks
- `POST /tasks` - Create a new task
- `GET /tasks/<id>` - Get a task by ID
- `PUT /tasks/<id>` - Update a task by ID
- `DELETE /tasks/<id>` - Delete a task by ID

## Important Notes

- Ensure the virtual environment is activated before running the app.
- All configurations are set in `config.py` and can be overridden by `instance/config.py`.
