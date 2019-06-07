from janome.tokenizer import Tokenizer
from os.path import join, dirname
from dotenv import load_dotenv
import os
import scraping_web

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

a = scraping_web.scraping("%s" % os.environ["FUN_PASSWORD"], "%s" % os.environ["FUN_MAIL"])
a.login()
a.kyuukou()
a.quit_Browser()

t = Tokenizer()
text_array = a.text_array

for text in text_array:
    print(text)