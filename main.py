def __get_response_data(parsed, keys):
    for ix in range(keys):
        if ix == len(keys) - 1:
            return parsed[keys[ix]]
        else:
            return __get_response_data(parsed, keys[1:])

print(__get_response_data({'1': {'2': {'3': {'4': '4', '5': ['5']}}}}, ['3', '2', '1']))