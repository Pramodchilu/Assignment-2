# Rules:
# 1. Only letters (a-z), number(0-9) and periods(.) is allowed
# 2.Username cannot contain consecutive periods (.)
# 3. Username 8 or more characters and must contain one alphabetic character
# 4. No whitespaces are allowed
# 5. The last letter of your username should be ascii letter(a-z) or number(0-9)
# 6. Capital letters are not allowed

#!/usr/local/bin/python3

import re



regex = '^[a-z0-9]+[a-z]{1,}[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'

valid_list=[]

invalid_list=[]



try:

    fp = open('./emailaddress.txt')

    email = fp.readline()

    while email:

       if(re.search(regex, email)):

          valid_list.append(email)

       else:

          invalid_list.append(email)

       email = fp.readline()



    # Print Valid Email Addresses:

    print("\n Valid Email Addresses are : ")

    for x in range(len(valid_list)):

       print(valid_list[x])



    # Print Invalid Email Addresses:

    print("\n InValid Email Addresses are : ")

    for x in range(len(invalid_list)):

       print(invalid_list[x])



finally:

    fp.close()
