def all_thing_is_obj(object: any) -> int:
    if type(object) is None or isinstance(object, int):
        print('Type not found')
    elif isinstance(object, str):
        print(f'{object} is in the kitchen : ', type(object))
    else:
        print(type(object))
    return 42
