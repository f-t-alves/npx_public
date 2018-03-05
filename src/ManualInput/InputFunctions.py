

def input_str(message='',):
    print(message, end = '')

    Str = input()

    if Str == None:
        return(Str)
    else:
        return str(Str)

def input_str_not_null(message='',):
    print(message, end = '')

    while True:
        var = input()
        if len(var) < 1:
            print('Not a valid input, please try again: ', end = '')
            continue

        else:
            break

    return str(var)

def get_float_value(message='',):

    print(message, end = '')

    try:
        value = float(input())
    except ValueError:
        print('Input not a number, please try again : ', end = '')
        return get_float_value()
    else:
        return value

def get_float_value_skip(message='',):

    print(message, end = '')

    value = input()
    if not value:
        return(None)
    else:
        try:
            float(value)
        except ValueError:
            print('Input not a number, please try again : ', end = '')
            return get_float_value_skip()

    return value


def get_int_value_skip(message='',):

    print(message, end = '')

    value = input()
    if not value:
        return(None)
    else:
        try:
            int(value)
        except ValueError:
            print('Input not a number, please try again : ', end = '')
            return get_int_value_skip()

    return value


def get_int_value(message='',):

    print(message, end = '')

    try:
        value = int(input())
    except ValueError:
        print('Input not a number, please try again : ', end = '')
        return get_int_value()
    else:
        return value

def get_valid_barcode(message='',):
    
    print(message, end = '')

    while True:
        try:
            value = int(input())
        except ValueError:
            print('Input not a number, please try again: ', end = '')
            continue
        else:
            break
    value = str(value)
    if len(value) < 12 or len(value) > 13:
        print('Not a valid BarCode, please try again: ', end = '')
        return get_valid_barcode()
    else:
        return int(value)
