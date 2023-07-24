- `<reg>` - (A,B,C,D,E,X or L)
- `<mem>` - memory address
- `<vid-addr>` - video memory address
- `<inst>` - address of memory instruction
- `<num>` - number

- `p1` - first param
- `p2` - second param etc

- `||` - logical or
## Registers
- Just special memory addresses
```arm
A - 000001
B - 000010
C - 000011
D - 000100
E - 000101
X - 000110
L - 000111
```
## Stage 1
- Each instruction's machine code is 17 bits long
- If the instruction doesn't have a param 2, it is just `000000`
```arm
opcode param1 param2
00001  000001 000010
00010  000100 000110
00111  000001 000000
```
```arm
Five-bit opcode | Instruction + params         | Explanation
00001             mov <reg>||<mem>,<reg>||<mem> -   Moves p1 to p2

00010 add <reg>,<reg> - X=p1+p2
00011 sub <reg>,<reg> - X=p1-p2
00100 mul <reg>,<reg> - X=p1*p2
00101 div <reg>,<reg> - X=p1/p2

00111 inc <reg> - p1++
01000 dec <reg> - p1--

01001 inv <reg> - p1=~p1

01010 and <reg>,<reg> - performs logical and on p1 and p2, stores in X
01011 or <reg>,<reg>
01100 xor <reg>,<reg>

01101 cmp <reg>,<reg> - examines the equality between the p1 & p2. Places result in L, for jump commands.

01111 stor <reg>,<num> - stors p2 in p1

11000 vid <reg> - displays p1 in the video adaptor
```
### Jumps
- Check out `L`, decides what to do based on its value
```arm
10000 je <inst> - ==
10001 jne - !=
10010 jz - L==0
10011 jg - if they were greater than
10100 jge - or equal to
10101 jl - less than
10111 jle - or equal to
```
## Examples
```arm
mov A,B
```
```arm
00001 000001 000010
```
<br>

```arm
add D,X
```
```arm
00010 000100 000110
```
<br>

```arm
inc A
```
```arm
00111 000001 000000
```
## Stage 2
```arm
push <reg>||<mem> - Pushes p1 to stack
```