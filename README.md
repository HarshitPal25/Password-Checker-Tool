# Password-Checker-Tool
It checks the user password and encorage them to Enter Password again until the passwor is Strong.

---

This is a simple Python program that checks the **strength of a password** based on several criteria, including the use of uppercase and lowercase letters, digits, special characters, and the length of the password.

---

##  Features

- Checks for:
  - ✅ Uppercase and lowercase letters
  - ✅ Digits (0–9)
  - ✅ Special characters (e.g., `!@#$%^&*`)
  - ✅ Password length
- Categorizes passwords as:
  - 🔴 Very Weak
  - 🟠 Weak
  - 🟡 Medium
  - 🟢 Strong
- Encourages user to re-enter a stronger password until it's secure enough.
- Simple, interactive command-line interface.

---

##  How It Works

The program evaluates the password based on 4 criteria:

1. Contains lowercase letters
2. Contains uppercase letters
3. Contains digits
4. Contains special characters

The total score (0–4) is combined with the password length to determine strength:

| Score | Length        | Strength     |
|-------|---------------|--------------|
| 4     | ≥ 12 chars    | Strong       |
| ≥ 3   | ≥ 8 chars     | Medium       |
| ≥ 2   | ≥ 6 chars     | Weak         |
| < 2   | < 6 chars     | Very Weak    |

---

##  Usage

1. Make sure you have **Python 3** installed.
2. Clone this repository or download the script.
3. Run the program using the terminal:

```bash
python password_checker.py
```
## Example
```
Enter your password: Hello123
Password strength: Medium
Enter a stronger password please.

Enter your password: Hello@123Secure
Password strength: Strong
```
