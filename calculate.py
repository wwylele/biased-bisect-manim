
from typing import NamedTuple, List


MAX_N = 100

def eta(s, t, x):
    l = s + t + 2
    n = [1] * l
    for i in range(s + t + 1, x + 1):
        n[i % l] = n[(i-s) % l] + n[(i-t) % l]
    return n[x % l]

def node(s, t):
    return eta(s, t, s*t+s+t)+1


class ST(NamedTuple):
    s: int
    t: int

    def get_x(self):
        return (self.s - self.t) / (self.s + self.t)


def generateTicks(left, right, maxN):
    middle = ST(left.s + right.s, left.t + right.t)
    middleNode = node(middle.s, middle.t)
    if middleNode > maxN:
        return [left, middle]
    else:
        return generateTicks(left, middle, maxN) + generateTicks(middle, right, maxN)


class Eseries(NamedTuple):
    st: ST
    e: List[int]
    wmin: List[int]
    wmax: List[int]
    wtil: List[float]
    necks: List[int]

    def get_x(self):
        return self.st.get_x()


def calcD(eseries, n, w):
    return eseries.e[w] + eseries.e[n-w] + w*eseries.st.t + (n-w) * eseries.st.s


def calcE(st, maxN):
    # print(st)
    e = [0] * (maxN + 1)
    wmin = [0] * (maxN + 1)
    wmax = [0] * (maxN + 1)
    wtil = [0] * (maxN + 1)
    wmin[2] = wmax[2] = wtil[2] = 1
    e[2] = st.s + st.t
    necks = [2]
    eseries = Eseries(st, e, wmin, wmax, wtil, necks)
    for n in range(3, maxN+1):
        prevMin = eseries.wmin[n-1]
        prevMax = eseries.wmax[n-1]
        d1 = calcD(eseries, n, prevMin)
        d2 = calcD(eseries, n, prevMin+1)
        d3 = calcD(eseries, n, prevMax)
        d4 = calcD(eseries, n, prevMax+1)
        if d1 <= d2:
            wmin = prevMin
        else:
            wmin = prevMin+1

        if d4 <= d3:
            wmax = prevMax+1
        else:
            wmax = prevMax
        e1 = min(d1, d2)
        e2 = min(d3, d4)
        if e1 != e2:
            raise Exception("what")
        eseries.wmin[n] = wmin
        eseries.wmax[n] = wmax
        eseries.e[n] = e1
        if wmin == wmax:
            necks.append(n)

    for i in range(len(necks) - 1):
        left = necks[i]
        right = necks[i + 1]
        for n in range(left + 1, right + 1):
            s = (n - left) / (right - left)
            eseries.wtil[n] = eseries.wmin[left] * \
                (1 - s) + eseries.wmin[right] * s
    return eseries

def g_generate(max_n):
    global MAX_N
    print("Generating")

    MAX_N = max_n

    ticks = generateTicks(ST(1, 1), ST(1, 0), MAX_N)
    # ticks will be alternating between node, non-node, node, non-node..., starting with 1/1, towards 1/0
    ticks.append(ST(1, 0))

    revticks = [ST(st.t, st.s) for st in ticks[1:]]
    revticks.reverse()
    ticks = revticks + ticks

    # Now ticks are between 0/1 and 1/0, inclusive
    return [calcE(st, MAX_N) for st in ticks]

def get_series_at(eserieses: list[Eseries], st: ST) -> Eseries:
    geq_i, geq_e = next(((i, e) for i, e in enumerate(eserieses) if e.st.s * st.t >= st.s * e.st.t))
    if geq_e.st == st:
        return geq_e

    if geq_i % 2 == 1:
        return geq_e
    return eserieses[geq_i-1]

