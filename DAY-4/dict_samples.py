# def new_dict():
#     d={}
#     print(d)
# def add_items_in_dict():
#     d={'apples':30,"banana":50}
#     print(d)
# def nested_dict():
#     d={'drinks':{'coke':20,'pepsi':35}}
#     print(d['drinks'])
# def zipped_dict():
#     l1=['name','age','class']
#     l2=['sid',21,10]
#     d=dict(zip(l1,l2))
#     print(d)#
def main():
    # print("another way to create dictionary is :\n")
    # d=dict(age=18,classes=10)
    d={'sub A':75,'sub b':60,'sub c':85}
    d1={'abc':2,'sdgs':3}
    d1.update(d)
    print(d1)
    print(d.items())
    x=d.copy()
    print(x)
    print(d.get('sub A'))
    print(d.pop('sub b'))
    print(d)
    print(len(d))
    # new_dict()
    # add_items_in_dict()
    # nested_dict()
    # zipped_dict()
main()
