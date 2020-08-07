class BossConfiguration:
    def __init__(self, name):
        self.name = name
        self.wing = None
        self.dps = 0
        self.condidps = 0
        self.bs = 0
        self.tank = 0
        self.druid = 0
        self.hfb = 0
        self.alacrane = 0
        self.separator = " | "

    def add_configuration(self, dps = 0 , condidps = 0, bs = 0, tank = 0, druid = 0, hfb = 0, alacrane = 0):
        self.dps = dps
        self.condidps = condidps
        self.bs = bs
        self.tank = tank
        self.druid = druid
        self.hfb = hfb
        self.alacrane = alacrane

    def subtract_roles(self, dps = 0 , condidps = 0, bs = 0, tank = 0, druid = 0, hfb = 0, alacrane = 0):
        self.dps -= dps
        self.condidps -= condidps
        self.bs -= bs
        self.tank -= tank
        self.druid -= druid
        self.hfb -= hfb
        self.alacrane -= alacrane

    def create_list(self, kp):
        string = ""

        if self.wing is not None:       string += self.wing + self.separator
        else:                           string += self.name + self.separator

        string += kp + self.separator

        if self.dps > 0:               string += str(self.dps) + "xdps "
        if self.condidps > 0:          string += str(self.condidps) + "xcondidps "
        if self.bs > 0:                string += str(self.bs) + "xbs "
        if self.tank > 0:              string += str(self.tank) + "xtank "
        if self.druid > 0:             string += str(self.druid) + "xdruid "
        if self.hfb > 0:               string += str(self.hfb) + "xhfb "
        if self.alacrane > 0:          string += str(self.alacrane) + "xalacrane "
        return string


# fractal = BossConfiguration("CMs + T4")
# fractal.add_configuration(dps=2, bs=1, hfb=1, alacrane=1)
# fractal.subtract_roles(dps=1, alacrane=1)
# print(fractal.create_list("251kp"))