class CPU:
    def __init__(self, x):
        pass
class Memory:
    def __init__(self, x): 
        pass
class Hard_drive:
    def __init__(self, x): 
        pass
class Facade:
    def CheckCPU(x): 
        return CPU(x)
    CheckCPU = staticmethod(CheckCPU)
    def CheckMemory(x): 
        return Memory(x)
    CheckMemory = staticmethod(CheckMemory)
    def CheckHD(x): 
        return Hard_drive(x)
    CheckHD = staticmethod(CheckHD)
if __name__ == '__main__':
    a = Facade.CheckCPU("Intel Core i5")
    b = Facade.CheckMemory("Corsair 12GB ")
    c = Facade.CheckHD("HDD Blue 1TB")