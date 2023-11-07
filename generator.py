from Logics import logics

class Generator:
    """
        # Color Pallate Generator

        ### This is an Smart Color Pallate Generator for web developers and designer.
        generate full color pallate scheme by asking only one Main Color in `Hex Code` 
  
    """
    def __init__(self,hex) -> None:
        self.hex = hex
        logic = logics()
        self.rgb = logic.hextorgb(self.hex)
        self.hsv = logic.rgbtohsv(self.rgb[0],self.rgb[1],self.rgb[2])
        # variable for calculating shades. s for saturation and v for value
        self.__s19 = 22
        self.__s37 = 12
        self.__s26 = 17
        self.__s48 = 7

        self.__v19 = 30
        self.__v37 = 15
        self.__v26 = 22
        self.__v48 = 10

        # Creating Colors Default Hue amount
        self.__red = 1
        self.__orange = 37
        self.__blue = 210
        self.__green = 125

        self.__SupportingColorDict = {"red":{},"blue":{},"green":{},"orange":{}}
        

    def mainColor(self) -> dict:
        mainColorDict = {"hex":self.hex,"rgb":self.rgb,"hsv":self.hsv}
        return mainColorDict

    def NeutralColor(self) -> dict:
        Neutralcolor = {"100": "[0,0,94]",
                        "200": "[0,0,84]",
                        "300": "[0,0,74]",
                        "400": "[0,0,64]",
                        "500": "[0,0,54]",
                        "600": "[0,0,44]",
                        "700": "[0,0,34]",
                        "800": "[0,0,24]",
                        "900": "[0,0,10]"}
        return Neutralcolor

    def SupportingColor(self) -> dict:
        # Calculating Color Shades Dict and variable
        SaturationDict = {}
        ValueDict = {}
        # Saturation
        SaturationDict["100"] = self.hsv[1] - self.__s19
        SaturationDict["200"] = self.hsv[1] - self.__s26
        SaturationDict["300"] = self.hsv[1] - self.__s37
        SaturationDict["400"] = self.hsv[1] - self.__s48
        SaturationDict["500"] = self.hsv[1]
        SaturationDict["600"] = self.hsv[1] + self.__s26
        SaturationDict["700"] = self.hsv[1] + self.__s37
        SaturationDict["800"] = self.hsv[1] + self.__s48
        SaturationDict["900"] = self.hsv[1] + self.__s19

        # Value
        ValueDict["100"] = self.hsv[2] + self.__v19
        ValueDict["200"] = self.hsv[2] + self.__v26
        ValueDict["300"] = self.hsv[2] + self.__v37
        ValueDict["400"] = self.hsv[2] + self.__v48
        ValueDict["500"] = self.hsv[2]
        ValueDict["600"] = self.hsv[2] - self.__s26
        ValueDict["700"] = self.hsv[2] - self.__s37
        ValueDict["800"] = self.hsv[2] - self.__s48
        ValueDict["900"] = self.hsv[2] - self.__s19

        # applying Condition

        for k in SaturationDict.keys():
            if SaturationDict[k] < 10:
                SaturationDict[k] = 10
            elif SaturationDict[k] > 100:
                SaturationDict[k] = 100

        for k in ValueDict.keys():
            if ValueDict[k] < 15:
                ValueDict[k] = 15
            elif ValueDict[k] > 100:
                ValueDict[k] = 100
            
        # Generating Result 
        for cname in ["red","orange","green","blue"]:
            for k in ValueDict.keys():
                if cname == "red":
                    self.__SupportingColorDict[cname][k] = f"{self.__red,SaturationDict[k],ValueDict[k]}"
                elif cname == "orange":
                    self.__SupportingColorDict[cname][k] = f"{self.__orange,SaturationDict[k],ValueDict[k]}"
                elif cname == "green":
                    self.__SupportingColorDict[cname][k] = f"{self.__green,SaturationDict[k],ValueDict[k]}"
                else:
                    self.__SupportingColorDict[cname][k] = f"{self.__blue,SaturationDict[k],ValueDict[k]}"

        return self.__SupportingColorDict


