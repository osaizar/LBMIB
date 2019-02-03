from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date, DateTime
import datetime
from database import Base
from user_database import User_Base

PERTSONA_DATA = ["bazkide_zbk","izena","abizena1","abizena2","email",\
                 "helbidea","herria","auzoa","telefono1","telefono2","nan",\
                 "jaiotze_data","kontu_korrontea","alta_data","baja_data",\
                 "alta","ord_kontutik", "sexua"]

PERTSONA_DATA_EXTRA = ["mota", "ikasketa", "baja_arrazoia", "prestutasuna"]

class Oharra(Base):
    __tablename__ = "oharra"
    id = Column(Integer, primary_key=True)
    izenburua = Column(String(250), nullable=False)
    oharra = Column(String(1000), nullable=False)
    pertsonaId = Column(Integer, ForeignKey("pertsona.id"))

    def __init__(self, izenburua, oharra, pertsonaId):
        self.izenburua = izenburua
        self.oharra = oharra
        self.pertsonaId = pertsonaId

    def serialize(self):
        return {"id" : self.id , "izenburua" : self.izenburua, "oharra" : self.oharra}

class Probintzia(Base):
    __tablename__ = "probintzia"
    id = Column(Integer, primary_key=True)
    izena = Column(String(250), nullable=False)
    izenaseo = Column(String(250), nullable=False)
    izena3 = Column(String(3), nullable=False)

    def __init__(self, id, izena, izenaseo, izena3):
        self.id = id
        self.izena = izena
        self.izenaseo = izenaseo
        self.izena3 = izena3

    def serialize(self):
        return {"id" : self.id , "data" : self.izena}

class Herria(Base):
    __tablename__ = "herria"
    id = Column(Integer, primary_key=True)
    probintziaId = Column(Integer, ForeignKey("probintzia.id"))
    izena = Column(String(250), nullable=False)
    izenaseo = Column(String(250), nullable=False)
    pk = Column(String(10), nullable=False)

    def __init__(self, id, probintziaId, izena, izenaseo, pk):
        self.id = id
        self.probintziaId = probintziaId
        self.izena = izena
        self.izenaseo = izenaseo
        self.pk = pk

    def serialize(self):
        return {"id" : self.id , "data" : self.izena, "probintzia" : self.probintziaId}

class BajaArrazoia(Base):
    __tablename__ = "baja_arrazoia"
    id = Column(Integer, primary_key=True)
    arrazoia = Column(String(250), nullable=False)

    def __init__(self, arrazoia):
        self.arrazoia = arrazoia

    def serialize(self):
        return {"id" : self.id , "data" : self.arrazoia}

class Mota(Base):
    __tablename__ = "mota"
    id = Column(Integer, primary_key=True)
    mota = Column(String(250), nullable=False)

    def __init__(self, mota):
        self.mota = mota

    def serialize(self):
        return {"id" : self.id , "data" : self.mota}

class Prestutasuna(Base):
    __tablename__ = "prestutasuna"
    id = Column(Integer, primary_key=True)
    prestutasuna = Column(String(250), nullable=False)

    def __init__(self, prestutasuna):
        self.prestutasuna = prestutasuna

    def serialize(self):
        return {"id" : self.id , "data" : self.prestutasuna}

class Ikasketa(Base):
    __tablename__ = "ikasketa"
    id = Column(Integer, primary_key=True)
    ikasketa = Column(String(250), nullable=False)

    def __init__(self, ikasketa):
        self.ikasketa = ikasketa

    def serialize(self):
        return {"id" : self.id, "data" : self.ikasketa}

