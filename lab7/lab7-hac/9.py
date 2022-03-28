if __name__ == '__main__':
    d={} #1
for _ in range(int(raw_input())): 
    Name=raw_input() 
    Grade=float(raw_input()) 
    d[Name]=Grade 
v=d.values()#6
second=sorted(list(set(v)))[1] 
second_lowest=[] 
for key,value in d.items():  
    if value==second: 
        second_lowest.append(key) 
second_lowest.sort() 
for name in second_lowest: 
    print name 
        
