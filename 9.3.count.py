filehandle=open('words.txt')
string=filehandle.read()
List=string.split()
diction={}
for everyone in List:
    diction[everyone]=diction.get(everyone,0)+1
bigcount=None
bigword=None
for word,count in diction.items():
    if bigcount is None or count > bigcount:
        bigword=word;
        bigcount=count;
print(bigword,bigcount)
# for key in diction:
#     print(key,diction[key])
# for k,v in diction.items():
#     print(k,v)
