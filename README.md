# User Validator

A simple username and password validation tool with both a **Python CLI** and an **interactive web frontend**.

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
- Must match the confirmation password

## How to Use

### 1. Interactive Frontend (Recommended)

Just open the `index.html` file in your browser:

```bash
# Option A – double-click the file
# Option B – from terminal
open index.html          # macOS
start index.html        # Windows
xdg-open index.html     # Linux
```

Or serve it locally:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

Features:
- Real-time validation as you type
- Visual rule checklist (✓ / ○)
- Show/hide password toggle
- Submit button only enables when everything is valid

### 2. Python CLI

```bash
python username_password.py
```

Follow the prompts in the terminal.

## Project Structure

```
User--Validator/
├── index.html              # Interactive web frontend
├── username_password.py    # Python CLI version
└── README.md
```

## License

Free to use and modify.
