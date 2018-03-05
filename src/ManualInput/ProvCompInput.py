import traceback
import src.ManualInput.InputFunctions as inf

def ProvCompInput(db):
    cursor = db.cursor()

    ProvCompName = inf.input_str_not_null('Input ProvCompName please: ')
    ProvCompCNPJ = inf.input_str_not_null('Input ProvCompCNPJ please: ')
    ProvOfficeAddress = inf.input_str('Input ProvOfficeAddress please: ')
    ProvContactEmail1 = inf.input_str('Input ProvContactEmail1 please: ')
    ProvContactEmail2 = inf.input_str('Input ProvContactEmail2 please: ')
    ProvContactPhone1 = inf.input_str('Input ProvContactPhone1 please: ')
    ProvContactPhone2 = inf.input_str('Input ProvContactPhone2 please: ')
    ProvContactFax = inf.input_str('Input ProvContactFax please: ')

    to_db = [(ProvCompName,ProvCompCNPJ,ProvOfficeAddress,ProvContactEmail1,
    ProvContactEmail2,ProvContactPhone1,ProvContactPhone2,ProvContactFax)]

    try:
        cursor.execute('''INSERT INTO ProviderCompany(ProvCompName,
           ProvCompCNPJ,ProvOfficeAddress,ProvContactEmail1,ProvContactEmail2,
           ProvContactPhone1,ProvContactPhone2,ProvContactFax)
           VALUES (?,?,?,?,?,?,?,?);''', to_db)
        print()
        db.commit('ProvCompInput suceeded')
   except:
       db.rollback()
       print('ProvCompInput failed')
       traceback.print_exc()
