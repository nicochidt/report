# -*- coding: utf-8 -*-
import wx
from MainView import *
from HiEnds import *
from LowEnds import *
from Polipo import *


class MainFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, style =  wx.DEFAULT_FRAME_STYLE)
        
        
        self.DefinePanels()
        self.BindNavigators()
        
        self.CreateStatusBar()
        menu = self.CreateMenu(self.MainMenuData() )
        
        self.baja = False
        self.alta = True
        self.active_window = "main"
        
        self.SetMenuBar(menu)
        self.Show()
    
    def DefinePanels(self):
        self.mainPanel = MainView(self)
        self.SetSize(self.mainPanel.size)
        self.HiEnds = HiEnds(self)
        self.HiEnds.Hide()
        self.LowEnds = LowEnds(self)
        self.LowEnds.Hide()
        
        self.Layout()
        self.mainPanel.Layout()
    
    def BindNavigators(self):
        self.mainPanel.bNext.Bind(wx.EVT_BUTTON, self.OnNext)
        self.HiEnds.bNext.Bind(wx.EVT_BUTTON, self.OnNext)
        self.HiEnds.bPrev.Bind(wx.EVT_BUTTON, self.OnPrev)
        
        self.LowEnds.bPrev.Bind(wx.EVT_BUTTON, self.OnPrev)
        self.LowEnds.bNext.Bind(wx.EVT_BUTTON, self.OnGen)
        self.LowEnds.polipos_but.Bind(wx.EVT_BUTTON, self.OnPolipo)
        
        
        
    def MainMenuData(self):
        data = [('Archivo', [(wx.ID_ANY, 'Salir', 'Sale del programa', self.OnExit), (wx.ID_ANY, 'Guardar', 'Guardar datos', self.OnSave)]),
                ('Ayuda',   [(wx.ID_ANY, 'Sobre', 'Información sobre el programa', self.OnAbout)])
                ]
        return data
    
    

    def CreateMenu(self, data):

        menuBar = wx.MenuBar()
        for m, d in data:
            menu = wx.Menu()
            for i,j,k,l in d:
                item = menu.Append(i,j,k)
                self.Bind(wx.EVT_MENU, l, item)
                menu.AppendSeparator()

            menuBar.Append(menu, m)


        return menuBar
    
    
    def GenerarInforme(self):
        pass
    
    def switchPanel(self, prevpanel, newpanel):
        prevpanel.Hide()
        newpanel.Show()
        self.SetSize(newpanel.size)
        
        
    # Handlers
    def OnAbout(self, event):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog( self, "Autor: Nicolás Chiaraviglio", "Sobre", wx.OK)
        dlg.ShowModal() # Show it
        dlg.Destroy() # finally destroy it when finished.

    def OnExit(self, event):
        self.Close(True)
    
    
    def OnNew(self, event):
        return

    def OnSave(self, event):
        return
    
    def OnNext(self, event):
        if self.mainPanel.IsShown():
            self.baja = self.mainPanel.bBaja.GetValue()
            self.alta = self.mainPanel.bAlta.GetValue()
            if self.alta:
                self.switchPanel(self.mainPanel, self.HiEnds )
                self.HiEnds.bNext.SetLabel("Siguiente")
                if not self.baja:
                    self.HiEnds.bNext.SetLabel("Generar Informe")
                return
            if self.baja:
                self.switchPanel(self.mainPanel, self.LowEnds )
                return
            
        if self.HiEnds.IsShown():
            if not self.baja:
                self.GenerarInforme()
            else:
                self.switchPanel(self.HiEnds, self.LowEnds)
                return
    
        
    def OnGen(self, event):
        self.GenerarInforme()
        
        
    def OnPrev(self, event):
        if self.LowEnds.IsShown():
            if self.alta:
                self.switchPanel(self.LowEnds, self.HiEnds) 
            else:    
                self.switchPanel(self.LowEnds, self.mainPanel)    
            return
        
        if self.HiEnds.IsShown():
            self.switchPanel(self.HiEnds, self.mainPanel)    
        
    
    def OnPolipo(self, event):
        self.win = PolipoFrame(self)
        self.win.Show()
    
    

#Execute the application

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None, 'Generador de reportes')
    app.MainLoop()
