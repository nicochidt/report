# -*- coding: utf-8 -*-
import wx

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
        
        return esofSizer
    
    def _mucosa(self):
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
        self.other = wx.TextCtrl(self, size = (300,60), style= wx.TE_MULTILINE )
        self.abnormalWid.append(self.other)
        Sizer.Add(self.other)
        stSizer.Add(Sizer, pos = (6,0), span= (1,4))
        
        mucoSizer.Add(stSizer)
        
        return mucoSizer
    
    def OnNormal(self, event):
        
        print event
        print dir(event)
        print event.Checked()
        if event.Checked() == True:
            
            for i in self.abnormalWid:
                i.Disable()
        
        else:
            for i in self.abnormalWid:
                i.Enable()

    
    def _reason(self):
        
        box = wx.StaticBox(self, wx.ID_ANY, "Motivo de estudio")
        Sizer = wx.StaticBoxSizer(box)
        self.reason = wx.TextCtrl(self, size = (900,60), style = wx.TE_MULTILINE)
        Sizer.Add(self.reason)
        
        return Sizer
        
    def MainWindow(self):
  
        globalSizer = wx.BoxSizer(wx.VERTICAL)
    
        reasonSizer = self._reason()
        esofSizer = self._esofago()
        globalSizer.Add((10,10), 0)
        mucoSizer = self._mucosa()
        esofSizer.Add(mucoSizer)
        
        globalSizer.Add(reasonSizer)
        globalSizer.Add(esofSizer)
        #globalSizer.Add(mucoSizer)
        self.SetSizer(globalSizer)
        globalSizer.Fit(self)
        
            
            