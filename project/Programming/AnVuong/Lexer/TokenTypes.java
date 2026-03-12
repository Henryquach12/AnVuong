package Lexer;


public enum TokenTypes {
    // Literals 
    NUMBER, STRING, BOOLEAN,
    
    // Keywords
    DAT, NEU, NEU_KHONG, KHONG,TRONGKHI, LAP, TRAVE, NGUNG, SAI, DUNG, VA, HOAC,

    //Identifier
    Identifier,

    // Operators
    PLUS,       // +
    MINUS,      // -
    STAR,       // *
    SLASH,      // /
    EQUALS,     // =
    EQUAL_EQUAL,// ==
    BANG_EQUAL, // !=
    GREATER,    // >
    LESS,       // 

    // Punctuation
    LPAREN,     // (
    RPAREN,     // )
    LBRACE,     // {
    RBRACE,     // }
    COMMA,      // ,

    // Special
    NEWLINE,
    EOF
}

