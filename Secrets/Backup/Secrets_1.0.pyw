import hashlib, tkinter, base64, shutil, subprocess
from PIL import Image, ImageTk, ImageSequence
import time, os, pyautogui
from functools import partial
from tkinter import ttk
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from tkinter import scrolledtext
from cryptography.fernet import Fernet

registrer = False

#This section decides how big the GUI window should be out from the monitor resolution
HEIGHT = 480 
WIDTH = 480

class App:
    def __init__(self, parent):
        if not os.path.exists('bin'):
            os.mkdir('bin')
        if not os.path.exists('bin\\giphy.gif'):
            if os.path.exists('Backup_files\\bin\\giphy.gif'):
                shutil.copyfile('Backup_files\\bin\\giphy.gif','bin\\giphy.gif')
            else:
                shutil.copyfile('Backup\\bin\\giphy.gif','bin\\giphy.gif')
        if not os.path.exists('bin\\Bruker.txt'):
            if not os.path.exists('Backup_files\\bin\\Bruker.txt'):
                with open('bin\\Bruker.txt','w') as f:
                    f.write('Brukere' + '\n')
            else:
                shutil.copyfile('Backup_files\\bin\\Bruker.txt','bin\\Bruker.txt')
        self.parent = parent
        self.canvas = tkinter.Canvas(parent, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.sequence = [ImageTk.PhotoImage(img)
                            for img in ImageSequence.Iterator(
                                    Image.open(
                                    r'bin\giphy.gif'))]
        self.image = self.canvas.create_image(240,240, image=self.sequence[0])
        self.animate(1)
    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter+1) % len(self.sequence)))

def generate_key():
    msgU = usernameEntry.get()
    msgP = passwordEntry.get()
    msg = msgU + ':' + msgP
    hsh = hashlib.sha512()
    hsh.update(msg.encode('utf-8'))
    hshDigest = hsh.hexdigest()
    with open('bin\\Bruker.txt','r') as f:
        lines = f.readlines()
        for i in range(len(lines)):
            linje = lines[i]
            bruker = linje[9:137]
            salt = linje[143:229]
            if hshDigest in bruker:
                bruker_update = bruker
                salt_update = salt
    salt_update = salt_update.encode('utf-8')
    bruker_update = bruker_update.encode('utf-8')
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt_update,
    iterations=100000,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(bruker_update))
    key = key.decode('utf-8')
    return key

def backup():
    if not os.path.exists('Backup_files\\bin'):
        shutil.copytree('bin', 'Backup_files\\bin')
    if not os.path.exists('Backup_files\\Brukere'):
        shutil.copytree('Brukere', 'Backup_files\\Brukere')
    t0 = time.time()
    filnavn1 = os.path.join('Backup_files\\junk',str(t0))
    os.mkdir(filnavn1)
    junk1 = os.path.join(filnavn1,'bin')
    junk2 = os.path.join(filnavn1,'Brukere')
    os.rename('Backup_files\\bin',junk1)
    os.rename('Backup_files\\Brukere',junk2)
    shutil.copytree('bin', 'Backup_files\\bin')
    shutil.copytree('Brukere', 'Backup_files\\Brukere')
    os.chmod('Backup_files\\bin\\Bruker.txt', 0o000)
    liste = os.listdir('Backup_files\\Brukere')
    for i in range(len(liste)):
        filename = os.path.join('Backup_files\\Brukere',liste[i])
        os.chmod(filename, 0o000)
        filnavn = os.path.join('Brukere',liste[i])
        os.chmod(filnavn, 0o000)
    try:
        os.chmod('bin\\Bruker.txt', 0o000)
        os.chmod('bin',0o000)
        os.chmod('Brukere',0o000)
        os.chmod('Backup_files\\bin',0o000)
        os.chmod('Backup_files\\Brukere',0o000)
    except:
        SystemError

