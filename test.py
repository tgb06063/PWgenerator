list=[]
names=[]
temp_names=[]
phoneNo=''
dob=input("생년월일(ENG)(YYMMDD)(필수):")
if(len(dob)==6):
    year=dob[:2]
    month=dob[2:4]
    day=dob[4:]
else:
    print("틀린 양식입니다. YYMMDD에 맞춰 6자로 완성하시오.")
    exit()

phoneNo=input("전화번호(-빼고 작성):")

def ListOfImportantWords():
    names.append(input("성(ENG):"))
    names.append(input("이름(ENG):"))
    names.append(input("별명(ENG):"))
    names.append(input("나라(영어):"))
    names.append(input("지역(영어):"))
    names.append(input("좋아하는 색(영어):"))
    names.append(input("아무단어(ENG):"))
    print("아무키나 눌러주세요: ")
    while True:
        inp = input()
        if inp == '':
            break
        names.append(inp)
    while('' in names) : 
        names.remove('') 

def permute(inp): 
    n = len(inp) 
   
    mx = 1 << n 
   
    inp = inp.lower() 
      
    for i in range(mx): 
        combination = [k for k in inp] 
        for j in range(n): 
            if (((i >> j) & 1) == 1):
                combination[j] = inp[j].upper() 
   
        temp = "" 
        for i in combination: 
            temp += i 
        temp_names.append(temp) 



def WordListCreator(list):
    for word in names:
        for i in range(0,len(word)+1):
            list.append(word[:i]+day+word[i:])
            list.append(word[:i]+month+word[i:])
            list.append(word[:i]+year+word[i:])
            list.append(word[:i]+phoneNo[3:7]+word[i:])
            list.append(word[:i]+phoneNo[7:]+word[i:])
    if not phoneNo=='':
        list.append(phoneNo)

def WriteToFile(list):
    with open('wordlist.txt', 'w') as f:
        for item in list:
            if len(item) >= 8:
                f.write("%s\n" % item)
            else:
                pass



ListOfImportantWords()
for i in names:
    permute(i)       
names=names+temp_names
WordListCreator(list)
WriteToFile(list)

