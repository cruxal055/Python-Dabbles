import urllib.request

retriever = urllib.request.urlopen("https://www.ics.uci.edu/~thornton/ics32a/Notes/HTTP/")
data = retriever.read()
retriever.close()
str_data = data.decode("utf-8")
list_of_data = str_data.split('/n')
for x in list_of_data:
    print(x)
