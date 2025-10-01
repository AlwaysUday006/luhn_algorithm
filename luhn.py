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
        # Example: 12 → 1 + 2 = 3
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number

    # Total sum of odd and even positioned digits
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)  # Debugging: shows the computed sum

    # Valid card if total is divisible by 10
    return total % 10 == 0


def main():
    # Example card number (contains dashes like a real card)
    card_number = '4111-1111-4555-1141'

    # Remove dashes and spaces for clean processing
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    # Validate using Luhn Algorithm
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')


# Run the program
main()
