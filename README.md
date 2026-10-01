# User Validator + Python Quiz

Register or login with validated credentials, then take an interactive Python basics quiz.

## Features

- **Username & password validation** (same rules as before)
- **Register / Login** with hashed passwords (SQLite)
- **Python Quiz** — 10 multiple-choice questions
- **Scores saved** per user in the database
- Must be logged in to play the quiz

## Quick Start

```bash
pip install -r requirements.txt
python3 app.py
```

Open: **http://127.0.0.1:5000**

1. Register a new account (or login)
2. You’re taken to the quiz automatically
3. Answer the questions and submit
4. See your score

## Validation Rules

**Username:** 8+ characters, no spaces, no digits  
**Password:** 7+ characters, at least one digit, at least one uppercase letter

## Project Structure

```
User--Validator/
├── app.py                  # Flask backend (auth + quiz API)
├── index.html              # Register / Login page
├── quiz.html               # Interactive quiz
├── username_password.py    # Original CLI validator
├── requirements.txt
├── users.db                # Created on first run
└── README.md
```

## API (overview)

| Endpoint | Description |
|----------|-------------|
| POST `/api/register` | Register + start session |
| POST `/api/login` | Login + start session |
| POST `/api/logout` | End session |
| GET `/api/me` | Current user |
| GET `/api/quiz/questions` | Quiz questions (login required) |
| POST `/api/quiz/submit` | Submit answers, save score |
| GET `/api/quiz/my-scores` | Your past scores |
