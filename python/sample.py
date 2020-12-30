def find_header_line( line ):
    #isheader = ":"
    #if isheader in line:
    result = line.endswith(':')
    if result:
        return "pass"
    else:
        return "fail"

