def analyze_string(s):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    vowels_count = 0
    consonants_count = 0
    digits_count = 0
    special_char_count = 0
    
    for char in s:
        if char in vowels:
            vowels_count += 1
        elif char in digits:
            digits_count += 1
        elif char.isalpha():
            consonants_count += 1
        else:
            special_char_count += 1
    
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string  
 
    print(f"Vowels count: {vowels_count}")
    print(f"Consonants count: {consonants_count}")
    print(f"Digits count: {digits_count}")
    print(f"Special characters count: {special_char_count}")
    print(f"Reversed string: {reversed_string}")

def main():
    user_input = input("Enter a string: ")
    analyze_string(user_input)

main()
