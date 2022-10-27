import json
about_me='''
{
'name':'bagrat
'age':14
'hobby':none
}
'''

with open('pipi.json','w') as file:
    json.dump(about_me,file)

with open('pipi.json','r')as file:
    a=json.load(file)
print(a)