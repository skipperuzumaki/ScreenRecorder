import subprocess

cmd = ['xrandr']
cmd2 = ['grep','*']
p=subprocess.Popen(cmd,stdout=subprocess.PIPE)
p2=subprocess.Popen(cmd2,stdin=p.stdout,stdout=subprocess.PIPE)
p.stdout.close()


RS, junk = p2.communicate()
rs = RS.split()[0]
w,h=str(rs).split('x')
k=w.split("'")[1]
j=h.split("'")[0]
