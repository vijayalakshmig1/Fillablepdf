import datetime
from fillpdf import fillpdfs

form_field = list(fillpdfs.get_form_fields('Fillable form(1).pdf').keys())

print(form_field)

cus=123
bus=456

data_dict={
    form_field[0]:cus,
    form_field[1]:cus,
    form_field[2]:cus,
    form_field[3]:cus,
    form_field[4]:cus,
    form_field[5]:cus,
    form_field[6]:cus,
    form_field[7]:cus,
    form_field[8]:cus,
    form_field[9]:cus,
    form_field[10]:bus,
    form_field[11]:bus,
    form_field[12]:bus,
    form_field[13]:bus,
    form_field[14]:bus,
    form_field[15]:bus,
    form_field[16]:bus,
    form_field[17]:bus,
    form_field[18]:bus
}

fillpdfs.write_fillable_pdf('Fillable form(1).pdf','new.pdf',data_dict)
