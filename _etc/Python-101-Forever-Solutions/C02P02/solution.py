import sys
import json


CLI_ARGS = sys.argv[1:]

def elements_index_spliter(element):
    try:
        return (
                    (element.split('['))[0],
                    int(((element.split('['))[1]).replace(']',''))
                )
    except:
        return element

def json_elements_dumper(CLI_ARGS):

    json_file = open(CLI_ARGS[0])
    json_input = CLI_ARGS[1].split('.')
    json_data = json.load(json_file)
    arguments = list()

    for x in range(len(json_input)):
        arguments.append(elements_index_spliter(json_input[x]))

    result = dict()
    
    for x in arguments:
        if isinstance(x, tuple):
            try:
                result = json_data[f'{x[0]}'][x[1]]
            except:
                    return 'Error: Property not found'            
        else:
            try:
                int(x)
                result = json_data[x]
            except:
                try:
                    result = json_data[f'{x}']
                except:
                    return 'Error: Property not found'            
        json_data = result
    try: 
        return result
        json_file.close() 
    except:
        return 'Error: Property not found'
        json_file.close()

print(json_elements_dumper(CLI_ARGS))