def validate_pin (pin):
    if (len(pin) !=4) and (len(pin) !=6):
        return False;
    else:
        if pin.isdigit():
            return True
        else:
            return False


print(validate_pin("129095"))