def encrypt(username,root3,masterpassword):
    i = 0
    try:
        os.chmod('bin',0o777)
        os.chmod('Brukere',0o777)
        os.chmod('bin\\Bruker.txt', 0o777)
        os.chmod('Backup_files\\bin',0o777)
        os.chmod('Backup_files\\Brukere',0o777)
        os.chmod('Backup_files\\bin\\Bruker.txt',0o777)
    except:
        SystemError
    with open('bin\\Bruker.txt','r') as f:
        lines = f.readlines()
    while i <= len(lines):
        linje = lines[i]
        verdi = linje[9:137]
        if verdi == masterpassword:
            salt = linje[143:231]
            break
        else:
            i += 1
    msgU_update = username.encode('utf-8')
    salt_update = salt.encode('utf-8')
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt_update,
    iterations=85309,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(msgU_update))
    key_update = key.decode('utf-8')
    filnavn = key_update + '.txt'
    path = os.path.join('Brukere',filnavn)
    try:
        os.chmod(path,0o777)
        path2 = os.path.join('Backup_files\\Brukere',filnavn)
        os.chmod(path2,0o777)
        os.chmod('Backup_files\\bin\\Bruker.txt',0o777)
    except:
        SystemError
    M = T.get("1.0","end-1c")
    M = M.encode('utf-8')
    f = Fernet(key)
    encrypted = f.encrypt(M)
    encrypted = encrypted.decode('utf-8')
    with open(path,'w') as f:
        f.write(encrypted)
    backup()
    root3.destroy()
    
    
def decrypt(username,masterpassword,root3):
    i = 0
    with open('bin\\Bruker.txt','r') as f:
        lines = f.readlines()
    while i <= len(lines):
        linje = lines[i]
        verdi = linje[9:137]
        if verdi == masterpassword:
            salt = linje[143:231]
            break
        else:
            i += 1
    msgU_update = username.encode('utf-8')
    salt_update = salt.encode('utf-8')
    kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt_update,
    iterations=85309,
    backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(msgU_update))
    key_update = key.decode('utf-8')
    filnavn = key_update + '.txt'
    path = os.path.join('Brukere',filnavn)
    with open(path,'r') as f:
        lines = f.read()
    if lines == '':
        return lines
    lines = lines.encode('utf-8')
    f = Fernet(key)
    try:
        decrypted = f.decrypt(lines)
    except:
        troubleshoot(masterpassword,username,None,True)
        pyautogui.alert('Filen er korrupt og har blitt gjennopprettet' + '\n' + 'Start programmet på nytt')
        root3.destroy()
    decrypted = decrypted.decode('utf-8')
    try:
        os.chmod(path, 0o000)
        path2 = os.path.join('Backup_files\\Brukere',filnavn)
        os.chmod(path2, 0o000)
        os.chmod('bin\\Bruker.txt', 0o000)
        os.chmod('Backup_files\\bin\\Bruker.txt', 0o000)
        os.chmod('bin',0o000)
        os.chmod('Brukere',0o000)
        os.chmod('Backup_files\\bin',0o000)
        os.chmod('Backup_files\\Brukere',0o000)
    except:
        SystemError
    return decrypted

def slett():
    T.delete("1.0","end")

def delete_user(masterpassword,username,root3):
    svar = pyautogui.confirm(text='Er du sikker på at du vil slette brukeren og all data', title='Slett', buttons=['Ja', 'Avbryt'])
    if svar == 'Ja':
        try:
            os.chmod('bin',0o777)
            os.chmod('Brukere',0o777)
            os.chmod('bin\\Bruker.txt', 0o777)
            os.chmod('Backup_files\\bin',0o777)
            os.chmod('Backup_files\\Brukere',0o777)
            os.chmod('Backup_files\\bin\\Bruker.txt',0o777)
        except:
            SystemError
        with open('bin\\Bruker.txt','r') as f:
            lines = f.readlines()
        i = 0
        while i <= len(lines):
            linje = lines[i]
            verdi = linje[9:137]
            if verdi == masterpassword:
                salt = linje[143:231]
                slette = verdi
                break
            else:
                i += 1
        samlet = 'brukere["' + slette + '"] = "' + salt + '"'
        with open('bin\\Bruker.txt','w') as b:
            for line in lines:
                if line.strip('\n') != samlet:
                    b.write(line)
        msgU_update = username.encode('utf-8')
        salt_update = salt.encode('utf-8')
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_update,
        iterations=85309,
        backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(msgU_update))
        key_update = key.decode('utf-8')
        filnavn = key_update + '.txt'
        path = os.path.join('Brukere',filnavn)
        try:
            os.chmod(path, 0o777)
            path2 = os.path.join('Backup_files\\Brukere',filnavn)
            os.chmod(path2, 0o777)
        except:
            SystemError
        os.remove(path)
        backup()
        root3.destroy()
    else:
        return 0


