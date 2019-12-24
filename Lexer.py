import string

from Token import Token
from SusekaException import *

DATA_TYPES  = ['int', 'bool', 'char']
BOOL_VALUES = ['true', 'false']
OPERATORS   = ["+", "-", "/", "*"]

BINARY_OPERATORS     = ["&&", "||"]
COMPARISON_OPERATORS = [">", "<", "=="]

ASCII_LETTERS = list(string.ascii_letters)

class Lexer:
	def __init__(self, program):
		self.program = program
		self.tokens = []


	def run(self):
		print("Start lexer")

		self.split_tokens()
		self.tokens_analysis()


	def split_tokens(self):
		line = 1
		position = 0
		content = ''

		for elem in self.program:
			if elem == ' ' or elem == '\n':
				content = content.strip()
				if content != '':
					t = Token(position, line, content)
					content = ''
					self.tokens.append(t)

			if elem == '\n':
				line += 1
				position = 0

				t = Token(position, line, '<endln>')
				self.tokens.append(t)

			position += 1
			content += elem


	def tokens_analysis(self):
		for token in self.tokens:
			c = token.content
			if   c == 'if':
				token.type = 'IF'
			elif c == 'else':
				token.type = 'else'
			elif c == 'while':
				token.type = 'WHILE'
			elif c == 'print':
				token.type = 'PRINT'
			elif c == '=':
				token.type = 'EQ'
			elif c == 'do':
				token.type = 'DO'
			elif c == '{':
				token.type = 'BEGIN'
			elif c == '}':
				token.type = 'END'
			elif c == '<endln>':
				token.type = 'ENDLN'
			elif c in DATA_TYPES:
				token.type = 'DATA_TYPE'
			elif c in BOOL_VALUES:
				token.type = 'BOOL_VALUE'
			elif c in OPERATORS:
				token.type = 'OPERATOR'
			elif c in BINARY_OPERATORS:
				token.type = 'B_OPERATOR'
			elif c in COMPARISON_OPERATORS:
				token.type = 'C_OPERATOR'
			elif c.startswith('@@'):
				token.type = 'COMMENT'
			elif c[0] in ASCII_LETTERS:
				token.type = 'VARIABLE'
			else:
				try:
					c = int(c)
					token.type = 'INTEGER_VALUE'
				except ValueError:
					mes = "Unexpected token '{}' at line {} position {}".format(
							c, token.line, token.position)
					raise LexerError(mes)

			print(token.content, token.type)