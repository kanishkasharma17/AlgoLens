def uses_memoization(function_node):

    memo_names = {
        "dp",
        "memo",
        "cache"
    }

    found = False

    def visit(node):

        nonlocal found

        if found:
            return

        if node.type=="assignment_expression":
             text=node.text.decode("utf8")
             if "[" in text and "]" in text:
                  found=True
                  return
        # Look for array subscripts:
        # dp[n], memo[i], cache[x]
        if node.type == "subscript_expression":


            text = node.text.decode("utf8")
            if node.type=="subscript_expression":
                    found = True
                    return

        for child in node.children:
            visit(child)

    visit(function_node)

    return found