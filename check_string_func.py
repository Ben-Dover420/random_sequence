def check_string(s):
    try:
        int(s)
    except ValueError:
        return False
    else:
        return True