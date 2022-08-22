class AI_Task:


    # -_-

    # def removeChar(self, str, target):
    #     return str.replace(target, "")

    # -_-

    def removeChar(self, str, target):        
        result = ""
        for c in str:
            if c != target: result += c
            else: result += ""

        return result

    def findPrimNum(self, f, t):

        prim_numbers_list = []
        f = 2 if f < 2 else f

        for n in range(f, t):
            # check if the number will give me a whole number by dividing it on a range of numbers if not its a prime number
            for i in range(2, int(n/2)+1):
                if (n % i) == 0:
                    break
            else:
                prim_numbers_list.append(n)
                
        return prim_numbers_list

    # It's Case Sensitive sry :(
    def removeRepeatedChar(self, str):
        chars = { c : 1 for c in str }
        isDone = { c : False for c in str }

        for i in range( 0, len(str) - 1 ):
            for j in range( i + 1, len(str) - 1 ):
                if str[i] == str[j]:
                    if isDone[str[i]] == False:
                        chars[str[i]] += 1
            isDone[str[i]] = True
        
        mostRepeated = max(chars, key=chars.get)

        return mostRepeated

        

ai = AI_Task()

print(ai.removeChar("AbuAlhassan", "A"))
print(ai.findPrimNum(0, 1000))
print(ai.removeRepeatedChar("abualhassan"))