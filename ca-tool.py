#!/usr/bin/python3

from tkinter import Tk     
from tkinter.filedialog import askopenfilename


from tkinter import *
import os # https://stackoverflow.com/questions/58475025/typeerror-an-integer-is-required-got-type-str-for-writing-to-file
import subprocess

import re
import io


def main():

    
    def mkdirrootca():
        ...
        os.system("gnome-terminal -e 'bash -c \"watch tree; exec bash\"'")
        cmd = "mkdir ca; mkdir ./ca/rootca"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("rootCA directory created...")

    def mkdb():
        cmd = 'mkdir ./ca/rootca/ca.db.certs;touch ./ca/rootca/ca.db.serial;touch ./ca/rootca/ca.db.index;echo "000001" > ./ca/rootca/ca.db.serial;touch ./ca/rootca/ca.db.rand;perl -e "print int(rand(90)+10);" > ./ca/rootca/ca.db.rand'
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("rootCA database created...")



    def mkrootcakey():
        ...
        password = rootPassword_Entry.get()
        p = print(password)
        passwordFile = open("ca/rootca/rootcapassword.txt", "w")
        passwordFile.write(password)
        passwordFile.close()
        print("root ca password saved...")
        ...
        cmd = "openssl genrsa -des3 -passout file:./ca/rootca/rootcapassword.txt -out ./ca/rootca/rootca.key.pem 4096"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("rootca key created...")

    def mkIndexerkey():
        ...
        password = indexerPassword_Entry.get()
        p = print(password)
        passwordFile = open("ca/rootca/indexerpassword.txt", "w")
        passwordFile.write(password)
        passwordFile.close()
        print("indexer password saved...")
        ...
        cmd = "openssl genrsa -des3 -passout file:./ca/indexer/indexerpassword.txt -out ./ca/indexer/indexer.key.pem 2048"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("index key created. Password is: ",password)



    def deldirCA():
        cmd = "rm -rfv ./ca"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("rootCA directory deleted...")

    def mkrootcacert():
        cmd = "rm -rfv ./ca"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("rootCA directory deleted...")

    def mkrootcacert():
        cmd = "openssl req -config rootca.conf -new -x509 -days 7600 -passin file:./ca/rootca/rootcapassword.txt -key ./ca/rootca/rootca.key.pem -out ./ca/rootca/rootca.cert.crt; openssl x509 -in ./ca/rootca/rootca.cert.crt -passin file:./ca/rootca/rootcapassword.txt -out ./ca/rootca/rootca.cert.pem"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("root ca crt pem certificates created...")

########################################splunk web

    def mksplunkwebdir():
        ...
        os.system("gnome-terminal -e 'bash -c \"watch tree; exec bash\"'")
        cmd = "mkdir ./ca/splunkweb"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("splunk web directory created...")

    def mksplunkwebkey():
        ...
        cmd = "openssl genrsa -out ./ca/splunkweb/splunkweb.key.pem 2048"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("splunk web key created...")

    def mksplunkwebcsr():
        ...
        cmd = 'openssl req -key ./ca/splunkweb/splunkweb.key.pem -new -sha256  -out ./ca/splunkweb/splunkweb.csr -subj "/C=GB/ST=UK/L=UK/O=Splunk Web/OU=Splunk Web/CN=www.splunkweb.co.uk/emailAddress=admin@cyberprotectionteam.com"'
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("splunk web csr created...")

    def signsplunkweb():
        cmd = 'yes | openssl ca -config splunkweb.conf -days 365 -passin file:./ca/rootca/rootcapassword.txt -in ./ca/splunkweb/splunkweb.csr -extfile v3-splunkweb.ext -out ./ca/splunkweb/splunkweb.cert.pem '
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("splunk web certificate signed created...")

    def deldirsplunkweb():
        cmd = "rm -rfv ./ca/splunkweb"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("indexer directory deleted...")


