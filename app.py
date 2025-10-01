import streamlit as st

# Function to verify card number using the Luhn Algorithm
def verify_card_number(card_number):
    sum_of_odd_digits = 0
    # Reverse the card number for easier position handling
    card_number_reversed = card_number[::-1]

    # Take all digits in odd positions (0, 2, 4...) from the reversed number
    odd_digits = card_number_reversed[::2]

    # Add odd-position digits directly
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    sum_of_even_digits = 0
    # Take all digits in even positions (1, 3, 5...) from the reversed number
    even_digits = card_number_reversed[1::2]

    # For each even-position digit → double it
    for digit in even_digits:
        number = int(digit) * 2
        # If doubling makes it 2 digits (e.g., 12), add those digits together
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Total sum of odd and even positioned digits
    total = sum_of_odd_digits + sum_of_even_digits

    # Valid card if total is divisible by 10
    return total % 10 == 0


# Streamlit UI
def main():
    st.title("💳 Credit/Debit Card Validator (Luhn Algorithm)")

    st.write("Enter your card number below to check if it's valid:")

    # Input box for card number
    card_number = st.text_input("Card Number (with or without spaces/dashes)", "")

    if st.button("Validate"):
        if card_number.strip() == "":
            st.warning("⚠️ Please enter a card number.")
        else:
            # Clean the card number (remove dashes and spaces)
            card_translation = str.maketrans({'-': '', ' ': ''})
            translated_card_number = card_number.translate(card_translation)

            if not translated_card_number.isdigit():
                st.error("❌ Invalid input! Please enter only digits, spaces, or dashes.")
            else:
                # Validate card number
                if verify_card_number(translated_card_number):
                    st.success("✅ VALID Card Number!")
                else:
                    st.error("❌ INVALID Card Number!")


if __name__ == "__main__":
    main()
