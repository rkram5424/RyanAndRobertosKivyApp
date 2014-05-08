#!/usr/bin/env python2
# -*- coding: utf-8 -*-

# RYAN'S NOTES
# Maybe we could have a threshold of tens in 
# terms of how many jumbled letters to show.
# < 10, show 10 letters.
# 10 < x <= 20 show 20 letters.
# 10 to a row so it's not scrunched.
# Maybe make 20 characters the limit.
# Spaces allowable, not tiles though. Spaces
# appear as gaps in fillable slots.

# imports
import random as r
import sys

class Jumblaya:

	jb = ['','','']

	def __init__(self, bowl):
		hint, word = self.random_line(bowl).split('|')
		word = word.lower()
		self.jb = [hint, word, self.jumble_letters(word)]
		self.return_data()

	def return_data(self):
		return self.jb
		
	def jumble_letters(self, word): # takes in word and spits out a jumbled mess.
		word = word.replace(' ', '')
		jumble_num = 0
		new_num = 0
		jumble_arr = []
		if self.count_letters(word) > 1 & self.count_letters(word) < 10:
			jumble_num = 10
		elif self.count_letters(word) > 10 & self.count_letters(word) <= 20:
			jumble_num = 20
		new_num = jumble_num - self.count_letters(word)
		for i in range(new_num):
			word = word + self.random_letter()
		jumble_arr = list(word)
		r.shuffle(jumble_arr)
		return jumble_arr
		
	def count_letters(self, answer):
		non_letters = 0
		answer = answer.lower()
		letters = 'abcdefghijklmnopqrstuvwxyz'
		for i in range(len(answer)):
			if not answer[i] in letters:
				non_letters += 1
		return len(answer) - non_letters
		
	def random_letter(self):
		letters = 'abcdefghijklmnopqrstuvwxyz'
		return r.choice(letters)
		
	def random_line(self, afile):
		return r.choice(list(open(afile + '.txt')))

if __name__ == '__main__':
	Jumblaya()

