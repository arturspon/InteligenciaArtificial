from random import *
class Pergunta:
	def __init__(self):
		self.level = [
			['O seu Pet está comendo bem?','alimentado'],
			['Seu Pet está agitado?','agitado'],
			['O seu Pet fez atividade física?','se_movimenta'],
			['O seu Pet possui itens para brincar?','brinquedos'],
			['O seu Pet está se isolando socialmente?','isolado'],
			['O seu Pet está hiperventilando?','hiperventilacao'],
			['O seu Pet está latindo constantemente?','latindo'],
			['O pelo do seu Pet está brilhante (bonito)?','pelo_brilhante'],
			['O ambiente é adequado?','ambiente_adequado'],
			['O seu Pet é castrado?','castrado'],
			['O seu Pet possui odor muito forte?','odor_forte'],
			['O seu Pet está se lambendo constantemente?','lambendo'],
		]

	def texto(self):
		string = self.level[0]
		del self.level[0]
		return string
