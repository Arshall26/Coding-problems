"""Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2]."""

"""Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0]."""

"""L'idée c de prendre le tableau inserer chaque element dans une chaine
   convertir la chaine en int -> faire +1 -> reconvertir en chaine
   inserer dans un tableau vide chaque caractere et c bon"""

def plusOne(digits):
    num = ""
    for i in digits:
         num +=str(i)
    num = int(num)
    num+=1
    num = str(num)
    ans = []
    for i in num:
         ans.append(int(i))
    return ans


def plusOne2(digits):
    return list(map(int, list(str(int(''.join(map(str, digits))) + 1))))


digits = [4,3,2,1]
digits2 = [9,9,9]
print(plusOne(digits))
print(plusOne2(digits2))

