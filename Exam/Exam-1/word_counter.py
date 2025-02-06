def word_counter(sentence):
    word_counts = {}
    word = ""  # 
    
    for char in sentence.lower():  
        if char != " " and char.isalnum(): 
            word += char
        else:
            if word:  
                if word in word_counts:
                    word_counts[word] += 1
                else:
                    word_counts[word] = 1
                word = ""  
    
    if word:  
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

def main():
    sentence = input("Enter a sentence: ")
    word_counts = word_counter(sentence)
    
    for word in word_counts: 
        print(f"{word}: {word_counts[word]}")

main()
