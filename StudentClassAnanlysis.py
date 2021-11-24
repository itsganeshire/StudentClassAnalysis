import streamlit as st
st.set_page_config(page_title='Analysis',page_icon='logo.png')
import pandas as pd
import matplotlib.pyplot as plt
import random

df = pd.read_excel('fydata.xlsx')
atd = pd.read_excel('atd.xlsx')
#atd[atd.TOTAL*100,atd.MPMC*100,atd.DS*100,atd.DSA*100,atd.IP*100,atd.PDE*100,atd.OB*100,atd.MPMC_TUT*100,atd.MPMC_PR*100,atd.DS_PR*100,atd.DS_TUT*100,atd.DSA_TUT*100,atd.IP_PR*100,atd.PDE_PR*100]
#st.write(atd[atd.TOTAL,atd.MPMC])

st.set_option('deprecation.showPyplotGlobalUse', False)
users = {'ganesh':'123','admin':'000'}

def displayMarksByName(name):
    rno=l.index(name)
    col11,col12= st.beta_columns(2)
    marks=[int(df.subject1.iloc[rno]),int(df.subject2.iloc[rno]),int(df.subject3.iloc[rno]),int(df.subject4.iloc[rno]),int(df.subject5.iloc[rno]),int(df.subject6.iloc[rno])]
    attdns=[int(atd.MPMC.iloc[rno]*100),int(atd.DS.iloc[rno]*100),int(atd.DSA.iloc[rno]*100),int(atd.IP.iloc[rno]*100),int(atd.PDE.iloc[rno]*100),int(atd.OB.iloc[rno]*100)]

    subs = ['mpmp', 'ds', 'dsa','ip', 'pde', 'ob']
	
    #plt.title(df.name[rno]+"'s Marks")
    plt.title("Marks")
    plt.xlabel("Subjects")
    plt.ylim([0,100])
    plt.ylabel("percentage(%)")
    plt.bar(subs,marks)
    col11.pyplot()    

    plt.title("Attendance")
    plt.xlabel("Subjects")
    plt.ylim([0,100])
    plt.ylabel("percentage(%)")
    plt.bar(subs,attdns, edgecolor='blue')
    col12.pyplot()    

    col21,col22 = st.beta_columns(2)

    x = [random.randrange(0,3),random.randrange(0,3),random.randrange(0,3),random.randrange(0,3),random.randrange(0,3)]
    y = [1,2,3,4,5]
    plt.title("Extracurricular Activities")
    plt.fill_between(y,x, color="Slateblue",alpha=0.6, linewidth=2)        
    plt.plot(y,x, color="Slateblue",alpha=0.6, linewidth=2)
    plt.ylim([0,10])
    col21.pyplot()
  
    names = ['sub1 assignments', 'sub2 assignments', 'sub3  assignments', 'sub4 assignments','sub5 assignments','sub6 assignments']
    size = [random.randrange(1,5),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,14),random.randrange(1,11)]
    
    my_circle = plt.Circle( (0,0), 0.7, color='white')

    plt.title("Submitted Assignments")
    plt.pie(size, labels=names, colors=['red','green','blue','skyblue','yellow','orange'])
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    col22.pyplot()

    col31,col32,col33 = st.beta_columns([1,3,1])
    fct = pd.read_excel('factor.xlsx')
    labels=['communication','productivity','honesty','punctuality','attendance','take intiative']
    facts=[fct.communication.iloc[rno],fct.productivity.iloc[rno],fct.honesty.iloc[rno],fct.punctuality.iloc[rno],fct.attendance.iloc[rno],fct.takes_initiative.iloc[rno]]
    plt.barh(labels,facts)
    plt.xlabel("Factors")
    plt.ylim([0,10])
    plt.ylabel("Score")
    col32.pyplot()


def displayMarksByRoll(rno):
    rno = rno-1
    col11,col12= st.beta_columns(2)
    marks=[int(df.subject1.iloc[rno]),int(df.subject2.iloc[rno]),int(df.subject3.iloc[rno]),int(df.subject4.iloc[rno]),int(df.subject5.iloc[rno]),int(df.subject6.iloc[rno])]
    attdns=[int(atd.MPMC.iloc[rno]*100),int(atd.DS.iloc[rno]*100),int(atd.DSA.iloc[rno]*100),int(atd.IP.iloc[rno]*100),int(atd.PDE.iloc[rno]*100),int(atd.OB.iloc[rno]*100)]

    subs = ['mpmp', 'ds', 'dsa','ip', 'pde', 'ob']
	
    plt.title(df.name[rno]+"'s Marks")
    plt.xlabel("Subjects")
    plt.ylim([0,100])
    plt.ylabel("percentage(%)")
    plt.bar(subs,marks)
    col11.pyplot()    

