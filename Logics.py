

class logics:

    def __init__(self) -> None:
        pass

    def __roundUp(self,val:float) -> int:
        """
        # Round Up
        To Round Up The Value to nearest Point
        """
        intVal = int(val)
        Valans = intVal+1

        if val + 0.5 >= Valans:
            return Valans
        elif val + 0.5 <= Valans:
            return intVal
        
    def __Max(self,r,g,b):
        if r > g and r > b:
            return r
        elif g > r and g > b:
            return g
        else:
            return b
        
  
    def __Min(self,r,g,b):
        if r < g and r < b:
            return r
        elif g < r and g < b:
            return g
        else:
            return b

    


    def rgbtohsv(self,r : str,g : str,b : str) -> list:
        """
        # RGB to HSV

        ### Approach :-

        1. Divide rgb by 255 so that no range change from 0..255 to 0..1
        2. Compute maxV,minV,diff
        3. Hue Calculation :
            - if maxV and minV are equal, then h=0
            - if maxV equal r then compute h = (60*((g-b)/diff) + 360) % 360
            - if maxV equal g then compute h = (60*((b-r)/diff) + 120) % 360
            - if maxV equal b then compute h = (60*((r-g)/diff) + 240) % 360
        4. Saturation Calculation :
            - if maxV = 0 then s = 0
            - if maxV does not equal 0 then compute s = (diff/maxV)* 100
        5. Value Calculation :
            - v = maxV*100
        """
    

        # step 1

        R = r/255.0
        G = g/255.0
        B = b/255.0

        # step 2

        maxV = self.__Max(R,G,B)
        minV = self.__Min(R,G,B)
        diff = (maxV - minV)

        # step 3 Hue Calculation

        if maxV == minV:
            h = 0
        elif maxV == R:
            h = (60*((G-B)/diff) + 360) % 360
        elif maxV == G:
            h = (60*((B-R)/diff) + 120) % 360
        elif maxV == B:
            h = (60*((R-G)/diff) + 240) % 360

        # step 4 Saturation Calculation

        if maxV == 0:
            s = 0
        else:
            s = (diff/maxV)*100

        # step 5 Value Calculation
        
            v = maxV*100

        # return HSV
        HSV = [self.__roundUp(h),self.__roundUp(s),self.__roundUp(v)]


        return HSV
    
    def rgbtohex(self,r:int,g:int,b:int) -> str:
        """
            # RGB to HEX 
            ### This function will convert rgb color code to hex color code.
        """
        return "#{:02x}{:02x}{:02x}".format(r,g,b)
    

    def hextorgb(self,hex:str) -> list:
        """
            # HEX to RGB 
            ### This Function Will Convert Hex code to RGB Code
        """

        rgb = []

        for i in (0,2,4):
            decimal = int(hex[i:i+2], 16)
            rgb.append(decimal)

        return rgb