#################################################### Indexer

    def mksplunkindexerdir():
        cmd = 'mkdir ./ca/indexer'
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk indexer directory created")

   # def mkindexerprivatekey():
        #cmd = "openssl genrsa -out ./ca/indexer/indexer.key.pem 2046"
        #cmdFile = open("command.sh", "w")
        #cmdFile.write(cmd)
        #cmdFile.close()
       # print(os.system('chmod +x command.sh'))
       # print(os.system('./command.sh'))
       # print("Splunk indexer priveate key created")

    def mkindexerkey():
        ...
        password = rootPassword_Entry.get()
        p = print(password)
        passwordFile = open("ca/indexer/indexerpassword.txt", "w")
        passwordFile.write(password)
        passwordFile.close()
        print("indexer password saved...")
        ...
        cmd = "openssl genrsa -des3 -passout file:./ca/indexer/indexerpassword.txt -out ./ca/indexer/indexer.key.pem 2048"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("indexer key created, password is: ", password)


    def mkindexercsr():
        cmd = 'openssl req -new -key ./ca/indexer/indexer.key.pem -passin file:./ca/indexer/indexerpassword.txt -out ./ca/indexer/indexer.csr -sha256 -subj "/C=GB/ST=Indexer/L=Indexer/O=Indexer/OU=Indexer/CN=www.splunk.co.uk"'
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk indexer certificate signing request created")

    def mkindexcertificate():
        cmd = 'yes | openssl ca -config splunkIndexer.conf -passin file:./ca/rootca/rootcapassword.txt -in ./ca/indexer/indexer.csr -extfile v3-server.ext -days 370 -out ./ca/indexer/indexer.cert.pem'
        #cmd = "yes | openssl x509 -req -config splunkIndexer.conf -in ./ca/indexer/indexer.csr -CA ./ca/rootca/rootca.cert.pem -CAkey ./ca/rootca/rootca.key.pem -passin file:./ca/rootca/rootcapassword.txt -extensions server -days 370 -outform PEM -out ./ca/indexer/indexer.cert.pem -sha256" #-set_serial 111111
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk indexer certificate created")

    def bundleindexerroot():
        cmd = "cat ./ca/indexer/indexer.cert.pem ./ca/rootca/rootca.cert.pem > ./ca/indexer/splunkindexer.bundle.cert.pem"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk indexer  and root certificate bundled" )

    def deldirindexer():
        cmd = "rm -rfv ./ca/indexer"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("indexer directory deleted...")

#################### Forwarder

    def mksplunkforwarderdir():
        cmd = 'mkdir ./ca/forwarder'
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk forwarder directory created")

