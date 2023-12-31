import numpy as np
import csv

"""
Connections and neurones are built using information and data from WormAtlas: 
https://www.wormatlas.org/neurons/Individual%20Neurons/Neuronframeset.html [Last Accessed: 21/12/2023]
"""

class Neuron:
    def __init__(self, name: str, neuron_types: list):
        self.name = name
        self.neuron_types = neuron_types
        self.weights = []  # List of weights for connections to other neurons
        self.bias = np.random.rand()  # Initialize bias with random values
        self.output = None  # Placeholder for neuron output

    def add_connection(self, neuron, weight):
        # Add a connection to another neuron with a given weight
        self.weights.append((neuron, weight))

adal = Neuron("ADAL", ["interneuron"])
adar = Neuron("ADAR", ["interneuron"])
adel = Neuron("ADEL", ["sensory neuron"])
ader = Neuron("ADER", ["sensory neuron"])
adfl = Neuron("ADFL", ["sensory neuron"])
adfr = Neuron("ADFR", ["sensory neuron"])
adll = Neuron("ADLL", ["sensory neuron"])
adlr = Neuron("ADLR", ["sensory neuron"])
afdl = Neuron("AFDL", ["sensory neuron"])
afdr = Neuron("AFDR", ["sensory neuron"])
aial = Neuron("AIAL", ["interneuron"])
aiar = Neuron("AIAR", ["interneuron"])
aibl = Neuron("AIBL", ["interneuron"])
aibr = Neuron("AIBR", ["interneuron"])
aiml = Neuron("AIML", ["interneuron"])
aimr = Neuron("AIMR", ["interneuron"])
ainl = Neuron("AINL", ["interneuron"])
ainr = Neuron("AINR", ["interneuron"])
aiyl = Neuron("AIYL", ["interneuron"])
aiyr = Neuron("AIYR", ["interneuron"])
aizl = Neuron("AIZL", ["interneuron"])
aizr = Neuron("AIZR", ["interneuron"])
ala = Neuron("ALA", ["interneuron", "sensory neuron"])
alml = Neuron("ALML", ["sensory neuron"])
almr = Neuron("ALMR", ["sensory neuron"])
alnl = Neuron("ALNL", ["sensory neuron"])
alnr = Neuron("ALNR", ["sensory neuron"])
aqr = Neuron("AQR", ["sensory neuron"])
as1 = Neuron("AS1", ["motor neuron"])
as2 = Neuron("AS2", ["motor neuron"])
as3 = Neuron("AS3", ["motor neuron"])
as4 = Neuron("AS4", ["motor neuron"])
as5 = Neuron("AS5", ["motor neuron"])
as6 = Neuron("AS6", ["motor neuron"])
as7 = Neuron("AS7", ["motor neuron"])
as8 = Neuron("AS8", ["motor neuron"])
as9 = Neuron("AS9", ["motor neuron"])
as10 = Neuron("AS10", ["motor neuron"])
as11 = Neuron("AS11", ["motor neuron"])
asel = Neuron("ASEL", ["sensory neuron"])
aser = Neuron("ASER", ["sensory neuron"])
asgl = Neuron("ASGL", ["sensory neuron"])
asgr = Neuron("ASGR", ["sensory neuron"])
ashl = Neuron("ASHL", ["sensory neuron"])
ashr = Neuron("ASHR", ["sensory neuron"])
asil = Neuron("ASIL", ["sensory neuron"])
asir = Neuron("ASIR", ["sensory neuron"])
asjl = Neuron("ASJL", ["sensory neuron"])
asjr = Neuron("ASJR", ["sensory neuron"])
askl = Neuron("ASKL", ["sensory neuron"])
askr = Neuron("ASKR", ["sensory neuron"])
aual = Neuron("AUAL", ["interneuron"])
auar = Neuron("AUAR", ["interneuron"])
aval = Neuron("AVAL", ["interneuron"])
avar = Neuron("AVAR", ["interneuron"])
avbl = Neuron("AVBL", ["interneuron"])
avbr = Neuron("AVBR", ["interneuron"])
avdl = Neuron("AVDL", ["interneuron"])
avdr = Neuron("AVDR", ["interneuron"])
avel = Neuron("AVEL", ["interneuron"])
aver = Neuron("AVER", ["interneuron"])
avfl = Neuron("AVFL", ["interneuron"])
avfr = Neuron("AVFR", ["interneuron"])
avg = Neuron("AVG", ["interneuron"])
avhl = Neuron("AVHL", ["interneuron"])
avhr = Neuron("AVHR", ["interneuron"])
avjl = Neuron("AVJL", ["interneuron"])
avjr = Neuron("AVJR", ["interneuron"])
avkl = Neuron("AVKL", ["interneuron"])
avkr = Neuron("AVKR", ["interneuron"])
avl = Neuron("AVL", ["interneuron", "motor neuron"])
avm = Neuron("AVM", ["sensory neuron"])
awal = Neuron("AWAL", ["sensory neuron"])
awar = Neuron("AWAR", ["sensory neuron"])
awbl = Neuron("AWBL", ["sensory neuron"])
awbr = Neuron("AWBR", ["sensory neuron"])
awcl = Neuron("AWCL", ["sensory neuron"])
awcr = Neuron("AWCR", ["sensory neuron"])
bagl = Neuron("BAGL", ["sensory neuron"])
bagr = Neuron("BAGR", ["sensory neuron"])
bdul = Neuron("BDUL", ["interneuron"])
bdur = Neuron("BDUR", ["interneuron"])
canl = Neuron("CANL", ["unknown"])
canr = Neuron("CANR", ["unknown"])
cepdl = Neuron("CEPDL", ["sensory neuron"])
cepdr = Neuron("CEPDR", ["sensory neuron"])
cepvl = Neuron("CEPVL", ["sensory neuron"])
cepvr = Neuron("CEPVR", ["sensory neuron"])
da1 = Neuron("DA1", ["motor neuron"])
da2 = Neuron("DA2", ["motor neuron"])
da3 = Neuron("DA3", ["motor neuron"])
da4 = Neuron("DA4", ["motor neuron"])
da5 = Neuron("DA5", ["motor neuron"])
da6 = Neuron("DA6", ["motor neuron"])
da7 = Neuron("DA7", ["motor neuron"])
da8 = Neuron("DA8", ["motor neuron"])
da9 = Neuron("DA9", ["motor neuron"])
db1 = Neuron("DB1", ["motor neuron", "sensory neuron"])
db2 = Neuron("DB2", ["motor neuron", "sensory neuron"])
db3 = Neuron("DB3", ["motor neuron", "sensory neuron"])
db4 = Neuron("DB4", ["motor neuron", "sensory neuron"])
db5 = Neuron("DB5", ["motor neuron", "sensory neuron"])
db6 = Neuron("DB6", ["motor neuron", "sensory neuron"])
db7 = Neuron("DB7", ["motor neuron", "sensory neuron"])
dd1 = Neuron("DD1", ["motor neuron"])
dd2 = Neuron("DD2", ["motor neuron"])
dd3 = Neuron("DD3", ["motor neuron"])
dd4 = Neuron("DD4", ["motor neuron"])
dd5 = Neuron("DD5", ["motor neuron"])
dd6 = Neuron("DD6", ["motor neuron"])
dva = Neuron("DVA", ["interneuron", "sensory neuron"])
dvb = Neuron("DVB", ["motor neuron", "interneuron"])
dvc = Neuron("DVC", ["interneuron"])
flpl = Neuron("FLPL", ["sensory neuron"])
flpr = Neuron("FLPR", ["sensory neuron"])
hsnl = Neuron("HSNL", ["motor neuron"])
hsnr = Neuron("HSNR", ["motor neuron"])
i1l = Neuron("I1L", ["interneuron"])
i1r = Neuron("I1R", ["interneuron"])
i2l = Neuron("I2L", ["interneuron"])
i2r = Neuron("I2R", ["interneuron"])
i3 = Neuron("I3", ["interneuron"])
i4 = Neuron("I4", ["interneuron"])
i5 = Neuron("I5", ["interneuron"])
i6 = Neuron("I6", ["interneuron"])
il1dl = Neuron("IL1DL", ["sensory neuron", "motor neuron", "interneuron"])
il1dr = Neuron("IL1DR", ["sensory neuron", "motor neuron", "interneuron"])
il1l = Neuron("IL1L", ["sensory neuron", "motor neuron", "interneuron"])
il1r = Neuron("IL1R", ["sensory neuron", "motor neuron", "interneuron"])
il1vl = Neuron("IL1VL", ["sensory neuron", "motor neuron", "interneuron"])
il1vr = Neuron("IL1VR", ["sensory neuron", "motor neuron", "interneuron"])
il2dl = Neuron("IL2DL", ["sensory neuron"])
il2dr = Neuron("IL2DR", ["sensory neuron"])
il2l = Neuron("IL2L", ["sensory neuron"])
il2r = Neuron("IL2R", ["sensory neuron"])
il2vl = Neuron("IL2VL", ["sensory neuron"])
il2vr = Neuron("IL2VR", ["sensory neuron"])
lual = Neuron("LUAL", ["interneuron"])
luar = Neuron("LUAR", ["interneuron"])
m1 = Neuron("M1", ["motor neuron"])
m2l = Neuron("M2L", ["motor neuron"])
m2r = Neuron("M2R", ["motor neuron"])
m3l = Neuron("M3L", ["motor neuron"])
m3r = Neuron("M3R", ["motor neuron"])
m4 = Neuron("M4", ["motor neuron"])
m5 = Neuron("M5", ["motor neuron"])
mcl = Neuron("MCL", ["motor neuron"])
mcr = Neuron("MCR", ["motor neuron"])
mi = Neuron("MI", ["motor neuron", "interneuron"])
nsml = Neuron("NSML", ["neurosecretory neuron", "motor neuron", "sensory neuron"])
nsmr = Neuron("NSMR", ["neurosecretory neuron", "motor neuron", "sensory neuron"])
olll = Neuron("OLLL", ["sensory neuron"])
ollr = Neuron("OLLR", ["sensory neuron"])
olqdl = Neuron("OLQDL", ["sensory neuron", "interneuron"])
olqdr = Neuron("OLQDR", ["sensory neuron", "interneuron"])
olqvl = Neuron("OLQVL", ["sensory neuron", "interneuron"])
olqvr = Neuron("OLQVR", ["sensory neuron", "interneuron"])
pda = Neuron("PDA", ["motor neuron"])
pdb = Neuron("PDB", ["motor neuron"])
pdel = Neuron("PDEL", ["sensory neuron"])
pder = Neuron("PDER", ["sensory neuron"])
phal = Neuron("PHAL", ["sensory neuron"])
phar = Neuron("PHAR", ["sensory neuron"])
phbl = Neuron("PHBL", ["sensory neuron"])
phbr = Neuron("PHBR", ["sensory neuron"])
phcl = Neuron("PHCL", ["sensory neuron"])
phcr = Neuron("PHCR", ["sensory neuron"])
plml = Neuron("PLML", ["sensory neuron"])
plmr = Neuron("PLMR", ["sensory neuron"])
plnl = Neuron("PLNL", ["sensory neuron"])
plnr = Neuron("PLNR", ["sensory neuron"])
pqr = Neuron("PQR", ["sensory neuron"])
pvcl = Neuron("PVCL", ["interneuron"])
pvcr = Neuron("PVCR", ["interneuron"])
pvdl = Neuron("PVDL", ["sensory neuron"])
pvdr = Neuron("PVDR", ["sensory neuron"])
pvm = Neuron("PVM", ["sensory neuron"])
pvnl = Neuron("PVNL", ["interneuron", "motor neuron"])
pvnr = Neuron("PVNR", ["interneuron", "motor neuron"])
pvpl = Neuron("PVPL", ["interneuron"])
pvpr = Neuron("PVPR", ["interneuron"])
pvql = Neuron("PVQL", ["interneuron"])
pvqr = Neuron("PVQR", ["interneuron"])
pvr = Neuron("PVR", ["interneuron"])
pvt = Neuron("PVT", ["interneuron"])
pvwl = Neuron("PVWL", ["interneuron"])
pvwr = Neuron("PVWR", ["interneuron"])
rial = Neuron("RIAL", ["interneuron"])
riar = Neuron("RIAR", ["interneuron"])
ribl = Neuron("RIBL", ["interneuron"])
ribr = Neuron("RIBR", ["interneuron"])
ricl = Neuron("RICL", ["interneuron"])
ricr = Neuron("RICR", ["interneuron"])
rid = Neuron("RID", ["motor neuron", "interneuron"])
rifl = Neuron("RIFL", ["interneuron"])
rifr = Neuron("RIFR", ["interneuron"])
rigl = Neuron("RIGL", ["interneuron"])
rigr = Neuron("RIGR", ["interneuron"])
rih = Neuron("RIH", ["interneuron"])
riml = Neuron("RIML", ["motor neuron", "interneuron"])
rimr = Neuron("RIMR", ["motor neuron", "interneuron"])
ripl = Neuron("RIPL", ["interneuron"])
ripr = Neuron("RIPR", ["interneuron"])
rir = Neuron("RIR", ["interneuron"])
ris = Neuron("RIS", ["interneuron"])
rivl = Neuron("RIVL", ["interneuron", "motor neuron"])
rivr = Neuron("RIVR", ["interneuron", "motor neuron"])
rmddl = Neuron("RMDDL", ["motor neuron"])
rmddr = Neuron("RMDDR", ["motor neuron"])
rmdl = Neuron("RMDL", ["motor neuron"])
rmdr = Neuron("RMDR", ["motor neuron"])
rmdvl = Neuron("RMDVL", ["motor neuron"])
rmdvr = Neuron("RMDVR", ["motor neuron"])
rmed = Neuron("RMED", ["motor neuron"])
rmel = Neuron("RMEL", ["motor neuron"])
rmer = Neuron("RMER", ["motor neuron"])
rmev = Neuron("RMEV", ["motor neuron"])
rmfl = Neuron("RMFL", ["motor neuron"])
rmfr = Neuron("RMFR", ["motor neuron"])
rmgl = Neuron("RMGL", ["interneuron"])
rmgr = Neuron("RMGR", ["interneuron"])
rmhl = Neuron("RMHL", ["motor neuron"])
rmhr = Neuron("RMHR", ["motor neuron"])
saadl = Neuron("SAADL", ["motor neuron", "interneuron"])
saadr = Neuron("SAADR", ["motor neuron", "interneuron"])
saavl = Neuron("SAAVL", ["motor neuron", "interneuron"])
saavr = Neuron("SAAVR", ["motor neuron", "interneuron"])
sabd = Neuron("SABD", ["motor neuron", "interneuron"])
sabvl = Neuron("SABVL", ["motor neuron", "interneuron"])
sabvr = Neuron("SABVR", ["motor neuron", "interneuron"])
sdql = Neuron("SDQL", ["interneuron", "sensory neuron"])
sdqr = Neuron("SDQR", ["interneuron", "sensory neuron"])
siadl = Neuron("SIADL", ["interneuron", "motor neuron"])
siadr = Neuron("SIADR", ["interneuron", "motor neuron"])
siavl = Neuron("SIAVL", ["interneuron", "motor neuron"])
siavr = Neuron("SIAVR", ["interneuron", "motor neuron"])
sibdl = Neuron("SIBDL", ["interneuron", "motor neuron"])
sibdr = Neuron("SIBDR", ["interneuron", "motor neuron"])
sibvl = Neuron("SIBVL", ["interneuron", "motor neuron"])
sibvr = Neuron("SIBVR", ["interneuron", "motor neuron"])
smbdl = Neuron("SMBDL", ["motor neuron"])
smbdr = Neuron("SMBDR", ["motor neuron"])
smbvl = Neuron("SMBVL", ["motor neuron"])
smbvr = Neuron("SMBVR", ["motor neuron"])
smddl = Neuron("SMDDL", ["motor neuron"])
smddr = Neuron("SMDDR", ["motor neuron"])
smdvl = Neuron("SMDVL", ["motor neuron"])
smdvr = Neuron("SMDVR", ["motor neuron"])
uradl = Neuron("URADL", ["motor neuron", "putative sensory neuron"])
uradr = Neuron("URADR", ["motor neuron", "putative sensory neuron"])
uravl = Neuron("URAVL", ["motor neuron", "putative sensory neuron"])
uravr = Neuron("URAVR", ["motor neuron", "putative sensory neuron"])
urbl = Neuron("URBL", ["interneuron"])
urbr = Neuron("URBR", ["interneuron"])
urxl = Neuron("URXL", ["sensory neuron", "interneuron"])
urxr = Neuron("URXR", ["sensory neuron", "interneuron"])
urydl = Neuron("URYDL", ["sensory neuron"])
urydr = Neuron("URYDR", ["sensory neuron"])
uryvl = Neuron("URYVL", ["sensory neuron"])
uryvr = Neuron("URYVR", ["sensory neuron"])
va1 = Neuron("VA1", ["motor neuron"])
va2 = Neuron("VA2", ["motor neuron"])
va3 = Neuron("VA3", ["motor neuron"])
va4 = Neuron("VA4", ["motor neuron"])
va5 = Neuron("VA5", ["motor neuron"])
va6 = Neuron("VA6", ["motor neuron"])
va7 = Neuron("VA7", ["motor neuron"])
va8 = Neuron("VA8", ["motor neuron"])
va9 = Neuron("VA9", ["motor neuron"])
va10 = Neuron("VA10", ["motor neuron"])
va11 = Neuron("VA11", ["motor neuron"])
va12 = Neuron("VA12", ["motor neuron"])
vb1 = Neuron("VB1", ["motor neuron", "sensory neuron"])
vb2 = Neuron("VB2", ["motor neuron", "sensory neuron"])
vb3 = Neuron("VB3", ["motor neuron", "sensory neuron"])
vb4 = Neuron("VB4", ["motor neuron", "sensory neuron"])
vb5 = Neuron("VB5", ["motor neuron", "sensory neuron"])
vb6 = Neuron("VB6", ["motor neuron", "sensory neuron"])
vb7 = Neuron("VB7", ["motor neuron", "sensory neuron"])
vb8 = Neuron("VB8", ["motor neuron", "sensory neuron"])
vb9 = Neuron("VB9", ["motor neuron", "sensory neuron"])
vb10 = Neuron("VB10", ["motor neuron", "sensory neuron"])
vb11 = Neuron("VB11", ["motor neuron", "sensory neuron"])
vc1 = Neuron("VC1", ["motor neuron"])
vc2 = Neuron("VC2", ["motor neuron"])
vc3 = Neuron("VC3", ["motor neuron"])
vc4 = Neuron("VC4", ["motor neuron"])
vc5 = Neuron("VC5", ["motor neuron"])
vc6 = Neuron("VC6", ["motor neuron"])
vd1 = Neuron("VD1", ["motor neuron"])
vd2 = Neuron("VD2", ["motor neuron"])
vd3 = Neuron("VD3", ["motor neuron"])
vd4 = Neuron("VD4", ["motor neuron"])
vd5 = Neuron("VD5", ["motor neuron"])
vd6 = Neuron("VD6", ["motor neuron"])
vd7 = Neuron("VD7", ["motor neuron"])
vd8 = Neuron("VD8", ["motor neuron"])
vd9 = Neuron("VD9", ["motor neuron"])
vd10 = Neuron("VD10", ["motor neuron"])
vd11 = Neuron("VD11", ["motor neuron"])
vd12 = Neuron("VD12", ["motor neuron"])
vd13 = Neuron("VD13", ["motor neuron"])

