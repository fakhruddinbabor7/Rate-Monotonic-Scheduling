import random

#finding LCM
def find_lcm(num1, num2): 
    if(num1>num2): 
        num = num1 
        den = num2 
    else: 
        num = num2 
        den = num1 
    rem = num % den 
    while(rem != 0): 
        num = den 
        den = rem 
        rem = num % den 
    gcd = den 
    lcm = int(int(num1 * num2)/int(gcd)) 
    return lcm 
    
#   implementtaion for rate monotonic scheduling  
def tasktable(task,num,lcm,SC):
    timetable=[]
    timeclock=[]
    sc=1

    #creating timeclock
    for i in range(0,lcm):
        timetable.append(0)
        timeclock.append(i+1)
        
    ##numsl captures how much execution time needed for its execution within a hyperperiod     
    numsl=[]
    for x in range(0,len(task)):
        numsl.append(task[x][0]*(lcm/task[x][1]))
        
    # timeperiods captures arriaval time of each task within a hyperperiod    
    timeperiods=[]
    for i in range(0,num):
         n=[]
         for a in range(0,lcm):
            if(a%task[i][1]==0):
                  n.append(a)
         timeperiods.append(n)
         
    #print(timeclock)
    #print(timetable)
    print(numsl)
    print(timeperiods)
    
    #pushing each task in the timetable according to priority
    l=len(timeperiods)
    for i in range (l):
        tas=i
        #p=i
        m=len(timeperiods[i])
        for j in range (m):
            c=task[i][0]
            per=task[i][1]
            s=timeperiods[i][j]
            ns=s+per
            if(s>lcm):
                break
            if(s==lcm):
                break
            while c!=0:
                if(s==ns):
                    sc=0
                    break
                if(s>lcm):
                    break
                if(s==lcm):
                    break
                if (timetable[s]==0):
                    timetable[s]=tas+1
                    s=s+1
                    c=c-1
                else:
                    s=s+1

    print(timetable)
    #SC.append(sc)



SC=[] 
n=int(input("Enter number of tasks: "))
#n=random.rand(2,10)
task=[]
print("Enter Execution time and Period of tasks")
for i in range(0,n):
    pair=[]
    inp1=input()
    c,t=map(int,inp1.split(','))
    #c=random.randint(2,6)
    #t=random.randint(12,50)
    pair.append(int(c))
    pair.append(int(t))
    task.append(pair)

#sorting task following priority
task.sort(key=lambda x:x[1])
u=0
num1 = task[0][1] 
num2 = task[1][1]
lcm = find_lcm(num1, num2) 
  
for i in range(2, len(task)): 
    lcm = find_lcm(lcm, task[i][1]) 
      
for i in range(0,n):
    u=u+(task[i][0]/task[i][1])
u= round(u, 2)    
print('utilization is:', u)

#U is to check schedulability gurantee
U=((n*((2**(1/n))-1)))

if(u<1):
    if(u<=(n*((2**(1/n))-1))):
        print('Scheduling is guaranteed as utilization', u ,"less than ", U)
        tasktable(task,n,lcm,SC)
    else:
        print('Scheduling is guaranteed as utilization', u ,"greater than ", U)
        tasktable(task,n,lcm,SC)       
else:
    print('Scheduling not possible as utilization ', u ,"greater than 1")
    
