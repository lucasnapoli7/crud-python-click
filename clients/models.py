import uuid #Modulo para generar ids únicas

class Client:
    
    def __init__(self, name, company, email, position, uid=None):
        self.name = name
        self.company = company
        self.email = email
        self.position = position
        self.uid = uid or uuid.uuid4() #Estandar de la industria, para generar ids únicos, en el caso que no se pase un id de forma manual se generará automaticamente con dicha libreria
    
    def to_dict(self):
        return vars(self) #Representa como diccionario nuestro objeto, para poder escribirlo en disco ya que usamos csv
    
    @staticmethod #Metodo estático, es método que se puede ejecutar sin necesidad de una instancia de clase
    #Lo utilizaremos para declarar el esquema
    def schema():
        return['name', 'company', 'email', 'position', 'uid']
    