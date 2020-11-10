def LinearRegressor(data,d):
    w=[0]*len(data[0])
    dw=[0]*len(w)
    e=0
    it=float(input('Enter the iterations: '))
    damp_decay=float(input('Enter the Damping Decay: '))
    i=0
    while i<=it:
        if i==it-1:
            print('Predicted   Original')
            print('---------   --------')
        for j in range(len(data)):
            pred=0
            for k in range(len(w)):
                if k!=len(w)-1:
                    pred=pred+data[j][k]*w[k]
                else:
                    pred=pred+w[-1]
                    
            if i==it-1:
                print(pred,data[j][-1],sep='   ')
            
            for k in range(len(w)):
                if i==it-1:
                    t=pred-data[j][-1]
                    e=e+((t**2)**(1/2))
                if k!=len(w)-1:
                    dw[k]=d*(pred-data[j][-1])*data[j][k]
                else:
                    dw[k]=d*(pred-data[j][-1])
                    
            for k in range(len(w)):
                w[k]=w[k]-dw[k]        
            
        d=d/damp_decay
        i=i+1
    return w,e
    
def readData(fileName):
    f=open(fileName,'r')
    data=[]
    attr=f.readline().split(',')
    attr=attr[:-1]
    temp=f.readline()
    while 'eof' not in temp:
        temp=temp[:-1]
        ttemp=temp.split(',')
        data.append(ttemp)
        temp=f.readline()
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j]=float(data[i][j])
    
    f.close()
    return data,attr    
    
def main():
    fileName=input('Enter the file name with path :')
    data,attr=readData(fileName)
    d=float(input('Enter the Damping Coefficient: '))
    print()
    wt,e=LinearRegressor(data,d)
    print('\n\n')
    print('The best fitted line is: y = ',end='')
    for i in range(len(wt)):
        if i!=len(wt)-1:
            print(wt[i],'*',attr[i],' + ',end='')
        else:
            print(wt[i],' with error ',e,' units ')
    print('\n\nFor accuracy,try changing minimizing Damping coefficient.') 
    input()
    
    
main()