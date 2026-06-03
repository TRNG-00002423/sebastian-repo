def validate_password(password):
    special_char = "!@#$%^&*"
    has_len = False
    has_up     = False 
    has_low    = False
    has_digit  = False
    has_special= False

    if len(password) >= 8:
        has_len = True

    err_message = [] 


    for passw in password:
        if passw == passw.lower():
            has_low = True
        if passw == passw.upper():
            has_up = True
        if passw.isdigit():
            has_digit = True
        if passw in special_char:
            has_special = True
    
    if has_len and has_special and has_low and has_up and has_digit:
        return True

    
    if not has_len:
        err_message.append("too short")
    if not has_low:
        err_message.append("doesn't have lower case words")
    if not has_up:
        err_message.append("Doesn't have upper case letter")
    if not has_digit:
        err_message.append("doesnt have digit")
    if not has_special:
        err_message.append("doesnt have special character")
    
    return {
    "valid": False,
    "errors": err_message
    }
if __name__ == "__main__":
    assert validate_password("Abc123!x")   # valid                                     
    assert validate_password("abc") == {'valid': False, 'errors': ['too short', "Doesn't have upper case letter", 'doesnt have digit', 'doesnt have special character']}
# too short, no upper, no digit, no special
    assert validate_password("ABCDEFGH") == {'valid': False, 'errors': ["doesn't have lower case words", 'doesnt have digit', 'doesnt have special character']}# no lower, no digit, no special
    assert validate_password("ABCDefgh1!") # valid

