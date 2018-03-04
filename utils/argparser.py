import sys

def usage():
    text = '''
usage: dinheiro
    more details here
    '''
    raise Exception(text)

def parseArgs(argv=sys.argv):
    argc = len(argv)

    try:
        # month
        result = parseMonth(argc, argv)
        if (result[0]):
            return result

        # ls
        result = parseLs(argc, argv)
        if (result[0]): 
            return result

        # rm
        result = parseRm(argc, argv)
        if (result[0]):
            return result

        # add
        result = parseAdd(argc, argv)
        if (result[0]):
            return result

        # edit
        result = parseEdit(argc, argv)
        if (result[0]):
            return result

        result = parsePay(argc, argv)
        if (result[0]):
            return result

        # no valid commands
        usage()
    except ValueError:
        usage()

def parseMonth(argc, argv):
    method_name = None
    param = None
    if argc > 1 and argv[1] == 'month':
        method_name = 'change_month'
        if argc < 2:
            usage()

        param = [argv[2]]

    return [method_name, param]

def parseLs(argc, argv):
    method_name = None
    param = None
    if (argc > 1 and argv[1] == 'ls'):
        if (argc > 2):
            # ls despesa
            if (argv[2] == 'despesa'):
                method_name ='ls_desp'
                # ls despesa anual | temp
                if (argc > 3):
                    # ls despesa anual
                    if (argv[3] == 'anual'):
                        method_name += '_an'
                    # ls despesas temp
                    elif (argv[3] == 'temp'):
                        method_name += '_tmp'
                    else:
                        usage()
            # ls renda
            elif (argv[2] == 'renda'):
                method_name ='ls_renda'

            # ls tipo renda
            elif (argv[2] == 'tipo'):
                method_name = 'ls_tipo'
                if (argc > 3 and argv[3] == 'renda'):
                    method_name += '_renda'
                else:
                    usage()

            # ls carne leao
            elif (argv[2] == 'carne'):
                method_name = 'ls_carne'
                if (argc > 3 and argv[3] == 'leao'):
                    method_name += '_leao'
                else:
                    usage()

            # ls parameter
            elif (argv[2] == 'parameter'):
                method_name = 'ls_param'

            else:
                usage()
        else:
            usage()

    return [method_name, param]

def parseRm(argc, argv):
    method_name = None
    param = None
    if (argc > 1 and argv[1] == 'rm'):
        if (argc > 2):
            # rm despesa <id>
            if (argv[2] == 'despesa'):
                method_name = 'rm_desp'
                if (argc > 3):
                    # rm despesa anual 
                    if (argv[3] == 'anual'):
                        method_name += '_an'
                    # rm despesa temp
                    elif (argv[3] == 'temp'):
                        method_name += '_tmp'

            # rm renda <id>
            elif (argv[2] == 'renda'):
                method_name = 'rm_renda'
                        
            # rm tipo renda <id>
            elif (argv[2] == 'tipo'):
                method_name = 'rm_tipo'
                if (argc > 3 and argv[3] == 'renda'):
                    method_name += '_renda'
                else:
                    usage()

            # rm parameter <[namespace, name]>
            elif (argv[2] == 'parameter'):
                method_name = 'rm_param'

            else:
                usage()    
        else:
            usage()        
        param = parseMethodParams(method_name, argc, argv)                                    

    return [method_name, param]

def parseAdd(argc, argv):
    method_name = None
    param = None
    if (argc > 1 and argv[1] == 'add'):
        if (argc > 2):
            # add despesa
            if (argv[2] == 'despesa'):
                method_name = 'add_desp' 
                if (argc > 3):
                    # add despesa anual
                    if (argv[3] == 'anual'):
                        method_name += '_an'
                    # add despesa temp
                    elif (argv[3] == 'temp'):
                        method_name += '_tmp'
                    else:
                        usage()

            # add renda
            elif (argv[2] == 'renda'):
                method_name = 'add_renda'

            # add tipo renda
            elif (argv[2] == 'tipo'):
                method_name = 'add_tipo' 
                if (argc > 3 and argv[3] == 'renda'):
                    method_name += '_renda'
                else:
                    usage()
              
            # add parameter                    
            elif (argv[2] == 'parameter'):
                method_name = 'add_parameter'
        else:
            usage()

    return [method_name, param]

def parseEdit(argc, argv):
    method_name = None
    param = None
    if (argc > 1 and argv[1] == 'edit'):
        if (argc > 2):
            # edit despesa <id> [<fields list>]
            if (argv[2] == 'despesa'):
                method_name = 'edit_desp'
                if (argc > 3):
                    # edit despesa anual <id> [<fields list>]
                    if (argv[3] == 'anual'):
                        method_name += '_an'
                    # edit despesa temp <id> [<fields list>]
                    elif (argv[3] == 'temp'):
                        method_name += '_tmp'

            # edit renda <id> [<fields list>]
            elif (argv[2] == 'renda'):
                method_name = 'edit_renda'
                                
            # edit tipo renda <id>
            elif (argv[2] == 'tipo'):
                method_name = 'edit_tipo'
                if (argc > 3 and argv[3] == 'renda'):
                    method_name += '_renda'
                else:
                    usage()

            # edit parameter <[namespace, name]>
            elif (argv[2] == 'parameter'):
                method_name = 'edit_param'

            else:
                usage()
        else:
            usage()

        param = parseMethodParams(method_name, argc, argv)

    return [method_name, param]

def parsePay(argc, argv):
    method_name = None
    param = None
    if (argc > 1 and argv[1] == 'pay'):
        if (argc > 2):
            # pay despesa <id> [<value>]
            if (argv[2] == 'despesa'):
                method_name = 'pay_desp'
                if (argc > 3):
                    # pay despesa anual <id> [<value>]
                    if (argv[3] == 'anual'):
                        method_name += '_an'
                    # pay despesa temp <id> [<value>]
                    elif (argv[3] == 'temp'):
                        method_name += '_tmp'

            else:
                usage()
        else:
            usage()

        param = parseMethodParams(method_name, argc, argv)

    return [method_name, param]

def parseMethodParams(method_name, argc, argv):
    method_words = method_name.split('_')
    word_count = len(method_words)
    param_start_index = word_count + 1
    param = []
    if (argc > param_start_index):
        param = argv[param_start_index:]
        # the first parameter is an id, so should be conversible to an int
        param[0] = int(param[0])
    else:
        action = method_words[0]
        if (action in ['rm', 'edit', 'pay']):
            raise ValueError('id cannot be empty')   

    return param
