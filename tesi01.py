class student:
    name="宋自杰"
    age=24
    score=[12,33,50]
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_course(self):
        return max(self.score)
    def __str__(self):
        print("查看我的西南西")
# s1=student("xxx",20,[11,22,33])
# print(s1.get_age(),s1.get_name(),s1.get_course())
# print(student.score)
class dictcalss:
    def __init__(self,dict1):
        self.dict1=dict1
    def del_dict(self,key):
        del self.dict1[key]
    def get_dict(self,key):
        try:
            return self.dict1[key]
        except:
            return "没找到"
    def get_key(self):
        return list(self.dict1.keys())
    def update_dict(self,*dict):
        for i in dict:
            self.dict1.update(i)

# d1=dictcalss({"姓名":"宋自杰","年龄":23,"性格":"一般"})
# print(d1.get_key(),type(d1.get_key()))
# print(d1.get_dict("姓名"))
# d1.update_dict({"a":1,"B":2},{"c":1,"d":2})
# print(d1.get_key())
class Listinfo:
    def __init__(self,lsit1):
        self.list1=lsit1
    def add_key(self,keyname):
        self.list1.append(keyname)
    def get_key(self,num):
        return self.list1[num]
    def update_list(self,list2):
        self.list1.extend(list2)
    def del_key(self):
        return self.list1.pop()
    def look_list(self):
        return self.list1
# l1=Listinfo([44,222,111,333,454,'sss','333'])
# l1.add_key("宋自杰")
# print(l1.get_key(2))
# print(l1.del_key())
# l1.update_list(["ggg","hhh"])
# print(l1.look_list())
class Setinfo:
    def __init__(self,set1):
        self.set1=set1
    def add_setinfo(self,keyname):
        self.set1.append(keyname)
    def get_intersection(self,unioninfo):
        return self.set1&unioninfo
    def get_union(self,unioninfo):
        return self.set1|unioninfo
    def del_difference(self,a):
        return self.set1-a
    def buji(self,a):
        return self.set1^a
    def get_set1(self):
        return self.set1
s1=Setinfo({"1",1,"3","3"})
print(s1.get_set1())
print(s1.buji({"1"}))