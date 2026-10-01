# User Validator

A username and password validation tool with:
- **Python CLI**
- **Interactive web frontend**
- **Flask backend** that stores users in SQLite (passwords are hashed)

## Rules

### Username
- At least 8 characters long
- Must not contain spaces
- Must not contain digits

### Password
- At least 7 characters long
- Must contain at least one digit
- Must contain at least one uppercase letter
- Special characters are allowed (but not required)
- Must match the confirmation password (on register)

## Quick Start (Backend + Frontend)

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the server

```bash
python app.py
```

### 3. Open in browser

Go to: **http://127.0.0.1:5000**

You can:
- **Register** a new user (validated + stored in SQLite)
- **Login** with an existing user
- See the list of registered usernames

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/register` | Register a new user |
| POST | `/api/login` | Login with username + password |
| GET | `/api/users` | List registered usernames |

### Example register request

```json
{
  "username": "johndoe",
  "password": "Secret1",
  "confirm": "Secret1"
}
```

## Project Structure

```
User--Validator/
├── app.py                  # Flask backend + SQLite
├── index.html              # Interactive frontend
├── username_password.py    # Original CLI version
├── requirements.txt
├── users.db                # Created automatically on first run
└── README.md
```

## Notes

- Passwords are stored using **Werkzeug** password hashing (not plain text).
- The database file `users.db` is created automatically when you first run `app.py`.
- This is a learning/demo project — not production-ready security.
