#coding:utf-8
import random,os,sys,io

cac,cacc='#','|'
dire,fich='./','vbs.nath'

def inp(txt):
    vp=sys.version_info
    if vp[0]==2: return inp(txt)
    else: return input(txt)
    
def a():
    vbs=[]
    if fich in os.listdir(dire):
        f=io.open(dire+fich,'r',encoding="utf-8").read().split(cacc)
        for ff in f:
            g=ff.split(cac)
            if len(g)>2: vbs.append(g)
    return vbs

def b(vbs):
    nb=random.randint(4,10)
    dif=random.randint(1,3)
    pts=0
    for x in range(nb):
        v=random.choice(vbs)
        vv=[]
        lvl=[]
        while len(lvl) < dif:
            lvl.append( random.randint(0,3) )
        tt=""
        rep=""
        for y in range(0,4):
            rep+="("+str(y)+")="+v[y]+" - "
            tt+='('+str(y)+')'
            if y in lvl:
                tt+=v[y]
            else:
                tt+='?'
            tt+=' - '
        tt=tt[:-2]
        rep=rep[:-2]
        print(tt)
        for y in range(0,4):
            tt=str(y)+" - "
            vv.append( inp(tt) )
        if v==vv:
            pts+=1
            print("juste ! ;)")
        else: 
            print("faux ! :(")
            print("c'était : "+rep)
        print(str(pts)+"/"+str(x+1))
    print("Vous avez un score de : "+str(pts)+"/"+str(nb))

def c():
    tt=''
    for x in range(0,4):
        txt=str(x)+" : "
        tt+=inp(txt)+cac
    tt=tt[:-1]
    f=open(dire+fich,'a')
    f.write(cacc+tt)
    f.close()

def d():
    aa=''
    while aa != 'q':
        c()
        aa=inp(">>> ")

#d()
b(a())




