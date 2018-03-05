import traceback
import InputFunctions as inf

def MedInput(db):
    cursor = db.cursor()

    EAN = inf.get_valid_barcode('Please enter your BarCode: ')
    ProdName = inf.input_str_not_null('Please enter your ProdName: ')
    LabID = inf.get_int_value('Please enter your LabID: ')
    PrinAtivo = inf.input_str_not_null('Please enter your PrinAtivo:')
    CodGGREM = inf.get_int_value_skip('Please enter your CodGGREM: ')
    Registro = inf.get_int_value('Please enter your Registro: ')
    Description = inf.input_str_not_null('Please enter your Description:')
    TeraClassID = input('Please enter your TeraClassID:')
    ProdType = inf.input_str_not_null('Please enter your ProdType:')
    PF0p = inf.get_float_value_skip('Please enter your PF0p:')
    PF12p = inf.get_float_value_skip('Please enter your PF12p:')
    PF17p = inf.get_float_value_skip('Please enter your PF17p:')
    PF17p_ALC = inf.get_float_value_skip('Please enter your PF17p_ALC:')
    PF17p5 = inf.get_float_value_skip('Please enter your PF17p5:')
    PF17p5_ALC = inf.get_float_value_skip('Please enter your PF17p5_ALC:')
    PF18p = inf.get_float_value_skip('Please enter your PF18p:')
    PF18p_ALC = inf.get_float_value_skip('Please enter your PF18p_ALC:')
    PF20p = inf.get_float_value_skip('Please enter your PF20p:')
    PMC0p = inf.get_float_value_skip('Please enter your PMC0p:')
    PMC12p = inf.get_float_value_skip('Please enter your PMC12p:')
    PMC17p = inf.get_float_value_skip('Please enter your PMC17p:')
    PMC17p_ALC = inf.get_float_value_skip('Please enter your PMC17p_ALC:')
    PMC17p5 = inf.get_float_value_skip('Please enter your PMC17p5:')
    PMC17p5_ALC = inf.get_float_value_skip('Please enter your PMC17p5_ALC:')
    PMC18p = inf.get_float_value_skip('Please enter your PMC18p:')
    PMC18p_ALC = inf.get_float_value_skip('Please enter your PMC18p_ALC:')
    PMC20p = inf.get_float_value_skip('Please enter your PMC20p:')
    RestHosp = inf.get_int_value('Please enter your RestHosp:')
    CAP = inf.get_int_value('Please enter your CAP:')
    CONFAZ87 = inf.get_int_value('Please enter your CONFAZ87:')
    AnalRecur = inf.get_int_value('Please enter your AnalRecur:')
    ListaTribID = inf.get_int_value('Please enter your ListaTribID:')
    Comerc2016 = inf.get_int_value_skip('Please enter your Comerc2016:')
    Tarja = inf.get_int_value('Please enter your Tarja:')


    to_db =[(EAN,ProdName,LabID,
    PrinAtivo,CodGGREM,Registro,
    Description,TeraClassID,ProdType,PF0p,PF12p,PF17p,PF17p_ALC,
    PF17p5,PF17p5_ALC,PF18p,PF18p_ALC,PF20p,PMC0p,PMC12p,PMC17p,
    PMC17p_ALC,PMC17p5,PMC17p5_ALC,PMC18p,
    PMC18p_ALC,PMC20p,RestHosp,CAP,CONFAZ87,AnalRecur,
    ListaTribID,Comerc2016,Tarja)]

    try:
        cursor.executemany('''INSERT INTO Products VALUES (?,?,?,?,?,?,?,?,?,?,?
           ,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);''', to_db)
        print('MedInput succeeded')
        db.commit()
    except:
        db.rollback()
        print('MedInput failed')
        traceback.print_exc()
