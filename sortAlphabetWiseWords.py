# Program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

def sort_words(search):
    
    words = search.split(',')    # spliting from the commas
    
    sorted_words = sorted(words, key=lambda x: x.lower())  
    # providing the preferences
    
    result = ','.join(sorted_words)  # joining the sorted words
    
    return result


search = input("Enter comma-separated sequence of words: ") 
# Example: Dog,cat,Boy,apple

output = sort_words(search)
print("\nAfter alphabatically sorting, output is:", output)
