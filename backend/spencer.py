from addressBook import AddressBook
from entry import *
from fileIO import *
from app import App

#setup basic app
app = App()

#Open an existing AddressBook

app.open_address_book('docs/sample_input.json')
entry = app.open_address_books.get(0).get('object').get_entries().get(0).get_values().copy()
entry['first_name'] = '123'
entry['last_name'] = '456'
app.create_entry(0,entry)
app.save_address_book(0,'docs/testme.json')

# #printing number of open addressbooks
# print('Number of open AddressBooks =', app.address_book_count)
# print('Current AddressBook = ', app.open_address_books)
# entry = app.open_address_books.get(0).get('object').get_entries().get(0).get_values()
# # print(app.open_address_books.get(0).get('object'))

# entry['custom_fields'] = {'notes':{'label':'notes' , 'value': 'DunnderMiflin','global' : True, 'applied_globally': False}}
# app.update_entry(entry)
# app.save_address_book(0,'docs/testme.json')
# app.export_tsv(0,'docs/testme.tsv')
# print(app.open_address_books.get(0).get('object').get_meta('numEntries'))
# # # #removing recent entry
# app.delete_entry(0,1)
# print(app.open_address_books.get(0).get('object').get_meta('numEntries'))

# #create an empty AddressBook
# app.create_address_book('AD 1')

# #printing number of open addressbooks
# print('Number of open AddressBooks =', app.address_book_count)
# print('Current AddressBook = ', app.open_address_books)

# #creating an entry for newly created address book
# app.create_entry(0,{'hish':'two'})

# #performing "save as" operation
# app.save_address_book(0,'docs/testme.json')



# #printing entry of newly opened address Book
# print('Number of open AddressBooks =', app.address_book_count)
# print('Entry 0 of AD 1= ', app.open_address_books.get(1).get('object').get_entry(0))

# # #removing recent entry
# # app.delete_entry(0,1)

# #performing "save" operation
# app.save_address_book(0)

# #perform the save operation
# app.save_address_book(0)

# #get json of addressbook 0
# print('TO JSON TESTING = ',app.get_address_book(0))

# #import from tsv to file
# app.import_tsv(0,'docs/sample_input.tsv')

# #perform the save operation
# app.save_address_book(0)

# #creating an entry for newly created address book
# # app.create_entry(0,{'hish':'two'})

# #performing "save as" operation
# app.save_address_book(0,'docs/testme.json')

# #editing recently saved addressbook
# # app.create_entry(0,{'hish':'three'})

# #performing "save" operation
# app.save_address_book(0)

# #print remaining entry
# entry_dict = app.open_address_books.get(0).get('object').get_entry(0).get_values()
# print('Entry 0 of AD 0= ',entry_dict)

# #update that entry
# # entry_dict['hish'] = 'five'
# # app.update_entry(entry_dict)

# #add a custom field
# dict1 = {}
# dict2 = {}

# dict1['label'] = 'greengrocery'
# dict1['value'] = '10'
# dict1['global'] = 'yes'

# dict2['whatever'] = dict1
# app.open_address_books.get(0).get('object').get_entry(0).set_value('custom_fields',dict2)


# #performing "save" operation
# app.save_address_book(0)

#export to tsv
# app.export_tsv(0,'docs/exporttsv.tsv')

