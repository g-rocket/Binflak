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

Finally, this number (as a sequence of extended-ASCII characters or whatnot) is your program.

Decoding a BinFlak program into BrainFlak follows this process in reverse.


As an example, let's translate the BrainFlak program `[()()]` into BinFlak.

* To convert it to a base-5 number, we reverse it and follow the table above to get `001012`, or 132.
* Compacting this, we subtract 30, because there are 30 invalid programs less than 1012: 
  - 10,
20,
30,
40,
100,
110,
120,
130,
140,
200,
210,
220,
230,
240,
300,
310,
320,
330,
340,
400,
410,
420,
430,
440,
1000,
1001,
1002,
1003,
1004, and
1010 are all invalid because they attempt to close a bracket they never open.
* Finally, the program is `102`, or read as ASCII `f`.
