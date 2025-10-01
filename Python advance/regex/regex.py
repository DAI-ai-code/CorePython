import re


tr = "Hello all world my phone number is 1234567890 and my roll number is 1234 and my email id is abc@def.com"
text = ("Hello all world my phone number is 1234567890 and my roll number is 1234 and my email id is ab1c@def.com and also@d .com @abc.com")

print(re.findall(r"[a-zA-Z]+[@][a-zA-Z]+[.][a-zA-Z]+", text))


# print(re.search(r"\d{10}", text))
#
# print(re.findall(r"\d+", text))