def flatten_dict(d, parent_key='', sep='_'):
    items = {}

    for key, value in d.items():
        new_key = parent_key + sep + key if parent_key else key

        if isinstance(value, dict):
            items.update(flatten_dict(value, new_key, sep=sep))
        else:
            items[new_key] = value

    return items
data = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print(flatten_dict(data))