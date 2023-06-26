def reduce_file_path(path):
    dirs = path.split('/')    
    reduced_dirs = []
    result = ''

    for directory in dirs:
        if directory == '..':
            try:
                reduced_dirs.pop()
            finally:
                continue
            
        if directory ==  '.':
            continue

        reduced_dirs.append(directory)

    for directory in reduced_dirs:
        if directory:
            result += "/" + str(directory)

    if not result:
        return '/' 
         
    return result



tests = [
reduce_file_path("/") == "/",
reduce_file_path("/srv/../") == "/",
reduce_file_path("/srv/www/htdocs/wtf/") == "/srv/www/htdocs/wtf",
reduce_file_path("/srv/www/htdocs/wtf") == "/srv/www/htdocs/wtf",
reduce_file_path("/srv/./././././") == "/srv",
reduce_file_path("/etc//wtf/") == "/etc/wtf",
reduce_file_path("/etc/../etc/../etc/../") == "/",
reduce_file_path("//////////////") == "/",
reduce_file_path("/../") == "/",
reduce_file_path("/../../../") == "/",
]


for test in tests:
    print(test)