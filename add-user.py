import argparse
from Database import create_tables, Users as DB


parser = argparse.ArgumentParser(description='Add new user to deGram')

parser.add_argument('ig', help="Instagram username")
parser.add_argument('tg', help="Telegram username")

args = parser.parse_args()

ig = args.ig
tg = args.tg


user = DB.replace(
    ig=ig,
    tg=tg
).execute()
