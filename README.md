# Py Quiz Game

An interactive **Python basics quiz** with account registration, login, a welcome home screen, a timed challenge, and saved scores.

## Features

- **Create account / Sign in** with live username & password validation
- **Welcome home page** with how-to-play instructions
- **10 multiple-choice** Python questions
- **5-minute countdown timer** (auto-submits when time runs out)
- **Progress bar** and question step indicators
- **Results screen** with score percentage and per-question review
- **Passwords hashed** and stored in **SQLite**
- Scores saved per user in the database

## How to run

```bash
pip install -r requirements.txt
python3 app.py
```

Open in your browser:

**http://127.0.0.1:5000**

### Flow

1. **Create account** or **Sign in**
2. Land on the **Home** page (welcome + instructions)
3. Click **Start quiz**
4. Answer 10 questions within 5 minutes
5. View your score and correct answers

## Validation rules

| Field | Rules |
|-------|--------|
| **Username** | At least 8 characters, no spaces, no digits |
| **Password** | At least 7 characters, at least one digit, at least one uppercase letter |

## Project structure

```
py-quiz-game1/
├── app.py                  # Flask backend (auth, routes, quiz API)
├── index.html              # Create account / Sign in
├── home.html               # Welcome page + how to play
├── quiz.html               # Timed quiz + results
├── username_password.py    # Original CLI validator (optional)
├── requirements.txt        # flask, flask-cors
├── users.db                # Created automatically on first run
└── README.md
```

## Main routes

| Route | Description |
|-------|-------------|
| `GET /` | Sign in / register page |
| `POST /auth/register` | Create account → redirect to `/home` |
| `POST /auth/login` | Sign in → redirect to `/home` |
| `GET /home` | Welcome + instructions (login required) |
| `GET /quiz` | Quiz challenge (login required) |

## API overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/api/me` | Current logged-in user |
| `POST` | `/api/logout` | End session |
| `GET` | `/api/quiz/questions` | Quiz questions (no answers) |
| `POST` | `/api/quiz/submit` | Submit answers, save score |
| `GET` | `/api/quiz/my-scores` | Your past scores |

## Notes

- Use **http://127.0.0.1:5000** (served by Flask), not opening HTML files directly.
- `users.db` is created on first run; do not commit it if it contains real passwords.
- This is a learning/demo project — not production-hardened security.