class Pertsona(Base):
    __tablename__ = "pertsona"
    id = Column(Integer, primary_key=True)
    bazkide_zbk = Column(Integer)
    izena = Column(String(250), nullable=False)
    abizena1 = Column(String(250), nullable=False)
    abizena2 = Column(String(250), nullable=False)
    email = Column(String(250))
    helbidea = Column(String(500))
    herria = Column(Integer, ForeignKey("herria.id"))
    auzoa = Column(String(500))
    telefono1 = Column(String(20), nullable=False)
    telefono2 = Column(String(20))
    nan = Column(String(20))
    jaiotze_data = Column(Date)
    kontu_korrontea = Column(String(100))
    alta_data = Column(Date)
    baja_data = Column(Date)
    alta = Column(Boolean)
    ord_kontutik = Column(Boolean)
    sexua = Column(Boolean) # True -> Emakumea False -> Gizonezkoa

    def __init__(self, bazkide_zbk, izena, abizena1, abizena2, email, helbidea, \
                 herria, auzoa, telefono1, telefono2, nan, jaiotze_data, kontu_korrontea, \
                 alta_data, baja_data, alta, ord_kontutik, sexua):

        self.bazkide_zbk = bazkide_zbk
        self.izena = izena
        self.abizena1 = abizena1
        self.abizena2 = abizena2
        self.email = email
        self.helbidea = helbidea
        self.herria = herria
        self.auzoa = auzoa
        self.telefono1 = telefono1
        self.telefono2 = telefono2
        self.nan = nan
        self.jaiotze_data = jaiotze_data
        self.kontu_korrontea = kontu_korrontea
        self.alta_data = alta_data
        self.baja_data = baja_data
        self.alta = alta
        self.ord_kontutik = ord_kontutik
        self.sexua = sexua

    def check_values(self):
        for p in PERTSONA_DATA:
            if getattr(self, str(p)) == '':
                setattr(self, str(p), None)

        return self

    def serialize(self):
        import db_helper as db
        rt = {}
        baja_arrazoiak = []
        ikasketak = []
        prestutasuna = []
        motak = []

        m = db.get_pertsona_mota_by_pertsona_id(self.id)
        if m != None:
            motak = [e.mota for e in m]

        b = db.get_pertsona_baja_arrazoia_by_pertsona_id(self.id)
        if b != None:
            baja_arrazoiak = [e.baja_arrazoia for e in b]

        i = db.get_pertsona_ikasketa_by_pertsona_id(self.id)
        if i != None:
            ikasketak = [e.ikasketa for e in i]

        p = db.get_pertsona_prestutasuna_by_pertsona_id(self.id)
        if p != None:
            prestutasunak = [e.prestutasuna for e in p]

        for p in PERTSONA_DATA:
            if getattr(self, str(p)) == None:
                rt[p] = ""
            elif p == "ord_kontutik" or p == "alta":
                if str(getattr(self, p)) == "True":
                    rt[p] = "bai"
                else:
                    rt[p] = "ez"
            elif p == "sexua":
                if str(getattr(self, p)) == "True":
                    rt[p] = "emakumea"
                else:
                    rt[p] = "gizonezkoa"
            elif p == "alta_data" or p == "baja_data" or p == "jaiotze_data":
                rt[p] = str(getattr(self, p))
            elif p == "bazkide_zbk" and not 1 in motak:
                rt[p] = ""
            elif p == "herria":
                h = db.get_herria_by_id(getattr(self,p))
                if h == None:
                    rt[p] = ""
                else:
                    rt[p] = {"herria" : h.id, "probintzia" : h.probintziaId}
            else:
                rt[p] = getattr(self, p)

        rt["id"] = self.id
        rt["mota"] = motak
        rt["baja_arrazoia"] = baja_arrazoiak
        rt["ikasketa"] = ikasketak
        rt["prestutasuna"] = prestutasunak

        return rt

# Lotura Taulak

class PertsonaMota(Base):
    __tablename__ = "pertsona_mota"
    id = Column(Integer, primary_key=True)
    mota = Column(Integer, ForeignKey("mota.id"))
    pertsona = Column(Integer, ForeignKey("pertsona.id"))

    def __init__(self, pertsona, mota):
        self.pertsona = pertsona
        self.mota = mota

class PertsonaPrestutasuna(Base):
    __tablename__ = "pertsona_prestutasuna"
    id = Column(Integer, primary_key=True)
    prestutasuna = Column(Integer, ForeignKey("prestutasuna.id"))
    pertsona = Column(Integer, ForeignKey("pertsona.id"))

    def __init__(self, pertsona, prestutasuna):
        self.pertsona = pertsona
        self.prestutasuna = prestutasuna

class PertsonaIkasketa(Base):
    __tablename__ = "pertsona_ikasketa"
    id = Column(Integer, primary_key=True)
    ikasketa = Column(Integer, ForeignKey("ikasketa.id"))
    pertsona = Column(Integer, ForeignKey("pertsona.id"))

    def __init__(self, pertsona, ikasketa):
        self.pertsona = pertsona
        self.ikasketa = ikasketa

class PertsonaBajaArrazoia(Base):
    __tablename__ = "pertsona_baja_arrazoia"
    id = Column(Integer, primary_key=True)
    baja_arrazoia = Column(Integer, ForeignKey("baja_arrazoia.id"))
    pertsona = Column(Integer, ForeignKey("pertsona.id"))

    def __init__(self, pertsona, baja_arrazoia):
        self.pertsona = pertsona
        self.baja_arrazoia = baja_arrazoia

# Web aplikazioko administrazioko taulak:

class User(User_Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    permission_level = Column(Integer, nullable=False) # 0 = Ez aktibatuta 1 = Irakurri 2 = Idatzi 3 = Admin
    password_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, username, email, password, permission_level):
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        self.permission_level = permission_level

    def check_password_expired(self):
        cur_time = datetime.datetime.utcnow()
        expire_date = self.password_date + datetime.timedelta(days=365) # pasahizak urte bat irauten du
        if cur_time > expire_date:
            return True
        else:
            return False

    def serialize(self):
        return {"id" : self.id , "username" : self.username, "email" : self.email, "permission" : self.permission_level, "name" : self.name}

class Session(User_Base):
    __tablename__ = "session"
    user = Column(Integer, ForeignKey("user.id"), primary_key=True)
    token = Column(String(20), nullable=False)
    token_date = Column(DateTime, default=datetime.datetime.utcnow)

    def __init__(self, user, token):
        self.user = user
        self.token = token

    def check_token_expired(self):
        cur_time = datetime.datetime.utcnow()
        expire_date = self.token_date + datetime.timedelta(days=2) # tokenak 2 egun irauten ditu
        if cur_time > expire_date:
            return True
        else:
            return False