#    nm= atd.Student_name[rno].split(' ')
#   plt.title(nm[1]+"'s Attendanbce")
    plt.title(df.name[rno]+"'s Attendance")
    plt.xlabel("Subjects")
    plt.ylim([0,100])
    plt.ylabel("percentage(%)")
    plt.bar(subs,attdns, edgecolor='blue')
    col12.pyplot()    

    col21,col22 = st.beta_columns(2)
    x = [random.randrange(0,3),random.randrange(0,3),random.randrange(0,3),random.randrange(0,3),random.randrange(0,3)]
    y = [1,2,3,4,5]
    plt.title("Extracurricular Activities")
    plt.fill_between(y,x, color="Slateblue",alpha=0.6, linewidth=2)        
    plt.plot(y,x, color="Slateblue",alpha=0.6, linewidth=2)
    plt.ylim([0,10])
    plt.xlim([1,10])
    col21.pyplot()
  
    names = ['sub1 assignments', 'sub2 assignments', 'sub3  assignments', 'sub4 assignments','sub5 assignments','sub6 assignments']
    size = [random.randrange(1,5),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,14),random.randrange(1,11)]
    
    my_circle = plt.Circle( (0,0), 0.7, color='white')

    plt.title("Submitted Assignments")
    plt.pie(size, labels=names, colors=['red','green','blue','skyblue','yellow','orange'])
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    col22.pyplot()

    col31,col32,col33 = st.beta_columns([1,3,1])
    fct = pd.read_excel('factor.xlsx')
    labels=['communication','productivity','honesty','punctuality','attendance','take intiative']
    facts=[int(fct.communication.iloc[rno]),int(fct.productivity.iloc[rno]),int(fct.honesty.iloc[rno]),int(fct.punctuality.iloc[rno]),int(fct.attendance.iloc[rno]),int(fct.takes_initiative.iloc[rno])]
    plt.barh(labels,facts)
    plt.xlabel("Factors")
    plt.xlim([0,10])
    plt.ylim([-1,6])
    plt.ylabel("Score")
    col32.pyplot()

s1,s2,s3 = st.beta_columns([1,1,6])
s2.image('logo.png',width=100)
s3.markdown('# The Student & Class Analysis')

c1,c2,c3 = st.beta_columns(3)
c2.markdown('## **Authentication**')

c1,c2,c3 = st.beta_columns(3)
usr=c2.text_input('Username')

c1,c2,c3 = st.beta_columns(3)
pas=c2.text_input('Password',type='password')

c1,b2,c3 = st.beta_columns([2,1,2])
button = b2.checkbox('Login/Logout')

counter = False
if button:
    try:
        if users[usr]==pas:
            counter=True
        else:
            c1,c2,c3 = st.beta_columns([1,3,1])
            c2.error('ㅤㅤㅤWrong username/password')
    except:
        c1,c2,c3 = st.beta_columns([1,2,1])
        c2.error('ㅤㅤㅤWrong username/password')

if counter:
    section = st.sidebar.radio('Section', ['Student Analysis','Class Analysis'])
    if section == 'Class Analysis':
        st.title("Class Analysis")

        dd = st.selectbox('Select Class',('First Year','Second Year','Third Year','Last Year'))

        col11,col12 = st.beta_columns(2)
        col21,col22 = st.beta_columns(2)

        year = list()

        for i in range(int(2015),int(2020)):
            year.append(i)

        plt.title("Class Score that they scored")
        plt.xlim([2014,2020])
        plt.ylim([0,100])
        plt.plot(year,[random.randrange(10,100),random.randrange(10,100),random.randrange(10,100),random.randrange(10,100),random.randrange(10,100)],'o-g')       
        col11.pyplot()

        plt.title("Attendance of the Class")
        plt.ylim([0,100])
        plt.xlim([2014,2020])
        plt.plot(year,(atd.TOTAL[:5]*100),'.--')       
        col12.pyplot()

        x = [random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10),random.randrange(1,10)]
        y = [1,2,3,4,5]
        plt.title("Extracurricular Activities")
        plt.fill_between(y,x, color="Slateblue",alpha=0.6, linewidth=2)        
        plt.plot(y,x, color="Slateblue",alpha=0.6, linewidth=2)
        plt.ylim([0,10])
        col21.pyplot()

        names = ['sub1 assignments', 'sub2 assignments', 'sub3  assignments', 'sub4 assignments','sub5 assignments','sub6 assignments']
        size = [random.randrange(1,25),random.randrange(1,25),random.randrange(1,25),random.randrange(1,25),random.randrange(1,25),random.randrange(1,25)]
        
        my_circle = plt.Circle( (0,0), 0.7, color='white')

        plt.title("Submitted Assignments")
        plt.pie(size, labels=names, colors=['red','green','blue','skyblue','yellow','orange'])
        p = plt.gcf()
        p.gca().add_artist(my_circle)
        col22.pyplot()
    elif section == 'Student Analysis':
    #    st.title("Student Analysis")
        exp = st.text_input("Expression:")
        try:
            if '<' in exp:
                n = exp.split('<')
                r = df[df.percentage >= int(n[-1])]
                r=r.sort_values('percentage')
                st.table(r[::-1])
            if '>' in exp:
                n = exp.split('>')
                r = df[df.percentage <= int(n[-1])]
                r=r.sort_values('percentage')
                st.table(r[::-1])
            elif '%' in exp:
                n = exp.split('%')
                r = df[round(df.percentage) == float(n[0])]
                r=r.sort_values('percentage')
                st.table(r[::-1])
            if '<' in exp:
                n = exp.split('<')
                st.write(atd)
                r = atd[atd.TOTAL >= int(n[1])]
                st.write(r)
                r=r.sort_values('TOTAL')
                st.table(r[::-1])
            elif '>' and 'atd' in exp:
                n = exp.split('>')
                r = atd[atd.TOTAL <= int(n[1])*100]
                r=r.sort_values('TOTAL')
                st.table(r[::-1])
            elif '%' and 'atd' in exp:
                n = exp.split('%')
                r = atd[round(atd.TOTAL) == float(n[0])]
                r=r.sort_values('TOTAL')
                st.table(r[::-1])
            l = list(df.name)
            n = list(df.rollno)
            if exp in l:
                displayMarksByName(exp)
            elif int(exp) in n:
                displayMarksByRoll(int(exp))
        except:
            st.warning('No data')