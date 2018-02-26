from src.setup.DBCreate import *
import traceback

def createDB(db):
    cursor = db.cursor()
    try:
        createLaboratoryTable(cursor)
        db.commit()
        print('Laboratory table created')
    except Exception as e:
        db.rollback()
        print('Laboratory table failed')
        traceback.print_exc()

    try:
        createProviderTable(cursor)
        db.commit()
        print('Provider table created')
    except Exception as e:
        db.rollback()
        print('Provider table failed')
        traceback.print_exc()

    try:
        createTerapeuticClassTable(cursor)
        db.commit()
        print('TeraClass table created')
    except Exception as e:
        db.rollback()
        print('TeraClass table failed')
        traceback.print_exc()

    try:
        createListaTributaria(cursor)
        db.commit()
        print('ListaTributaria table created')
    except Exception as e:
        db.rollback()
        print('ListaTributaria table failed')
        traceback.print_exc()

    try:
        createProductTable(cursor)
        db.commit()
        print('Product table created')
    except Exception as e:
        db.rollback()
        print('Product table failed')
        traceback.print_exc()

    try:
        populateListaTributaria(cursor) #Test-only, add tributary info later
        db.commit()
        print('ListaTributaria table populated')
    except Exception as e:
        db.rollback()
        print('ListaTributaria populate failed')
        traceback.print_exc()
