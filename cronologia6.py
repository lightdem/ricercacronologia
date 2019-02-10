#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Cronologia6.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Finestraprincipale(object):
    def setupUi(self, Finestraprincipale):
        Finestraprincipale.setObjectName("Finestraprincipale")
        Finestraprincipale.resize(641, 451)
        self.gridLayout = QtWidgets.QGridLayout(Finestraprincipale)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_ricerca = QtWidgets.QPushButton(Finestraprincipale)
        self.btn_ricerca.setEnabled(False)
        self.btn_ricerca.setObjectName("btn_ricerca")
        self.gridLayout.addWidget(self.btn_ricerca, 6, 3, 1, 1)
        self.testo_ricerca = QtWidgets.QLineEdit(Finestraprincipale)
        self.testo_ricerca.setObjectName("testo_ricerca")
        self.gridLayout.addWidget(self.testo_ricerca, 6, 1, 1, 2)
        self.etichetta_ricerca = QtWidgets.QLabel(Finestraprincipale)
        self.etichetta_ricerca.setObjectName("etichetta_ricerca")
        self.gridLayout.addWidget(self.etichetta_ricerca, 6, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 1, 1, 1)
        self.btn_appunti = QtWidgets.QPushButton(Finestraprincipale)
        self.btn_appunti.setEnabled(False)
        self.btn_appunti.setObjectName("btn_appunti")
        self.gridLayout.addWidget(self.btn_appunti, 0, 3, 1, 1)
        self.btn_ripristina = QtWidgets.QPushButton(Finestraprincipale)
        self.btn_ripristina.setEnabled(False)
        self.btn_ripristina.setObjectName("btn_ripristina")
        self.gridLayout.addWidget(self.btn_ripristina, 1, 3, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.listarisultati = QtWidgets.QListWidget(Finestraprincipale)
        self.listarisultati.setObjectName("listarisultati")
        self.gridLayout.addWidget(self.listarisultati, 0, 0, 6, 3)
        self.chk_alfabetico = QtWidgets.QCheckBox(Finestraprincipale)
        self.chk_alfabetico.setObjectName("chk_alfabetico")
        self.gridLayout.addWidget(self.chk_alfabetico, 2, 3, 1, 1)
        self.btn_chiudi = QtWidgets.QPushButton(Finestraprincipale)
        self.btn_chiudi.setObjectName("btn_chiudi")
        self.gridLayout.addWidget(self.btn_chiudi, 3, 3, 1, 1)
        self.etichetta_ricerca.setBuddy(self.testo_ricerca)

        self.retranslateUi(Finestraprincipale)
        QtCore.QMetaObject.connectSlotsByName(Finestraprincipale)
        Finestraprincipale.setTabOrder(self.testo_ricerca, self.btn_ricerca)
        Finestraprincipale.setTabOrder(self.btn_ricerca, self.btn_appunti)
        Finestraprincipale.setTabOrder(self.btn_appunti, self.btn_ripristina)
        Finestraprincipale.setTabOrder(self.btn_ripristina, self.listarisultati)
        
        # colleghiamo i signal (output dei widget) e gli slot (metodi)
        self.btn_chiudi.clicked.connect(self.chiudi)
        self.btn_appunti.clicked.connect(self.copiaTesto)
        self.btn_ricerca.clicked.connect(self.filtraLista)
        self.testo_ricerca.textChanged.connect(self.testoRicercaCambiato)
        self.testo_ricerca.returnPressed.connect(self.filtraLista)
        self.btn_ripristina.clicked.connect(self.ripristinaCronologia)
        self.listarisultati.itemSelectionChanged.connect(self.selezioneCambiata)
        self.listarisultati.itemDoubleClicked.connect(self.copiaTestoOggetto)
        self.chk_alfabetico.stateChanged.connect(self.cambiaOrdinamento)
        
        # variabili
        self.fileCronologia = ''
        self.listaNonOrdinata = []
        
        

    def retranslateUi(self, Finestraprincipale):
        _translate = QtCore.QCoreApplication.translate
        Finestraprincipale.setWindowTitle(_translate("Finestraprincipale", "Dialog"))
        self.btn_ricerca.setText(_translate("Finestraprincipale", "Esegui ricerca"))
        self.etichetta_ricerca.setText(_translate("Finestraprincipale", "Ricerca"))
        self.btn_appunti.setText(_translate("Finestraprincipale", "Copia\n"
"Selezione\n"
"negli\n"
"Appunti"))
        self.btn_ripristina.setText(_translate("Finestraprincipale", "Ripristina\n"
"Cronologia"))
        self.chk_alfabetico.setText(_translate("Finestraprincipale", "Ordine\n"
"Alfabetico"))
        self.btn_chiudi.setText(_translate("Finestraprincipale", "Chiudi"))

    def svuotaListBox(self):         # elimina tutti gli oggetti dal listWidget
        while self.listarisultati.count() > 0:
            self.listarisultati.takeItem(0)
            
    def chiudi(self):                # termina il programma
        sys.exit(0)

    def selezioneCambiata(self):     # oggetto selezionato in listarisultati cambiato
        if self.listarisultati.currentItem():
            self.btn_appunti.setEnabled(True)
        else:
            self.btn_appunti.setEnabled(False)

    def copiaTestoOggetto(self, oggetto):   # doppio click su listarisultati
        self.testo_ricerca.setText(oggetto.text())

    def copiaTesto(self):             # copiamo negli appunti
        if self.listarisultati.currentItem():
            appunti = app.clipboard()
            appunti.setText(self.listarisultati.currentItem().text())
    
    def filtraLista(self):             # filtra la cronologia
        stringaRicerca = self.testo_ricerca.text()
        if stringaRicerca != '':
            righeDaSalvare = []
            for riga in self.listaNonOrdinata:
                if riga.decode('utf-8').__contains__(stringaRicerca):
                    righeDaSalvare.append(riga)
            self.svuotaListBox()
            self.listaNonOrdinata = []
            for riga in righeDaSalvare:
                self.listaNonOrdinata.append(riga)
                self.listarisultati.addItem(riga)
            self.cambiaOrdinamento()
            self.btn_ripristina.setEnabled(True)

    def testoRicercaCambiato(self):
        if self.testo_ricerca.text():
            self.btn_ricerca.setEnabled(True)
        else:
            self.btn_ricerca.setEnabled(False)
    
    def ripristinaCronologia(self):   # ripristina la cronologia originale
        self.svuotaListBox()
        self.popolaLista('')
        self.btn_ripristina.setEnabled(False)
        
    def cambiaOrdinamento(self):    # ordina alfabeticamente la lista o riprisina l'ordinamento originale
        if self.chk_alfabetico.checkState() == QtCore.Qt.Unchecked:
            self.listarisultati.setSortingEnabled(False)
            self.svuotaListBox()
            for riga in self.listaNonOrdinata:
                self.listarisultati.addItem(riga)
        else:
            self.listarisultati.setSortingEnabled(True)
            self.listarisultati.sortItems()
    
    def popolaLista(self, testo):    # popola la cronologia la prima volta e la ripristina al bisogno
        fd = open(self.fileCronologia, 'r')
        righe = fd.read().splitlines()
        #rimuoviamo i duplicati
        nuoveRighe = []
        self.listaNonOrdinata = []
        for riga in righe:
            if riga not in nuoveRighe:
                nuoveRighe.append(riga)
        for riga in reversed(nuoveRighe):     # in ordine dal più recente
            if riga.__contains__(testo):
                self.listaNonOrdinata.append(riga)
                self.listarisultati.addItem(riga)
        fd.close()
        self.cambiaOrdinamento()

if __name__ == "__main__":
    import sys, os
    app = QtWidgets.QApplication(sys.argv)
    Finestraprincipale = QtWidgets.QDialog()
    ui = Ui_Finestraprincipale()
    ui.setupUi(Finestraprincipale)
    ui.fileCronologia = os.path.expandvars("$HOME/.bash_history")
    testo = ''
    if len(sys.argv) > 1:   # l'utente ha inserito un argomento?
        testo = sys.argv[1]
        ui.btn_ripristina.setEnabled(True)
    ui.popolaLista(testo)
    Finestraprincipale.show()
    sys.exit(app.exec_())

