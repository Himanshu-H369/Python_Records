def palindrome(num):
    n=num
    reverse=0
    while num!=0:
        reverse=(reverse*10)+num%10
        num//=10
    return n==reverse

num=int(input('Enter a number: '))
ans=palindrome(num)
if ans:
    print('Number is Palindrome',num)
else:
    print('Number is not a Palindrome',num)