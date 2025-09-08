data=[]
result=0

for i in range(5):
    num=int(input("정수 입력 : "))
    data.append(num)
    result+=num

print(data)
print(f"평균 = {result/len(data)}")