def main_program(key,username,masterpassword):
    global T
    root3 = tkinter.Tk()
    root3.title('Kryptert tekst')
    root3.focus_force()
    canvas3 = tkinter.Canvas(root3, height=100, width=800)
    canvas3.pack()
    text = 'Innlogget som ' + username
    Label2 = tkinter.Label(root3, text=text, font=100)
    Label2.place(relwidth=0.5, relheight=0.1, rely=0.05, relx=0.2)
    S = tkinter.Scrollbar(root3)
    T = tkinter.Text(root3, height=30, width=80,bd=7)
    S.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    T.pack(side=tkinter.LEFT, fill=tkinter.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = decrypt(username,masterpassword,root3)
    T.insert(tkinter.END, quote)
    SaveButton2 = tkinter.Button(root3, text="Close", command=lambda: encrypt(username,root3,masterpassword), bg='gray99')
    SaveButton2.place(relwidth=0.15, relheight=0.07, relx=0.03, rely=0.05)
    SlettButton = tkinter.Button(root3, text="Slett bruker", command=lambda: delete_user(masterpassword,username,root3), bg='gray99')
    SlettButton.place(relwidth=0.15, relheight=0.07, relx=0.8, rely=0.05)
    SlettButton2 = tkinter.Button(root3, text="Clear", command=lambda: slett(), bg='gray99')
    SlettButton2.place(relwidth=0.15, relheight=0.07, relx=0.64, rely=0.05)
    root3.mainloop


def troubleshoot(masterpassword,username,trouble1=None,trouble2=None):
    if not os.path.exists('Brukere'):
        os.mkdir('Brukere')
    if not os.path.exists('Backup_files'):
        os.mkdir('Backup_files')
    if not os.path.exists('Backup_files\\junk'):
        os.mkdir('Backup_files\\junk')
    path_1 = os.path.join('bin','Bruker.txt')
    path_2 = os.path.join('Backup_files\\bin','Bruker.txt')
    if not os.path.exists(path_1) and os.path.exists(path_2):
        with open(path_1,'w') as f:
            f.write('Brukere' + '\n')
    if not os.path.exists('bin\\Bruker.txt') or trouble1 == True:
        pyautogui.alert('Brukerfilen ble gjennopprettet!')
        shutil.copyfile('Backup_files\\bin\\Bruker.txt','bin\\Bruker.txt')
    i = 0
    bruker = False
    with open('bin\\Bruker.txt','r') as f:
        lines = f.readlines()
    while i < len(lines):
        linje = lines[i]
        verdi = linje[9:137]
        if verdi == masterpassword:
            salt = linje[143:231]
            bruker = True
            break
        else:
            i += 1
    if bruker == False:
        return 0
    trouble3 = False
    try:
        msgU_update = username.encode('utf-8')
        salt_update = salt.encode('utf-8')
        kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt_update,
        iterations=85309,
        backend=default_backend()
        )
        key = base64.urlsafe_b64encode(kdf.derive(msgU_update))
        key_update = key.decode('utf-8')
        filnavn = key_update + '.txt'
        path = os.path.join('Brukere',filnavn)
        os.chmod(path, 0o777)
        path2 = os.path.join('Backup_files\\Brukere',filnavn)
        os.chmod(path2, 0o777)
        dir_backup = os.listdir("Backup_files\\Brukere")
        dir_brukere = os.listdir("Brukere")
        if len(dir_brukere) < len(dir_backup):
            print(str(len(dir_backup)),str(len(dir_brukere)))
            trouble3 = True
    except:
        SystemError
    if not os.path.exists(path) or trouble2 == True or trouble3 == True:
        if trouble2 != True:
            path2 = os.path.join('Backup_files\\Brukere',filnavn)
            pyautogui.alert('Brukerfilene ble gjennopprettet!!')
            if os.path.exists(path) and trouble2 == True:
                t0 = time.time()
                path3 = os.path.join('Backup_files\\junk',str(t0))
                os.rename(path,path3)
            dir_backup = os.listdir("Backup_files\\Brukere")
            for i in range(len(dir_backup)):
                linje1 = dir_backup[i]
                dir_brukere = os.listdir("Brukere")
                if linje1 not in dir_brukere:
                    path2 = os.path.join('Backup_files\\Brukere',linje1)
                    path_new = os.path.join('Brukere',linje1)
                    try:
                        shutil.copyfile(path2,path_new)
                    except:
                        with open(path,'w') as f:
                            f.write('')
        else:
            os.remove(path)
            if os.path.exists(path):
                t0 = time.time()
                path3 = os.path.join('Backup_files\\junk',str(t0))
                os.rename(path,path3)
            dir_brukere = os.listdir("Brukere")
            for i in range(len(dir_backup)):
                linje1 = dir_backup[i]
                if linje1 not in dir_brukere:
                    path2 = os.path.join('Backup_files\\Brukere',linje1)
                    try:
                        path_new = os.path.join('Brukere',linje1)
                        shutil.copyfile(path2,path_new)
                    except:
                        with open(path,'w') as f:
                            f.write('')
    path_junk = os.path.join('Backup_files','junk')
    dict_junk = os.listdir(path_junk)
    for i in range(len(dict_junk)):
        linje = dict_junk[i]
        path_file = os.path.join(path_junk,linje)
        os.chmod(path_file, 0o777)
        try:
            path_bin = os.path.join(path_file,'bin')
            path_giphy = os.path.join(path_bin,'giphy.gif')
            path_Bruker = os.path.join(path_bin,'Bruker.txt')
            path_Brukere = os.path.join(path_file,'Brukere')
            os.chmod(path_bin, 0o777)
            os.chmod(path_giphy, 0o777)
            os.chmod(path_Bruker, 0o777)
            os.chmod(path_Brukere, 0o777)
            innhold_Brukere = os.listdir(path_Brukere)
            for i in range(len(innhold_Brukere)):
                fil = innhold_Brukere[i]
                path_innhold_Brukere = os.path.join(path_Brukere,fil)
                os.chmod(path_innhold_Brukere, 0o777)
            shutil.rmtree(path_file,ignore_errors=True)
        except:
            SystemError

