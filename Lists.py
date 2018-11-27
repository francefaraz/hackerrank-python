N = int(input())
l=[]
for _ in range(N):
	cmd= input().split()
	 cmd1=cmd[0]
	args=cmd[1:]
	 if(cmd1!='print'):
		cmd1+="("+ ",".join(args)+")"
		eval("l."+cmd1);
	else :
		 print(l)