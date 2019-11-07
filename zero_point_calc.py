import numpy as np





def main():

    band= raw_input("Which band are you observing in?")
    airmass= float(input("What airmass is your object at?"))
    data= raw_input("What is the name of your data file?")
    filein= open(data, "r")
    counts=[]
    speccount=[]
    am=[1.02,1.15,1.7]
    

    for line in filein.readlines():
        if not line.startswith("#"):
            counts.append(float(line))
    filein.close()

    if band in ['u','U']:
        for i in range(0,2):
            speccount.append(3*i)

    elif band in ['g','G']:
        for i in range(0,2):
            speccount.append((3*i)+1)
        
    else:
        for i in range(0,2):
            speccount.append((3*i)+2)

    def zeropoint(speccount,am,airmass,):
        xbar= np.mean(am)
        ybar= np.mean(speccount)
        numerator= 0.0
        denominator= 0.0
        for i in range(0,len(speccount)):
            num=((speccount[0]-xbar)*(am[0]-ybar))
            den=(speccount[0]-xbar)**2
            numerator += num
            denominator += den
        m= numerator/denominator
        c= ybar -(m*xbar)
        zp= (m*airmass)+c
        return(zp)

    output= zeropoint(speccount,am,airmass)
    print(output)

main()
            
            
        