neurons = {
    "ADAL": adal,
    "ADAR": adar,
    "ADEL": adel,
    "ADER": ader,
    "ADFL": adfl,
    "ADFR": adfr,
    "ADLL": adll,
    "ADLR": adlr,
    "AFDL": afdl,
    "AFDR": afdr,
    "AIAL": aial,
    "AIAR": aiar,
    "AIBL": aibl,
    "AIBR": aibr,
    "AIML": aiml,
    "AIMR": aimr,
    "AINL": ainl,
    "AINR": ainr,
    "AIYL": aiyl,
    "AIYR": aiyr,
    "AIZL": aizl,
    "AIZR": aizr,
    "ALA": ala,
    "ALML": alml,
    "ALMR": almr,
    "ALNL": alnl,
    "ALNR": alnr,
    "AQR": aqr,
    "AS1": as1,
    "AS2": as2,
    "AS3": as3,
    "AS4": as4,
    "AS5": as5,
    "AS6": as6,
    "AS7": as7,
    "AS8": as8,
    "AS9": as9,
    "AS10": as10,
    "AS11": as11,
    "ASEL": asel,
    "ASER": aser,
    "ASGL": asgl,
    "ASGR": asgr,
    "ASHL": ashl,
    "ASHR": ashr,
    "ASIL": asil,
    "ASIR": asir,
    "ASJL": asjl,
    "ASJR": asjr,
    "ASKL": askl,
    "ASKR": askr,
    "AUAL": aual,
    "AUAR": auar,
    "AVAL": aval,
    "AVAR": avar,
    "AVBL": avbl,
    "AVBR": avbr,
    "AVDL": avdl,
    "AVDR": avdr,
    "AVEL": avel,
    "AVER": aver,
    "AVFL": avfl,
    "AVFR": avfr,
    "AVG": avg,
    "AVHL": avhl,
    "AVHR": avhr,
    "AVJL": avjl,
    "AVJR": avjr,
    "AVKL": avkl,
    "AVKR": avkr,
    "AVL": avl,
    "AVM": avm,
    "AWAL": awal,
    "AWAR": awar,
    "AWBL": awbl,
    "AWBR": awbr,
    "AWCL": awcl,
    "AWCR": awcr,
    "BAGL": bagl,
    "BAGR": bagr,
    "BDUL": bdul,
    "BDUR": bdur,
    "CANL": canl,
    "CANR": canr,
    "CEPDL": cepdl,
    "CEPDR": cepdr,
    "CEPVL": cepvl,
    "CEPVR": cepvr,
    "DA1": da1,
    "DA2": da2,
    "DA3": da3,
    "DA4": da4,
    "DA5": da5,
    "DA6": da6,
    "DA7": da7,
    "DA8": da8,
    "DA9": da9,
    "DB1": db1,
    "DB2": db2,
    "DB3": db3,
    "DB4": db4,
    "DB5": db5,
    "DB6": db6,
    "DB7": db7,
    "DD1": dd1,
    "DD2": dd2,
    "DD3": dd3,
    "DD4": dd4,
    "DD5": dd5,
    "DD6": dd6,
    "DVA": dva,
    "DVB": dvb,
    "DVC": dvc,
    "FLPL": flpl,
    "FLPR": flpr,
    "HSNL": hsnl,
    "HSNR": hsnr,
    "I1L": i1l,
    "I1R": i1r,
    "I2L": i2l,
    "I2R": i2r,
    "I3": i3,
    "I4": i4,
    "I5": i5,
    "I6": i6,
    "IL1DL": il1dl,
    "IL1DR": il1dr,
    "IL1L": il1l,
    "IL1R": il1r,
    "IL1VL": il1vl,
    "IL1VR": il1vr,
    "IL2DL": il2dl,
    "IL2DR": il2dr,
    "IL2L": il2l,
    "IL2R": il2r,
    "IL2VL": il2vl,
    "IL2VR": il2vr,
    "LUAL": lual,
    "LUAR": luar,
    "M1": m1,
    "M2L": m2l,
    "M2R": m2r,
    "M3L": m3l,
    "M3R": m3r,
    "M4": m4,
    "M5": m5,
    "MCL": mcl,
    "MCR": mcr,
    "MI": mi,
    "NSML": nsml,
    "NSMR": nsmr,
    "OLLL": olll,
    "OLLR": ollr,
    "OLQDL": olqdl,
    "OLQDR": olqdr,
    "OLQVL": olqvl,
    "OLQVR": olqvr,
    "PDA": pda,
    "PDB": pdb,
    "PDEL": pdel,
    "PDER": pder,
    "PHAL": phal,
    "PHAR": phar,
    "PHBL": phbl,
    "PHBR": phbr,
    "PHCL": phcl,
    "PHCR": phcr,
    "PLML": plml,
    "PLMR": plmr,
    "PLNL": plnl,
    "PLNR": plnr,
    "PQR": pqr,
    "PVCL": pvcl,
    "PVCR": pvcr,
    "PVDL": pvdl,
    "PVDR": pvdr,
    "PVM": pvm,
    "PVNL": pvnl,
    "PVNR": pvnr,
    "PVPL": pvpl,
    "PVPR": pvpr,
    "PVQL": pvql,
    "PVQR": pvqr,
    "PVR": pvr,
    "PVT": pvt,
    "PVWL": pvwl,
    "PVWR": pvwr,
    "RIAL": rial,
    "RIAR": riar,
    "RIBL": ribl,
    "RIBR": ribr,
    "RICL": ricl,
    "RICR": ricr,
    "RID": rid,
    "RIFL": rifl,
    "RIFR": rifr,
    "RIGL": rigl,
    "RIGR": rigr,
    "RIH": rih,
    "RIML": riml,
    "RIMR": rimr,
    "RIPL": ripl,
    "RIPR": ripr,
    "RIR": rir,
    "RIS": ris,
    "RIVL": rivl,
    "RIVR": rivr,
    "RMDDL": rmddl,
    "RMDDR": rmddr,
    "RMDL": rmdl,
    "RMDR": rmdr,
    "RMDVL": rmdvl,
    "RMDVR": rmdvr,
    "RMED": rmed,
    "RMEL": rmel,
    "RMER": rmer,
    "RMEV": rmev,
    "RMFL": rmfl,
    "RMFR": rmfr,
    "RMGL": rmgl,
    "RMGR": rmgr,
    "RMHL": rmhl,
    "RMHR": rmhr,
    "SAADL": saadl,
    "SAADR": saadr,
    "SAAVL": saavl,
    "SAAVR": saavr,
    "SABD": sabd,
    "SABVL": sabvl,
    "SABVR": sabvr,
    "SDQL": sdql,
    "SDQR": sdqr,
    "SIADL": siadl,
    "SIADR": siadr,
    "SIAVL": siavl,
    "SIAVR": siavr,
    "SIBDL": sibdl,
    "SIBDR": sibdr,
    "SIBVL": sibvl,
    "SIBVR": sibvr,
    "SMBDL": smbdl,
    "SMBDR": smbdr,
    "SMBVL": smbvl,
    "SMBVR": smbvr,
    "SMDDL": smddl,
    "SMDDR": smddr,
    "SMDVL": smdvl,
    "SMDVR": smdvr,
    "URADL": uradl,
    "URADR": uradr,
    "URAVL": uravl,
    "URAVR": uravr,
    "URBL": urbl,
    "URBR": urbr,
    "URXL": urxl,
    "URXR": urxr,
    "URYDL": urydl,
    "URYDR": urydr,
    "URYVL": uryvl,
    "URYVR": uryvr,
    "VA1": va1,
    "VA2": va2,
    "VA3": va3,
    "VA4": va4,
    "VA5": va5,
    "VA6": va6,
    "VA7": va7,
    "VA8": va8,
    "VA9": va9,
    "VA10": va10,
    "VA11": va11,
    "VA12": va12,
    "VB1": vb1,
    "VB2": vb2,
    "VB3": vb3,
    "VB4": vb4,
    "VB5": vb5,
    "VB6": vb6,
    "VB7": vb7,
    "VB8": vb8,
    "VB9": vb9,
    "VB10": vb10,
    "VB11": vb11,
    "VC1": vc1,
    "VC2": vc2,
    "VC3": vc3,
    "VC4": vc4,
    "VC5": vc5,
    "VC6": vc6,
    "VD1": vd1,
    "VD2": vd2,
    "VD3": vd3,
    "VD4": vd4,
    "VD5": vd5,
    "VD6": vd6,
    "VD7": vd7,
    "VD8": vd8,
    "VD9": vd9,
    "VD10": vd10,
    "VD11": vd11,
    "VD12": vd12,
    "VD13": vd13
}

