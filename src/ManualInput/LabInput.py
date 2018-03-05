import traceback
import src.ManualInput.InputFunctions as inf

def LabInput(db):
    cursor = db.cursor()

    LabName = inf.input_str_not_null('Input LabName please: ')
    LabCNPJ = inf.input_str_not_null('Input LabCNPJ please: ')
    LabOfficeAddress = inf.input_str('Input LabOfficeAddress please: ')
    LabContactEmail1 = inf.input_str('Input LabContactEmail1 please: ')
    LabContactEmail2 = inf.input_str('Input LabContactEmail2 please: ')
    LabContactPhone1 = inf.input_str('Input LabContactPhone1 please: ')
    LabContactPhone2 = inf.input_str('Input LabContactPhone2 please: ')
    LabContactFax = inf.input_str('Input LabContactFax please: ')

    to_db = [(LabName,LabCNPJ,LabOfficeAddress,LabContactEmail1,LabContactEmail2,
    LabContactPhone1,LabContactPhone2,LabContactFax)]

    try:
        cur.execute('''INSERT INTO Laboratories(LabName,LabCNPJ,
           LabOfficeAddress,LabContactEmail1,LabContactEmail2,
           LabContactPhone1,LabContactPhone2,LabContactFax)
           VALUES (?,?,?,?,?,?,?,?);''', to_db)
        print()
        db.commit('LabInput suceeded')
   except:
       db.rollback()
       print('LabInput failed')
       traceback.print_exc()
