#Container To Hold Contacts

contacts = []


def add_contact():
    #Collecting Contact Details
    contact_id = input("Enter an ID for contact: \n")
    contact_name = input("Enter contact's name: \n")
    phone_number = input("Enter contact's phone number: \n")
    email = input("Enter contact's email: \n")
    website = input("Enter contact's website: \n")
    home_address = input("Enter contact's home address: \n")
    work_address = input("Enter contact's work address: \n")
    dob = input("Enter contact's date of birth(dd/mm/year): \n")
    note = input("Enter a note about the contact: \n")
    
    
    #Validation(All fields are required)
    if not all([contact_id, contact_name, phone_number]):
        print("These Fields are Required: ID, Name and Phone Number. kindly try again!")
    else:
        #Storing In A Dictionary
        new_contact = {
        "ID": contact_id, 
        "Name": contact_name,
        "Phone Number": phone_number,
        "Email": email,
        "Website": website,
        "Home Address": home_address,
        "Work Address": work_address,
        "Date of Birth": dob,
        "Note": note
    }

    
        #Adding New Contact Record to List
        contacts.append(new_contact)
        print(f"New Contact with Unique ID: {unique_contact_id} with name: {contact_name} and {mobile_number} Added Successfully.")
        
        

def view_contacts():
    if not contacts:
        print("No Contacts in the system, Kindly Add Contacts")
    else:
        print("\nContacts List!!!")
        for contact in contacts:
            print(f"ID:{contact['ID']}\nName: {contact['Name']}\nMobile Number: {contact['Mobile Number']}\nPhone Number: {contact['Phone Number']}\nEmail: {contact['Email']}\nWebsite: {contact['Website']}\nHome Address: {contact['Home Address']}\nWork Address: {contact['Work Address']}\nDate of Birth: {contact['Date of Birth']}\nNote: {contact['Note']}\n")


def update_contact():
    unique_contact_id = input("Enter the Unique Contact ID you want to update:\n")
    for contact in contacts:
        if contact["ID"] != unique_contact_id:
            print(f"The Contact with Unique Contact ID: {unique_contact_id} not found")
            break
        elif contact["ID"] == unique_contact_id:
            print("Current Contact Details\n")
            print(f"ID:{contact['ID']}\nName: {contact['Name']}\nMobile Number: {contact['Mobile Number']}\nPhone Number: {contact['Phone Number']}\nEmail: {contact['Email']}\nWebsite: {contact['Website']}\nHome Address: {contact['Home Address']}\nWork Address: {contact['Work Address']}\nDate of Birth: {contact['Date of Birth']}\nNote: {contact['Note']}\n")
            
        #Update Information 
        contact_name = input("Enter contact's name (Press enter to keep the current value): \n")
        mobile_number = input("Enter contact's mobile number (Press enter to keep the current value): \n")
        phone_number = input("Enter contact's phone number (Press enter to keep the current value): \n")
        email = input("Enter contact's email (Press enter to keep the current value): \n")
        website = input("Enter contact's website (Press enter to keep the current value)e: \n")
        home_address = input("Enter contact's home address (Press enter to keep the current value): \n")
        work_address = input("Enter contact's work address (Press enter to keep the current value): \n")
        dob = input("Enter contact's date of birth(dd/mm/year) (Press enter to keep the current value): \n")
        note = input("Enter a note about the contact (Press enter to keep the current value): \n")
        print(f"The contact with Unique Contact ID: {unique_contact_id} Updated Successfully.")
        
        #get updated value
        if contact_name:
            contact['Name'] = contact_name
        if mobile_number:
            contact['Home Mobile Number'] = mobile_number
        if phone_number:
            contact['Work Phone Number'] = phone_number
        if email:
            contact['Email'] = email
        if website:
            contact['Website'] = website
        if home_address:
            contact['Home Address'] = home_address
        if work_address:
            contact['Work Address'] = work_address
        if dob:
            contact['Date of Birth'] = dob
        if note:
            contact['Note'] = note
            break
    

def delete_contact():
    unique_contact_id = input("Enter the Unique Contact ID of the contact you want to delete: ")
    for contact in contacts:
        if contact["ID"] == unique_contact_id:
            contacts.remove(contact)
            print(f"The contact with Contact ID: {unique_contact_id} deleted successfully")
            break
        else:
            print(f"The contact with Unique Contact ID: {unique_contact_id} not found in contacts.")

def exit_program():
    exit(1)