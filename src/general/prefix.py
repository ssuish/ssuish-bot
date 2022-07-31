import re 

class Prefix:
    def_prefix = re.compile(r"^s\.")
    new_prefix = []
    cmdln_isValid = bool(False)
    
    