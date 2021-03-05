from sys import argv
import os.path

class AppParams:
    def __init__(self):
        self.ID_TKN, self.DATA_TKN =  'id','data',
        self.NAME_TKN, self.ACCE_TKN,self.PROT_TKN =  'name', 'acc', 'prot'
        self.params = {self.DATA_TKN : None, self.ID_TKN : dict(),  'query' : []}
        self.queries = ["files", "totals", "header", "dnaseq" , "proteinlist", "proteinseq"]
        for a in argv[1:]:
            if a in self.queries or a.startswith("proteinseq="):
                 self.params['query'].append(a)
                 continue
            parts = a.split('=') if '=' in a else [None,None]
            if parts[0] == self.DATA_TKN: self.check_data_path(parts[1])
            elif parts[0] == self.ID_TKN: self.get_id(parts[1])
            else:
                print("command option '{}' invalid".format(a))
        
    def get_id(self:object,arg:str)->None:
        for idarg in arg.split():
            if ':' not in idarg:
                raise SyntaxError("id options need a value prefixed. Please verify option '{}'.".format(idarg))
            parts = idarg.split(':')
            if parts[0] in [self.ACCE_TKN,self.NAME_TKN,self.PROT_TKN]:
                self.params[self.ID_TKN][parts[0]] = parts[1]
            else:
                print("id option '{}' is invalid.".format(parts[0]))

    def check_data_path(self:object, path:str)->None:
        if not os.path.isdir(path):
            raise FileExistsError("ruta <{}> no existe.".format(path))
        else:
            self.params[self.DATA_TKN] = path
    
    def get_params(self)->dict:
        return self.params
