# -*- coding: utf-8 -*-
import wx


class PolipoFrame(wx.Frame):

    def __init__(self, parent, title = "Pólipos"):
        size = (900,480)
        wx.Frame.__init__(self, parent, title=title, style =  wx.DEFAULT_FRAME_STYLE, size = size)
        
        self.panel = self.screen(self)
        
        self.panel.accept.Bind(wx.EVT_BUTTON, self.OnAccept)
        
        self.CreateStatusBar()
        

        
        
    class screen(wx.Panel):
        def __init__(self, parent):
            wx.Panel.__init__(self, parent = parent)
            self.MainWindow()
        
        
        def MainWindow (self):
            
            globalGrid = wx.GridBagSizer(hgap = 5, vgap = 5)
            box = wx.StaticBox(self, wx.ID_ANY, "")
            globalBoxSizer = wx.StaticBoxSizer(box)
            
            vSizer = wx.BoxSizer(wx.VERTICAL)
            gSizer = wx.GridBagSizer(hgap = 5, vgap = 5)
            
            tx = wx.StaticText(self, label = 'Cantidad:')
            gSizer.Add(tx, pos = (1, 0))
            loc = ['CD', 'CT', 'Sigmoides', 'Recto']
            self.loc_tags = loc
            self.location = []
            for i,j in enumerate(loc):
                tx = wx.StaticText(self, label = j)
                gSizer.Add(tx, pos = (0, i + 1), flag = wx.ALIGN_CENTER_HORIZONTAL | wx.SHAPED)
                tc = wx.SpinCtrl(self, size = (50,20))
                self.location.append(tc)
                gSizer.Add(tc, pos = (1, i + 1), flag = wx.ALIGN_CENTER_HORIZONTAL | wx.SHAPED)
            vSizer.Add(gSizer)
            vSizer.Add((10,10))
            
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            tx = wx.StaticText(self, label = 'Tamaño:')
            hSizer.Add(tx)
            hSizer.Add((10,10))
            self.size = wx.TextCtrl(self, size =(200,20))
            hSizer.Add(self.size)
            vSizer.Add(hSizer)
            vSizer.Add((10,10))
            
            box = wx.StaticBox(self, wx.ID_ANY, "Clasificaión de Paris")
            boxSizer = wx.StaticBoxSizer(box)
            gSizer = wx.GridBagSizer(hgap = 5, vgap = 5)
            
            tags = ['I-P', 'I-SP', 'IS', 'IIA', 'IIB', 'IIC']
            self.paris_tags = tags
            self.paris = []
            for i in range(0,2):
                for j in range(0,3):
                    cb = wx.RadioButton(self, label = tags[i * 2 + j])
                    gSizer.Add(cb, pos = (i,j))
                    self.paris.append(cb)
            boxSizer.Add(gSizer)
            vSizer.Add(boxSizer)
            vSizer.Add((10,10))
            
            
            
            box = wx.StaticBox(self, wx.ID_ANY, "Patrón de Kudo")
            boxSizer = wx.StaticBoxSizer(box)
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            tags = ['I', 'II', 'III', 'IV', 'V']
            self.kudo_tags = tags
            self.kudo = []
            for i,j in enumerate(tags):
                if i == 0:
                    cb = wx.RadioButton(self, label = j, style = wx.RB_GROUP)
                else:
                    cb = wx.RadioButton(self, label = j)
                hSizer.Add(cb)
                self.kudo.append(cb)
            boxSizer.Add(hSizer)
            vSizer.Add(boxSizer)
            vSizer.Add((10,10))
           
            box = wx.StaticBox(self, wx.ID_ANY, "Otros")
            boxAuxSizer = wx.StaticBoxSizer( box, wx.HORIZONTAL)
            self.otros = wx.TextCtrl(self, size = (270,80), style = wx.TE_MULTILINE)
            boxAuxSizer.Add(self.otros)
            vSizer.Add(boxAuxSizer)
            vSizer.Add((10,10))
            
            box = wx.StaticBox(self, wx.ID_ANY, "Polipectomía")
            boxAuxSizer = wx.StaticBoxSizer( box, wx.HORIZONTAL)
            hSizer = wx.BoxSizer(wx.HORIZONTAL)
            
            tx = wx.StaticText(self, label = 'Método')
            hSizer.Add(tx)
            self.polipectomia = wx.TextCtrl(self, size = (220,20))
            hSizer.Add(self.polipectomia)
            
            boxAuxSizer.Add(hSizer)
            vSizer.Add(boxAuxSizer)
            vSizer.Add((10,10))
            globalBoxSizer.Add(vSizer)
            globalGrid.Add(globalBoxSizer, pos = (0,0), span = (12, 4))
            
            
            # rigth column
            box = wx.StaticBox(self, wx.ID_ANY, "")
            globalBoxSizer = wx.StaticBoxSizer(box)
            
            self.list = wx.ListCtrl(self, style = wx.LC_REPORT)
            cols= ['#', 'Ubicación' ,'Tamaño', 'Paris', 'Kudo', 'Comentarios', 'Polipectomía']
            for i,j in enumerate(cols):
                self.list.InsertColumn(i, j)
                
            globalGrid.Add(self.list, pos = (0,5), span = (1,4))
            
            self.add    = wx.Button(self, label = '+')
            self.add.Bind(wx.EVT_BUTTON, self.OnAdd)
            
            self.remove = wx.Button(self, label = '-')
            self.remove.Bind(wx.EVT_BUTTON, self.OnRemove)
            globalGrid.Add(self.add, pos = (1,5), flag = wx.ALIGN_RIGHT| wx.EXPAND)
            globalGrid.Add(self.remove, pos = (1,6), flag = wx.ALIGN_RIGHT| wx.EXPAND)
            
            self.accept = wx.Button(self, label = 'Aceptar')
            
            self.cancel = wx.Button(self, label = 'Cancelar')
            self.cancel.Bind(wx.EVT_BUTTON, self.OnCancel)
            globalGrid.Add(self.accept, pos = (2,5), flag = wx.ALIGN_RIGHT | wx.EXPAND)
            globalGrid.Add(self.cancel, pos = (2,6), flag = wx.ALIGN_RIGHT | wx.EXPAND)
            
            
            self.SetSizer(globalGrid)
            globalGrid.Fit(self)
        
        
        #handlers
        def OnAdd(self, evt):
            self.pol = []
            sum = 0
            paris = ''
            kudo = ''
            size = self.size.GetValue().split(',')
            
            
            for i,j in enumerate(self.paris):
                if j.GetValue():
                    paris = self.paris_tags[i]
            
            for i,j in enumerate(self.kudo):
                if j.GetValue():
                    kudo = self.kudo_tags[i]
            s = 0
            num = []
            pos = 0
            for i,j in zip(self.loc_tags, self.location):    
                aux = j.GetValue()
                s += aux
                if aux > 0:
                    pos +=1
                num.append(aux)
            polipect = self.polipectomia.GetValue() if len(self.polipectomia.GetValue()) > 0 else None
            
            if s == 0:
                return
            
            if len(size) != s:
                if len(size) == 1:
                    aux = size * s
                elif len(size) == pos:
                    aux = []
                    ind = 0
                    for i in self.locations:
                        if i >0:
                            aux.extend([size[ind]] * i)
                elif len(size) > s:
                    aux = size[0:s]
                else:   # len(size) < s
                    aux = size
                    aux.extend([size[-1]] * ( s - len(size)))                        
                size = aux
            
            
            
            for i,j,k,l in zip(num, self.location, size, self.loc_tags):
                if i >0 :
                    p = Polipo(i, k, l, paris, kudo, self.otros.GetValue() , polipect)
                    self.pol.append(p)
                    self.list.Append(p.getList())
                    
            
            
    
        
        def OnRemove(self,evt):
            pass
        
        
        
        def OnCancel(self, evt):
            pass
        
    def OnAccept(self, evt):    
        self.Close()

        
        
        
        
class Polipo():
    
    def __init__(self, num, size, loc, paris, kudo, other = None, polipect =None):
        self.num = num
        self.location = loc
        self.size = size
        self.paris = paris
        self.polipectomia = polipect
        self.kudo = kudo
        self.other = other
        
    def getDic(self):
        ret = {}
        ret['num'] = self.num
        ret['size'] = self.size
        ret['paris'] = self.paris
        ret['location'] = self.location
        ret['kudo'] = self.kudo
        ret['polipectomia'] = self.polipectomia if self.polipectomia != None else None
        ret['comments'] = self.other
        
        return ret
    
    def getList(self):
        ret = []
        ret.append(self.num)
        ret.append(self.location)
        ret.append(self.size)
        ret.append(self.paris)
        ret.append(self.kudo)
        ret.append(self.other)
        ret.append(self.polipectomia if self.polipectomia != None else None)
        
        return ret
        
    
    
