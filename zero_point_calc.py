import numpy as np





def main():

    band= raw_input("Which band are you observing in?")
    airmass= float(input("What airmass is your object at?"))
    data= raw_input("What is the name of your data file?")
    errdata= raw_input("What is the name of your errors file?")
    filein= open(data, "r")
    filein2= open(errdata, "r")
    errcounts=[]
    counts=[]
    speccount=[]
    errspeccount=[]
    am=[1.02,1.15,1.7]
    

    for line in filein.readlines():
        if not line.startswith("#"):
            counts.append(float(line))
    filein.close()

    for line in filein2.readlines():
        if not line.startswith("#"):
            errcounts.append(float(line))
    filein.close()

    if band in ['u','U']:
        for i in range(0,3):
            x= counts[3*i]
            ex= errcounts[3*i]
            speccount.append(x)
            errspeccount.append(ex)

    elif band in ['g','G']:
        for i in range(0,3):
            x= counts[(3*i)+1]
            ex= errcounts[(3*i)+1]
            speccount.append(x)
            errspeccount.append(ex)
            
        
    else:
        for i in range(0,3):
            x= counts[(3*i)+2]
            ex= errcounts[(3*i)+2]
            speccount.append(x)
            errspeccount.append(ex)

#Here we are converting instrumental counts and errors on counts, into appropriate zeropoints (using accepted values for standard star magnitudes), and an error on the zero point due to the error on the counts,then each calculated zp and error is set to be the same list element it was when it was a count

    c= (2.5/np.log(10))
    x= 15+(c*np.log(speccount[0]))
    y= 12+(c*np.log(speccount[1]))
    z= 15+(c*np.log(speccount[2]))
    ex= (errspeccount[0])*(c/speccount[0])
    ey= (errspeccount[1])*(c/speccount[1])
    ez= (errspeccount[2])*(c/speccount[2])
    speccount[0]=x
    speccount[1]=y
    speccount[2]=z
    errspeccount[0]=ex
    errspeccount[1]=ey
    errspeccount[2]=ez

    def zeropoint(speccount,am,airmass,errspeccount):
        xbar= np.mean(am)
        ybar= np.mean(speccount)
        errybar= (1/3)*((errspeccount[0])**2 + (errspeccount[1])**2 +(errspeccount[2])**2)**0.5
        numerator= 0.0
        denominator= 0.0
        for i in range(0,len(speccount)):
            num=((speccount[0]-ybar)*(am[0]-xbar))
            den=(am[0]-xbar)**2
            numerator += num
            denominator += den
        m=numerator/denominator
        c=ybar -(m*xbar)
        zp=(m*airmass)+c
        a1=(am[0]-xbar)
        a2=(am[1]-xbar)
        a3=(am[2]-xbar)
        errm=(1/denominator)*((errybar*(-a1-a2-a3))**2 + (errspeccount[0]*a1)**2 + (errspeccount[1]*a2)**2 + (errspeccount[2]*a3)**2)**0.5
        errzp=errm*airmass
        return(zp,errzp)

    output= zeropoint(speccount,am,airmass,errspeccount)
    print(output)

main()
            
            
        
