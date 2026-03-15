
# tests/test_bootcamp_practice.py
import loopy_practice
from loopy_practice import (
    even_index_sum,
    count_vowels,
    reverse_words,
    find_duplicates,
    running_total,
    word_frequency,
    largest_row_sum,
    flatten_two_levels,
    phone_number_validator,
    password_checker,
    common_elements,
    chunk_list,
    palindrome_checker,
    matrix_transpose,
    longest_streak,
    remove_negatives,
    merge_dictionaries,
    count_matrix_even,
    email_validator_no_regex,
    rotate_list
)


# -----------------------------
# Question 1
# -----------------------------

def test_even_index_sum_basic():
    assert even_index_sum([10,20,30,40,50]) == 90


def test_even_index_sum_small():
    assert even_index_sum([5]) == 5


# -----------------------------
# Question 2
# -----------------------------

def test_count_vowels_basic():
    assert count_vowels("Hello World") == 3


def test_count_vowels_case():
    assert count_vowels("AEIOU") == 5


# -----------------------------
# Question 3
# -----------------------------

def test_reverse_words():
    assert reverse_words("python is fun") == "fun is python"


def test_reverse_words_single():
    assert reverse_words("hello") == "hello"


# -----------------------------
# Question 4
# -----------------------------

def test_find_duplicates_basic():
    result = find_duplicates([1,2,3,2,4,5,1])
    assert set(result) == {1,2}


def test_find_duplicates_none():
    assert find_duplicates([1,2,3]) == []


# -----------------------------
# Question 5
# -----------------------------

def test_running_total():
    assert running_total([1,2,3,4]) == [1,3,6,10]


def test_running_total_single():
    assert running_total([5]) == [5]


# -----------------------------
# Question 6
# -----------------------------

def test_word_frequency_basic():

    result = word_frequency("apple banana apple orange banana apple")

    assert result["apple"] == 3
    assert result["banana"] == 2
    assert result["orange"] == 1


# -----------------------------
# Question 7
# -----------------------------

def test_largest_row_sum():

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]

    assert largest_row_sum(matrix) == 24
def test_common_elements():
    assert common_elements([1,2,3],[2,3,4]) == [2,3]


# -----------------------------
# Question 12
# -----------------------------

def test_chunk_list():
    assert chunk_list([1,2,3,4,5,6],2) == [[1,2],[3,4],[5,6]]


# -----------------------------


# -----------------------------
# Question 8
# -----------------------------

def test_flatten_two_levels():
    assert flatten_two_levels([[1,2],[3,4],[5,6]]) == [1,2,3,4,5,6]


# -----------------------------
# Question 9
# -----------------------------

def test_phone_number_validator_basic():

    numbers = ["0831234567","0719876543","12345"]

    result = phone_number_validator(numbers)

    assert "0831234567" in result["valid"]
    assert "0719876543" in result["valid"]
    assert "12345" in result["invalid"]


# -----------------------------
# Question 10
# -----------------------------

def test_password_checker_valid():
    assert password_checker("Password1") == True


def test_password_checker_invalid():
    assert password_checker("weak") == False


# -----------------------------
# Question 11
# -----------------------------

def test_common_elements():
    assert common_elements([1,2,3],[2,3,4]) == [2,3]


# -----------------------------
# Question 12
# -----------------------------

def test_chunk_list():
    assert chunk_list([1,2,3,4,5,6],2) == [[1,2],[3,4],[5,6]]


# -----------------------------
# Question 13
# -----------------------------

def test_palindrome_checker_true():
    assert palindrome_checker("racecar") == True


def test_palindrome_checker_false():
    assert palindrome_checker("hello") == False


# -----------------------------
# Question 14
# -----------------------------

def test_matrix_transpose():

    matrix = [
        [1,2,3],
        [4,5,6]
    ]

    assert matrix_transpose(matrix) == [
        [1,4],
        [2,5],
        [3,6]
    ]


# -----------------------------README.md
# Question 15
# -----------------------------

def test_longest_streak():
    assert longest_streak([1,1,2,2,2,3,3,3,3,1]) == 4


# -----------------------------
# Question 16
# -----------------------------

def test_remove_negatives():
    assert remove_negatives([3,-2,5,-1,7]) == [3,5,7]


# -----------------------------
# Question 17
# -----------------------------

def test_merge_dictionaries():

    result = merge_dictionaries(
        {"a":1,"b":2},
        {"b":3,"c":4}
    )

    assert result == {"a":1,"b":5,"c":4}


# -----------------------------
# Question 18
# -----------------------------

def test_count_matrix_even():

    matrix = [
        [1,2,3],
        [4,5,6]
    ]

    assert count_matrix_even(matrix) == 3


# -----------------------------
# Question 19
# -----------------------------

def test_email_validator_no_regex():

    emails = ["test@example.com","invalid.email"]

    result = email_validator_no_regex(emails)

    assert "test@example.com" in result["valid"]
    assert "invalid.email" in result["invalid"]


# -----------------------------
# Question 20
# -----------------------------

def test_rotate_list():

    assert rotate_list([1,2,3,4,5],2) == [4,5,1,2,3]

