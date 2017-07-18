# Double line dislocation
print('==========Data as per perfect lattice even number only==========')
h=int(input('Horizontal number of hexagon:'))                      #h=18
v=int(input('Vertical number of hexagon:'))                        #v=14
print('==========Data for bottom dislocation==========')
x1=int(input('Targeted hexagon#  from left in bottom row:'))  #x1=14
y1=int(input('Position of pentagon in hexagon(odd#) from bottom:')) #y1=9
print('==========Data for top dislocation==========')
x2=int(input('Targeted hexagon# from left in top row:'))     #x2=5
y2=int(input('Position of pentagon in hexagon(even#) from top:'))  #y2=6
# Atom number calculation
tar1=y1
tar2=y2+1
atomno=[]
vv=list(range(1,v+2))
for li in vv:
    if li==1:
        num1=h*2+2
    else:
        if tar1==tar2:
            num1=h*2+atomno[li-2]
        elif tar1>tar2:
            if li<tar2:
                num1=h*2+atomno[li-2]
            elif li==tar2:
                num1=h*2+atomno[li-2]-1
            elif li==tar1:
                num1=h*2+atomno[li-2]-1
            elif li>tar1:
                num1=h*2+atomno[li-2]
            else: #tar2<li<tar1
                num1=(h-1)*2+atomno[li-2]
        else:
            if li<tar1:
                num1=h*2+atomno[li-2]
            elif li==tar1:
                num1=h*2+atomno[li-2]+1
            elif li==tar2:
                num1=h*2+atomno[li-2]+1
            elif li>tar2:
                num1=h*2+atomno[li-2]
            else: #tar1<li<tar2
                num1=(h+1)*2+atomno[li-2]
    atomno.append(num1)
