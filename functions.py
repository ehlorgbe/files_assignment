import os
import json
import csv

'''Function that loads json file from directory'''
def load_json_file():
    try:
        # Prompt user for folder path and file name
        folder_path = '/Users/3lliot/Documents/GitHub/' + input("Enter the folder name where the JSON file is stored: ")
        file_name = "elliothlorgbe_adoptions.json"
        file_path = os.path.join(folder_path, file_name)
        
        # Check if the file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_name} not found in {folder_path}")
        
        # Open and load the JSON data
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data
    
    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except json.JSONDecodeError:
        print("Error decoding JSON. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")


''' Functions that create four csv files from elliothlorgbe_adoptions.json : University, Contacts, Adoptions and messages'''
def university_data_to_csv(data, file_name="university_information.csv"):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["University_ID", "Name", "Address", "City", "State", "Zip_code", "Website"])
        for record in data:
            university = record.get('university', {})
            writer.writerow([university.get('id'), university.get('name'), university.get('address'), university.get('city'), university.get('state'), university.get('zip'), university.get('website')])


def adoptions_to_csv(data, file_name="adoptions.csv"):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Adoption_ID", "Date", "Quantity", "Book_ID", "ISBN10", "ISBN13", "Title", "Category"])
        for record in data:
            for adoption in record.get('adoptions', []):
                book = adoption.get('book', {})
                writer.writerow([adoption.get('id'), adoption.get('date'), adoption.get('quantity'), book.get('id'), book.get('isbn10'), book.get('isbn13'), book.get('title'), book.get('category')])


def export_contacts_to_csv(data, file_name="contacts.csv"):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Contact_order", "Gender", "First Name", "Last Name"])
        for record in data:
            for contact in record.get('contacts', []):
                writer.writerow([contact.get('order'), contact.get('gender'), contact.get('firstname'), contact.get('lastname')])

def export_messages_to_csv(data, file_name="messages.csv"):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Message_ID", "Date", "Content", "Category"])
        for record in data:
            for message in record.get('messages', []):
                writer.writerow([message.get('id'), message.get('date'), message.get('content'), message.get('category')])
def export_messages_to_csv(data, file_name="messages.csv"):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Message ID", "Date", "Content", "Category"])
        for record in data:
            for message in record.get('messages', []):
                writer.writerow([ message.get('date'), message.get('content'), message.get('category')])

'''function that accepts a state name and displays list of universities in that state'''
def list_universities_by_state(data, state_name):
    universities_in_state = []
    for record in data:
        university = record.get('university', {})
        if university.get('state') == state_name:
            universities_in_state.append(university.get('name'))
    
    if universities_in_state:
        print(f"Universities in {state_name}:")
        for uni in universities_in_state:
            print(uni)
    else:
        print(f"No universities found in {state_name}.")
