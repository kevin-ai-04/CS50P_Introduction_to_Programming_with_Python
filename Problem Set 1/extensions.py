name=input("File Name: ")
name=name.lower().strip()

if name.endswith(".jpg") or name.endswith(".jpeg"):
    type="image"
    name="jpeg"
elif name.endswith(".png"):
    type="image"
    name="png"
elif name.endswith(".gif"):
    type="image"
    name="gif"
elif name.endswith(".pdf"):
    type="application"
    name="pdf"
elif name.endswith(".txt"):
    type="text"
    name="plain"
elif name.endswith(".zip"):
    type="application"
    name="zip"
else:
    type="application"
    name="octet-stream"

print("The MIME Type is: ",type,"/",name,sep='')