# Master loop starts here for the calculation on co-ordinates
SrNo=[]
Xco=[]
Yco=[]
for li in vv:
    if li==1:
        templist=list(range(1,atomno[0]+1))
        for num1 in templist:
            if num1==1:
                x3=1.212435
                y3=2.1
            else:
                num2=2*x1+2
                num3=2*x1+3
                if num1!=num2 and num1!=num3:
                    x3=1.212435+x4
                else:
                    x3=1.212435*2+x4
            if num1==1:
                x4=0
            else:
                x4=x3
            if num1%2==1 and num1!=1:
                y3=0
            elif num1==1:
                y3=2.1
            else:
                y3=0.7
            SrNo.append(num1)
            Xco.append(round(x3,6))
            Yco.append(round(y3,6))
    else:
        templist=list(range(atomno[li-2]+1,atomno[li-1]+1))
        for num4 in templist:
            if tar1>tar2:
                if li<tar2:
                    if li%2==1:
                        num5=atomno[li-2]+x1*2
                        num6=atomno[li-2]+x1*2+1
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num5 and num4!=num6:
                                x3=1.212435+Xco[num4-2]
                            else:
                                x3=1.212435*2+Xco[num4-2]
                    else:
                        num7=atomno[li-1]-((x1-1)*2)
                        num8=atomno[li-1]-((x1-1)*2)-1
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num7 and num4!=num8:
                                x3=Xco[num4-2]-1.212435
                            else:
                                x3=Xco[num4-2]-1.212435*2
                    if num4%2==0:
                        y3=li*2.1-1.4
                    else:
                        y3=(li-1)*2.1
                elif li>tar1:
                    if li%2==1:
                        num9=atomno[li-2]+1+(x2-1)*2
                        num10=atomno[li-2]+2+(x2-1)*2
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num9 and num4!=num10:
                                x3=1.212435+Xco[num4-2]
                            else:
                                x3=1.212435*2+Xco[num4-2]
                    else:
                        num11=atomno[li-1]-(x2-1)*2
                        num12=atomno[li-1]-(x2-1)*2+1
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num11 and num4!=num12:
                                x3=-1.212435+Xco[num4-2]
                            else:
                                x3=-1.212435*2+Xco[num4-2]
                    if num4%2==0:
                        y3=li*2.1-1.4
                    else:
                        y3=(li-1)*2.1
                elif li>tar2 and li<tar1:
                    if li%2==0:  # no. from left
                        num13=atomno[li-1]-(x1-1)*2+1
                        num14=atomno[li-1]-(x1-1)*2+2
                        num15=atomno[li-1]-(x2-1)*2+1
                        num16=atomno[li-1]-(x2-1)*2
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num13 and num4!=num14 and num4!=num15 and num4!=num16:
                                x3=Xco[num4-2]-1.212435
                            else:
                                x3=Xco[num4-2]-1.212435*2
                    else:
                        num17=atomno[li-2]+x2*2-1
                        num18=atomno[li-2]+x2*2
                        num19=atomno[li-2]+(x1-1)*2
                        num20=atomno[li-2]+(x1-1)*2+1
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num17 and num4!=num18 and num4!=num19 and num4!=num20:
                                x3=Xco[num4-2]+1.212435
                            else:
                                x3=Xco[num4-2]+1.212435*2
                    if num4%2==0:
                        y3=(li-1)*2.1
                    else:
                        y3=li*2.1-1.4
                elif li==tar2:
                    num21=atomno[li-2]+2*x2
                    num22=atomno[li-2]+2*x1-1
                    num23=atomno[li-2]+2*x1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if num4!=num21 and num4!=num22 and num4!=num23:
                            x3=Xco[num4-2]+1.212435
                        else:
                            x3=Xco[num4-2]+1.212435*2
                    if num4<num21:
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                    else:
                        if num4%2==1:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                else: #li=tar1
                    num24=atomno[li-2]+x2*2-1
                    num25=atomno[li-2]+x2*2
                    num26=atomno[li-2]+x1*2-1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if num4!=num24 and num4!=num25 and num4!=num26:
                            x3=Xco[num4-2]+1.212435
                        else:
                            x3=Xco[num4-2]+1.212435*2
                    if num4<num26:
                        if num4%2==0:
                            y3=(li-1)*2.1
                        else:
                            y3=li*2.1-1.4
                    else:
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
            elif tar1<tar2:
                if li<tar1:
                    if li%2==0:
                        num27=atomno[li-1]-x1*2+1
                        num28=atomno[li-1]-x1*2+2
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num27 and num4!=num28:
                                x3=Xco[num4-2]-1.212435
                            else:
                                x3=Xco[num4-2]-1.212435*2
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                    else:
                        num29=atomno[li-2]+2*x1
                        num30=atomno[li-2]+2*x1+1
                        if num4==(atomno[li-2]+1):
                            x3=Xco[num4-2]
                        else:
                            if num4!=num29 and num4!=num30:
                                x3=Xco[num4-2]+1.212435
                            else:
                                x3=Xco[num4-2]+1.212435*2
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                elif li>tar2:
                    if num4%2==0:
                        y3=li*2.1-1.4
                    else:
                        y3=(li-1)*2.1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if li%2==0:
                            num31=atomno[li-1]-(x2-1)*2
                            num32=atomno[li-1]-(x2-1)*2+1
                            if num4!=num31 and num4!=num32:
                                x3=Xco[num4-2]-1.212435
                            else:
                                x3=Xco[num4-2]-1.212435*2
                        else:
                            num33=atomno[li-2]+(x2)*2
                            num34=atomno[li-2]+(x2)*2-1
                            if num4!=num33 and num4!=num34:
                                x3=Xco[num4-2]+1.212435
                            else:
                                x3=Xco[num4-2]+1.212435*2
                elif li==tar1:
                    num35=atomno[li-2]+x1*2+1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if num4!=num35:
                            x3=Xco[num4-2]+1.212435
                        else:
                            x3=Xco[num4-2]+1.212435*2
                    if num4<num35:
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                    else:
                        if num4%2==1:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                elif li==tar2:
                    num36=atomno[li-2]+x2*2
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if num4!=num36:
                            x3=Xco[num4-2]+1.212435
                        else:
                            x3=Xco[num4-2]+1.212435*2
                    if num4<num36:
                        if num4%2==1:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                    else:
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                else:
                    if num4%2==1:
                        y3=li*2.1-1.4
                    else:
                        y3=(li-1)*2.1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if li%2==0:
                            x3=Xco[num4-2]-1.212435
                        else:
                            x3=Xco[num4-2]+1.212435
            else:
                if li<tar1:
                    if num4%2==0:
                        y3=li*2.1-1.4
                    else:
                        y3=(li-1)*2.1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if li%2==1:
                            num37=atomno[li-2]+2*x1
                            num38=atomno[li-2]+2*x1+1
                            if num4!=num37 and num4!=num38:
                                x3=Xco[num4-2]+1.212435
                            else:
                                x3=Xco[num4-2]+1.212435*2
                        else:
                            num39=atomno[li-1]-2*x1+1
                            num40=atomno[li-1]-2*x1+2
                            if num4!=num39 and num4!=num40:
                                x3=Xco[num4-2]-1.212435
                            else:
                                x3=Xco[num4-2]-1.212435*2
                elif li>tar1:
                    if num4%2==0:
                        y3=li*2.1-1.4
                    else:
                        y3=(li-1)*2.1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if li%2==0:
                            num41=atomno[li-1]-2*(x2-1)
                            num42=atomno[li-1]-2*(x2-1)+1
                            if num4!=num41 and num4!=num42:
                                x3=Xco[num4-2]-1.212435
                            else:
                                x3=Xco[num4-2]-1.212435*2
                        else:
                            num43=atomno[li-2]+2*x2-1
                            num44=atomno[li-2]+2*x2
                            if num4!=num43 and num4!=num44:
                                x3=Xco[num4-2]+1.212435
                            else:
                                x3=Xco[num4-2]+1.212435*2
                else:
                    num45=atomno[li-2]+2*x2
                    num46=atomno[li-2]+2*x1
                    if num4==(atomno[li-2]+1):
                        x3=Xco[num4-2]
                    else:
                        if num4!=num45 and num4!=num46:
                            x3=Xco[num4-2]+1.212435
                        else:
                            x3=Xco[num4-2]+1.212435*2
                    if num4<num45 or num4>=num46:
                        if num4%2==0:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
                    else:
                        if num4%2==1:
                            y3=li*2.1-1.4
                        else:
                            y3=(li-1)*2.1
            SrNo.append(num4)
            Xco.append(round(x3,6))
            Yco.append(round(y3,6))
