from .datenmodelle import Bibliothek
from .GUI import App

# Weitere notwendige Importe...


bibliothek = Bibliothek()
screen = App(bibliothek=bibliothek)
screen.mainloop()