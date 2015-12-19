with open("inputs\problem13.txt") as f:
    contents = f.readlines()
contents = [x.strip('\n') for x in contents]
contents = [''.join(x) for x in contents]
contents = [int(x) for x in contents]
result = sum(contents)
print(str(result)[:10])