genlist=list(range(1,atomno[v]+1))
#for num5 in genlist:
#    print(SrNo[num5-1], Xco[num5-1], Yco[num5-1])
R=[]
M=[]
L=[]
for li in vv:
    if li==1:
        ni=list(range(1,atomno[0]+1))
        for atom in ni:
            if atom==1:
                r=atomno[1]
                m=2
                l=""
            elif atom%2==0:
                if atom==2:
                    r=3
                    m=1
                    l=""
                else:
                    r=atom+1
                    l=atom-1
                    if atom!=atomno[li-1]:
                        m=atomno[li-1]*2-atom+1
                    else:
                        m=""
            else:
                r=atom+1
                l=atom-1
                m=""
            R.append(r)
            M.append(m)
            L.append(l)
    else:
        ni=list(range(1+atomno[li-2],1+atomno[li-1]))
        for atom in ni:
            if atom==(atomno[li-2]+1) or atom==atomno[li-1]:
                if atom<atomno[v]:
                    r=atom+1
                else:
                    r=""
                l=atom-1
                if atom==(atomno[1]):
                    m=1
                else:
                    m=""
            else:
                r=atom+1
                l=atom-1
                if li<min(tar1,tar2) or li>max(tar1,tar2):
                    if atom%2==0:
                        if (atomno[tar2-3]+1)<atom<=(atomno[tar2-2]-2*x2):
                            m=atomno[li-1]*2-atom
                            if tar1==tar2:
                                if atom<=(atomno[tar2-2]-2*x1):
                                    m=m+1
                                else:
                                    pass
                        else:
                            m=atomno[li-1]*2-atom+1
                            if (atomno[tar1-3]+1)<atom<=(atomno[tar1-2]-2*x1) and tar1<tar2:
                                m=m+1
                            else:
                                pass
                    else:
                        if (atomno[tar1]-(x1-1)*2+1)<=atom<atomno[tar1]:
                            m=atomno[li-2]*2-atom+2
                            if atom>(atomno[li-1]-(x2-1)*2) and tar1==tar2:
                                m=m-1
                            else:
                                pass
                        else:
                            m=atomno[li-2]*2-atom+1
                            if tar2>tar1 and (atomno[tar2]-2*(x2-1))<atom<atomno[tar2]:
                                m=m-1
                            else:
                                pass
                    if m>atomno[v]:
                        m=""
                    else:
                        pass
                elif tar2<li<tar1:
                    if atom%2==1:
                        if (atomno[li-1]-2*(x1-1))>=atom>(atomno[li-2]) and li==(tar1-1):
                            m=atomno[li-1]*2-atom+2
                        else:
                            m=atomno[li-1]*2-atom+1
                    else:
                        m=atomno[li-2]*2-atom+1
                        if m<(atomno[tar2-2]+2*x2):
                            m=m-1
                        else:
                            pass
                elif tar1<li<tar2:
                    if atom%2==1:
                        m=atomno[li-1]*2-atom+1
                    else:
                        m=atomno[li-2]*2-atom+1
                        if (atomno[tar1]-2*x1)<atom<(atomno[tar1]):
                            m=m+1
                        else:
                            pass
                    if li==(tar2-1) and (atomno[li-2]+1)<atom<=(atomno[li-1]-2*x2):
                        if atom%2==1:
                            m=m-1
                        else:
                            pass
                    else:
                        pass
                else:
                    if tar1>tar2:
                        if li==tar1:
                            num47=atomno[li-2]+2*x1-1
                            if atom<num47:
                                if atom%2==1:
                                    m=atomno[li-1]*2-atom+2
                                else:
                                    m=atomno[li-2]*2-atom+1
                            else:
                                if atom%2==0:
                                    m=atomno[li-1]*2-atom+1
                                else:
                                    m=atomno[li-2]*2-atom+2
                        else:
                            num48=atomno[li-2]+2*x2
                            if atom<num48:
                                if atom%2==0:
                                    m=atomno[li-1]*2-atom
                                else:
                                    m=atomno[li-2]*2-atom+1
                            else:
                                if atom%2==0:
                                    m=atomno[li-2]*2-atom
                                else:
                                    m=atomno[li-1]*2-atom+1
                    elif tar1<tar2:
                        if li==tar1:
                            num49=atomno[li-2]+2*x1+1
                            if atom<num49:
                                if atom%2==0:
                                    m=atomno[li-1]*2-atom+2
                                else:
                                    m=atomno[li-2]*2-atom+1
                            else:
                                if atom%2==1:
                                    m=atomno[li-1]*2-atom+1
                                else:
                                    m=atomno[li-2]*2-atom+2
                        else:
                            num50=atomno[li-2]+2*x2
                            if atom<num50:
                                if atom%2==1:
                                    m=atomno[li-1]*2-atom
                                else:
                                    m=atomno[li-2]*2-atom+1
                            else:
                                if atom%2==0:
                                    m=atomno[li-1]*2-atom+1
                                else:
                                    m=atomno[li-2]*2-atom
                    else:
                        num51=atomno[li-2]+2*x2
                        num52=atomno[li-2]+2*x1
                        if atom<num51:
                            if atom%2==0:
                                m=atomno[li-1]*2-atom+1
                            else:
                                m=atomno[li-2]*2-atom+1
                        elif num51<=atom<num52:
                            if atom%2==1:
                                m=atomno[li-1]*2-atom+2
                            else:
                                m=atomno[li-2]*2-atom
                        else:
                            if atom%2==0:
                                m=atomno[li-1]*2-atom+1
                            else:
                                m=atomno[li-2]*2-atom+1
            R.append(r)
            M.append(m)
            L.append(l)
for mn in genlist:
    if M[mn-1]=="":
        M[mn-1]=L[mn-1]
        L[mn-1]=""
    else:
        pass
    if R[mn-1]=="":
        R[mn-1]=M[mn-1]
        M[mn-1]=L[mn-1]
        L[mn-1]=""
    else:
        pass
Atom_no=atomno[v]
myfile=open('./double line.xyz','w')
myfile.write('{}\t \n'.format(Atom_no))
for nn in genlist:
    #print(SrNo[nn-1], 'C', Xco[nn-1], Yco[nn-1], 0, 2, R[nn-1], M[nn-1], L[nn-1])
    myfile.write('{}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t {}\t \n'.format(SrNo[nn-1], 'C', Xco[nn-1], Yco[nn-1], 0, 2, R[nn-1], M[nn-1], L[nn-1]))
myfile.close()
