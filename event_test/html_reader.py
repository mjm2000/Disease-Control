def read_file(mayor,city):
    with open("text.html",'r') as file:
        file_list = list(file)

        #print(file_list[0])
        check = 0
        list123 = []
        st2 = ""
        
        events = {} 
        
        print(len(file_list[0]))
        for line in file_list:
            if len(line) >= 2:
                if  line[1] == '!':
                    sting = line.strip('<!-->') 
                    st = ""
                    for i in range(0,len(sting)-5):
                        st += sting[i]   
                    
                     
                    st2 = st 
                    check = 1
                elif line[1] == 'p':
                    sting_2 = line.strip('<p>')
                    sting_2 = sting_2.strip('</p>')
                     
                    sting_2 = sting_2.replace("Mayor","Mayor"+mayor)
                    sting_2 = sting_2.replace("<b>city</b>","<b>"+city+"</b>" )
                    check = 2
            if  check == 2:
                events[st2] = sting_2 
                st = ''
                check = 0
        print(events) 
            
        return events

read_file("jimbo","Moscow")

