mail_boxes=[]
for i in range(100):
    mail_boxes.append('000')

pc=0

calculator=0
# mail_boxes=['503','902','000','337']
# mail_boxes=['505', '306', '506', '902', '000', '123', '000']
# mail_boxes=['504', '205', '902', '000', '234', '123']

mail_boxes=['901', '312', '513', '114', '313', '212',
            '810', '513', '902', '602', '707', '000',
            '000', '000', '001']
def run():
    global pc,mail_boxes,calculator
    while 'k':
        # fatch
        mail = mail_boxes[pc]
        pc += 1

        # decode
        instruction=mail[0]
        xx=int(mail[1:3])
        

        # execute
        if instruction == '0':
            # halt
            break
        elif instruction == '1':
            #add
            calculator=f'{int(calculator)+int(mail_boxes[xx]):03}'
        elif instruction == '2':
            #subtract
            calculator=f'{int(calculator)-int(mail_boxes[xx]):03}'
        elif instruction == '3':
            # store
            mail_boxes[xx]=calculator
        elif instruction == '5':
            # load
            calculator=mail_boxes[xx]
            
        elif instruction == '6':
            # branch
            pc=xx
            
        elif instruction == '7':
            if int(calculator)==0:
                pc=xx
        
        elif instruction == '8':
            if 0 <= int(calculator) <= 499:
                pc=xx
                
        elif instruction == '9':
            if xx==2:
                print(calculator)
            elif xx==1:
                calculator=input('? ')
                

run()    
    
