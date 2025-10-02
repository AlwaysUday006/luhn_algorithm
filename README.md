# 🔢 Luhn Algorithm – Credit/Debit Card Validator

This project implements the **Luhn Algorithm** in Python to verify whether a given credit or debit card number is valid.  
The Luhn algorithm is widely used by payment systems (like Visa, MasterCard, Amex) for simple checksum validation of card numbers.  
It also demonstrates how the same project can be converted into a **simple interactive webpage using Streamlit**.

---

## 📖 About the Luhn Algorithm
The Luhn algorithm is a checksum formula used to validate identification numbers, mainly credit and debit card numbers.  

**Steps:**
1. Starting from the **rightmost digit**, double every second digit (even-positioned ones in reversed order).  
2. If doubling produces a two-digit number (e.g., 12), add those digits together (1 + 2 = 3).  
3. Add the sum of all doubled values with the sum of the remaining digits.  
4. If the total sum is divisible by 10, the card number is **VALID**. Otherwise, it is **INVALID**.  

---

## 🚀 Features
- Validates card numbers using the Luhn Algorithm.  
- Handles card numbers with **spaces** or **dashes**.  
- Prints `VALID!` or `INVALID!` accordingly.  
- Clean and beginner-friendly implementation with step-by-step logic.  
- **Interactive Streamlit app** for entering card numbers and checking validity online.  

---

## 🛠️ How It Works
1. Enter a credit/debit card number (with or without spaces/dashes).  
2. The algorithm processes digits according to the Luhn formula.  
3. Outputs **VALID** if it passes the checksum, else **INVALID**.  
4. Optional: Run the Streamlit app for an interactive webpage version.  

---

## 📂 Project Structure
- `luhn.py` – Core logic for validation.  
- `app.py` – Streamlit app for web-based interaction.  
- `README.md` – Project documentation and instructions.  

---

## 🎯 Steps Followed
1. Learned the logic of the Luhn Algorithm.  
2. Implemented validation logic in Python.  
3. Added input handling (ignoring spaces/dashes).  
4. Tested with sample card numbers.  
5. Built a Streamlit app for a simple online validator.  
6. Documented the project for easy understanding.  

---

## 💡 Outcome
This project demonstrates **practical cryptography and algorithmic validation** while reinforcing Python fundamentals.  
It also shows how a console program can be turned into a **user-friendly web application** with Streamlit.
