def check_pld(word):
    return word == word[::-1]

def new_sent(sentence):
    
    new_sen = ""
    i = 0
    while i < len(sentence):
        if sentence[i] == " " and (i + 1 < len(sentence) and sentence[i + 1] == " "):
            i += 1
            continue
        new_sen += sentence[i]
        i += 1

    words = []
    word = ""
    for char in new_sen:
        if char != " ":
            word += char
        else:
            if word:
                words.append(word)
            word = ""
    if word:
        words.append(word)

    palindrome_count = 0
    for word in words:
        if check_pld(word.lower()):
            palindrome_count += 1

    return new_sen, palindrome_count

def main():
    sentence = input("Enter a sentence: ")

    new_sen, palindrome_count = new_sent(sentence)

    print(new_sen)
    print(f"Number of Palindromes: {palindrome_count}")


main()
