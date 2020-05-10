import io

def locally(INfile,OUTfile):
    OUTfile = io.StringIO(OUTfile)
    try:
        with open(OUTfile ,  mode = 'wb', encoding='utf-8') as OUTfile:
            OUTfile.write(INfile.read())
            INfile.close()
    except Exception as err:
        print(err)



def locally(INfile,OUTfile):
    try:
        with open(OUTfile ,  mode = 'wb', encoding='utf-8') as OUTfile:
            OUTfile.write(INfile.read())
            INfile.close()
    except Exception as err:
        print(err)

def locally(INfile,OUTfile):
    print(INfile.readable())
    print(OUTfile.writable())
    try:
        with open(OUTfile ,  mode = 'r+b' , encoding='utf-8') as OUTf:
            with open(INfile ,  mode = 'r+b' , encoding='utf-8') as INf:
                OUTf.write(INf.read())
#            INfile.close()
    except Exception as err:
        print(err)
