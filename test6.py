import Tkinter as tk

class SampleApp(tk.Tk):

    global output,inpu
    output=[]

    def __init__(self, *args, **kwargs ):

        output = []
        tk.Tk.__init__(self, *args, **kwargs)
        lb = tk.Listbox(self)
        for i in range(len(inpu)):
            lb.insert('end',inpu[i])
        lb.bind("<Double-Button-1>", self.OnDouble)
        lb.pack(side="top", fill="both", expand=True)
        button=tk.Button(self)


    def OnDouble(self, event):
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        print "selection:", selection, ": '%s'" % value
        output.append(selection[0])


if __name__ == "__main__":
    inpu=[]
    for i in range(10):
        inpu.append(i)
    app = SampleApp()
    app.mainloop()
    print output