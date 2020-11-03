# -*- coding: utf-8 -*-
import re


def variableName(name):
    if name[0].isdigit():
        return False

    if " " in name:
        return False

    if name[0].isalpha():
        pass

    elif name[0] == "_":
        pass
    else:
        return False

    for i in range(1, len(name)):
        if name[i].isalnum():
            continue
        elif name[i] == "_":
            continue
        else:
            return False

    return True


print(variableName("/variable"))
