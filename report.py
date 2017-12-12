# -*- coding: utf-8 -*-
import wx
from MainView import *
from HiEnds import *

SIZE = (1000, 650)

class MainFrame(wx.Frame):

    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title=title, size = SIZE, style =  wx.DEFAULT_FRAME_STYLE)
        
        #self.mainPanel = MainView(self)
        self.HiEnds = HiEnds(self)
        
        
       # self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
        self.CreateStatusBar()

        menu = self.CreateMenu(self.MainMenuData() )

        self.SetMenuBar(menu)
        self.Show()

    
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



#Execute the application

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None, 'Generador de reportes')
    app.MainLoop()
