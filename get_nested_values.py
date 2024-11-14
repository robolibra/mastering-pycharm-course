data_structure = [{
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "preferences": {
            "notifications": {
                "email": True,
                "sms": False,
                "push": True
            },
            "theme": "dark",
        },
    },
},
{
    "user": {
        "id": 1,
        "name": "John Doe",
        "email": "john.doe@example.com",
        "preferences": {
            "notifications": {
                "email": True,
                "sms": False,
                "push": [True, False]
            },
            "theme": "dark",
        },
    },
}]


def get_nested_value(data, key_path):
    keys = key_path.split('__')
    result = []

    def recursive_get(data, keys):
        if not keys:
            return data
        current_key = keys[0]
        remaining_keys = keys[1:]

        if isinstance(data, list):
            # Apply the function recursively to each item in the list and collect results
            return [recursive_get(item, keys) for item in data if recursive_get(item, keys) is not None]
        elif isinstance(data, dict) and current_key in data:
            # Continue to traverse the dictionary
            return recursive_get(data[current_key], remaining_keys)
        return None

    # Handle the case when expecting a list of values (like `task_id`)
    result = recursive_get(data, keys)

    # Flatten result if it's a list of lists
    if isinstance(result, list):
        flat_result = []
        for item in result:
            if isinstance(item, list):
                flat_result.extend(item)
            else:
                flat_result.append(item)
        result = flat_result

    # Return a single value if only one item is in the list, else return the list
    if len(result) == 1:
        return result[0]
    return result

print(get_nested_value(data_structure, 'user__preferences__notifications__push'))
