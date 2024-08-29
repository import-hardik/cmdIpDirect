import subprocess
def isnext_adapter():
    if result.find("IPv4 Address. . . . . . . . . . . : ")!=-1:
        return 1
    else:
        return 0
print("This PC -->\n")
result = subprocess.run(['ipconfig'], capture_output=True, text=True)
result=str(result)
print("IP:\t",end="")
i=0
while(isnext_adapter()):
    i+=1
    first=result.find("IPv4 Address. . . . . . . . . . . : ")
    #print(first)
    print(result[first+36:first+result[first:].index("Subnet Mask")-5],end="\n\t")
    #print(result[first:first+result[first:].index("Subnet Mask")-5])
    result=result.replace(result[first:first+result[first:].index("Subnet Mask")-5],"")
input(f'\n\t{i} IPs Found...')
