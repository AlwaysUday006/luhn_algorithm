# 🔢 Luhn Algorithm – Credit/Debit Card Validator

This project implements the **Luhn Algorithm** in Python to verify whether a given credit or debit card number is valid.  
The Luhn algorithm is widely used by payment systems (like Visa, MasterCard, Amex) for simple checksum validation of card numbers.

---

## 📖 How the Luhn Algorithm Works
1. Starting from the **rightmost digit**, double every second digit (the even-positioned ones in reversed order).
2. If doubling produces a two-digit number (e.g., 12), add those digits together (1 + 2 = 3).
3. Add the sum of all doubled values with the sum of the remaining digits.
4. If the total sum is divisible by 10, the card number is **VALID**. Otherwise, it is **INVALID**.

---

## 🚀 Features
- Validates card numbers using the Luhn Algorithm.
- Handles card numbers with **spaces** or **dashes**.
- Prints `VALID!` or `INVALID!` accordingly.
- Easy-to-understand implementation with step-by-step logic.

---

## 📂 Project Structure
