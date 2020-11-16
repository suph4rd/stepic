class multifilter:
    def judge_half(pos, neg):
        # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
        return True if pos >= neg else False

    def judge_any(pos:int, neg):
        # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
        return True if pos >= 1 else False

    def judge_all(pos, neg):
        # допускает элемент, если его допускают все функции (neg == 0)
        return True if neg == 0 else  False

    def __init__(self, iterable, *funcs, judge=judge_any):
        """
        :param iterable: - исходная последовательность
        :param  funcs: - допускающие функции
        :param  judge: - решающая функция
        """
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge

    def __iter__(self):
        # возвращает итератор по результирующей последовательности
        for elem in self.iterable:
            pos, neg = 0, 0
            for func in self.funcs:
                if func(elem) == True:
                    pos += 1
                else:
                    neg += 1
            if self.judge(pos, neg) == True:
                yield elem