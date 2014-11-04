from itertools import takewhile
import unittest
def infix_to_postfix(infix_str, priorities):
	post_str = ''
	op_stack = ['st']
	for infix_char in infix_str:
		if infix_char.isdigit():
			post_str += infix_char
		elif infix_char in priorities.keys():
			if priorities[infix_char] <= priorities[op_stack[-1]]:
				op_lst = infix_to_postfix_helper(infix_char, op_stack, priorities)
				post_str += ''.join(op_lst)
				op_stack = op_stack[:-len(op_lst)]
				op_stack.append(infix_char)
			else: 
				op_stack.append(infix_char)
		else:
			pass
	post_str += ''.join(reversed(op_stack))
	return post_str[:-2]

def infix_to_postfix_helper(symbol, op_stack, priorities):
	return list(takewhile(lambda x: priorities[x] >= priorities[symbol], reversed(op_stack)))

class InfixToPostfix(unittest.TestCase):
	
	def setUp(self):
		self.priorities = {
			'*': 2,
			'/': 2,
			'+': 1,
			'-': 1,
			'st': 0
		}
	
	def tearDown(self):
		pass
	
	def test_infix_to_postfix_helper(self):
		self.assertEqual(infix_to_postfix_helper('/', ['/', '+'], self.priorities), [])
		self.assertEqual(infix_to_postfix_helper('+', ['+', '/'], self.priorities), ['/', '+'])
		self.assertEqual(infix_to_postfix_helper('+', ['+', '/', '+'], 
			self.priorities), ['/', '+'], 'but this case will not appear in ths case')

	def test_infix_to_postfix(self):
		self.assertEqual(infix_to_postfix('1+2+3+4', self.priorities), '12+3+4+')
		self.assertEqual(infix_to_postfix('1+2*3-3', self.priorities), '123*+3-')
		self.assertEqual(infix_to_postfix('1+2-3+4', self.priorities), '12+3-4+')
		self.assertEqual(infix_to_postfix('1*2+3*4', self.priorities), '12*34*+')

if __name__ == '__main__':
	unittest.main()