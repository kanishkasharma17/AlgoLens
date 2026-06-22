from tree_sitter import Language, Parser
from tree_sitter_cpp import language

CPP_LANGUAGE = Language(language())

parser = Parser(CPP_LANGUAGE)

def parse_cpp(code):

    tree = parser.parse(
        bytes(code, "utf8")
    )

    return tree.root_node