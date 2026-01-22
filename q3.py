# Corrected version avoiding default mutable argument pitfall

def save_error(error,errors=None):
    if errors is None:
        errors=[]
    errors.append(error)
    return errors
print(save_error("Error 404"))
print(save_error("Error 408"))
print(save_error("Error 401"))
