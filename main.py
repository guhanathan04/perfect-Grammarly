# Python3 code to demonstrate
# removal of unwanted_chars
# using replace()

# initializing bad_chars_list
import emoji
import itertools
import re
unwanted_chars = [';', ':', "*",'/','$','#','=','+','%','^','_','~',"`",'<',">"]
replace_chars=['@','&']

# initializing test string
test_string = "Gu;ha*n: @ s=r$ira*m pl+ay:s; Cr*ic%ke=^t_~💕👭 & @ B$o🙈th o%f t*he_m a~r`e g+o=o$#d😌 good, , ,f<r/ie*n_d~😂s? ??? ??"

# printing original string
print ("Original String : " + test_string)

# using replace() to
# remove unwanted_chars
for i in unwanted_chars :
    test_string = test_string.replace(i, '')
    for j in replace_chars:
         test_string = test_string.replace(j, 'and')
#After Punctuation and replace
print("\nAfter Removing Special Charcaters : ",test_string)
            
#For emoji removal
p=emoji.get_emoji_regexp().sub(r'', test_string)
print("\nAfter Emoji Removal : ",p)

#For Reduantact words
t=re.sub(r'\b(\w+\W*)\1{1,}','\\1',p)
print("\nNormal sentence : ",t)

s = re.sub('([.,!?()])', r' \1 ', t)
q= re.sub('\s{2,}', ' ', s)
a= ' '.join(k for k, _ in itertools.groupby(q.split()))
b=re.sub(r'\s([?,.!"](?:\s|$))', r'\1', a)
print("\nPerfect Sentence :",b)
