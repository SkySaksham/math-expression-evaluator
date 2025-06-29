def in_put(x=True) :
	if x== True :
		x= input("Enter Expression : ")	
	data=x.replace(" ","")
	data= data.replace ("--","+")
	data= data.replace("**+","**")
	data = data.replace("**","^")
	data = data.replace("÷","/")
	data=data.replace("x","×").replace("X","×")
	data = data.replace ("()","").replace(")(",")*(")
	
	for k in range (data.count("(") + data.count(")") ) :
		for i in range (1,len(data) - 1) :
			if data[i] == "(" and data[i-1].isnumeric() :
				new_data= data[0:i] + '*' + data[i:len(data)]
				
				data= new_data
				break 
			if data[i]==")" and data[i+1].isnumeric() :
				print (True)
				new_data = data[0:i+1] + "*" + data[i+1: len(data)]
				data=new_data
				break
		continue
	
	
	return data
	
	

def check_errors(data) :
	index = -1
	char = [".","(",")"] + [str(i) for i in range (10)]
	operators = "*","+","-","/","×","^"
	bracket = "(",")"
	
	if data.count("(") != data.count(")") :
		print ("\n Invalid Input !!")
		print ("Close all the Brackets !!")
		return None
	
	if len(data) == 0 :
		print("\nInvalid Input !!")
		print("No Input Recieved !!")
		return None
		

	if data[len(data)-1] in operators :
		print ("\nInvalid Input !!")
		print ("Expression Ends With An Operator !!")
		return None
	
	for i in data :
		index+=1		
		if i not in char and i not in operators :
			print ("\nInvalid Input !!")
			print (i," Cant Be Evaluated !!")
			return None
			
		if i in operators and data [index+1] in operators :
					if data [index+1] in ["-","+"] :
						continue 	
										
					else :
						print ("\nInvalid Input !!")
						error = i+data[index+1]
						print (error , "Cant Be Evaluated !!")
						return None
						
	for i in range (len(data)-3) :
	 			if data[i] in operators and data[i+1] in operators and data [i+2] in operators :
	 							check=data[i:i+2]
	 							print ("\nInvalid Input !!")
	 							print (check,"Three Operators Together !!")
	 							return None						
	 						
	return data



def list_maker(a) :
	data = list()
	index = -1
	s=''
	for i in a :
		index +=1
		if i.isdigit() or i== "." :
					s+=str(i)
		if i in ['+','-','/',"*","^","×","(",")"] :	
						if s!='':
							data.append(s)
							data.append(i)	
							s=''
						else :
							data.append(i)
							
	data.append(s)
	return (data)	

	
			
def unary_minus(a,operator ="-") :
	k=[]
	
	for i in range(len(a)-1) :
		if i==0 and a[i]== operator  :
			k.append(i)
		elif a[i] == operator:
			if a[i-1] in ["+","*","×","x","X","-","^","/"]:
				k.append(i)

	for i in k[::-1] :
				p = operator +a[i+1]
				a[i+1] = p
				del a[i]
	if operator == '-' :
		unary_minus(a,'+')
	return a				



def exponent_function(data) :

	total_operators = data.count("^")
	

	while total_operators > 0 :
		total_operators = data.count("^")
		count =0
		k=-1
		for i in data :
			k+=1
			if i in "^" :
				count+=1
				if count == total_operators :
					oput = float(data[k-1])**float(data[k+1])
					data[k]=str(oput)
					del data[k-1]
					del data[k]
					break ;
	return data



def division_function (data) :
	c=data.count('/') + data.count("÷")
	
	for loop in range(c):									
			index =-1
			for i in data :
				index+=1
				
				if i== '/' or i=='÷' :
						p=float(data[index-1])
						q= float(data[index+1])
						if q==float(0) :
							print ("\nZero Division Error")
							for i in data :
								print(i,end=" ")
							print("")
							print("Can't evaluate further !!")	
							return None
															
						Division= p/q
						data[index]=str(Division)
						del data[index-1]
						del data[index]
						break
	return data			
				


def multiplication(data) :

	a=data.count('x')+data.count("X")+data.count("*")+data.count("×")

	for loop in range (a+1) :
		k=-1
		for i in data :
			k+=1
			oper = "*","×","x","X"
		
			if i in oper :
				p=float(data[k-1])*float(data[k+1])
				data[k]=str(p)
				del data[k-1]
				del data[k]
				break ;
	return data		

								

def plus_minus(data) :

	a=data.count("+") + data.count("-")

	for loop in range (a):
		k= -1
		for i in data :
			k+=1
		
			if i=='-' :					
					p=float(data[k-1])-float(data[k+1])
					data[k]=str(p)
					del data[k-1]
					del data[k]
					break ;										
							
			if i=='+' :
				p=float(data[k-1])+float(data[k+1])
				data[k]=str(p)
				del data[k-1]
				del data[k]
				break;
															
	return data[0]

		
			
def expression_evaluator(x) :
	data1 = unary_minus(x)
	data2 = exponent_function (data1)
	data3= division_function(data2)
	
	if data3 == None :
		return None
		
	data4= multiplication(data3)
	solved_data= plus_minus(data4)
	
	return solved_data 
	


def bracket_evaluator(a) :
	bracket_index1=0
	bracket_index2=0
	index_bracket=[None,None]
	index =-1
	for i in a :
		index +=1
		if i == '(' :
			bracket_index1 +=1 
			index_bracket[0]=index
		if i == ')' :
			bracket_index2 +=1
			index_bracket[1]=index
		if bracket_index2 >0:
			p= index_bracket[0] +1
			q=index_bracket[1]
			data =  expression_evaluator(a[p:q])
			a[p-1] = data
			del a[p:q+1]
			bracket_evaluator(a)
	return a			
			



def evaluate(x=True) :
	data0 = in_put(x)
	
	if check_errors(data0) == None :
		return 
	
	tokens = list_maker (data0)
	result = expression_evaluator(bracket_evaluator(tokens))
	return result
	


