def get_argument_name(call_node):

    for child in call_node.children:

        if child.type == "argument_list":

            for arg in child.children:

                if arg.type == "identifier":

                    return arg.text.decode()

    return None