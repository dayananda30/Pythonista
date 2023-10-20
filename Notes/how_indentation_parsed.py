"""
Lexical analyzer uses stack to parse indentations.

At the beginning, the stack contains just the value 0, which is the leftmost position.
Whenever a nested block begins, the new indentation level is pushed on the stack,
and an "INDENT" token is inserted into the token stream which is passed to the parser.

There can never be more than one "INDENT" token in a row (IndentationError).

"""
foo = True
bar = True

if foo:
    if bar:
        x = 42
else:
    print(foo)


"""
<foo> <=> <True>                [0]
<bar> <=> <True>                [0]
<if> <foo> <:>                  [0]
<INDENT> <if> <bar> <:>         [0, 4]
<INDENT> <x> <=> <42>           [0, 4, 8]
<DEDENT> <DEDENT> <else> <:>    [0]
<INDENT> <print> <foo>          [0, 4]
<DEDENT>                        [0]
"""
