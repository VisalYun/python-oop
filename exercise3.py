'''
    Create a class call SuperList that has the same power as python list except for len method you need to return 1000 no matter what
'''
class SuperList(list):
    def __len__(self):
        return 1000

list = SuperList()
list.append(500)
print(list)
print(f"List length: {len(list)}")