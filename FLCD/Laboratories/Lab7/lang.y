%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function declarations
void yyerror(char *s);
int yylex();
extern int yydebug;
%}

// Union declaration for token and nonterminal values
%union {
    int intval;        // Integer constants
    float floatval;    // Float constants
    char *strval;      // Strings and identifiers
}

%debug


// Token definitions with appropriate types
%token <intval> INT_CONST
%token <floatval> FLOAT_CONST
%token <strval> STRING_CONST IDENTIFIER
%token INT FLOAT BOOL STRING IF ELSE FOR WHILE RETURN INPUT PRINT RANGE IN
%token PLUS MINUS MULT DIV ASSIGN EQ NEQ LT GT LEQ GEQ INC DEC
%token LBRACE RBRACE LPAREN RPAREN SEMICOLON COMMA BOOL_CONST
%token NEWLINE

// Nonterminal type declarations
%type <strval> declaration type_spec statement expression assignment
%type <strval> compound_stmt if_stmt while_stmt for_stmt print_stmt input_stmt
%type <strval> expression_list statement_list declaration_list program

// Precedence and associativity to resolve conflicts
%nonassoc LOWER_THAN_ELSE
%left PLUS MINUS
%left MULT DIV
%nonassoc LT GT LEQ GEQ EQ NEQ

// Start symbol
%start program

%%

program:
           declaration_list statement_list
    ;

declaration_list:
		    declaration_list declaration
    | declaration
    ;

declaration:
	       type_spec IDENTIFIER
                { printf("Declaration of %s with type %s\n", $2, $1); }
    ;

type_spec:
	              INT     { $$ = strdup("int"); }
    | FLOAT { $$ = strdup("float"); }
    | BOOL  { $$ = strdup("bool"); }
    | STRING { $$ = strdup("string"); }
    ;

statement_list:
	                        statement_list statement
    | statement
    | statement NEWLINE
    ;

statement:
	     compound_stmt
    | if_stmt
    | while_stmt
    | for_stmt
    | print_stmt
    | input_stmt
    | assignment
    ;

assignment:
	      IDENTIFIER ASSIGN expression
        { printf("Assignment to %s\n", $1); free($1); }
    ;

compound_stmt:
	                      LBRACE statement_list RBRACE
        { printf("Compound statement block\n"); }
    ;

if_stmt:
                  IF LPAREN expression RPAREN statement
        { printf("If statement\n"); }
    ;

while_stmt:
	                WHILE LPAREN expression RPAREN statement
        { printf("While loop\n"); }
    ;

for_stmt:
	            FOR IDENTIFIER IN RANGE LPAREN expression COMMA expression RPAREN compound_stmt
        { printf("For loop\n"); }
    ;

print_stmt:
	                PRINT LPAREN expression_list RPAREN SEMICOLON
        { printf("Print statement\n"); }
    ;
input_stmt:
	      IDENTIFIER ASSIGN INPUT LPAREN STRING_CONST RPAREN SEMICOLON
    {
        printf("Input function call assigning to %s\n", $1);
    }
    ;


expression_list:
	                          expression_list COMMA expression
        { printf("Expression list\n"); }
    | expression
        { printf("Single expression\n"); }
 ;


expression:
	      IDENTIFIER
        { printf("Identifier: %s\n", $1); $$ = $1; }
    | INT_CONST
        { printf("Integer constant: %d\n", $1); $$ = (char*)malloc(20); sprintf($$, "%d", $1); }
    | FLOAT_CONST
        { printf("Float constant: %f\n", $1); $$ = (char*)malloc(20); sprintf($$,"%f",$1); }
    | BOOL_CONST
        { printf("Boolean constant\n"); }
    | STRING_CONST
        { printf("String constant: %s\n", $1); $$ = $1; }
    | expression PLUS expression
        { printf("Addition\n"); }
    | expression MINUS expression
        { printf("Subtraction\n"); }
    | expression MULT expression
        { printf("Multiplication\n"); }
    | expression DIV expression
        { printf("Division\n"); }
    | expression EQ expression
        { printf("Equality check\n"); }
    | expression NEQ expression
        { printf("Inequality check\n"); }
    | expression LT expression
        { printf("Less than\n"); }
    | expression GT expression
        { printf("Greater than\n"); }
    | expression LEQ expression
        { printf("Less than or equal\n"); }
    | expression GEQ expression
        { printf("Greater than or equal\n"); }
    | RANGE LPAREN expression COMMA expression RPAREN
        { printf("Range function call\n"); }
    ;


%%

// Error handler
void yyerror(char *s) {
    fprintf(stderr, "Error1111: %s\n", s);
}

// Entry point
int main() {
    yydebug=0;
    yyparse();
    return 0;
}

