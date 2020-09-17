# write your code here
def regex_engine(regex, string):
    char = ""

    if len(regex) == 0:
        return True
    elif len(string) == 0:
        return False

    if string.find("\\") != -1 and len(string) == 1:
        string = string[0:string.find("\\")] + "\\" + string[string.find("\\"):]
    elif string.find("\\") != -1 and string[string.find("\\") + 1] != "\\":
        string = string[0:string.find("\\")] + "\\" + string[string.find("\\"):]

    if regex.find("\\") != -1 and len(regex) == 1:
        regex = regex[0:regex.find("\\")] + "\\" + regex[regex.find("\\"):]
    elif regex.find("\\") != -1 and regex[regex.find("\\") + 1] != "\\":
        regex = regex[0:regex.find("\\")] + "\\" + regex[regex.find("\\"):]

    if regex.find("\\") != -1 and regex[regex.find("\\") + 1] == "\\" and len(regex) > 2:
        char = regex[regex.find("\\") + 2]
        regex = regex[:regex.find("\\")] + regex[regex.find("\\") + 2:]

    if regex[0] == "^" and regex[-1] == "$" and regex.find("?") == -1 and regex.find("*") == -1 and regex.find("+") == -1:
        regex = regex[1:-1]
        return regex == string

    if regex[0] == "^" and (regex[1] == string[0] or regex[1] == "."):
        regex = regex[1:]
        if regex_match_chr(regex[0:len(regex)], string[0:len(regex)]):
            return True

    if regex[-1] == "$" and (regex[-2] == string[-1] or regex[-2] == "."):
        regex = regex[0:-1]
        if regex_match_chr(regex[0:], string[len(string) - len(regex):]):
            return True

    if regex.find("?") != -1 and char != "?":
        regex1 = regex[0:regex.index("?")] + regex[regex.index("?")+1:]
        regex2 = regex[0:regex.index("?")-1] + regex[regex.index("?") + 1:]
        for i in range(len(string)):
            for j in range(len(regex1)):
                if not regex_match_chr(regex1[j], string[j+i]):
                    break
            else:
                return True
        for i in range(len(string)):
            for j in range(len(regex2)):
                if not regex_match_chr(regex2[j], string[j+i]):
                    break
            else:
                return True
        else:
            return False

    elif regex.find("*") != -1 and char != "*":
        regex_char = ""
        regex1 = string
        while len(regex1) <= len(string):
            regex1 = regex[0:regex.index("*") - 1] + regex_char + regex[regex.index("*") + 1:]
            for i in range(len(string)):
                for j in range(len(regex1)):
                    if not regex_match_chr(regex1[j], string[j+i]):
                        break
                else:
                    return True
            regex_char = regex_char + regex[regex.index("*") - 1]
        else:
            return False

    elif regex.find("+") != -1 and char != "+":
        regex_char = regex[regex.index("+") - 1]
        regex1 = regex[0:regex.index("+") - 1] + regex_char + regex[regex.index("+") + 1:]
        while len(regex1) <= len(string):
            regex1 = regex[0:regex.index("+") - 1] + regex_char + regex[regex.index("+") + 1:]
            for i in range(len(string)):
                for j in range(len(regex1)):
                    if not regex_match_chr(regex1[j], string[j+i]):
                        break
                else:
                    return True
            regex_char = regex_char + regex[regex.index("+") - 1]
        else:
            return False
    else:
        for i in range(len(string)):
            for j in range(len(regex)):
                if not regex_match_chr(regex[j], string[j+i]):
                    break
            else:
                return True
        return False


def regex_match_chr(chr1, chr2):
    return chr1 in (chr2, ".")


regex_in, string_in = input().split("|")
print(regex_engine(regex_in, string_in))