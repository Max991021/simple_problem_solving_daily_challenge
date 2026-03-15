
"""
loopy_practice.py

Bootcamp Python Practice Functions

Implement the logic for each function so that all pytest tests pass.
"""


# ============================================================
# Question 1
# ============================================================

def even_index_sum(numbers):
    """
    Return the sum of values located at even indexes.
    Example: [10,20,30,40,50] -> 10+30+50 = 90
    """
    return sum([numbers[i] for i in range(0,len(numbers),2) ])
print(even_index_sum([10,20,30,40,50]))


# ============================================================
# Question 2
# ============================================================

def count_vowels(text):
    """
    Count vowels in a string (case insensitive).
    Vowels: a,e,i,o,u
    """
    return sum(1 for char in text.lower() if char in 'aeiou')
print(count_vowels("Hello WOrld"))


# ============================================================
# Question 3
# ============================================================

def reverse_words(sentence):
    """
    Reverse the order of words in a sentence.
    """
    ls = sentence.split(' ')
    
    return ' '.join(ls[::-1])
print(reverse_words("python is fun"))

# ============================================================
# Question 4
# ============================================================

def find_duplicates(numbers):
    """
    Return a list of numbers that appear more than once.
    Each duplicate should appear only once.
    """
    word = {}
    nums = []
    
    for num in numbers:
        word[num] = word.get(num, 0)+1
    for key,val in word.items():
        if val > 1:
            nums.append(int(key))
    return set(nums)
print(find_duplicates([1,2,3,2,4,5,1]))


# ============================================================
# Question 5
# ============================================================

def running_total(numbers):
    """
    Return a list containing running totals.
    Example: [1,2,3,4] -> [1,3,6,10]
    """
    total = 0
    nums = []
    for i in numbers:
        total += i
        nums.append(total)
    return nums
print(running_total([1,2,3,4]))

# ============================================================
# Question 6
# ============================================================

def word_frequency(sentence):
    """
    Count how many times each word appears.
    Return a dictionary.
    """
    pass


# ============================================================
# Question 7
# ============================================================

def largest_row_sum(matrix):
    """
    Return the largest row sum from a 2D list.
    """
    pass


# ============================================================
# Question 8
# ============================================================

def flatten_two_levels(data):
    """
    Flatten a list containing nested lists.
    Example: [[1,2],[3,4]] -> [1,2,3,4]
    """
    pass


# ============================================================
# Question 9
# ============================================================

def phone_number_validator(numbers):
    """
    Validate phone numbers.

    Valid rules:
    - start with 0
    - length 10
    - digits only

    Return:
    {
        "valid": [],
        "invalid": []
    }
    """
    pass


# ============================================================
# Question 10
# ============================================================

def password_checker(password):
    """
    Check if password is valid.

    Rules:
    - length >= 8
    - uppercase
    - lowercase
    - digit

    Return True or False.
    """
    pass


# ============================================================
# Question 11
# ============================================================

def common_elements(list1, list2):
    """
    Return elements that appear in both lists.
    """
    pass


# ============================================================
# Question 12
# ============================================================

def chunk_list(data, size):
    """
    Split a list into chunks of given size.
    Example: chunk_list([1,2,3,4],2) -> [[1,2],[3,4]]
    """
    pass


# ============================================================
# Question 13
# ============================================================

def palindrome_checker(text):
    """
    Check if string is a palindrome.
    Ignore case and spaces.
    """
    pass


# ============================================================
# Question 14
# ============================================================

def matrix_transpose(matrix):
    """
    Transpose a matrix.
    """
    pass


# ============================================================
# Question 15
# ============================================================

def longest_streak(numbers):
    """
    Return the longest consecutive streak of the same number.
    """
    pass


# ============================================================
# Question 16
# ============================================================

def remove_negatives(numbers):
    """
    Return list without negative numbers.
    """
    pass


# ============================================================
# Question 17
# ============================================================

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries.

    If keys collide, add the values.
    """
    pass


# ============================================================
# Question 18
# ============================================================

def count_matrix_even(matrix):
    """
    Count even numbers in a matrix.
    """
    pass


# ============================================================
# Question 19
# ============================================================

def email_validator_no_regex(emails):
    """
    Validate emails WITHOUT using regex.

    Rules:
    - exactly one '@'
    - characters before '@'
    - '.' after '@'
    - characters after last '.'

    Return:
    {
        "valid": [],
        "invalid": []
    }
    """
    pass


# ============================================================
# Question 20
# ============================================================

def rotate_list(numbers, k):
    """
    Rotate list right by k positions.

    Example:
    [1,2,3,4,5],2 -> [4,5,1,2,3]
    """
    pass

