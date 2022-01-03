# The following line creates a dictionary from the input. Do not modify it, please
test_dict = json.loads(input())

# Work with the 'test_dict'
reverse_dict = {}
for key, value in test_dict.items():
    reverse_dict[value] = key

min_key = reverse_dict[min(reverse_dict.keys())]
max_key = reverse_dict[max(reverse_dict.keys())]
print(f'min: {min_key}')
print(f'max: {max_key}')