class Rules:
    def __init__(self, vals):
        self.vals = vals
    
    def updateAlive(self, count):
        match self.vals.RULE_SET:
            case 1:
                if count == 3:
                    return True
            case 2:
                if count == 1 or count == 3:
                    return True
            case 3:
                if count == 2 or count == 3:
                    return True
            case 4:
                if count == 3 or count == 4:
                    return True
            case 5:
                if count == 3 or count == 5:
                    return True
            case 6:
                if count == 2 or count == 3 or count == 6:
                    return True
            case 7:
                if count == 1 or count == 3 or count == 5:
                    return True
            case 8:
                if count < 0 and count > 6:
                    return True
            case 9:
                if count == 1 or count == 3 or count == 5 or count == 7:
                    return True
            case 10:
                if count == 2 or count == 4:
                    return True
            case 11: 
                if count < 4:
                    return True
            case _:
                return False
    def updateDead(self, count):
        match self.vals.RULE_SET:
            case 1:
                if count == 3:
                    return True
            case 2:
                if count == 3:
                    return True
            case 3:
                if count == 3:
                    return True
            case 4:
                if count == 3:
                    return True
            case 5:
                if count == 3:
                    return True
            case 6:
                if count == 3:
                    return True
            case 7:
                if count == 3 or count == 5:
                    return True
            case 8:
                if count == 3:
                    return True
            case 9:
                if count == 1 or count == 3 or count == 5 or count == 7:
                    return True
            case 10:
                if count == 3 or count == 5:
                    return True
            case 11:
                if count < 5:
                    return True
            case _:
                return False

