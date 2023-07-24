import textwrap,sys,math

with open(sys.argv[1],"rb") as source:
    source=source.read().decode('ascii').replace("\n","")

class Computer():
    def __init__(self,source):
        self.mem={}
        self.inst=[]
        self.inst=textwrap.wrap(source,17)
        for x in range(64):
            i=bin(x)[2:].zfill(6)
            self.mem[str(i)]="00000000"
        for instruction in self.inst:
            self.process(instruction)
        print("Printing changed memory adresses:")
        for key,val in self.mem.items():
            if val!="00000000":
                tp=""
                match key:
                    case "000001":
                        tp="A"
                    case "000010":
                        tp="B"
                    case "000011":
                        tp="C"
                    case "000100":
                        tp="D"
                    case "000101":
                        tp="E"
                    case "000110":
                        tp="X"
                    case "000111":
                        tp="L"
                    case _:
                        tp=key
                print(f"Address {tp}: {val}")
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
                decres=math.floor(s1/s2)
            case "&":
                decres=s1&s2
            case "|":
                decres=s1|s2
            case "^":
                decres=s1^s2
        x=str(bin(decres)).replace("b","")
        if len(x)==7:
            return x[1:]
        else:
            return x.zfill(6)
        # return str(bin(decres)).replace("b","").zfill(6)
    
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