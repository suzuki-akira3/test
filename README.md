# MyTokenizer

## Abbreviations
TX: text  
TK: token  
LF: line field  
SP: space  
PN: punctuations  
BL: blackets

## Classes
### makeDicList
#### Functions
- text2diclist 
  - Input: text
  - Output: [dict={TX:'texts', dict={LF:'\n'}, ... ] 
 
### myTokenizer
#### Variables
 - dicTokenList = [dict={TK:'term', SP:' ', PN:'.'}, dict={LF:'\n'}, ... ]

#### Functions
 - labeled terms
   - label:LB, xref:RF
   - compound words
 - upwrap blackets
 - split by space
 - prefix
 - surfix
 - infix