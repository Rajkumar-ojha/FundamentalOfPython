words_upto_19=["","one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
words_for_tens=["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
n=int(input("enter a digit from 0 to 99:"))
output=("")
if (n==0):
    output="zero"
elif(n<=19):
    output=words_upto_19[n]
elif(n<=99):
    output=words_for_tens[n//10]+""+words_upto_19[n%10]
else:
    output="plz enter a valid value from 0 to  99 only"
print(output)




