import openpyxl
import modules.read

book = openpyxl.Workbook()
sheet = book.active

def write(cell,value):
    sheet[cell] = value
def save():
    book.save(modules.read.data[0].get('name'))
