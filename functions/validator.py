def validate(string: str) -> int:
    if string != '':
        if string.count(".") > 1: return 0
        else:
            if "." in string:
                string = string.split(".")
                if not (string[0].isdecimal() and string[1].isdecimal()): return 0
            else:
                if not string.isdecimal(): return 0
            return 1
    else: return 0


if __name__ == "__main__":
    print(validate("12"))
    print("12.5".count(".") > 1)
    print(not ("12".isdecimal() and "5".isdecimal()))
