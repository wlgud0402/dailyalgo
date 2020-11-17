def findEmailDomain(address):
    while "@" in address:
        idx = address.find("@")
        address = address[idx+1:]

    return address


print(findEmailDomain("fully-qualified-domain@codesignal.com"))
