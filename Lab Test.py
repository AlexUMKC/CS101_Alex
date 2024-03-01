#I tried using a simple way of trying to count the number of words
def word_count(user_input):
    count = len(user_input.split)
    return count

#I knew of the min and max so I tried to use them here since I was stuck on finding another way.
def find_longest_word(user_input):
    longest_word = " "
    user_input.split()
    longest_word = max(user_input, key=len)
    return longest_word

#
def count_substring(user_input, substring):
    string = user_input
    for l in string:
        if l.isalnum():

def extract_unique_words(user_input):
    unique = user_input
    user_input[0] = ""
    return unique
# I try using the same methods as I did in the past but it seem that it got too diffcult to sort.
def main():
    print("Welcome to the test procesing program!")
    user_input = str(input("Enter a text: "))
    print("Orginal Text",str((user_input)))
    while True:
        print("Text Analysis Option")
        print("1. Word count")
        print("2. Longest Word")
        print("3. Count of Substring")
        print("4. Unique Words")
        print("5. Exit")
        print("Enter the number of the analysis option (1-5): ")
        for x in range(4):
            user_pick = int(input(print("Enter the number of the analysis option (1-5): ")))
        if user_pick > 5 or user_pick < 1:
            print("Invaid option. Please try again")
        else:
            break
        if user_pick == 1:
            count = word_count(user_input)
            print(count)
        elif user_pick == 2:
            longest_word = find_longest_word(user_input)
            print(longest_word)
        elif user_pick == 3:
            substring = count_substring(user_input)
            print(substring)
        elif user_pick == 4:
            unique = extract_unique_words(user_input)
            print(unique)
        elif user_pick == 5:
            print("Goodbye")
            break


if __name__ == "__main__":
main()
