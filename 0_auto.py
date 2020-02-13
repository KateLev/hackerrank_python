import os

def main():
    var = os.listdir(path="variants")[-1]
    print(var)
    with open (f'variants/{var}', mode='r+') as f_var:
        old_data = f_var.read()
    f_base = open('База НОВЫЙ.txt')
 #   print(f_var.read(10))
 #   print(f_base.readline())
    str_list = []
    new_str = ''
    point = 0
    for line in f_base:
        if (line=='Вставка 2\n'):
            point = 2
        if (point==1):
            if line=='\n':
                continue
            str_list.append(line)
            new_str = new_str + line
        
        if (line=='Вставка 1\n'):              
            point = 1   
            
    
    print("str_list", str_list)
    print("new_str", new_str)
    new_data = old_data.replace('ВСТАВКА 1\n', new_str)

    with open (f'variants/{var}', mode='r+') as f_var:
        f_var.write(new_data)
  #  point = 0
  #  for line in f_var:
    #    if (line=='ВСТАВКА 2\n'):
   #         point = 2
    #    if (point==1):
   #         f_var.replace('ВСТАВКА 1\n', str_list)         
    #    if (line=='ВСТАВКА 1\n'):              
    #        point = 1      
    #        print('yes')

    f_var.close()
    f_base.close() 
    
if __name__ == '__main__':
    main()