##    def mkforwarderprivatekey():
##        cmd = "openssl genrsa -out ./ca/forwarder/forwarder.client.key.pem 2046"
##        cmdFile = open("command.sh", "w")
##        cmdFile.write(cmd)
##        cmdFile.close()
##        print(os.system('chmod +x command.sh'))
##        print(os.system('./command.sh'))
##        print("Splunk forwarder priveate key created")

    def mkforwarderkey():
        ...
        password = rootPassword_Entry.get()
        p = print(password)
        passwordFile = open("ca/forwarder/forwarderpassword.txt", "w")
        passwordFile.write(password)
        passwordFile.close()
        print("forwarder password saved...")
        ...
        cmd = "openssl genrsa -des3 -passout file:./ca/forwarder/forwarderpassword.txt -out ./ca/forwarder/forwarder.client.key.pem 2048"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Forwarder key created, password is: ", password)


    def mkforwardercsr():
        ##cp from index ###cmd = 'openssl req -new -key ./ca/indexer/indexer.key.pem -passin file:./ca/indexer/indexerpassword.txt -out ./ca/indexer/indexer.csr -sha256 -subj "/C=GB/ST=Indexer/L=Indexer/O=Indexer/OU=Indexer/CN=www.splunk.co.uk"'
        cmd = "openssl req -new -key ./ca/forwarder/forwarder.client.key.pem -passin file:./ca/forwarder/forwarderpassword.txt -config splunkForwarder.conf -out ./ca/forwarder/forwarder.client.csr"
        #openssl req -new -key ./ca/indexer/indexer.key.pem -out ./ca/indexer/indexer.csr -sha256 -subj "/C=GB/ST=Indexer/L=Indexer/O=Indexer/OU=Indexer/CN=www.splunkindexer.com"
        #cmd ="openssl req -config splunkIndexer.conf -key ./ca/forwarder/forwarder.key.pem -out ./ca/forwarder/forwarder.csr"
        #cmd = 'openssl req -new -key ./ca/forwarder/forwarder.client.key.pem -out ./ca/forwarder/forwarder.client.csr -sha256 -subj "/C=GB/ST=Forwarder/L=Forwarder/O=Forwarder/OU=Forwarder/CN=www.splunkindexer.com"'
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk forwarder certificate signing request created")

    def mkdforwardercertificate():
        #cmd = "yes | openssl ca -config splunkForwarder.conf -passin file:./ca/rootca/rootcapassword.txt -in ./ca/indexer/indexer.csr -extfile v3-server.ext -days 370 -out ./ca/indexer/indexer.cert.pem"
        #cmd = "yes | openssl x509 -req -in ./ca/forwarder/forwarder.client.csr -CA ./ca/rootca/rootca.cert.pem -CAkey ./ca/rootca/rootca.key.pem -passin file:./ca/rootca/rootcapassword.txt -set_serial 999999 -extensions client -days 370 -outform PEM -out ./ca/forwarder/forwarder.client.cert.pem -sha256"
        cmd = "yes | openssl ca -config splunkForwarder.conf -passin file:./ca/rootca/rootcapassword.txt -in ./ca/forwarder/forwarder.client.csr -extfile v3-client.ext -days 370 -out ./ca/forwarder/forwarder.client.cert.pem"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk forwarder certificate created")

    def bundleforwarderroot():
        cmd = "cat ./ca/forwarder/forwarder.client.cert.pem ./ca/rootca/rootca.cert.pem > ./ca/forwarder/splunkforwarder.bundle.cert.pem"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("Splunk forwarder  and root certificate bundled" )

    def deldirforwarder():
        cmd = "rm -rfv ./ca/forwarder"
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("forwarder directory deleted...")

    def varify():
        ...
        cmd = "openssl verify -CAfile ./ca/rootca/rootca.cert.pem  ./ca/forwarder/forwarder.client.cert.pem;openssl verify -CAfile ./ca/rootca/rootca.cert.pem  ./ca/indexer/indexer.cert.pem ; openssl verify -CAfile ./ca/rootca/rootca.cert.pem  ./ca/splunkweb/splunkweb.cert.pem;openssl verify -CAfile ./ca/rootca/rootca.cert.pem  ./ca/rootca/rootca.cert.pem "
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh > varified.txt'))
        os.system("gnome-terminal -e 'bash -c \"watch cat varified.txt; exec bash;rm varified.txt\"'")

    
    def export():
        cmd = 'mkdir ./ca/export; cp ./ca/splunkweb/splunkweb.key.pem ./ca/export;cp ./ca/splunkweb/splunkweb.cert.pem ./ca/export;cp ./ca/rootca/rootca.cert.pem ./ca/export; cp ./ca/indexer/indexer.cert.pem ./ca/export; cp ./ca/indexer/indexer.key.pem ./ca/export; cp ./ca/forwarder/forwarder.client.cert.pem ./ca/export; cp ./ca/forwarder/forwarder.client.key.pem ./ca/export;  cp ./ca/indexer/indexer.cert.pem ./ca/export; cp ./ca/indexer/indexer.key.pem ./ca/export;   tar -cvzf ./ca/export/archive.tar.gz ./ca/export/* '
        cmdFile = open("command.sh", "w")
        cmdFile.write(cmd)
        cmdFile.close()
        print(os.system('chmod +x command.sh'))
        print(os.system('./command.sh'))
        print("exported")

    def viewIndex():
        os.system("gnome-terminal -e 'bash -c \"watch cat ./ca/rootca/ca.db.index; exec bash\"'")
        print("Viewing Index")

        
#######################################################################

    # Bellow this is the GUI
    
    root = Tk()
    root.title(" Certificate Authority Tool ")

    welcome = Label(root, text="\n Welcome To Your Certificate Authority \n",  )
    welcome.pack()


