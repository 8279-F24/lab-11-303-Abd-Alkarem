input_data = input()
search_name = input()

contact_dict = dict(pair.split(',') for pair in input_data.split())

print(contact_dict.get(search_name, "Name not found."))
