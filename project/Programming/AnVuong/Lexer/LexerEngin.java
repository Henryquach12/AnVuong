package Lexer;
import java.util.ArrayList;
import java.util.List;

public class LexerEngin {
    String source;
    int position;
    int line;
    List<Token> tokens;

    // Sets up the lexer with the source code
    public LexerEngin(String source) {
        this.source = source;
        this.position = 0;
        this.line = 1;
        tokens = new ArrayList<>();
    }

    // Returns the position of current character
    private char current(){
        return source.charAt(position);
    }

    // Move the pointer
    private void advance(){
        position ++;
    }

    // Reads the entire source code and returns a list of tokens
    public List<Token> tokensize(){

        while(position < source.length()){

            // Skip spaces and tabs, no meaning in An Vuong
            if (current() == ' ' || current() == '\t'){
                advance(); 

            // Newlines end a statment, create a token
            } else if (current() == '\n'){
                tokens.add(new Token(TokenTypes.NEWLINE, "\n", line));
                line ++;
                advance();
            }
        }

        // A signal for the end of the file
        tokens.add(new Token(TokenTypes.EOF, "", line));
        return tokens;
    }
}
