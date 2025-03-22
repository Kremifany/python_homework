# Task 1
def hello ():
    return "Hello!"
# Task 2
def greet (name):
    return f"Hello, {name}!"
# Task 3
def calc (first, second, operator="multiply"):
    try: 
        match operator:
            case "multiply": return first * second
            case "add": return first + second
            case "subtract": return first - second
            case "divide": 
                if second == 0:
                    return "You can't divide by 0!"
                else:
                    return first / second
            case "modulo": return first % second
    except Exception as e:
        return "You can't multiply those values!"
# Task 4    
def data_type_conversion(value, data_type):
    try:
        match data_type:
            case "float":
                return float(value)
            case "int":
                try:
                    return int(value)
                except ValueError:
                    return f"You can't convert {value} into a int."
            case "str":
                    return str(value)
    except Exception as e:
        return f"You can't convert {value} into a {data_type}."

print(data_type_conversion("banana", "int"))
# Task 5    
def  grade (*args):
    try: 
        sum = 0
        for arg in args:
           sum+=arg
        match sum:
            case sum if sum/len(args) > 90 :
                return 'A'
            case sum if 80 <= sum/len(args) < 90 :
                return 'B'
            case sum if 70 <= sum/len(args) < 79 :
                return 'C'
            case sum if 60 <= sum/len(args) < 69 :
                return 'D'
            case sum if sum/len(args) < 60 :
                return 'F'
            case _:
                return "Invalid input"
    except Exception as e:
        return "Invalid data was provided."
    
print(grade(75,85,95))
# Task 6
def repeat(string,count):
    result = ""
    for i in range (count):
        result+=string
        count-1
    return result
# Task 7
def student_scores (param, **kwargs):
    if not kwargs:
        return None
    if(param == "mean"):
        sum=0
        for key, value in kwargs.items():
            sum+=value
        return sum/len(kwargs)
    elif(param=="best"):
        maxValue = 0
        maxKey = None
        print(kwargs.items())
        for key, value in kwargs.items():
            print(value)
            if value > maxValue:
                maxValue = value
                maxKey = key
        return maxKey
# Task 8
def titleize(title: str):
    words = title.split()
    return " ".join(
        word if word in ["a", "on", "an", "the", "of", "and", "is", "in"] 
        and index != 0
        and index != len(words) - 1
        else word.capitalize()
        for index, word in enumerate(words)
    )
# Task 9
def hangman(secret, guess):
    return "".join(
        letter  if letter in guess
                else "_"
        for letter in secret
    )
# Task 10
def pig_latin(input):
    output = ''
    for word in input.split(): 
        i=0
        while word[i] not in  ['a','e','i','o','u'] :
            i = i+1
        if word[i-1:i+1] =='qu':
            output+=word[i+1:]+word[:i+1]+'ay'
        else:
            output+=word[i:]+word[:i]+'ay'
        output+=' '
    return output[:-1]
print(pig_latin("the quick brown fox"))

