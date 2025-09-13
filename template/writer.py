import json

class Writer:
    def __init__(self,name):
        self.data = [{"name":name}]
        return
    def append(self,key,value):
        self.data.append({key:value})
        return
    def save(self,name):
        with open(name,'w',encoding='utf-8') as file:
            json.dump(self.data,file,indent=4)
            return
if __name__ == "__main__":
    wt = Writer('test.xls')
    wt.append("test","A1")
    wt.save("test.json")