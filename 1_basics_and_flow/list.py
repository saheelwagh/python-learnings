#list contains many values in a sequence
#negative indices refer from last
spam = ['cat', 'bat', 'rat', 'elephant']
a= spam[:2]
b= spam[1:]
print(len(spam))
print(len(a))
print(len(b))
spam = spam + ['dog', 'hog', 'giraffe']
print(spam)
del(spam[2])
print(spam)
cats = []
while True :
    print('Enter cat name: ')
    name = input()
    if name==' ' : 
        break
    cats = cats + [name]
print('Cat names are : ')
for i in cats:
    print(i)
#to search :
print()
print('Enter cat\'s name to search')
for name in range(len(cats)):
    if name not in cats :
        print("Cat not found")
    else :
        print(name +' is my cat in position: ' + cats.index(name))
languages = ['python', 'javascript', 'solidity']
py,js, sol = languages
lang1,lang2 = 'js', 'python'
lang1,lang2= lang2,lang1
languages.append('c')
languages.insert(2, 'c++')
try :
    languages.remove('c++')
except:
    print('language no longer exists')
sorted_languages = languages.sort()