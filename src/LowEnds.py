# -*- coding: utf-8 -*-
import wx

class LowEnds(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.size = (760,680) 
        self.MainWindow()
        
        
    def MainWindow(self):
        
        #globalSizer = wx.GridBagSizer(hgap = 5, vgap = 5)
        globalSizer = wx.BoxSizer(wx.VERTICAL)
        panelSizer = wx.BoxSizer(wx.HORIZONTAL)
        firstSizer = wx.BoxSizer(wx.VERTICAL)
        secondSizer = wx.BoxSizer(wx.VERTICAL)
        
        reasonSizer = self._reason()
        tacto = self._tacto()
        ciego = self._ciego()
        pat_vasc = self._patronVascular()
        mucosa = self._mucosa()
        calidad = self._calidad()
        
        
        globalSizer.Add(reasonSizer, 0, wx.ALL, 0)
        firstSizer.Add(tacto, 0, wx.ALL, 0)
        firstSizer.Add(ciego, 0, wx.ALL, 0)
        firstSizer.Add(pat_vasc, 0, wx.ALL, 0)
        firstSizer.Add(mucosa, 0, wx.ALL, 0)
        firstSizer.Add(calidad, 0, wx.ALL, 0)
        
        lessSizer = wx.BoxSizer(wx.VERTICAL)
        lesiones = self._lesiones()
        secondSizer.Add(lesiones, 0, wx.ALL, 0)
        
        self.bNext = wx.Button(self, -1, "Generar Informe", size = (150, 40))
        self.bPrev = wx.Button(self, -1, "Anterior", size = (150, 40))
        bSizer = wx.BoxSizer(wx.HORIZONTAL)
        bSizer.Add((55,100))
        bSizer.Add(self.bPrev, wx.EXPAND)
        bSizer.Add(self.bNext, wx.EXPAND)
        
        secondSizer.Add(bSizer)
        
        panelSizer.Add(firstSizer)
        panelSizer.Add(secondSizer)
        globalSizer.Add(panelSizer)
        self.SetSizer(globalSizer)
        globalSizer.Fit(self)
        
    def _reason(self):
        
        box = wx.StaticBox(self, wx.ID_ANY, "Motivo de estudio - Endoscopía Baja")
        Sizer = wx.StaticBoxSizer(box)
        self.reason = wx.TextCtrl(self, size = (710,60), style = wx.TE_MULTILINE)
        Sizer.Add(self.reason)
        
        return Sizer   
        
    def _tacto(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Tacto Rectal")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        tags = ['Normal', 'Esfinter hipotónico', 'Hemorroides externas']
        self.tacto_checks = []
        for i,j in enumerate(tags):
            ch = wx.CheckBox(self, label = j)
            boxSizer.Add(ch)
            self.tacto_checks.append(ch)
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        self.tacto_checks[0].Bind(wx.EVT_CHECKBOX, self.OnTactoNormal)
        tx = wx.StaticText(self, label = 'Otro')
        
        sizer.Add(tx, 0, wx.ALL, 1)
        self.tacto_other = wx.TextCtrl(self, size = (330,20))
        sizer.Add(self.tacto_other, 0, wx.ALL, 1)
        
        boxStSizer.Add(boxSizer)
        boxStSizer.Add((10,10))
        boxStSizer.Add(sizer)

        return boxStSizer
    
    def _ciego(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Llegada a ciego")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        self.ciego_checks = []
        tags = ['Si', 'No']
        for i in tags:
            cb = wx.RadioButton(self, label = i)
            boxSizer.Add(cb)
            self.ciego_checks.append(cb)
            cb.Bind(wx.wx.EVT_RADIOBUTTON, self.OnCiegoNo)
        
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self, label = 'Motivo')
        ct = wx.TextCtrl(self, size = (320,40), style = wx.TE_MULTILINE)
        self.ciego_reason = ct
        sizer.Add(tx)
        sizer.Add(ct)

        boxStSizer.Add(boxSizer)
        boxStSizer.Add(sizer)        
        return boxStSizer
        
        
    
    def _patronVascular(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Patrón Vascular")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        cb = wx.CheckBox(self, label = 'Conservado')
        boxStSizer.Add(cb)
        self.pat_vasc_check = cb
        cb.Bind(wx.EVT_CHECKBOX, self.OnPatVascCons)
        
        tx = wx.StaticText(self, label = 'Comentarios')
        tc = wx.TextCtrl(self, size = (280,60), style = wx.TE_MULTILINE)
        self.pat_vas_reason = tc
        boxSizer.Add(tx)
        boxSizer.Add(tc)

        boxStSizer.Add(boxSizer)
        return boxStSizer
        
    
    def _mucosa(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Mucosa")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        boxSizer = wx.BoxSizer(wx.HORIZONTAL)
        
        cb = wx.CheckBox(self, label = 'Normal')
        boxStSizer.Add(cb)
        self.mucosa_check = cb
        cb.Bind(wx.EVT_CHECKBOX, self.OnMucosaNormal)
        
        tx = wx.StaticText(self, label = 'Otros')
        tc = wx.TextCtrl(self, size = (320,40), style = wx.TE_MULTILINE)
        self.mucosa_reason = tc
        boxSizer.Add(tx)
        boxSizer.Add(tc)
        
        boxStSizer.Add(boxSizer)
        return boxStSizer
        

    def _calidad(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Calidad de la preparación")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        gridSizer = wx.GridBagSizer(hgap = 5, vgap =5)
        
        tags = ['0','1','2','3']
        
        for i,j in enumerate(tags):
            st = wx.StaticText(self, label = j)
            gridSizer.Add(st, pos = (0, i + 1))
        
        tags = ['CD', 'CT', 'CI']
        self.calidad_radio =[]
        for i,j in enumerate(tags):
            l = []
            st = wx.StaticText(self, label = j)
            gridSizer.Add(st, pos = (i + 1, 0))
            for k in range(0,4):
                if k == 0:
                    ch = wx.RadioButton(self, style = wx.RB_GROUP)
                else:
                    ch = wx.RadioButton(self)
                gridSizer.Add(ch, pos = (i + 1, k + 1))
                l.append(ch)
                ch.Bind(wx.EVT_RADIOBUTTON, self.OnCalidad)
            self.calidad_radio.append(l)
        
        tx = wx.StaticText(self, label = 'Boston: ')
        self.calidad_total = wx.StaticText(self, label = '0')
        gridSizer.Add(tx, pos = (3, 6))
        gridSizer.Add(self.calidad_total, pos = (3, 7))
        
        boxStSizer.Add(gridSizer)
        return boxStSizer
            
    def _lesiones(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Lesiones")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        
        
        box = wx.StaticBox(self, wx.ID_ANY, "Lesiones Vasculares")
        boxAuxSizer = wx.StaticBoxSizer( box, wx.HORIZONTAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        tags = ['CD','CT', 'Sigmoides', 'Recto']
        self.lesiones_vasculares = []
        for i,j in enumerate(tags):
            tx = wx.StaticText(self, label = j)
            hsizer.Add(tx)
            cb = wx.TextCtrl(self, size = (30,20))
            hsizer.Add(cb)
            hsizer.Add((10,10))
            self.lesiones_vasculares.append(cb)
        vsizer.Add(hsizer)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self, label = 'Comentarios')
        self.lesiones_vasc_otros = wx.TextCtrl(self, size = (207,40), style = wx.TE_MULTILINE)
        hsizer.Add(tx)
        hsizer.Add(self.lesiones_vasc_otros)
        vsizer.Add(hsizer)
        boxAuxSizer.Add(vsizer)
        boxStSizer.Add(boxAuxSizer)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Hemorroides")
        boxAuxSizer = wx.StaticBoxSizer( box, wx.HORIZONTAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        tags = ['INT','EXT']
        self.lesiones_hemorroides = []
        for i,j in enumerate(tags):
            cb = wx.CheckBox(self, label = j)
            hsizer.Add(cb)
            hsizer.Add((10,10))
            self.lesiones_hemorroides.append(cb)
        vsizer.Add(hsizer)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self, label = 'Comentarios')
        self.lesiones_hemorroides_otros = wx.TextCtrl(self, size = (207,40), style = wx.TE_MULTILINE)
        hsizer.Add(tx)
        hsizer.Add(self.lesiones_hemorroides_otros)
        vsizer.Add(hsizer)
        boxAuxSizer.Add(vsizer)
        boxStSizer.Add(boxAuxSizer)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Diverticulos")
        boxAuxSizer = wx.StaticBoxSizer( box, wx.HORIZONTAL)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        vsizer = wx.BoxSizer(wx.VERTICAL)
        tags = ['CD','CT', 'Sigmoides', 'Recto']
        self.lesiones_diverticulos = []
        for i,j in enumerate(tags):
            tx = wx.StaticText(self, label = j)
            hsizer.Add(tx)
            cb = wx.TextCtrl(self, size = (30,20))
            hsizer.Add(cb)
            hsizer.Add((10,10))
            self.lesiones_diverticulos.append(cb)
        vsizer.Add(hsizer)
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        tx = wx.StaticText(self, label = 'Comentarios')
        self.lesiones_diverticulos_otros = wx.TextCtrl(self, size = (207,40), style = wx.TE_MULTILINE)
        hsizer.Add(tx)
        hsizer.Add(self.lesiones_diverticulos_otros)
        vsizer.Add(hsizer)
        boxAuxSizer.Add(vsizer)
        boxStSizer.Add(boxAuxSizer)
        
        polipo = self._polipo()
        boxStSizer.Add(polipo)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Otros")
        boxAuxSizer = wx.StaticBoxSizer( box, wx.HORIZONTAL)
        
        self.lesiones_otros = wx.TextCtrl(self, size = (300,80), style = wx.TE_MULTILINE)
        
        boxAuxSizer.Add(self.lesiones_otros)
        
        boxStSizer.Add(boxAuxSizer)
        return boxStSizer
    
    
    def _polipo(self):
        box = wx.StaticBox(self, wx.ID_ANY, "Pólipos")
        boxStSizer = wx.StaticBoxSizer( box, wx.VERTICAL)
        
        self.polipos = []
        self.polipos_but = wx.Button(self, label = 'Cargar pólipos')
        boxStSizer.Add(self.polipos_but)
        
        return boxStSizer

    
    
    # Handlers
    def OnTactoNormal(self, event):
        if event.Checked() == True:
            for i in self.tacto_checks:
                i.SetValue(False)
                i.Disable()
            self.tacto_checks[0].Enable()
            self.tacto_checks[0].SetValue(True)
            self.tacto_other.Disable()
        else:
            self.tacto_other.Enable()
            for i in self.tacto_checks:
                i.Enable()
    
    def OnCiegoNo(self, event):
        if (self.ciego_checks[0].GetValue()):
            self.ciego_reason.Disable()
        if (self.ciego_checks[1].GetValue()):    
            self.ciego_reason.Enable()
    
    def OnPatVascCons(self, event):
        if event.Checked() == True:
            self.pat_vas_reason.Disable()
        else:
            self.pat_vas_reason.Enable()
            
    def OnMucosaNormal(self, event):
        if event.Checked() == True:
            self.mucosa_reason.Disable()
        else:
            self.mucosa_reason.Enable()
    
    def OnCalidad(self, event):
        def argmax(l):
            for i, b in enumerate(l): 
                if b.GetValue():
                    return i
            return 0
        
        total = 0 
        for l in self.calidad_radio:
            total += argmax(l)
        
        self.calidad_total.SetLabel(str(total))
        
    
        