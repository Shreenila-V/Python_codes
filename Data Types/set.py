#access a set
application={"name","roll no","age",21}
print('apllication details:',application)

#empty set
application=set()
print('application details',application)

#duplicate elements are not supported in set
application={1,1,2,3,4}
print(application)

#add
application={1,2,3,4,5}
(application.add(6))
print("the updated list",application)

#update
application={1,"name","roll no","reg no"}
application_1=[2,"name","roll no","reg no"]
application.update(application_1)
print(application)

#remove,discard()
application={1,"name","roll no","reg no"}
print("before discard",application)
application_1=application.discard("name")
print("after discard",application)

#loop
application={1,"name","roll no","reg no"}
for applications in application:
    print(applications)







