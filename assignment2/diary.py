# task 1
import traceback
try:
    with open('diary.txt', 'a') as file:
        pr= "What happened today? "
        line = input(pr)
        file.write(line+'\n')
        print(line)
        while line!="done for now": 
            pr= "What else?"
            line = input(pr)
            print(line)
            file.write(line+'\n') 
except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = list()
   for trace in trace_back:
      stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
      print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")