import os 
directory = ('/home/liam/Dissertation/Data/JP-5/plain/People')
files = [file for file in os.listdir(directory)]                                   
 
delete_term = 'このページは曖昧さ回避のためのページです。一つの語句が複数の意味・職能を有する場合の水先案内のために、異なる用法を一覧にしてあります。お探しの用語に一番近い記事を選んで下さい。このページへリンクしているページを見つけたら、リンクを適切な項目に張り替えて下さい。'

for file in os.listdir(directory):
    infile = open(directory+'/'+file, 'r')
    text = ' '.join([line for line in infile])
    if delete_term in text:
        os.remove(directory+'/'+file)
    



