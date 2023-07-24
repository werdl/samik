import interpret,textwrap
source=interpret.testgo()

source=source.replace("\n","").replace(" ","")

class Computer():
    def __init__(self,source):
        self.mem={}
        self.inst=[]
        self.inst=textwrap.wrap(source,17)
        for x in self.inst:
            print(x)
        for x in range(64):
            i=bin(x)[2:].zfill(6)
            self.mem[str(i)]="00000000"
        for instruction in self.inst:
            self.process(instruction)
    def bincalc(self,op,p1,p2):
        s1=int(self.mem[p1],2)
        s2=int(self.mem[p2],2)

        decres=0
        match op:
            case "+":
                decres=s1+s2
            case "-":
                decres=s1-s2
            case "*":
                decres=s1*s2
            case "/":
                decres=s1/s2
            case "&":
                decres=s1&s2
            case "|":
                decres=s1|s2
            case "^":
                decres=s1^s2
                
        return str(bin(decres)).replace("b","").zfill(6)
    
    def process(self,inst):
        
        x="000110"
        l="000111"

        opcode=inst[0:5]
        p1=inst[5:11]
        p2=inst[11:17]

        match opcode:
            case "00001": # mov
                self.mem[p2]=self.mem[p1]
            case "01111": # stor
                self.mem[p1]=p2
            case "00010": # add
                self.mem[x]=self.bincalc("+",p1,p2)
            case "00011": # sub
                self.mem[x]=self.bincalc("-",p1,p2)
            case "00100": # mul
                self.mem[x]=self.bincalc("*",p1,p2)
            case "00101": # div
                self.mem[x]=self.bincalc("/",p1,p2)
            
            case "00111": # inc
                self.mem[p1]=str(bin(int(self.mem[p1],2)+int("000001",2))).replace("b","").zfill(6)
            case "00111": # dec
                self.mem[p1]=str(bin(int(self.mem[p1],2)-int("000001",2))).replace("b","").zfill(6)
            
            case "11000": # vid
                print(int(self.mem[p1],2))

            case "01010": # and
                self.mem[x]=self.bincalc("&",p1,p2)
            case "01011": # or
                self.mem[x]=self.bincalc("|",p1,p2)
            case "01100": # xor
                self.mem[x]=self.bincalc("^",p1,p2)

            case "01001": # inv
                res=""
                for x in self.mem[p1]:
                    if x=="1":
                        res+="0"
                    elif x=="0":
                        res+="1"
                self.mem[p1]=res
            
comp=Computer(source)