#############################

    # Button to create the CA directories
    mkdirrootca_button = Button(root, text="\n 1) Creating the CA Directory \n", command=lambda:  mkdirrootca())
    mkdirrootca_button.pack()


#############################

    # Button to create the ca database
    mkdb_button = Button(root, text="\n 2) Creating the root database \n", command=lambda:  mkdb())
    mkdb_button.pack()

#############################

    # Button to set password and forge ca key

    takePassword_Label = Label(root, text=" Enter the Root CA password ")
    takePassword_Label.pack()
    rootPassword_Entry = Entry(root, width=70)
    rootPassword_Entry.pack()
    rootPassword_Entry.insert(0, " ")
    mkrootcakey_button = Button(root, text="\n 3) Set the password and create 4096 bit key. \n", command=lambda:  mkrootcakey())
    mkrootcakey_button.pack()
    

#############################

    # Button to create the ca database
    mkrootcacert_button = Button(root, text="\n 4) Make Root CA certificate \n", command=lambda:  mkrootcacert())
    mkrootcacert_button.pack()

###############################

    spacer = Label(root, text="\n ------------------------------------------------------------------------------------------ \n")
    spacer.pack()

#############################

    # Button to create the splunk web directory
    mkdirrootca_button = Button(root, text="\n 5) Creating the splunk web directory \n", command=lambda:  mksplunkwebdir())
    mkdirrootca_button.pack()


#############################

    # Button to create the splunk web key
    mkdirrootca_button = Button(root, text="\n 6) Creating the splunk web 2048 bit key \n", command=lambda:  mksplunkwebkey())
    mkdirrootca_button.pack()

#############################

    # Button to create the splunk web csr
    mkdirrootca_button = Button(root, text="\n 7) Creating the splunk web  CSR\n", command=lambda:  mksplunkwebcsr())
    mkdirrootca_button.pack()

#############################

    # Button to create the splunk web cert
    mkdirrootca_button = Button(root, text="\n 8) Sign the Splunk Web CSR & create a certificate \n", command=lambda:  signsplunkweb())
    mkdirrootca_button.pack()

###############################

    #del the indexer directory
    delDirCA_button = Button(root, text="\n Delete Splunk Web dir \n", command=lambda:  deldirsplunkweb(), bg="RED") 
    delDirCA_button.pack()

#############################

    spacer = Label(root, text="\n  ------------------------------------------------------------------------------------------  \n")
    spacer.pack()


################################################################################################################################################################# Indexer GUI

    # Button to create the indexer directory
    mkdirrootca_button = Button(root, text="\n 9) Creating the Splunk Indexer directory \n", command=lambda:  mksplunkindexerdir())
    mkdirrootca_button.pack()

############################### swap

    #takeIndexerPassword_Label = Label(root, text=" Enter the Indexer password ")
   # takeIndexerPassword_Label.pack()
   # indexerPassword_Entry = Entry(root, width=70)
   # indexerPassword_Entry.pack()
   # indexerPassword_Entry.insert(0, " ")
   # mkIndexercakey_button = Button(root, text="\n 3) Set the password and create 4096 bit key. \n", command=lambda:  mkIndexerCAKey())
   # mkIndexercakey_button.pack()

#############################

    # Button to set password and forge ca key

    takePassword_Label = Label(root, text=" Enter the Indexer password ")
    takePassword_Label.pack()
    rootPassword_Entry = Entry(root, width=70)
    rootPassword_Entry.pack()
    rootPassword_Entry.insert(0, " ")
    mkrootcakey_button = Button(root, text="\n 3) Set the password and create 2048 bit key. \n", command=lambda:  mkindexerkey())
    mkrootcakey_button.pack()
    

###############################

    # Button to create the indexer private key
   # mkdirrootca_button = Button(root, text="\n 10) Creating the Splunk Indexer private key \n", command=lambda:  mkindexerprivatekey())
   # mkdirrootca_button.pack()

###############################

    # Button to create the splunk indexer CSR
    mkdirrootca_button = Button(root, text="\n 11) Creating the Splunk Indexer CSR \n", command=lambda:  mkindexercsr())
    mkdirrootca_button.pack()

