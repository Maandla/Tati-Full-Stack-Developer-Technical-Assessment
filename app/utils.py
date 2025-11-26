import datetime

def validate_msno(msno):
    if not msno or len(msno) != 11 or not msno.isdigit():
        return "invalid_format"
    if msno == "01234567891":
        return "specific_fault"
    if msno == "01234567892":
        return "not_found"
    return "success"

def current_timestamp():
    return datetime.datetime.now().isoformat()
