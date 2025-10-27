def reverse(string):
    return string[::-1]


reverse_data_path = 'tests/test_data/reverse_data.txt'

with open(reverse_data_path) as data:
    text_to_reverse = data.read()
    reversed_data = reverse(text_to_reverse)