def validateLogin(registrer=None):
    msgU = usernameEntry.get()
    msgP = passwordEntry.get()
    msg = msgU + ':' + msgP
    hsh = hashlib.sha512()
    hsh.update(msg.encode('utf-8'))
    hshDigest = hsh.hexdigest()
    y = hshDigest
    try:
        os.chmod('Brukere',0o777)
        os.chmod('bin', 0o777)
        os.chmod('bin\\Bruker.txt', 0o777)
        os.chmod('Backup_files\\bin\\Bruker.txt', 0o777)
        os.chmod('Backup_files\\bin',0o777)
        os.chmod('Backup_files\\Brukere',0o777)
    except:
        SystemError
    if registrer == None:
        troubleshoot(y,msgU,None,None) #Troubleshooter
    else:
        troubleshoot(registrer,None,None,None) #Troubleshooter
    vertifikasjon = False
    registrert = False
    login = False
    with open('bin\\Bruker.txt','r') as f:
        lines = f.readlines()
        i = 0
        while True:
            verdi = lines[i]
            value = verdi[9:137]
            if registrer != None:
                if registrer in value:
                    vertifikasjon = True
                    registrert = False
                    break
                else:
                    vertifikasjon = True
                    registrert = True
            if y in value:
                vertifikasjon = True
                login = True
                break
            i += 1
            if i >= len(lines):
                break
    if vertifikasjon == False:
        pyautogui.alert('Ugyldig brukernavn eller passord')
    if login == True:
        key = generate_key()
        root.destroy()
        main_program(key,msgU,y)
    if vertifikasjon == True and registrert == False:
        return False
    usernameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    usernameEntry.focus()
    return registrert

def generate_salt():
    salt = os.urandom(64)
    salt = base64.b64encode(salt)
    salt = salt.decode("utf-8")
    return salt

def avbryt(root2):
    root2.destroy()

def ny_bruker(root2):
    try:
        os.chmod('bin',0o777)
        os.chmod('bin\\Bruker.txt', 0o777)
    except:
        SystemError
    msgU = usernameEntry2.get()
    msgP = passwordEntry2.get()
    msgPP = passwordEntry3.get()
    if msgP == msgPP:
        msg = msgU + ':' + msgP
        hsh = hashlib.sha512()
        hsh.update(msg.encode('utf-8'))
        masterpassword = hsh.hexdigest()
        sjekk = validateLogin(masterpassword)
        if sjekk == True:
            salt = generate_salt()
            with open('bin\\Bruker.txt','a') as f:
                f.write('brukere["' + masterpassword + '"] = "' + salt + '"\n')
            msgU_update = msgU.encode('utf-8')
            salt_update = salt.encode('utf-8')
            kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt_update,
            iterations=85309,
            backend=default_backend()
            )
            key = base64.urlsafe_b64encode(kdf.derive(msgU_update))
            key_update = key.decode('utf-8')
            filnavn = key_update + '.txt'
            path = os.path.join('Brukere',filnavn)
            with open(path,'w') as v:
                v.write('')
            pyautogui.alert('Brukeren er lagret')
            root2.destroy()
        else:
            pyautogui.alert('Brukeren eksisterer allerede fra før')
            usernameEntry2.delete(0, 'end')
            passwordEntry2.delete(0, 'end')
            passwordEntry3.delete(0, 'end')
            usernameEntry2.focus()
    else:
        pyautogui.alert('Passordene samsvarer ikke med hverandre')
        passwordEntry2.delete(0, 'end')
        passwordEntry3.delete(0, 'end')
        passwordEntry2.focus()

