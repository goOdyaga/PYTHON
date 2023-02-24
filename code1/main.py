input_datas= open("example_input.txt","r")
output_data= open("example_output1.txt","w")

# output_data.close()
# input_datas = [line[:-1] for line in input_datas]
list_operator=['+','-','*','/','//','**','%']
list_logical=['>=','<=','==','!=','<','>']
# flag=False
#control line for invalid input
def control_line(content):
    digits=["1","2","3","4","5","6","7","8","9","0"]
    for i in range(0,len(content)-2):
        if(content[i].isnumeric() and content[i+2].isnumeric() and ord(content[i+1])==32):
            return False
    content=content.replace(" ","")    
    for i in list_logical:
        if content.find(i)!=-1:
            content=content.replace((i),"")
    for i in content:
        if not((i  in list_operator) or  (i in digits) ):
            return False
    
    return True

def count_comparision(inputs):
    for content in inputs:
        if(len(content)!=1):
            content=content[:-1]
            couunt=0
            if(control_line(content)):
                content=content.replace(" ","")
                couunt=0
                for l in list_logical:
                    if(l=='<' or l=='>'):
                        if(content.find(l)!=-1):
                            a=content.index(l)
                            if(a<len(content) and content[a+1]=='='):
                                couunt-=1
                    couunt+=content.count(l)
                if(couunt>1):
                    output_data.write("ERROR")
                    output_data.write('\n')
                elif (couunt==1):
                    part1,part2,comp=for_comparision(content)
                    comparision_operations(part1,part2,comp)
                else:
                    part1_order_count=split_content(content)
                    if(part1_order_count!=-1):
                        if (control_content(part1_order_count)):

                            math_operation(part1_order_count,False)
                        else:
                            output_data.write("ERROR")
                            output_data.write('\n')
                    else:
                        output_data.write("ERROR")
                        output_data.write('\n')
            else:
                output_data.write("ERROR")
                output_data.write('\n')
        else:
            output_data.write('\n')

#divide 2 part to string
def for_comparision(content):
   
    for i in list_logical:
        if content.find(i)!=-1:
            a,b=content.split(i)
            return a,b,i

#calculate mathematical operations
def math_operation(order_content,flag=True):
    
    i=0
    while i < len(order_content):
        if(order_content[i]=='**'):
            m=order_content.index(order_content[i])
            a=float(float(order_content[m-1])**float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        elif(order_content[i]=='//'):
            m=order_content.index(order_content[i])
            a=float((order_content[m-1])//float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        i+=1
    i=0
    while i < len(order_content):
        if(order_content[i]=='*'):
            m=order_content.index(order_content[i])
            a=float(float(order_content[m-1])*float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        elif(order_content[i]=='/'):
            m=order_content.index(order_content[i])
            if(float(order_content[m+1])==0):
                flag=True
                return False
            a=float(float(order_content[m-1])/float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        elif(order_content[i]=='%'):
            m=order_content.index(order_content[i])
            if(float(order_content[m+1])==0):
                flag=True
                return False
            a=float(float(order_content[m-1])%float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        i+=1
    i=0
    while i < len(order_content):
        if(order_content[i]=='+'):
            m=order_content.index(order_content[i])
            a=float(float(order_content[m-1])+float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        elif(order_content[i]=='-'):
            m=order_content.index(order_content[i])
            a=float(float(order_content[m-1])-float(order_content[m+1]))
            order_content.pop(m)
            order_content.pop(m)
            order_content[m-1]=a
            i-=2
        i+=1
    if(flag):
        return order_content[0]
    else:
        output_data.write(str(order_content[0]))
        output_data.write('\n')

#split string input for math operation
def split_content(content):
    list_order_operator=[]
    list_operator1=[]
    int_str=""
    list_str=""
    i=int(0)
    while i < len(content):
        if(i==0 and content[i].isnumeric()==False):
            return -1
        elif(content[i].isnumeric()==False):
            list_order_operator.append(int(int_str))
            del int_str
            int_str=""
            if(i==len(content)-1):
                return -1
            list_str+=content[i]
            if(i!=len(content) and content[i+1].isnumeric()==False):
                list_str+=content[i+1]
                i+=1
            list_order_operator.append(list_str)
            list_operator1.append(list_str)
            del list_str
            list_str=""
        else:
            int_str+=content[i]
        if(i+1==len(content)):
            if(content[i].isnumeric()):
                list_order_operator.append(int(int_str))
            else:
                output_data.write("ERROR")
                output_data.write('\n')
        i+=1
    for i in list_operator1:
        if (i not in list_operator )and (i not in list_logical) :
            return -1
    return list_order_operator

#controlling input for error
def control_content(order_content):
    if(order_content==False):
        output_data.write("ERROR")
        output_data.write('\n')
    if(len(order_content)>0 and (type(order_content[0])==str or type(order_content[len(order_content)-1])==str )):
        output_data.write("ERROR")
        output_data.write('\n')
    for i in range(0,len(order_content)):
        if i%2==0:
            if type(order_content[i])!=int:
                output_data.write("ERROR")
                output_data.write('\n')
        elif i%2==1:
            if type(order_content[i])!=str:
                output_data.write("ERROR")
                output_data.write('\n')
    return True

#start operators and manipulate file
def comparision_operations(part1,part2,comp):
    part1_order_count=split_content(part1)
    part2_order_count=split_content(part2)
    if(part1_order_count!=-1 and part2_order_count!=-1):
        if(control_content(part1_order_count) and control_content(part1_order_count) ):
            part1_res=math_operation(part1_order_count,True)
            part2_res=math_operation(part2_order_count,True)
                
            if(comp=='<'):
                if(float(part1_res)<float(part2_res)):
                    output_data.writelines("TRUE")
                    output_data.write('\n')
                else:
                    output_data.write("FALSE")
                    output_data.write('\n')
           
            elif(comp=='>'):
                if(float(part1_res)>float(part2_res)):
                    output_data.writelines("TRUE")
                    output_data.write('\n')
                else:
                    output_data.write("FALSE")
                    output_data.write('\n')

            elif(comp=='<='):
                if(float(part1_res)<=float(part2_res)):
                    output_data.writelines("TRUE")
                    output_data.write('\n')
                else:
                    output_data.write("FALSE")
                    output_data.write('\n')

           
            elif(comp=='>='):
                if(float(part1_res)>=float(part2_res)):
                    output_data.writelines("TRUE")
                    output_data.write('\n')
                else:
                    output_data.write("FALSE")
                    output_data.write('\n')

            elif(comp=='=='):
                if(float(part1_res)==float(part2_res)):
                    output_data.writelines("TRUE")
                    output_data.write('\n')
                else:
                    output_data.write("FALSE")
                    output_data.write('\n')

            elif(comp=='!='):
                if(float(part1_res)!=float(part2_res)):
                    output_data.writelines("TRUE")
                    output_data.write('\n')
                else:
                    output_data.write("FALSE")
                    output_data.write('\n')
        else:
            output_data.write("ERROR")
            output_data.write('\n')
    else:
        output_data.write("ERROR")
        output_data.write('\n')


count_comparision(input_datas)


