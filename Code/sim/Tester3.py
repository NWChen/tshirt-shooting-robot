from gi.repository import Gtk, GObject
import cairo
import math
import time

class Example(Gtk.Window):

    def __init__(self):
        super(Example, self).__init__()
        
        self.init_ui()
        
        
    def init_ui(self):    

        darea = Gtk.DrawingArea()
        darea.connect("draw", self.on_draw)
        self.add(darea)

        self.set_title("Donut")
        self.resize(1000, 1000)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.connect("delete-event", Gtk.main_quit)
        self.show_all()
        
    
    def on_draw(self, wid, cr):

        cr.set_line_width(0.5)

        w, h = self.get_size()
       
        cr.translate(w/2, h/2)
        #cr.arc(0, 0, 120, 0, 2*math.pi)
        #cr.stroke()
         
        for i in xrange(1, 36):
            cr.save()
            #cr.translate(0, h/i)
            cr.rotate(i*math.pi/36)
            #cr.scale(1, 1)
            cr.rectangle(0, 0, 40, 40)
            cr.restore()
            cr.stroke()
    
def main():
    
    app = Example()
    Gtk.main()
        
        
if __name__ == "__main__":    
    main()