###############################

    # Button to create the splunk indexer cert
    mkdirrootca_button = Button(root, text="\n 12) Creating the Splunk Indexer Certificate \n", command=lambda:  mkindexcertificate())
    mkdirrootca_button.pack()

###############################

    # Button to create the bundle the indexer and root cert
   # mkdirrootca_button = Button(root, text="\n 13) Bundle the Indexer and Rootca Certificates \n", command=lambda:  bundleindexerroot())
   # mkdirrootca_button.pack()

#############################

    #del the indexer directory
    delDirCA_button = Button(root, text="\n Delete Indexer dir \n", command=lambda:  deldirindexer(), bg="RED") 
    delDirCA_button.pack()


################################

    spacer = Label(root, text="\n  ------------------------------------------------------------------------------------------  \n")
    spacer.pack()


####################################################################################################################################################################### Forwarder GUI

    # Button to create the forwarder directory
    mkdirrootca_button = Button(root, text="\n 13) Creating the Splunk Forwarder directory \n", command=lambda:  mksplunkforwarderdir())
    mkdirrootca_button.pack()

###############################

    # Button to create the forwarder private key
    #mkdirrootca_button = Button(root, text="\n 14) Creating the Splunk Forwarder private key \n", command=lambda:  mkforwarderprivatekey())
    #mkdirrootca_button.pack()

    takePassword_Label = Label(root, text=" Enter the Forwarder password ")
    takePassword_Label.pack()
    rootPassword_Entry = Entry(root, width=70)
    rootPassword_Entry.pack()
    rootPassword_Entry.insert(0, " ")
    mkrootcakey_button = Button(root, text="\n 3) Set the password and create 2048 bit key. \n", command=lambda:  mkforwarderkey())
    mkrootcakey_button.pack()

###############################

    # Button to create the splunk forwarder CSR
    mkdirrootca_button = Button(root, text="\n 15) Creating the Splunk Forwarder CSR \n", command=lambda:  mkforwardercsr())
    mkdirrootca_button.pack()

###############################

    # Button to create the splunk forwarder cert
    mkdirrootca_button = Button(root, text="\n 16) Creating the Splunk Forwarder Certificate \n", command=lambda:  mkdforwardercertificate())
    mkdirrootca_button.pack()

###############################

    # Button to create the bundle the forwarder and root cert
    #mkdirrootca_button = Button(root, text="\n 17) Bundle the Forwarder and Rootca Certificates \n", command=lambda:  bundleforwarderroot())
    #mkdirrootca_button.pack()

#############################

    #del the forwarder directory
    delDirCA_button = Button(root, text="\n 18) Delete Forwarder dir \n", command=lambda:  deldirforwarder(), bg="RED") 
    delDirCA_button.pack()


################################

    spacer = Label(root, text="\n  ------------------------------------------------------------------------------------------  \n")
    spacer.pack()


#############################

    delDirCA_button = Button(root, text="\n 19) Varify the certificates \n", command=lambda:  varify(), bg="GREEN") 
    delDirCA_button.pack()

    spacer = Label(root, text="\n")
    spacer.pack()


    delDirCA_button = Button(root, text="\n 19) View Index \n", command=lambda:  viewIndex(), bg="GREEN") 
    delDirCA_button.pack()

    
    
###############################

    spacer = Label(root, text="\n  ------------------------------------------------------------------------------------------ \n")
    spacer.pack()

#############################



# Export the bits and bobs
    mkdirrootca_button = Button(root, text="\n 20) Export the required certs to make splunk secure. \n", command=lambda:  export())
    mkdirrootca_button.pack()

###############################

    spacer = Label(root, text="\n  ------------------------------------------------------------------------------------------  \n")
    spacer.pack()

#############################

    delDirCA_button = Button(root, text="\n 21) Delete Entire CA \n", command=lambda:  deldirCA(), bg="RED") 
    delDirCA_button.pack()

###############################

    spacer = Label(root, text="\n  \n")
    spacer.pack()

#############################




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
