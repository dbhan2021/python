##diyabhan
##emailgen
import string

dash = "_"
school_site = str("@ashbury.com")
name = ""
while name != "q":
    name = str(input("Enter first name and surname with a space inbetween or type q to quit :"))
    if name != "q":
        # Split Name and Surname by space
        name_list = name.split()
        valid_name_len = len(name_list)
        if valid_name_len != 2:
            print(
                "Invalid format...Please type your first name and surname with a space inbetween, for example: Mary Jane"
            )
            continue
        else:
            # Get Last and First Name seaparately
            last_name = name_list[1].lower()
            first_name = name_list[0].lower()
            # Last Name needs to be only 6 characters
            six_char_last_name = last_name[0:6]
            # First Name needs ot be only 1
            first_char_name = first_name[0:1]
            email_address = six_char_last_name + dash + first_char_name + school_site
            print(email_address)
