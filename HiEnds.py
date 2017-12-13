# -*- coding: utf-8 -*-
import wx
import wx.grid as gridlib

class HiEnds(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.MainWindow()
    
    
    def _esofago(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Esófago")
        esofSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        
        #globalSizer = wx.BoxSizer(wx.VERTICAL)
        CMSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        # Cambio mucoso
        CMst1 = wx.StaticText(self, label = "Cambio mucoso")
        self.CMtc  = wx.TextCtrl(self, size = (35,-1))
        CMst2 = wx.StaticText(self, label = "cm")
        CMSizer.Add(CMst1, 0, wx.ALL, 5)
        CMSizer.Add(self.CMtc, 0, wx.ALL, 5)
        CMSizer.Add(CMst2, 0, wx.ALL, 5)
        
        esofSizer.Add(CMSizer)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Mucosa")
        mucoSizer = wx.StaticBoxSizer(box)     
        
        self.abnormalWid = []
        # Normal
        stSizer = wx.GridBagSizer(vgap = 12, hgap = 12)
        #stSizer.Add((10,10))
        tx = wx.StaticText(self, label = "Normal")
        self.normal = wx.CheckBox(self)
        self.normal.Bind(wx.EVT_CHECKBOX, self.OnNormal)
        
        stSizer.Add(tx, pos = (0,0))
        stSizer.Add(self.normal, pos = (0,1))
        
        box = wx.StaticBox(self, wx.ID_ANY, "Lengueta de Ascenso")
        LASizer = wx.StaticBoxSizer(box)
        LaSizer = wx.GridBagSizer(vgap = 5, hgap = 12)
        
        tx = wx.StaticText(self, label = "C")
        self.abnormalWid.append(tx)
        LaSizer.Add(tx, pos = (0,1))
        tx = wx.StaticText(self, label = "M")
        self.abnormalWid.append(tx)
        LaSizer.Add(tx, pos = (0,2))
        self.lenguetaAsc_C  = wx.TextCtrl(self, size = (35,-1))
        self.lenguetaAsc_M  = wx.TextCtrl(self, size = (35,-1))
        self.abnormalWid.append(self.lenguetaAsc_M)
        self.abnormalWid.append(self.lenguetaAsc_C)
        LaSizer.Add(self.lenguetaAsc_C, pos = (1,1))
        LaSizer.Add(self.lenguetaAsc_M, pos = (1,2))
        
        LASizer.Add(LaSizer)
        stSizer.Add(LASizer, pos = (1,0), span = (2,2))
        
        box = wx.StaticBox(self, wx.ID_ANY, "Hernia de Hiato")
        Sizer = wx.StaticBoxSizer(box)
        tSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.hiato  = wx.TextCtrl(self, size = (30,-1))
        self.abnormalWid.append(self.hiato)
        tx = wx.StaticText(self, label = "cm")
        self.abnormalWid.append(tx)
        
        tSizer.Add(self.hiato, 0, wx.ALL, 5)
        tSizer.Add(tx, 0, wx.ALL, 5)
        Sizer.Add(tSizer)
        
        stSizer.Add(Sizer, pos = (1,2), span = (1,2))
        
        box = wx.StaticBox(self, wx.ID_ANY, "Esofagitis")
        Sizer = wx.StaticBoxSizer(box)
        tSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.esofagitis_radio = []
        for i,j in enumerate(['a', 'b', 'c', 'd']):
            r = wx.RadioButton(self, label = j)    
            tSizer.Add(r, 0, wx.ALL, 5)
            self.esofagitis_radio.append(r)
            self.abnormalWid.append(r)
        Sizer.Add(tSizer)
        
        stSizer.Add(Sizer, pos = (3,0), span =(1,4))
        
        box = wx.StaticBox(self, wx.ID_ANY, "Varices Esofágicas")
        Sizer = wx.StaticBoxSizer(box)
        tSizer = wx.GridBagSizer(vgap=5, hgap = 12)
        self.varices_radio = []
        r = wx.RadioButton(self, label = 'grandes')
        self.varices_radio.append(r)
        tSizer.Add(r, pos=(0,0))
        r = wx.RadioButton(self, label = 'chicas')
        self.varices_radio.append(r)
        tSizer.Add(r, pos=(0,1))
        r = wx.CheckBox(self, label = 'GOV I')
        self.abnormalWid.append(r)
        tSizer.Add(r, pos=(1,0))
        r = wx.CheckBox(self, label = 'GOV II')
        self.abnormalWid.append(r)
        tSizer.Add(r, pos=(1,1))
        self.abnormalWid.extend(self.varices_radio)
        
        Sizer.Add(tSizer)
        stSizer.Add(Sizer, pos = (4,0), span = (2,2))
        
        box = wx.StaticBox(self, wx.ID_ANY, "Otros")
        Sizer = wx.StaticBoxSizer(box)
        self.other = wx.TextCtrl(self, size = (200,60), style= wx.TE_MULTILINE )
        self.abnormalWid.append(self.other)
        Sizer.Add(self.other)
        stSizer.Add(Sizer, pos = (6,0), span= (1,4))
        
        mucoSizer.Add(stSizer)
        esofSizer.Add(mucoSizer)
        
        return esofSizer
    
    
    def _estomago(self):
        
        ## Lesiones sizer
        box = wx.StaticBox(self, wx.ID_ANY, "Estómago")
        boxSizer = wx.StaticBoxSizer(box)
        vBoxSizer = wx.BoxSizer(wx.VERTICAL)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Mucosa")
        mucosaSizer = wx.StaticBoxSizer(box)
        
        sizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        tags = ['Normal', 'Edema', 'Eritema', 'Micronodular', 'Otro']
        for i,j in enumerate(tags):
            tx = wx.StaticText(self, label = j)
            sizer.Add(tx, pos = (0, i + 1), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        self.est_mucosa = {}
        loc = ['Antro', 'Cuerpo', 'Fundus']
        
        for i,j in enumerate(loc): 
            tx = wx.StaticText(self, label = j)
            sizer.Add(tx, pos = (i+1, 0))
            for k in range(0, len(tags) -1):
                cb = wx.CheckBox(self)
                sizer.Add(cb, pos = (i + 1, k + 1), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
                self.est_mucosa.setdefault(j,[]).append(cb)
            cb = wx.TextCtrl(self, size = (90, 20))
            sizer.Add(cb, pos = (i + 1, len(tags)))
            self.est_mucosa[j].append(cb)
            
        mucosaSizer.Add(sizer)    
        vBoxSizer.Add(mucosaSizer)
        
        
        ## Lesiones section
        box = wx.StaticBox(self, wx.ID_ANY, "Lesiones")
        lesSizer = wx.StaticBoxSizer(box)
        lessionSizer = wx.BoxSizer(wx.VERTICAL)
        
        
        # Ulceras section
        box = wx.StaticBox(self, wx.ID_ANY, "Ulceras")
        ulSizer = wx.StaticBoxSizer(box)
        sizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        
        tx = wx.StaticText(self, label = "Cantidad")
        sizer.Add(tx, pos = (1,0), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        tx = wx.StaticText(self, label = "Tamaños")
        sizer.Add(tx, pos = (2,0), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        
        tags = ['Antro', 'Curvatura Mayor', 'Curvatura Menor', 'Fundus']
        self.est_lesiones = {}
        self.est_lesiones['ulceras'] = {}
        self.est_lesiones['ulceras']['pos'] = []
        self.est_lesiones['ulceras']['size'] = []
        
        for i,j in enumerate(tags):
            tx = wx.StaticText(self, label = j)
            bx = wx.TextCtrl(self, size = (25,20))
            sizer.Add(tx, pos = (0, i + 1))
            sizer.Add(bx, pos = (1, i + 1), flag=wx.ALIGN_CENTER_HORIZONTAL)
            self.est_lesiones['ulceras']['pos'].append(bx)
            bx = wx.TextCtrl(self, size = (25,20))
            sizer.Add(bx, pos = (2, i + 1), flag=wx.ALIGN_CENTER_HORIZONTAL)
            self.est_lesiones['ulceras']['size'].append(bx)
        
        
        forrest = ['Ia', 'Ib', 'IIa', 'IIb', 'IIc', 'III', 'N/A']
        self.est_lesiones['ulceras']['forrest'] = []
        fSizer = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self, label = "Forrest")
        fSizer.Add(tx, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 4)
        fSizer.Add((10,10))
        for i,j in enumerate(forrest):
            tx = wx.RadioButton(self, label = j)
            self.est_lesiones['ulceras']['forrest'].append(tx)
            fSizer.Add(tx, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 4)
        
        tx = wx.StaticText(self, label = 'Otros')
        sizer.Add(tx, pos = (4,0))
        self.est_lesiones['ulceras']['otros'] = wx.TextCtrl(self, size = (300, 20))
        sizer.Add(self.est_lesiones['ulceras']['otros'], pos = (4,1), span = (1,4))
        sizer.Add(fSizer, pos = (3,0), span = (1,6))
        ulSizer.Add(sizer)    
        lessionSizer.Add(ulSizer)
        
        
        # Varices section
        box = wx.StaticBox(self, wx.ID_ANY, "Varices")
        varSizer = wx.StaticBoxSizer(box)
        varicesSizer = wx.BoxSizer(wx.HORIZONTAL)
        types = ['IGV I', 'IGV II', 'GOV I', 'GOV II']
        self.est_lesiones['varices'] = {}
        self.est_lesiones['varices']['names'] = types
        self.est_lesiones['varices']['checks'] = []
        
        for i in types:
            bt = wx.CheckBox(self, label = i)
            varicesSizer.Add(bt, 0, wx.ALL, 5)
            self.est_lesiones['varices']['checks'].append(bt)
        
        
        # Polipo
        box = wx.StaticBox(self, wx.ID_ANY, "Polipos")
        polSizer = wx.StaticBoxSizer(box)
        sizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        
        tx = wx.StaticText(self, label = "Cantidad")
        sizer.Add(tx, pos = (1,0), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        tx = wx.StaticText(self, label = "Tamaños")
        sizer.Add(tx, pos = (2,0), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
        
        tags = ['Antro', 'Curvatura Mayor', 'Curvatura Menor', 'Fundus']
        self.est_lesiones = {}
        self.est_lesiones['polipos'] = {}
        self.est_lesiones['polipos']['pos'] = []
        self.est_lesiones['polipos']['size'] = []
        
        for i,j in enumerate(tags):
            tx = wx.StaticText(self, label = j)
            bx = wx.TextCtrl(self, size = (25,20))
            sizer.Add(tx, pos = (0, i + 1))
            sizer.Add(bx, pos = (1, i + 1), flag=wx.ALIGN_CENTER_HORIZONTAL)
            self.est_lesiones['polipos']['pos'].append(bx)
            bx = wx.TextCtrl(self, size = (25,20))
            sizer.Add(bx, pos = (2, i + 1), flag=wx.ALIGN_CENTER_HORIZONTAL)
            self.est_lesiones['polipos']['size'].append(bx)
        
        tx = wx.StaticText(self, label = 'Otros')
        sizer.Add(tx, pos = (4,0))
        self.est_lesiones['polipos']['otros'] = wx.TextCtrl(self, size = (300, 20))
        sizer.Add(self.est_lesiones['polipos']['otros'], pos = (4,1), span = (1,4))
        polSizer.Add(sizer)    
        
        
        # Other section
        box = wx.StaticBox(self, wx.ID_ANY, "Otro")
        otherSizer = wx.StaticBoxSizer(box)
        self.est_lesiones['other'] = wx.TextCtrl(self, size = (400, 40), style = wx.TE_MULTILINE)
        otherSizer.Add(self.est_lesiones['other'])
        
        
        
        varSizer.Add(varicesSizer)
        lessionSizer.Add(varSizer)
        
        
        lessionSizer.Add(polSizer)
        lessionSizer.Add(otherSizer)
        lesSizer.Add(lessionSizer)
        
        vBoxSizer.Add(lesSizer)
        boxSizer.Add(vBoxSizer)
        
        
        
        
        return boxSizer
    
    def _gridPol(self):
        pass
    
    def OnNormal(self, event):
        if event.Checked() == True:
            for i in self.abnormalWid:
                i.Disable()
        else:
            for i in self.abnormalWid:
                i.Enable()

    
    def _reason(self):
        
        box = wx.StaticBox(self, wx.ID_ANY, "Motivo de estudio")
        Sizer = wx.StaticBoxSizer(box)
        self.reason = wx.TextCtrl(self, size = (1250,60), style = wx.TE_MULTILINE)
        Sizer.Add(self.reason)
        
        return Sizer
    
     
    def _duodeno(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Duodeno")
        duExtSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        duBoxSizer = wx.BoxSizer(wx.VERTICAL)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Mucosa")
        mucStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        mucBoxSizer = wx.GridBagSizer(vgap = 5, hgap = 5)
        
        
        self.duo_mucosa = []
        tags = ['Normal', 'Edema', 'Dism. Pliegues', 'Dism. Vellosidades']
        for i,j in enumerate(tags):
            ch = wx.CheckBox(self, label = j)
            mucBoxSizer.Add(ch, pos = (0, i))
            self.duo_mucosa.append(ch)
        self.duo_mucosa[0].Bind(wx.EVT_CHECKBOX, self.OnDuodenoNormal)
        mucStSizer.Add(mucBoxSizer)
        
        
        box = wx.StaticBox(self, wx.ID_ANY, "Lesiones")
        lessStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        lessBoxSizer = wx.BoxSizer(wx.VERTICAL)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Ulceras")
        ulcStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        ulcBoxSizer = wx.GridBagSizer(vgap = 5, hgap = 5)
        
        tag = ['Bulbo', '2da Porción', '3era Porción']
        self.duo_lesiones = {}
        self.duo_lesiones['ulceras'] = {}
        self.duo_lesiones['ulceras']['pos'] = []
        self.duo_lesiones['ulceras']['forrest'] = []
         
        for i,j in enumerate(tag): 
            tx = wx.StaticText(self, label = j)
            ulcBoxSizer.Add(tx, pos = (0,i))
            bx = wx.TextCtrl(self, size = (25,20))
            ulcBoxSizer.Add(bx, pos = (1,i), flag=wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL)
            self.duo_lesiones['ulceras']['pos'].append(bx)
        
        tx = wx.StaticText(self, label = 'Tamaños (cm)')
        ulcBoxSizer.Add(tx, pos = (2,0))
        bx = wx.TextCtrl(self, size = (200,20))
        ulcBoxSizer.Add(bx, pos = (2,1), span = (1,3))
        self.duo_lesiones['ulceras']['size'] = bx
        
        
        forrest = ['Ia', 'Ib', 'IIa', 'IIb', 'IIc', 'III', 'N/A']
        self.duo_lesiones['ulceras']['forrest'] = []
        fSizer = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self, label = "Forrest")
        fSizer.Add(tx, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 4)
        fSizer.Add((10,10))
        for i,j in enumerate(forrest):
            tx = wx.RadioButton(self, label = j)
            self.duo_lesiones['ulceras']['forrest'].append(tx)
            fSizer.Add(tx, 4, wx.ALIGN_CENTER_VERTICAL|wx.ALIGN_CENTER_HORIZONTAL, 4)
        
        tx = wx.StaticText(self, label = "Otro")
        self.duo_lesiones['ulceras']['otro'] = wx.TextCtrl(self, size= (200, 20), style = wx.TE_MULTILINE)
        
        ulcBoxSizer.Add(fSizer, pos = (3,0), span =(1,4))
        ulcBoxSizer.Add(tx, pos = (4,0))
        ulcBoxSizer.Add(self.duo_lesiones['ulceras']['otro'], pos = (4,1), span = (1,4))
        
        ulcStSizer.Add(ulcBoxSizer)
        
        # Other section
        box = wx.StaticBox(self, wx.ID_ANY, "Otro")
        otherSizer = wx.StaticBoxSizer(box)
        self.duo_lesiones['other'] = wx.TextCtrl(self, size = (400, 40), style = wx.TE_MULTILINE)
        otherSizer.Add(self.duo_lesiones['other'])
        
        
        
        lessBoxSizer.Add(ulcStSizer)
        lessBoxSizer.Add(otherSizer)
        lessStSizer.Add(lessBoxSizer)
        
        
        duBoxSizer.Add(mucStSizer)
        duBoxSizer.Add(lessStSizer)
        duExtSizer.Add(duBoxSizer)
        return duExtSizer
        
        
    def OnDuodenoNormal(self, event):
        if event.Checked() == True:
            for i in self.duo_mucosa:
                i.Disable()
            self.duo_mucosa[0].Enable()
        else:
            for i in self.duo_mucosa:
                i.Enable()
    
    def MainWindow(self):
  
        #globalSizer = wx.BoxSizer(wx.VERTICAL)
        globalSizer = wx.GridBagSizer(hgap = 5, vgap = 5)
    
        reasonSizer = self._reason()
        esofSizer = self._esofago()
        #globalSizer.Add((10,10), 0)
        estogSizer = self._estomago()
        duodeno = self._duodeno()
        
        globalSizer.Add(reasonSizer, pos =(0,0), span = (1,3))
        globalSizer.Add(esofSizer, pos = (1,0))
        globalSizer.Add(estogSizer, pos = (1,1))
        globalSizer.Add(duodeno, pos = (1,2))
        
        #globalSizer.Add(reasonSizer)
        #globalSizer.Add(esofSizer)
        self.SetSizer(globalSizer)
        globalSizer.Fit(self)
        
            
class PolipoEstomago():
    def __init__(self, loc, size, cecil= None, pediculado= None, otro = None):
        self.loc = loc
        self.size = size
        self.cecil = cecil
        self.pediculado = pediculado
        self.otro = otro
    