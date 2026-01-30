%{
%}

%token NULL ASSIGN LPAREN RPAREN LBRACE RBRACE LBRACKET RBRACKET READ PRINT FOR WHILE IF ELSE TYPE IDENTIFIER CONSTANT REL_OP EXPR_OP TERM_OP

%%

program:
    NULL { printf("program -> null\n"); }
    | statement_list { printf("program -> statement_list\n"); }
    | statement { printf("program -> statement\n"); }
    ;

statement_list:
    statement { printf("statement_list -> statement\n"); }
    | statement_list statement { printf("statement_list -> statement_list statement\n"); }
    ;

statement:
    assignment_stmt { printf("statement -> assignment_stmt\n"); }
    | declaration_stmt { printf("statement -> declaration_stmt\n"); }
    | io_stmt { printf("statement -> io_stmt\n"); }
    | if_stmt { printf("statement -> if_stmt\n"); }
    | while_stmt { printf("statement -> while_stmt\n"); }
    | for_stmt { printf("statement -> for_stmt\n"); }
    ;

declaration_stmt:
    TYPE IDENTIFIER { printf("declaration_stmt -> TYPE IDENTIFIER\n"); }
    | TYPE IDENTIFIER ASSIGN expression { printf("declaration_stmt -> TYPE IDENTIFIER = expression\n"); }
    ;

assignment_stmt:
    IDENTIFIER ASSIGN expression { printf("assignment_stmt -> IDENTIFIER = expression\n"); }
    ;

io_stmt:
    READ LPAREN IDENTIFIER RPAREN { printf("io_stmt -> read ( IDENTIFIER )\n"); }
    | PRINT LPAREN IDENTIFIER RPAREN { printf("io_stmt -> print ( IDENTIFIER )\n"); }
    ;

if_stmt:
    IF condition LBRACE statement_list RBRACE { printf("if_stmt -> if condition { statement_list }\n"); }
    | IF condition LBRACE statement_list RBRACE ELSE LBRACE statement_list RBRACE { printf("if_stmt -> if condition { statement_list } else { statement_list }\n"); }
    ;

while_stmt:
    WHILE condition LBRACE statement_list RBRACE { printf("while_stmt -> while condition { statement_list }\n"); }
    ;

for_stmt:
    FOR statement condition statement LBRACE statement_list RBRACE { printf("for_stmt -> for statement condition statement { statement_list }\n"); }
    ;

condition:
    expression REL_OP expression { printf("condition -> expression REL_OP expression\n"); }
    ;

expression:
    term { printf("expression -> term\n"); }
    | expression EXPR_OP term { printf("expression -> expression EXPR_OP term\n"); }
    ;

term:
    factor { printf("term -> factor\n"); }
    | term TERM_OP factor { printf("term -> term TERM_OP factor\n"); }
    ;

factor:
    LPAREN expression RPAREN { printf("factor -> ( expression )\n"); }
    | IDENTIFIER { printf("factor -> IDENTIFIER\n"); }
    | CONSTANT { printf("factor -> CONSTANT\n"); }
    ;

%%
