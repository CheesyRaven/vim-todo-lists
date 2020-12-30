def find_header_line( line ):
    result = line.endswith(':')
    if result:
        return "pass"
    else:
        return "fail"

