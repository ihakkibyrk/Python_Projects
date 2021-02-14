

def email_slicer():
    
    email_addr = input("Please write your email : ")
    slicer_email = email_addr[email_addr.index("@"):email_addr.index(".",email_addr.index("@"))]
    slicer_name = email_addr[0:email_addr.index(".")]
    print("Hey{}, looks like you have got your own custom setut up at {}. Impressive!.".format(slicer_name, slicer_email))

email_slicer()