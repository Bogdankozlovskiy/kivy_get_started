# from kivy.app import App
# from kivy.uix.button import Button
# from kivy.uix.codeinput import CodeInput 
from pygments.lexers import HtmlLexer
from kivy.config import Config
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scatter import Scatter
Config.set('graphics', 'resizable', '0')
Config.set('graphics', 'width', '700')
Config.set('graphics', 'height', '400')


class MyApp(App):
	def build(self):
		s = Scatter()
		f = FloatLayout(size=(300, 300))
		s.add_widget(f)
		f.add_widget(CodeInput(lexer = HtmlLexer(), size_hint=(.5, .5), pos=(0, 200)))
		f.add_widget(Button(text="hello", size_hint=(.25, .25), pos=(0, 0)))
		return s

MyApp().run()
