# Spliting text into a list then counts each word in the list
def word_count(text):
    words = text.split()
    return len(words)

#After spliting the text using max will find the lorgest word based on length 
def find_longest_word(text):
    words = text.split()
    longest_word = max(words, key=len)
    return longest_word

# Counts the occurrences a substring
def count_substring(text, substring):
    return text.count(substring)

# First coverting the text into lowercase and spliting into words allows for the removal of any duplicates 
def extract_unique_words(text):
    words = text.lower().split()
    unique_words = list(set(words))  # Set() is unchangeable but allows items to be added or remove 
    return unique_words

# Prompting the  user for input text
def main():
    print("Welcome to the Text Analysis Program!")
    user_text = input("Enter a text: ")  
    print(f"\nOriginal Text:\n{user_text}\n")
    
    # Using a while loop to ensure that menu keeps on asking to pick an option until ask the exit
    while True:
        print("Text Analysis Options:")
        print("1. Word Count")
        print("2. Longest word")
        print("3. Count of substring")
        print("4. Unique words")
        print("5. Exit")
        
        choice = input("\nEnter the number of analysis option (1-5): ")

        if choice == '1':
            print(f"Word Count: {word_count(user_text)}\n")
        elif choice == '2':
            print(f"Longest Word: {find_longest_word(user_text)}\n")
        elif choice == '3':
            substring = input("Enter the substring to search for: ")
            print(f"Count of substring '{substring}': {count_substring(user_text, substring)}\n")
        elif choice == '4':
            unique_words = extract_unique_words(user_text)
            print(f"Unique Words: {unique_words}\n")
        elif choice == '5':
            print("Thank you for using the text processing program!")
            break
        else:
            print("Please pick an option (1-5).")

if __name__ == "__main__":
    main()
