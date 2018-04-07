import traceback
from src.setup.DBCreate import *
from src.setup.DBPopulate import *
from  src.setup import SQLTables as tb

def createDB(db):
    cursor = db.cursor()

    command = createTableCommand(tb.labsTable)
    try:
        cursor.execute(command)
        db.commit()
        print('Laboratory table created')
    except Exception as e:
        db.rollback()
        print('Laboratory table failed')
        traceback.print_exc()

    command = createTableCommand(tb.provsTable)
    try:
        cursor.execute(command)
        db.commit()
        print('Provider table created')
    except Exception as e:
        db.rollback()
        print('Provider table failed')
        traceback.print_exc()

    command = createTableCommand(tb.teraClassTable)
    try:
        cursor.execute(command)
        db.commit()
        print('TeraClass table created')
    except Exception as e:
        db.rollback()
        print('TeraClass table failed')
        traceback.print_exc()

    command = createTableCommand(tb.listTribTable)
    try:
        cursor.execute(command)
        db.commit()
        print('ListaTributaria table created')
    except Exception as e:
        db.rollback()
        print('ListaTributaria table failed')
        traceback.print_exc()

    command = createTableCommand(tb.prodsTable)
    try:
        cursor.execute(command)
        db.commit()
        print('Product table created')
    except Exception as e:
        db.rollback()
        print('Product table failed')
        traceback.print_exc()

    command = createTableCommand(tb.stockTable)
    try:
        cursor.execute(command)
        db.commit()
        print('Stock table created')
    except Exception as e:
        db.rollback()
        print('Stock table failed')
        traceback.print_exc()

    command = createTableCommand(tb.NFeTable)
    try:
        cursor.execute(command)
        db.commit()
        print('NFe table created')
    except Exception as e:
        db.rollback()
        print('NFe table failed')
        traceback.print_exc()

def populateDB(db):
    cursor = db.cursor()
    try:
        populateListaTributaria(cursor) #Test-only, add tributary info later
        db.commit()
        print('ListaTributaria table populated')
    except Exception as e:
        db.rollback()
        print('ListaTributaria populate failed')
        traceback.print_exc()

    try:
        dataFrame = populateLabs(cursor) #Test-only, add tributary info later
        db.commit()
        print('Laboratory table populated')
    except Exception as e:
        db.rollback()
        print('Laboratory populate failed')
        traceback.print_exc()

    try:
        dataFrame = populateTeraClass(cursor) #Test-only, add tributary info later
        db.commit()
        print('TeraClass table populated')
    except Exception as e:
        db.rollback()
        print('TeraClass populate failed')
        traceback.print_exc()

    try:
        dataFrame = populateProducts(cursor) #Test-only, add tributary info later
        db.commit()
        print('Product table populated')
        return dataFrame
    except Exception as e:
        db.rollback()
        print('Product populate failed')
        traceback.print_exc()
