#1
import re
emails = "zuck26@facebook.com" "page33@google.com" "jeff42@amazon.com"
pattern = r'([\w]{1,20}[\w]{1,20})[@]([\w]{1,9})[.]([\w]{1,3})'
print(re.findall(pattern, emails, flags = re.IGNORECASE))


#2
import re
text = "Betty bought a bit of butter,But the butter was so bitter,So she bought some better butter,To make the bitter butter better."
print(re.findall(r'\bB\w+', text, flags = re.IGNORECASE))


#3
import re
sentence = "A, very very: irregular_sentence"
print("".join(re.split('[:,\n]+', sentence)))