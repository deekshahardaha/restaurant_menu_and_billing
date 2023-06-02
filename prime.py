# def primegenerator(a,b):
#     li=[]
#     while a<=b:
#         f=False
#         for i in range(2,a//2):
#             if a%i==0:
#                 f=True
#                 break
#         if f!=True:
#             li.append(a)
#             a+=2
#         else:
#             a+=1
#     return li

# def findc(a,b,c):
#     if c<b and c>a:
#         return True
        

# a=5 
# b=77
# c=65
# prime=primegenerator(a, b)
# print(prime)
# h=findc(a, b, c)
# print(h)

# def fucn(in1,in2):
#     val=set(in1).intersection(set(in2))
#     print(val)
#     sum=0
#     for i in val:
#         sum+=ord(i[0])
#     print(sum)
#     final=sum
#     while final>10:
#         temp=0
#         while sum>0:
#             temp+=sum%10
#             sum=sum//10
#         final=temp
#         sum=final
#     return final

# in1=['a','b','c']
# in2=['v','b','c']
# print(fucn(in1, in2))

ih=[]
ik=[1,2,3]
print(sum(ih))