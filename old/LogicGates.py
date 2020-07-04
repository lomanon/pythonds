class LogicGate:
    def __init__(self,n):
        self.label = n
        self.output = None

    def GetLabel(self):
        return self.label

    def GetOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pinA = None
        self.pinB = None

    def GetPinA(self):
        if self.pinA is None:
            return int(input("Enter Pin A for Gate {} -->".format(self.GetLabel())))
        else:
            return self.pinA.getFrom().GetOutput()

    def GetPinB(self):
        if self.pinB is None:
            return int(input("Enter Pin B for Gate {} -->".format(self.GetLabel())))
        else:
            return self.pinB.getFrom().GetOutput()

    def setNextPin(self, source):
        if self.pinA == None:
            self.pinA = source
        elif self.pinB == None:
            self.pinB = source
        else:
            raise RuntimeError("Error - NO EMPTY PINS")

class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None

    def GetPin(self):
        if self.pin is None:
            return int(input("Get Pin for Gate {} -->".format(self.GetLabel())))
        else:
            return self.pin.getFrom().GetOutput()

    def setNextPin(self,source):
        if self.pin is None:
            self.pin = source
        else: raise RuntimeError("Unary gate has no empty pins")


class AndGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        # super(BinaryGate,self).__init__(n)

    def performGateLogic(self):
        a = self.GetPinA()
        b = self.GetPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.GetPinA()
        b = self.GetPinB()

        if a == 1 or b == 1:
            return 1
        else:
            return 0

class XorGate(BinaryGate):
    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):
        a = self.GetPinA()
        b = self.GetPinB()

        if (a == 1 and b == 0) or (b == 1 and a == 0):
            return 1
        else:
            return 0

class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.GetPin()
        if a == 1:
            return 0
        else:
            return 1


class NandGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)
        # super(BinaryGate,self).__init__(n)

    def performGateLogic(self):
        a = self.GetPinA()
        b = self.GetPinB()
        if a == 1 and b == 1:
            return 0
        else:
            return 1

class NorGate(BinaryGate):
    def __init__(self, n):
        BinaryGate.__init__(self, n)

    def performGateLogic(self):
        a = self.GetPinA()
        b = self.GetPinB()

        if a == 1 or b == 1:
            return 0
        else:
            return 1


class Connector:

    def __init__(self,fgate,tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

class InputConnector:
    def __init__(self,g1,g2):
        self.gate_1 = g1
        self.gate_2 = g2

    gate_2.setNextPin()

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1,g2)
c2 = Connector(g2,g3)
c2 = Connector(g3,g4)

print(g4.GetOutput())

# Make a half-adder

h1 = XorGate("H1")
h2 = AndGate("H2")
