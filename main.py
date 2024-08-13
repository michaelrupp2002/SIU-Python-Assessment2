
# Online Python - IDE, Editor, Compiler, Interpreter

def replace_spaces(sentence, char):
    newSentence = sentence.replace(' ',char)

    return (newSentence)

def max_values(numList):
    maxnum1 = 0
    maxnum2 = 0
    for num in numList:
        num = int(num)
        if num > maxnum2:
            maxnum1 = maxnum2
            maxnum2 = num
        elif num > maxnum1:
            maxnum1 = num
            
    return(maxnum1, maxnum2)    
    
def youngest_student(studentList):
    youngest = 1000
    youngestname = ''
    for name in studentList:
        if int(studentList[name]) < youngest:
            youngest = studentList[name]
            youngestname = name
        
    return youngestname


sentence = "Test  This is a test   Testing "
sentence2 = replace_spaces(sentence, "_")

print(sentence2)
print(max_values([4, 7, 2, 8, 10, 9]))

students = {"Alice": 19, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student(students))
