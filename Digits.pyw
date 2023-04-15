#! /usr/bin/python
# -*- coding: utf-8 -*-
# Digits.pyw, version 1.0, for python 3
import sys, tkinter
import itertools

def solve_digits( target, numbers):
   for i in range( 2, 7):
      for subset in itertools.permutations( numbers, i):
         for ops in itertools.product( "+-*/", repeat=i-1):
            temp = list( subset)
            result = temp.pop( 0)
            for j, op in enumerate( ops):
               b = temp[j]
               if op == "+":
                  result += b
               elif op == "-":
                  result -= b
                  if result < 1:
                     break
               elif op == "*":
                  result *= b
               elif op == "/":
                  if b == 0 or result % b != 0:
                     result = 0
                     break
                  result //= b
            if result == target:
               solution = ''
               index = 0
               for number in subset:
                  if solution != '':
                     solution += ' '+ops[ index]+' '
                     index += 1
                  solution += str( number)
               solution += ' = '+str( result)
               return( solution)

class SolverDialog( tkinter.Frame):
   def __init__( self, root):
      tkinter.Frame.__init__( self, root, border=5)

      sticky = tkinter.constants.W + tkinter.constants.E

      self.status = tkinter.Label( self, text='Enter the numbers separated by spaces, Target Numbers1-6, e.g. 484 7 9 11 19 20 23')
      self.status.pack( fill=tkinter.constants.X, expand=1)

      body = tkinter.Frame( self)
      body.pack( fill=tkinter.constants.X, expand=1)
      body.grid_columnconfigure( 1, weight=2)

      tkinter.Label( body, text='Numbers: ').grid( row=1)
      self.numbers = tkinter.Entry( body, width=30)
      self.numbers.grid( row=1, column=1, sticky=sticky, pady=2)
      self.numbers.focus_set()

      tkinter.Label( body, text='Solution: ').grid( row=2)
      self.solution = tkinter.Entry( body, width=30)
      self.solution.grid( row=2, column=1, sticky=sticky, pady=3)

      buttons = tkinter.Frame( self)
      buttons.pack()

      buttonClear = tkinter.Button( buttons, text="Clear", width=10, command=self.clear)
      buttonClear.pack( side=tkinter.constants.LEFT)
      tkinter.Frame( buttons, width=30).pack( side=tkinter.constants.LEFT)

      buttonSolve = tkinter.Button( buttons, text="Solve", width=10, command=self.solve)
      buttonSolve.pack( side=tkinter.constants.LEFT)
      tkinter.Frame( buttons, width=30).pack( side=tkinter.constants.LEFT)

      buttonQuit = tkinter.Button( buttons, text="Quit",   width=10, command=self.quit)
      buttonQuit.pack( side=tkinter.constants.LEFT )
      tkinter.Frame( buttons, width=30).pack( side=tkinter.constants.LEFT)

      return

   def clear( self):
      numbers = ''
      self.numbers.delete( 0, tkinter.constants.END)
      self.numbers.insert( 0, numbers)
      self.numbers.focus_set()

      solution = ''
      self.solution.delete( 0, tkinter.constants.END)
      self.solution.insert( 0, solution)

      return

   def solve( self):
      numbers = self.numbers.get()
      numbers = numbers.strip()
      temp = numbers

      target = 0
      numbers = []

      count = 0
      solution = ''
      while temp != '':
         space = temp.find(' ')
         if space != -1:
            number = temp[:space]
            temp = temp[space+1:]
         if space == -1:
            number = temp
            temp = ''
         value = int( number)
         if count == 0:
            target = value
         if count != 0:
            numbers.append( value)
         count += 1

      solution = solve_digits( target, numbers)

      self.solution.delete( 0, tkinter.constants.END)
      self.solution.insert( 0, solution)
      self.solution.focus_set()

      return

def gui_main():
   root = tkinter.Tk()
   root.title( 'NYT Digits Solver')
   root.resizable( True, False)
   root.minsize( 600, 0)
   root.geometry('+50+200')
   SolverDialog( root).pack( fill=tkinter.constants.X, expand=1)
   root.mainloop()
   return 0

if __name__ == '__main__':
   sys.exit( gui_main())

