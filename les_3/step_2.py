def my_map(func, temp) -> list:
    result = []
    for itm in temp:
        result.append(func(itm))
    return result
