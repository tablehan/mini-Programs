import xlrd
import xlwt
import difflib
import time
print('start time:',time.ctime())
fn='C:/Users/OIR_UX430/Desktop/python_test/string_similarity/20220216similarity.xlsx'
wb=xlrd.open_workbook(fn)
sh1=wb.sheets()[8]
stack=list(map(str,sh1.col_values(1)[1:]))
dic={}
for title in stack:
    dic[title]=difflib.get_close_matches(title, stack , n=20, cutoff=0.7)
print('load time:',time.ctime())
nwn='C:/Users/OIR_UX430/Desktop/python_test/string_similarity/期刊論文相似度比對.xls'
nwb=xlwt.Workbook()
nsh=nwb.add_sheet('sheet1',cell_overwrite_ok=True)
nsh.write(0,0,'論文標題')
nsh.write(0,1,'相似論文標題篇數')
nsh.write(0,2,'相似論文_向右延伸')
count=1
for key,val in dic.items():
    nsh.write(count,0,key)
    nsh.write(count,1,len(val))
    j=0
    for v in val:
        nsh.write(count,2+j,v)
        j+=1
    count+=1
print('write time:',time.ctime())
nwb.save(nwn)
