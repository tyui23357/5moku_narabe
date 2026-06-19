import pyxel

pyxel.init(240, 160)
pyxel.mouse(True)

position = [[] for _ in range(5)]
moves = [0]

class select:
    def __init__(self):
        self.player = moves[0] % 2

    def lines(self):
        for i in range(60, 181, 30):
            pyxel.line(i, 50, i, 150, 7)
        pyxel.line(30, 150, 210, 150, 7)
    
    def which(self):
        pyxel.text(10, 10, f"PLAYER{self.player + 1}", 7)
        pyxel.text(200, 10, "RESTART", 7)
    
    def choice(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            for j in range(5):
                if 45 + 30 * j <= pyxel.mouse_x < 45 + 30 * (j + 1):
                    if len(position[j]) < 5:
                        position[j].append(self.player)
                        if self.player:
                            pyxel.circ(60 + 30 * j, 150 - len(position[j]) * 20 + 10, 10, 7)
                        else:
                            pyxel.circb(60 + 30 * j, 150 - len(position[j]) * 20 + 10, 10, 7)
                        moves[0] += 1

    def restart(self):
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            if 200 <= pyxel.mouse_x and 20 >= pyxel.mouse_y:
                for v in range(5):
                    position[v].clear()
                moves[0] = abs(self.player - 1)
                        
    def ever(self):
        for k in range(5):
            for l in range(5):
                if len(position[k]) <= l:
                    break
                col = 7 if position[k][l] else 0
                if col:
                    pyxel.circ(60 + 30 * k, 150 - (l + 1) * 20 + 10, 10, 7)
                else:
                    pyxel.circb(60 + 30 * k, 150 - (l + 1) * 20 + 10, 10, 7)

class clear:
    def __init__(self):
        self.hight = min(len(position[0]), len(position[1]), len(position[2]), len(position[3]), len(position[4]))
        self.d = 0

    def judg(self):
        for h in range(self.hight):
            if position[0][h] == position[1][h] == position[2][h] == position[3][h] == position[4][h]:
                self.d = position[0][h] + 1
                pyxel.line(50, 150 - (h + 1) * 20 + 10, 190, 150 - (h + 1) * 20 + 10, 8)
                break

        for w in range(5):
            if len(position[w]) >= 5:
                if position[w][0] == position[w][1] == position[w][2] == position[w][3] == position[w][4]:
                    self.d = position[w][0] + 1
                    pyxel.line(60 + w * 30, 50, 60 + w * 30, 150, 8)
                    break

        if len(position[0]) >= 5 and len(position[1]) >= 4 and len(position[2]) >= 3 and len(position[3]) >= 2 and len(position[4]) >= 1:
            if position[0][4] == position[1][3] == position[2][2] == position[3][1] == position[4][0]:
                pyxel.line(190, 150, 50, 50, 8)
                self.d = position[0][4] + 1

        if len(position[4-0]) >= 5 and len(position[4-1]) >= 4 and len(position[4-2]) >= 3 and len(position[4-3]) >= 2 and len(position[4-4]) >= 1:
            if position[4-0][4] == position[4-1][3] == position[4-2][2] == position[4-3][1] == position[4-4][0]:
                pyxel.line(190, 50, 50, 150, 8)
                self.d = position[4-0][4] + 1
        
        if self.d:
            moves[0] = abs(moves[0] % 2 - 2)



def update():
    pyxel.cls(0)
    if moves[0] >= 0:
        select().choice()

def draw():
    select().lines()
    select().ever()
    select().which()
    clear().judg()
    select().restart()


pyxel.run(update, draw)