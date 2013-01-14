study='ds102'
f=open(study+'/condition_key.txt')
ckey=f.readlines()
f.close()

f=open(study+'/task_key.txt')
tkey=f.readlines()
f.close()

print '<table border="1">'
print '<caption><EM>Description of tasks and conditions</EM></caption>'

for task in range(len(tkey)):
    print '<tr><th colspan="2">%s'%tkey[task].strip().replace(' ',': ',1)
    for c in ckey:
        if c.strip().split(' ')[0]==tkey[task].strip().split(' ')[0]:
            print '<tr><td>%s<td>%s'%(c.strip().split(' ')[1],' '.join(c.strip().split(' ')[2:]))

print '</table>'

## <TABLE border="1"
##           summary="This table gives some statistics about fruit
##                    flies: average height and weight, and percentage
##                    with red eyes (for both males and females).">
## <CAPTION><EM>A test table with merged cells</EM></CAPTION>
## <TR><TH rowspan="2"><TH colspan="2">Average
##     <TH rowspan="2">Red<BR>eyes
## <TR><TH>height<TH>weight
## <TR><TH>Males<TD>1.9<TD>0.003<TD>40%
## <TR><TH>Females<TD>1.7<TD>0.002<TD>43%
## </TABLE>
