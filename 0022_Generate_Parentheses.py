def generateParenthesis4(n):
    def generate(p, left, right, parens=[]):
        '''
        Значение аргумента по умолчанию выполняется во время определения, а не во время выполнения.
        parents не нужно передавать в качества аргумента в рекурсивных вызовых, как я делаю ниже
        '''
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,  # parens.append(p). Данный трюк делает из p кортеж
        return parens
    return generate('', n, n)


def balanced_parens(n, st="", op=0, cl=0, res=None):
    ''' Идиотский костыль для передачи иззменяемого list в рекурсивую функцию для inplace модернизации. '''
    if res is None: res = []
    '''Как и выше, первым мы обязательно помещаем открывающую скобку, так как все правильные скобочные последовательности n >= 1 начинаются с неё.'''
    if op < n: balanced_parens(n, st+"(", op+1, cl, res) # Если число открывающих меньше n. Условие с n, чтобы оно смогло выполниться при начальном состоянии op=0, cl=0
    if cl < op: balanced_parens(n, st+")", op, cl+1, res) # Добиваем закрывающими
    if op == cl == n: res.append(st)
    return res


def balanced_parens_stack(n):
    """
    Вариант без рекурсии (с самописным stack) для понимания принципа работы алгоритма.
    """
    res = []
    stack = [('', 0, 0)]
    while stack:
        temp, op, cl = stack.pop()
        if op < n: stack.append((temp+'(', op+1, cl))
        if cl < op: stack.append((temp + ')', op, cl+1))
        if op == cl == n: res.append(temp)
    return res


class MagicSoluthions:
    """
    Это ещё предстоит переварить... :)
    """
    @staticmethod
    def generateParenthesis(n, open=0):
        """
        Если в последнем ретёрне поставить 0 вместо (not n) ничего не будет в выходном списке. Если 1, список с некоторыми лишними значениями
        Для n = 3 и замен (not n) на 0:
        Ожидаемое - ['((()))', '(()())', '(())()', '()(())', '()()()']
        Получается ['((()))', '(()())', '(())()', '(()))', '()(())', '()()()', '()())', '())', ')']
        Таким образом, при n = 0 
        """
        if n > 0 <= open:
            return ['(' + p for p in MagicSoluthions.generateParenthesis(n - 1, open + 1)] + [')' + p for p in MagicSoluthions.generateParenthesis(n, open - 1)]
        return [')' * open] * (not n)

    @staticmethod
    def generateParenthesis2(n):
        def generate(p, left, right):
            if right >= left >= 0:
                if not right: yield p
                yield from generate(p + '(', left-1, right)
                yield from generate(p + ')', left, right-1)
        return list(generate('', n, n))


print(MagicSoluthions.generateParenthesis2(3))
