student ={}
#insert an element 
student['name']='khushi aggarwal'
student['roll']=1024
student['hindi']=45
#insert another element
student ['english']=56
student['hindi']=67
print(student)
for key in student :
    print("key",key,"value",student[key])
#keys() to return all the keys in a dictionary
print("keys are:",student.keys())
#it helps to find 
print(student.get('address','not found'))
student.pop('hindi')    
print(student)