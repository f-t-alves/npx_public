from src.setup.HighCommands import *
import sqlite3
import os

os.makedirs('data',exist_ok=True)

db = sqlite3.connect('data/testdb.db')

createDB(db)
