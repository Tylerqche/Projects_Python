
# HW3
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
class Node:
    def __init__(self, value):
        self.value = value  
        self.next = None 
    
    def __str__(self):
        return "Node({})".format(self.value) 
    __repr__ = __str__
                          
#=============================================== Part I ==============================================
class Stack:
    '''
        >>> x=Stack()
        >>> x.pop()
        >>> x.push(2)
        >>> x.push(4)
        >>> x.push(6)
        >>> x
        Top:Node(6)
        Stack:
        6
        4
        2
        >>> x.pop()
        6
        >>> x
        Top:Node(4)
        Stack:
        4
        2
        >>> len(x)
        2
        >>> x.peek()
        4
    '''
    def __init__(self):
        self.top = None
    
    def __str__(self):
        temp=self.top
        out=[]
        while temp:
            out.append(str(temp.value))
            temp=temp.next
        out='\n'.join(out)
        return ('Top:{}\nStack:\n{}'.format(self.top,out))
    __repr__=__str__

    def isEmpty(self):
        # YOUR CODE STARTS HERE
        return self.top == None
    
    def __len__(self): 
        # YOUR CODE STARTS HERE
        count = 0 # Count
        current = self.top
        while current != None:
            count += 1 # Iterates count up
            current = current.next # Iterates to next node
        return count

    def push(self,value):
        # YOUR CODE STARTS HERE
        new_node = Node(value)
        if self.isEmpty():
            self.top = new_node # Create top node
        else:
            new_node.next = self.top # Pushes top node to next
            self.top = new_node # Creates new top node
     
    def pop(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty(): # Check if empty
            return None
        else:
            popped = self.top.value # Stores popped value
            self.top = self.top.next # Creates new top node
        return popped

    def peek(self):
        # YOUR CODE STARTS HERE
        if self.isEmpty(): # Check if empty
            return None
        else:
            return self.top.value # Returns tope node value
#=============================================== Part II ==============================================
class Calculator:
    def __init__(self):
        self.__expr = None
    @property
    def getExpr(self):
        return self.__expr
    def setExpr(self, new_expr):
        if isinstance(new_expr, str):
            self.__expr=new_expr
        else:
            print('setExpr error: Invalid expression')
            return None
    def _isNumber(self, txt):
        '''
            >>> x=Calculator()
            >>> x._isNumber(' 2.560 ')
            True
            >>> x._isNumber('7 56')
            False
            >>> x._isNumber('2.56p')
            False
        '''
        # YOUR CODE STARTS HERE
        try: # Try/Except block
            float(txt)
        except:
            return False
        return True
    def _getPostfix(self, txt):
        '''
            Required: _getPostfix must create and use a Stack object for expression
processing
            >>> x=Calculator()
            >>> x._getPostfix('2 ^ 4')
            '2.0 4.0 ^'
            >>> x._getPostfix('2')
            '2.0'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4.45')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.45 +'
            >>> x._getPostfix('2 * 5.34 + 3 ^ 2 + 1 + 4')
            '2.0 5.34 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('2.1 * 5 + 3 ^ 2 + 1 + 4')
            '2.1 5.0 * 3.0 2.0 ^ + 1.0 + 4.0 +'
            >>> x._getPostfix('( 2.5 )')
            '2.5'
            >>> x._getPostfix('( 2 { 5.0 } )')
            '2.0 5.0 *'
            >>> x._getPostfix(' 5 ( 2 + { 5 + 3.5 } )')
            '5.0 2.0 5.0 3.5 + + *'
            >>> x._getPostfix ('( { 2 } )')
            '2.0'
            >>> x._getPostfix ('2 * ( [ 5 + -3 ] ^ 2 + { 1 + 4 } )')
            '2.0 5.0 -3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('[ 2 * ( < 5 + 3 > ^ 2 + ( 1 + 4 ) ) ]')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix ('( { 2 * { { 5 + 3 } ^ 2 + ( 1 + 4 ) } } )')
            '2.0 5.0 3.0 + 2.0 ^ 1.0 4.0 + + *'
            >>> x._getPostfix('2 * < -5 + 3 > ^ 2 + < 1 + 4 >')
            '2.0 -5.0 3.0 + 2.0 ^ * 1.0 4.0 + +'
            >>> x._getPostfix('2 * 5 + 3 ^ + -2 + 1 + 4')
            >>> x._getPostfix('2 * 5 + 3 ^ - 2 + 1 + 4')
            >>> x._getPostfix('2    5')
            >>> x._getPostfix('25 +')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ( 1 + 4 ]')
            >>> x._getPostfix(' ( 2 * { 5 + 3 ) ^ 2 + ( 1 + 4 ] }')
            >>> x._getPostfix(' 2 * ( 5 + 3 ) ^ 2 + ) 1 + 4 (')
            >>> x._getPostfix('2 * 5% + 3 ^ + -2 + 1 + 4')
        '''
        # YOUR CODE STARTS HERE
        postfixStack = Stack()  # method must use postfixStack to compute the postfix expression
        postfix = [] # Post fix
        operator = {'+':1, '-':1, '*':2, '/':2, '^':3} # Operators and priority
        paren = {"(":")", "[":"]", "{":"}", "<":">"} # Paren left and right
        txt_list = txt.split(" ") # Splits text
        txt_list = [ch for ch in txt_list if ch != '']

        
        #Iterate through text list
        for i in range(len(txt_list)):
            # Check for invalid input: Double Operator
            if i != len(txt_list)-1 and txt_list[i] in operator and txt_list[i+1] in operator:
                return None
            # Check for invalid input: Double Number
            elif i != len(txt_list)-1 and self._isNumber(txt_list[i]) and self._isNumber(txt_list[i+1]):
                return None
            # Checks if using paren to mulitply
            elif i != len(txt_list)-1 and self._isNumber(txt_list[i]) and txt_list[i+1] in paren:
                postfixStack.push("*")
                postfix += [str(float(txt_list[i]))]
            # Checks for left part of paren "("
            elif txt_list[i] in paren:
                postfixStack.push(txt_list[i])
            # Checks for right part of paren ")"
            elif txt_list[i] in paren.values():
                    temp=postfixStack.top
                    out=[]
                    while temp:
                        out.append(str(temp.value))
                        temp=temp.next
                    if list(paren.keys())[list(paren.values()).index(txt_list[i])] in out:
                    # Pops until find right part of paren
                        while postfixStack.peek() != list(paren.keys())[list(paren.values()).index(txt_list[i])]: 
                            postfix += [postfixStack.pop()]
                        postfixStack.pop()
                    else:
                        return None
                    # Checks for double paren
                    if i != len(txt_list)-1 and txt_list[i] in paren.values() and txt_list[i+1] in paren:
                        postfixStack.push("*")
            # Check if txt_list[i] is an operator
            elif txt_list[i] in operator:
                # Checks for double ^
                if txt_list[i] == "^" and txt_list[i-2] == "^":
                    postfixStack.push(txt_list[i])                    
                elif postfixStack.isEmpty():
                    postfixStack.push(txt_list[i])
                # Check if not empty
                elif not postfixStack.isEmpty():
                    # Pops top value and adds to postfix until higher pirority
                    while not postfixStack.isEmpty() and postfixStack.top.value not in paren and operator[postfixStack.top.value] >= operator[txt_list[i]]:
                        postfix += [postfixStack.pop()]
                    postfixStack.push(txt_list[i])
            # Check is value is a num
            elif self._isNumber(txt_list[i]):
                postfix += [str(float(txt_list[i]))]
            else:
                return None
        # Add rest of stack to postfix
        while not postfixStack.isEmpty():
            postfix += [postfixStack.pop()]
        
        # Check for invalid input: Missing Paren
        for ch in postfix:
            if ch in paren:
                return None
        # Check for invalid input: Two Characters
        count = 0
        for ch in postfix:
            count += 1
        if count == 2:
            return None
        # Check for invalid input: Empty List
        if len(postfix) == 0:
            return None


        return " ".join(postfix)

    @property
    def calculate(self):
        '''
            >>> x=Calculator()
            >>> x.setExpr('4 + 3 - 2')
            >>> x.calculate
            5.0
            >>> x.setExpr('-2 + 3.5')
            >>> x.calculate
            1.5
            >>> x.setExpr('4 + 3.65 - 2 / 2')
            >>> x.calculate
            6.65
            >>> x.setExpr('23 / 12 - 223 + 5.25 * 4 * 3423')
            >>> x.calculate
            71661.91666666667
            >>> x.setExpr(' 2 - 3 * 4')
            >>> x.calculate
            -10.0
            >>> x.setExpr('7 ^ 2 ^ 3')
            >>> x.calculate
            5764801.0
            >>> x.setExpr(' 3 * ( [ ( 10 - 2 * 3 ) ] )')
            >>> x.calculate
            12.0
            >>> x.setExpr('8 / 4 * { 3 - 2.45 * [ 4 - 2 ^ 3 ] } + 3')
            >>> x.calculate
            28.6
            >>> x.setExpr('2 * [ 4 + 2 * < 5 - 3 ^ 2 > + 1 ] + 4')
            >>> x.calculate
            -2.0
            >>> x.setExpr(' 2.5 + 3 * ( 2 + { 3.0 } * ( 5 ^ 2 - 2 * 3 ^ ( 2 ) ) * <
4 > ) * [ 2 / 8 + 2 * ( 3 - 1 / 3 ) ] - 2 / 3 ^ 2')
            >>> x.calculate
            1442.7777777777778
            >>> x.setExpr('( 3.5 ) [ 15 ]') 
            >>> x.calculate
            52.5
            >>> x.setExpr('3 { 5 } - 15 + 85 [ 12 ]') 
            >>> x.calculate
            1020.0
            >>> x.setExpr("( -2 / 6 ) + ( 5 { ( 9.4 ) } )") 
            >>> x.calculate
            46.666666666666664
            >>> x.setExpr(" 4 + + 3 + 2") 
            >>> x.calculate
            >>> x.setExpr("4  3 + 2")
            >>> x.calculate
            >>> x.setExpr('( ( 2 ) * 10 - 3 * [ 2 - 3 * 2 ) ]')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * ( 2 - 3 * 2 ) )')
            >>> x.calculate
            >>> x.setExpr('( 2 ) * 10 - 3 * / ( 2 - 3 * 2 )')
            >>> x.calculate
            >>> x.setExpr(' ) 2 ( * 10 - 3 * ( 2 - 3 * 2 ) ')
            >>> x.calculate
        '''
        if not isinstance(self.__expr,str) or len(self.__expr)<=0:
            print("Argument error in calculate")
            return None
        calcStack = Stack()   # method must use calcStack to compute the  expression
        # YOUR CODE STARTS HERE
        try:
            calc_list = self._getPostfix(self.getExpr).split(" ")
        except:
            return None

        operator = ['+', '-', '*', '/', '^']
        
        for ch in calc_list:
            if self._isNumber(ch): # If number push to stack
                calcStack.push(ch)
            elif ch in operator:
                if ch == "+": # Pop 2 push value
                    x = float(calcStack.pop())
                    y = float(calcStack.pop())
                    value = y + x
                    calcStack.push(value)
                if ch == "-": # Pop 2 push value
                    x = float(calcStack.pop())
                    y = float(calcStack.pop())
                    value = y - x 
                    calcStack.push(value)
                if ch == "/": # Pop 2 push value
                    x = float(calcStack.pop())
                    y = float(calcStack.pop())
                    value = y / x 
                    calcStack.push(value)
                if ch == "*": # Pop 2 push value
                    x = float(calcStack.pop())
                    y = float(calcStack.pop())
                    value = y * x 
                    calcStack.push(value)
                if ch == "^": # Pop 2 push value
                    x = float(calcStack.pop())
                    y = float(calcStack.pop())
                    value = y ** x 
                    calcStack.push(value)
        return float(calcStack.pop())
            
#=============================================== Part III ==============================================
class AdvancedCalculator:
    '''
        >>> C = AdvancedCalculator()
        >>> C.states == {}
        True
        >>> C.setExpression('a = 5;b = 7 + a;a = 7;c = a + b;c = a * 0;return c')
        >>> C.calculateExpressions() == {'a = 5': {'a': 5.0}, 'b = 7 + a': {'a': 
5.0, 'b': 12.0}, 'a = 7': {'a': 7.0, 'b': 12.0}, 'c = a + b': {'a': 7.0, 'b': 12.0,
'c': 19.0}, 'c = a * 0': {'a': 7.0, 'b': 12.0, 'c': 0.0}, '_return_': 0.0}
        True
        >>> C.states == {'a': 7.0, 'b': 12.0, 'c': 0.0}
        True
        >>> C.setExpression('x1 = 5;x2 = 7 [ x1 - 1 ];x1 = x2 - x1;return x2 + x1 ^
3')
        >>> C.states == {}
        True
        >>> C.calculateExpressions() == {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 
1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 = x2 - x1': {'x1': 23.0, 'x2': 28.0}, 
'_return_': 12195.0}
        True
        >>> print(C.calculateExpressions())
        {'x1 = 5': {'x1': 5.0}, 'x2 = 7 [ x1 - 1 ]': {'x1': 5.0, 'x2': 28.0}, 'x1 =
x2 - x1': {'x1': 23.0, 'x2': 28.0}, '_return_': 12195.0}
        >>> C.states == {'x1': 23.0, 'x2': 28.0}
        True
        >>> C.setExpression('x1 = 5 * 5 + 97;x2 = 7 * { x1 / 2 };x1 = x2 * 7 / 
x1;return x1 ( x2 - 5 )')
        >>> C.calculateExpressions() == {'x1 = 5 * 5 + 97': {'x1': 122.0}, 'x2 = 7 
* { x1 / 2 }': {'x1': 122.0, 'x2': 427.0}, 'x1 = x2 * 7 / x1': {'x1': 24.5, 'x2': 
427.0}, '_return_': 10339.0}
        True
        >>> C.states == {'x1': 24.5, 'x2': 427.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;C = A + B;A = 20;D = A + B + C;return 
D - A')
        >>> C.calculateExpressions() == {'A = 1': {'A': 1.0}, 'B = A + 9': {'A': 
1.0, 'B': 10.0}, 'C = A + B': {'A': 1.0, 'B': 10.0, 'C': 11.0}, 'A = 20': {'A': 
20.0, 'B': 10.0, 'C': 11.0}, 'D = A + B + C': {'A': 20.0, 'B': 10.0, 'C': 11.0, 
'D': 41.0}, '_return_': 21.0}
        True
        >>> C.states == {'A': 20.0, 'B': 10.0, 'C': 11.0, 'D': 41.0}
        True
        >>> C.setExpression('A = 1;B = A + 9;2C = A + B;A = 20;D = A + B + C;return
D + A')
        >>> C.calculateExpressions() is None
        True
        >>> C.states == {}
        True
    '''
    def __init__(self):
        self.expressions = ''
        self.states = {}
    def setExpression(self, expression):
        self.expressions = expression
        self.states = {}
    def _isVariable(self, word):
        '''
            >>> C = AdvancedCalculator()
            >>> C._isVariable('volume')
            True
            >>> C._isVariable('4volume')
            False
            >>> C._isVariable('volume2')
            True
            >>> C._isVariable('vol%2')
            False
        '''
        # YOUR CODE STARTS HERE
        if word == "": # Check if word is blank
            return False
        if len(word) == 1 and word.isalpha(): # Check is 1 letter variable
            return True
        if word[0].isalpha(): # Check if first ch is alpha
            for i in range(len(word)): # Check if rest are alnumeric
                if not word[i].isalnum():
                    return False
        else:
            return False
        return True

    def _replaceVariables(self, expr):
        '''
            >>> C = AdvancedCalculator()
            >>> C.states = {'x1': 23.0, 'x2': 28.0}
            >>> C._replaceVariables('1')
            '1'
            >>> C._replaceVariables('105 + x')
            >>> C._replaceVariables('7 ( x1 - 1 )')
            '7 ( 23.0 - 1 )'
            >>> C._replaceVariables('x2 - x1')
            '28.0 - 23.0'
        '''
        # YOUR CODE STARTS HERE
        operators = ['+', '-', '*', '/', '^', "(", ")", "[", "]", "{", "}", "<", ">"]
        expr_list = expr.split(" ")
        for i in range(len(expr_list)): 
            if self._isVariable(expr_list[i]): # Checks for all True variables
                if expr_list[i] in self.states:
                    expr_list[i] = str(self.states[expr_list[i]]) # Replaces variable
                else:
                    return None
            elif not expr_list[i].isdigit() and expr_list[i] not in operators: # Checks if word is a digit or operator
                return None
        return " ".join(expr_list) # Joins expression
    
    def calculateExpressions(self):
        self.states = {} 
        calcObj = Calculator()     # method must use calcObj to compute each expression
        # YOUR CODE STARTS HERE
        pass
        calc_expr = {}

        expr_list = self.expressions.split(";") # Splits 
        for expr in expr_list:
            expr = expr.strip() # Strips white space
            ch_list = expr.split(" ") # SPlits
            if self._isVariable(ch_list[0]) and "=" in expr: # Checks if expression
                key = ch_list[0] # Sets first ch to variable
                func = self._replaceVariables(" ".join(ch_list[2:])) # Sets rest to function and replaces variables
                calcObj.setExpr(func) # Calculate function
                self.states[key] = calcObj.calculate # Inputs to states dict
                d = self.states.copy() # Creates copy of states
                calc_expr[expr] = d # Inputs to calc_expr dict
            elif not self._isVariable(ch_list[0]) and "=" in expr: # Check if expression has valid variable
                self.states = {} # Sets states to empty
                return None
            elif ch_list[0] == 'return':
                func = self._replaceVariables(" ".join(ch_list[1:])) # Replaces and joins return equation
                calcObj.setExpr(func)
                calc_expr["_return_"] = calcObj.calculate # Adds to calc_expr
            
        return calc_expr

def run_tests():
    import doctest
    #- Run tests in all docstrings
    #doctest.testmod(verbose=True)
    
    #- Run tests per class - Uncomment the next line to run doctest by function. Replace Stack with the name of the function you want to test
    doctest.run_docstring_examples(AdvancedCalculator, globals(), name='HW3',verbose=True)   
if __name__ == "__main__":
    run_tests()