def enter3(event):
    passwordEntry2.focus()
def enter4(event):
    passwordEntry3.focus()

def ny_bruker_vindu(HEIGHT,WIDTH):

    global usernameEntry2
    global passwordEntry2
    global passwordEntry3
    global loginButton2

    root2 = tkinter.Tk()
    root2.title('Ny bruker')
    root2.focus_set()
    root2.attributes('-topmost', True)
    canvas2 = tkinter.Canvas(root2, height=HEIGHT/1.5, width=WIDTH/1.5)
    canvas2.pack()
   
    #Brukernavn
    usernameLabel2 = tkinter.Label(root2, text="Skriv inn brukernavn")
    usernameLabel2.place(relwidth=0.5, relheight=0.1, rely=0.1, relx=0.15)
    username2 = tkinter.StringVar()
    usernameEntry2 = tkinter.Entry(root2, textvariable=username2)
    usernameEntry2.place(relwidth=0.6, relheight=0.1, rely=0.19, relx=0.2)
    usernameEntry2.focus()
    usernameEntry2.bind('<Return>', enter3)
    usernameEntry2.pack

    #Passord 1
    passwordLabel2 = tkinter.Label(root2,text="Skriv inn passord")
    passwordLabel2.place(relwidth=0.5, relheight=0.1, rely=0.29, relx=0.12)
    password2 = tkinter.StringVar()
    passwordEntry2 = tkinter.Entry(root2, textvariable=password2, show='*')
    passwordEntry2.place(relwidth=0.6, relheight=0.1, rely=0.38, relx=0.2)
    passwordEntry2.bind('<Return>', enter4)
    passwordEntry2.pack

    #Passord 2
    passwordLabel3 = tkinter.Label(root2,text="Skriv inn passord på nytt")
    passwordLabel3.place(relwidth=0.5, relheight=0.1, rely=0.48, relx=0.2)
    password3 = tkinter.StringVar()
    passwordEntry3 = tkinter.Entry(root2, textvariable=password3, show='*')
    passwordEntry3.place(relwidth=0.6, relheight=0.1, rely=0.57, relx=0.2)

    loginButton2 = tkinter.Button(root2, text="Registrer", command=lambda: ny_bruker(root2), bg='gray99')
    loginButton2.place(relwidth=0.3, relheight=0.12, relx=0.2, rely=0.7)

    Avbryt = tkinter.Button(root2, text="Avbryt", command=lambda: avbryt(root2), bg='gray99')
    Avbryt.place(relwidth=0.3, relheight=0.12, relx=0.2, rely=0.85)

    root2.mainloop()


def enter(event):
    passwordEntry.focus()
def enter_2(event):
    validateLogin(None)


        
root = tkinter.Tk()
root.title('Login')
app = App(root)
root.resizable(False, False)
root.overrideredirect(False)

global usernameEntry
global passwordEntry

event='event'

#username label and text entry box
usernameLabel = tkinter.Label(root, text="Brukernavn")
usernameLabel.place(relwidth=0.2, relheight=0.05, rely=0.5, relx=0.2)
username = tkinter.StringVar()
usernameEntry = tkinter.Entry(root, textvariable=username)
usernameEntry.place(relwidth=0.4, relheight=0.08, rely=0.55, relx=0.2)
usernameEntry.focus()
usernameEntry.bind('<Return>', enter)
usernameEntry.pack

#password label and password entry box
passwordLabel = tkinter.Label(root,text="Passord")
passwordLabel.place(relwidth=0.2, relheight=0.05, rely=0.65, relx=0.2)
password = tkinter.StringVar()
passwordEntry = tkinter.Entry(root, textvariable=password, show='*')
passwordEntry.place(relwidth=0.4, relheight=0.08, rely=0.7, relx=0.2)
passwordEntry.bind('<Return>', enter_2)

#login button

loginButton = tkinter.Button(root, text="Login", command=lambda: validateLogin(None), bg='gray99')
loginButton.place(relwidth=0.2, relheight=0.1, relx=0.2, rely=0.8)

#Registrer bruker

registrerButton = tkinter.Button(root, text="Registrer ny bruker", command=lambda: ny_bruker_vindu(HEIGHT,WIDTH), bg='gray99')
registrerButton.place(relwidth=0.4, relheight=0.1, relx=0.4, rely=0.8)


root.mainloop()


