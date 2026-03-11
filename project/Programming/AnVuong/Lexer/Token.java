package Lexer;

public class Token {
    TokenTypes type;
    String text;
    int line;
    
    public Token(TokenTypes type, String text, int line) {
        this.type = type;
        this.text = text;
        this.line = line;
    }
}
