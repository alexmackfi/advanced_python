def drow_table(table_strings,name='mytable.tex'):
    string = '\\begin{table}\n'
    string+='\\begin{tabular}{|'+'c|'*len(table_strings[0])+'}\n'+'\hline\n'
    ind = 0
    for i in table_strings:
        if ind==1:
            string+='\\hline\n'
        for j in i[:-1]:
            string+=str(j)+' &    '
        string+=str(i[-1])+'\\'+'\\'+'\n'
        ind+=1
    string+='\\hline\n'+'\\end{tabular}\n\\end{table}'
    with open(name, 'a') as tf:
        tf.write(string)


def drow_image(path,name='mytable.tex'):
    string = '\n\n'+'\\begin{figure}\n\centering\n'
    string+='\\includegraphics[width=0.5\linewidth]{'+ path +'}\n\end{figure}'
    with open(name, 'a') as tf:
        tf.write(string)
    print(string)

def start_document(name='mytable.tex'):
    string = '\\documentclass{article}\n\\begin{document}'
    with open(name, 'w') as f:
        f.write(string)

def finish_document(name='mytable.tex'):
    string = '\n\\end{document}'
    with open(name, 'a') as f:
        f.write(string)
