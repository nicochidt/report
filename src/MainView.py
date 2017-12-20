# -*- coding: utf-8 -*-
import wx
import wx.calendar

class MainView(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent = parent)
        self.size = (370,400)
        self.MainWindow()
        
    
    def MainWindow (self):

        # a few sizers
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        gridSizer = wx.GridBagSizer(hgap=5, vgap = 5)
        buttSizer = wx.GridBagSizer(hgap=5, vgap =5)

        box = wx.StaticBox(self, wx.ID_ANY, "Información del paciente")
        persSizer = wx.StaticBoxSizer(box)


        # Personal Information
        text = ['Nombre', 'Apellido', 'DNI', 'Obra Social', 'Nro. Afiliado']
        self.textField = []

        gridSizer.Add((10,10), pos = (0,0))
        for j,i in enumerate(text):
            gridSizer.Add((10, 5), pos=(j + 1,0))
            t = wx.StaticText(self, label = i)
            gridSizer.Add(t, pos = (j + 1,1))
            b = wx.TextCtrl(self, size = (200,20))
            self.textField.append(b)
            gridSizer.Add(b, pos = (j + 1,2))
        persSizer.Add(gridSizer)
        
        box = wx.StaticBox(self, wx.ID_ANY, "Información del Estudio")
        Sizer = wx.StaticBoxSizer(box)
        gridSizer = wx.GridBagSizer(wx.VERTICAL)
        
        tx = wx.StaticText(self, label = 'Fecha')
        gridSizer.Add(tx, pos = (0,0))
        self.cal = wx.DatePickerCtrl(self, -1, wx.DateTime_Now(), style=wx.DP_DROPDOWN)
        gridSizer.Add(self.cal, pos = (0,1))
        tx = wx.StaticText(self, label = 'Operador')
        gridSizer.Add(tx, pos = (1,0))
        self.operator = wx.Choice(self, choices = ['Chiaraviglio', 'Perez'])
        gridSizer.Add(self.operator, pos = (1,1))
        self.add_operator = wx.Button(self, -1, '+', size = (30,20))
        gridSizer.Add(self.add_operator, pos = (1,2))
        
        
        Sizer.Add(gridSizer)

        
        # Buttons
        buttSizer.Add((10,10), pos = (0,10))
        self.bAlta = wx.ToggleButton(self, -1, "Endoscopía Alta")
        buttSizer.Add(self.bAlta,  pos = (0,1))
        #buttSizer.Add(self.bAlta,  pos = (0,1))
        self.bBaja = wx.ToggleButton(self, -1, "Endoscopía Baja")
        
        buttSizer.Add(self.bBaja,  pos = (0,2))
        self.bNext = wx.Button(self, -1, "Siguiente")
        buttSizer.Add(self.bNext,  pos = (1,2))
        

        # Arrange Layout
        mainSizer.Add(persSizer, 0, wx.ALL, 5)
        mainSizer.Add(Sizer, 0, wx.ALL, 5)
        mainSizer.Add(buttSizer,0, wx.ALL, 5)

        persSizer.SetSizeHints(self)
        buttSizer.SetSizeHints(self)
        mainSizer.SetSizeHints(self)
        self.SetSizer(mainSizer)

        self.SetAutoLayout(1)

        mainSizer.Fit(self)


    # Event handlers

    def OnTab(self, event):
        keycode = event.GetKeyCode()
        if keycode == wx.WXK_RETURN or keycode == wx.WXK_NUMPAD_ENTER or keycode == wx.WXK_TAB:
            event.EventObject.Navigate()
        event.Skip()

