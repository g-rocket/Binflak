BinFlak
=================
BinFlak is a language a lot like BrainFlak, but compressed so that programs are a lot shorter, and any sequence of bytes is a unique syntactially-valid program.

Encoding a BrainFlak program into BinFlak is a two-step process:

First, the program is encoded as a base-five number (with the end of the program going in the high bits).
Since only one closing-bracket is valid at any given position in a program, all closing-brackets are mapped to 0.

| char | digit |
|------|-------|
| ), ], }, > | 0 |
|(|1|
|[|2|
|{|3|
|<|4|

Second, the numbers are "compacted," by subtracting the number of invalid programs (with more closing than opening braces) are less than it.

Decoding a BinFlak program into BrainFlak follows this process in reverse.
