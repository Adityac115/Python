file=input('Enter the full path to the file you want to open : ')
handle = open(file)
punctuations = '''!()-[];:'"\\,<>./?@#$%^&*_~'''

text_need=""
frequency_count={}
lines=handle.readline()
for char in lines:
    if char not in punctuations:
        text_need+=char
            
word_list=text_need.split()
    
    
for word in word_list:
        frequency_count[word]=frequency_count.get(word,0) + 1
        
print(frequency_count)