# USING Neuronal Connectivity II: by L.R. Varshney, B.L. Chen, E. Paniagua, D.H. Hall and D.B. Chklovskii
# Part 2.1; webpage: https://www.wormatlas.org/neuronalwiring.html#Connectivitydata [Last Accessed: 21/12/2023]

# N1: Neuron 1 name
# N2: Neuron 2 name
# Type: type of synapse:
#   S: Send or output (Neuron 1 pre-synaptic to Neuron 2)
#   Sp: Send-poly (Neuron 1 is pre-synaptic to more than one postsynaptic partner.  Neuron 2 is just one of these post-synaptic neurons)
#   R: Receive or input (Neuron 1 is post-synaptic to Neuron 2)
#   Rp: Receive-poly (Neuron 1 is one of several post-synaptic partners of Neuron 2)
#   EJ: Electric junction
#   NMJ: Neuromuscular junction
# Nbr: Number of synapses between the given neuron pair

# Only considering chemical synapses. Structure of the list for the connectome:
#   [(nbr, neuron), (nbr, neuron), .., ..., (nbr, neuron)]
# example: "ADAL": [(1, "AIBL"), (2, "AIBR"), etc.]

connectome = {}

with open("/Users/ferran/Library/Mobile Documents/com~apple~CloudDocs/Documents/UCL/AI Soc/NEXUS LABS/c_elegans_proj/NeuronConnect.csv") as neurconnect:
    csvreader = csv.reader(neurconnect)
    header = next(csvreader)
    for row in csvreader:
        if row[2] == "S" or row[2] == "Sp":
            if row[0] in connectome:
                connectome[row[0]].append((row[3], row[1]))
            else:
                connectome[row[0]] = [(row[3], row[1])]

# # Connect neurons
# for source_neuron, target_neurons in connectome.items():
#     for target_neuron in target_neurons:
#         weight = np.random.rand()  # You may want to set weights based on biological knowledge
#         neurons[source_neuron].add_connection(neurons[target_neuron], weight)
