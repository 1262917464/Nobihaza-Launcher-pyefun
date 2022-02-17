import configparser

conf = configparser.RawConfigParser()

def load_lang():
    conf.read("config.ini")
    if "config" in conf and "lang" in conf['config']:
        return conf['config']['lang']
    else:
        return "eng"


def load_text(label):
    conf.read("lang\\" + load_lang() + ".ini",encoding="utf-8")
    return conf['text'][label].replace("\\n","\n")
