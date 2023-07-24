import re
class SyntaxError(Exception):
    pass

class Converter():
    def __init__(self,source: list):
        """Source - line-seperated list"""
        self.source=source
        self.machine=""
        self.line=-1 # Zero-indexed
        self.regdict={
            "A": "000001",
            "B": "000010",
            "C": "000011",
            "D": "000100",
            "E": "000101",
            "X": "000110",
            "L": "000111"
        }
        self.registers=self.regdict.keys()
    def __str__(self):
        return self.machine
    def reg(self,strs):
        if strs not in self.registers:
            raise SyntaxError(f"Parameter {strs} is not recognised as a valid register.")
        else: 
            return self.regdict[strs]
    def RegOrMem(self,strs):
        m=re.search("[0-1]{6}",strs)
        if strs in self.registers:
            return self.regdict[strs]
        elif m.group(0)==strs:
            return strs
        else:
            raise SyntaxError(f"Parameter {strs} is not recognised as a valid register.")
        
    def num(self,strs):
        try:
            int(strs)
            if int(strs)>31: 
                return str(bin(int(strs))).replace("b","")[1:]
            return str(bin(int(strs))).replace("b","").zfill(6)
        except:
            raise SyntaxError(f"Parameter {strs} is not recognised as a valid number.")
    def none(self):
        return "000000"
    def go(self):
        for line in self.source:
            self.step()
        self.line=-1
        return self.machine
    def step(self):
        self.line+=1
        SpaceSeperated=self.source[self.line].split(" ")
        params=SpaceSeperated[1].split(",")
        p1=params[0]
        if len(params)!=1:
            p2=params[1]
        op=SpaceSeperated[0]
        match op:
            case "add":
                self.machine+="00010"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)
            case "sub":
                self.machine+="00011"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)
            case "mul":
                self.machine+="00100"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)
            case "div":
                self.machine+="00101"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)

            case "inc":
                self.machine+="00111"
                self.machine+=self.reg(p1)
                self.machine+=self.none()
            case "dec":
                self.machine+="01000"
                self.machine+=self.reg(p1)
                self.machine+=self.none()  
            
            case "inv":
                self.machine+="01001"
                self.machine+=self.reg(p1)
                self.machine+=self.none()  

            case "and":
                self.machine+="01010"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)
            case "or":
                self.machine+="01011"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)
            case "xor":
                self.machine+="01100"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)

            case "cmp":
                self.machine+="01101"
                self.machine+=self.reg(p1)
                self.machine+=self.reg(p2)

            case "stor":
                self.machine+="01111"
                self.machine+=self.reg(p1)
                self.machine+=self.num(p2)

            case "vid":
                self.machine+="11000"
                self.machine+=self.reg(p1)
                self.machine+=self.none()
            
            case "mov":
                self.machine+="00001"
                self.machine+=self.RegOrMem(p1)
                self.machine+=self.RegOrMem(p2)
            case _:
                raise SyntaxError(f"Invalid opcode {op}")
        self.machine+="\n"


mine= \
"""stor A,45
vid A
inv A
vid A"""
test=Converter(mine.split("\n"))
def testgo():
    return test.go()
if __name__=="__main__":
    print(testgo())