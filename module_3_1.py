calls = 0
def count_calls ():
    global calls
    calls = 4
count_calls()
def string_info (string):
    length = len(string)
    upper_case = string.upper()
    lower_case = string.lower()
    return (length, upper_case, lower_case)
print(string_info('Capybara'))
print(string_info('Armageddon'))
def is_contains (string: str,  list_to_search: list):
    count_calls()
    string = string.lower()
    for word in list_to_search:
        if word.lower() == string:
            return True
    return False
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)