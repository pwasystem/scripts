from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class MinhaApp(App):
    def build(self):
        # Cria um layout de caixa vertical
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Cria um rótulo (Label)
        self.rotulo = Label(text="Olá, Kivy!", font_size='24sp')
        
        # Cria um botão
        botao = Button(text="Clique Aqui!", size_hint=(None, None), size=(300, 150))
        botao.bind(on_press=self.atualizar_texto)
        
        # Adiciona os widgets ao layout
        layout.add_widget(self.rotulo)
        layout.add_widget(botao)
        
        return layout

    def atualizar_texto(self, instance):
        self.rotulo.text = "Texto Atualizado!"

if __name__ == '__main__':
    MinhaApp().run()