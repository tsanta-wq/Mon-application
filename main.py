from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivy.graphics.context_instructions import PushMatrix, PopMatrix, Rotate
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window

# 1. ÉCRAN DE DÉMARRAGE (Splash Screen)
class ScreenDemarrage(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        
        # Fond noir pour le style jeu vidéo
        with self.canvas.before:
            Color(0.05, 0.05, 0.1, 1)
            self.rect = Rectangle(size=Window.size, pos=self.pos)
            
        # Votre nom écrit en gros au milieu
        self.label_titre = Label(
            text="FIDIMANANTSOA Tsantaniaina\nprésente...", 
            font_size='28sp',
            halign='center',
            color=(0, 0.8, 1, 1)
        )
        layout.add_widget(self.label_titre)
        self.add_widget(layout)

# 2. L'INTERFACE DU JEU 3D (Simulation de Cube 3D en rotation)
class Jeu3D(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')
        
        # Label d'instructions
        self.layout.add_widget(Label(text="Simulation Moteur 3D Python", size_hint_y=0.1, color=(1,1,1,1)))
        
        # Zone d'affichage du cube 3D
        self.zone_rendu = BoxLayout()
        with self.zone_rendu.canvas:
            Color(0.2, 0.2, 0.2, 1)
            Rectangle(size=(Window.width, Window.height * 0.8), pos=(0, 0))
            
            # Application d'une matrice de rotation pour l'effet 3D
            Color(1, 0, 0.4, 1) # Couleur du cube
            PushMatrix()
            self.rot = Rotate(angle=0, axis=(1, 1, 0), origin=(Window.width/2, Window.height/2))
            # Dessin des faces du cube (coordonnées)
            self.cube = Rectangle(size=(200, 200), pos=(Window.width/2 - 100, Window.height/2 - 100))
            PopMatrix()
            
        self.layout.add_widget(self.zone_rendu)
        self.add_widget(self.layout)
        
        # Mettre en mouvement le cube toutes les 60èmes de seconde
        Clock.schedule_interval(self.update_rotation, 1.0 / 60.0)

    def update_rotation(self, dt):
        self.rot.angle += 1 # Fait tourner l'objet 3D

# 3. GESTIONNAIRE DE L'APPLICATION
class MonJeu3DApp(App):
    def build(self):
        self.sm = ScreenManager()
        
        # Création des écrans
        self.ecran_debut = ScreenDemarrage(name='menu')
        self.ecran_jeu = Jeu3D(name='jeu')
        
        self.sm.add_widget(self.ecran_debut)
        self.sm.add_widget(self.ecran_jeu)
        
        # Changer d'écran automatiquement après 4 secondes d'affichage de votre nom
        Clock.schedule_once(self.lancer_jeu, 4)
        
        return self.sm

    def lancer_jeu(self, dt):
        self.sm.current = 'jeu'

if __name__ == '__main__':
    MonJeu3DApp().run()
