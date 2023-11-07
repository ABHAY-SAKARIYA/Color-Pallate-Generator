# Color Pallate Generator

### This is an Smart Color Pallate Generator for web developers and designer.
generate full color pallate scheme by asking only one Main Color in `Hex Code` 

### Approach :
1. first take `hex color code` as `input` from user and convert them to `RGB` then `HSV`.
2. Generate Supporting Color According To The `HSV` Color Code Get.
    - Required Supporting Color :
        - Red : 9 shades : from lighter to darker
        - Orange : 9 shades : from lighter to darker
        - Green : 9 shades : from lighter to darker
        - Blue : 9 shades : from lighter to darker
    - To Generate Red Color :
        - point to remeber that `S` could not be less then `10` and greater than `100` and `V` could not be less than `15` and greater than `100`
        - Red Color `H` = `1` and `S` and `V` be same as `HSV` Color Get and name it `500` .
        - For Lighter Shades We Require 4 Color Shades We Name Them `100  200  300  400`.
            - for shade no. `100` `S` Could be `-22` and `V` could be `+30`.
            - for shade no. `300` `S` Could be `-12` and `V` could be `+15`.
            - for shade no. `200` `S` Could be `-17` and `V` could be `+22`.
            - for shade no. `400` `S` Could be `-7` and `V` could be `+10`.
        - For Darker Shade We Require 4 color Shades we Name Them `600  700  800  900`.
            - for shade no. `900` `S` Could be `+22` and `V` could be `-30`.
            - for shade no. `700` `S` Could be `+12` and `V` could be `-15`.
            - for shade no. `600` `S` Could be `+17` and `V` could be `-22`.
            - for shade no. `800` `S` Could be `+7` and `V` could be `-10`.

    - To Generate Orange Color :
        - point to remeber that `S` could not be less then `10` and greater than `100` and `V` could not be less than `15` and greater than `100`
        - Red Color `H` = `37` and `S` and `V` be same as `HSV` Color Get and name it `500` .
        - For Lighter Shades We Require 4 Color Shades We Name Them `100  200  300  400`.
            - for shade no. `100` `S` Could be `-22` and `V` could be `+30`.
            - for shade no. `300` `S` Could be `-12` and `V` could be `+15`.
            - for shade no. `200` `S` Could be `-17` and `V` could be `+22`.
            - for shade no. `400` `S` Could be `-7` and `V` could be `+10`.
        - For Darker Shade We Require 4 color Shades we Name Them `600  700  800  900`.
            - for shade no. `900` `S` Could be `+22` and `V` could be `-30`.
            - for shade no. `700` `S` Could be `+12` and `V` could be `-15`.
            - for shade no. `600` `S` Could be `+17` and `V` could be `-22`.
            - for shade no. `800` `S` Could be `+7` and `V` could be `-10`.

    - To Generate Blue Color :
        - point to remeber that `S` could not be less then `10` and greater than `100` and `V` could not be less than `15` and greater than `100`
        - Red Color `H` = `210` and `S` and `V` be same as `HSV` Color Get and name it `500` .
        - For Lighter Shades We Require 4 Color Shades We Name Them `100  200  300  400`.
            - for shade no. `100` `S` Could be `-22` and `V` could be `+30`.
            - for shade no. `300` `S` Could be `-12` and `V` could be `+15`.
            - for shade no. `200` `S` Could be `-17` and `V` could be `+22`.
            - for shade no. `400` `S` Could be `-7` and `V` could be `+10`.
        - For Darker Shade We Require 4 color Shades we Name Them `600  700  800  900`.
            - for shade no. `900` `S` Could be `+22` and `V` could be `-30`.
            - for shade no. `700` `S` Could be `+12` and `V` could be `-15`.
            - for shade no. `600` `S` Could be `+17` and `V` could be `-22`.
            - for shade no. `800` `S` Could be `+7` and `V` could be `-10`.

    - To Generate Green Color :
        - point to remeber that `S` could not be less then `10` and greater than `100` and `V` could not be less than `15` and greater than `100`
        - Red Color `H` = `125` and `S` and `V` be same as `HSV` Color Get and name it `500` .
        - For Lighter Shades We Require 4 Color Shades We Name Them `100  200  300  400`.
            - for shade no. `100` `S` Could be `-22` and `V` could be `+30`.
            - for shade no. `300` `S` Could be `-12` and `V` could be `+15`.
            - for shade no. `200` `S` Could be `-17` and `V` could be `+22`.
            - for shade no. `400` `S` Could be `-7` and `V` could be `+10`.
        - For Darker Shade We Require 4 color Shades we Name Them `600  700  800  900`.
            - for shade no. `900` `S` Could be `+22` and `V` could be `-30`.
            - for shade no. `700` `S` Could be `+12` and `V` could be `-15`.
            - for shade no. `600` `S` Could be `+17` and `V` could be `-22`.
            - for shade no. `800` `S` Could be `+7` and `V` could be `-10`.

3. Pass Neutral Color Which Are From White To Black.
    - `100` `H = 0, S = 0, V = 94`
    - `200` `H = 0, S = 0, V = 84`
    - `300` `H = 0, S = 0, V = 74`
    - `400` `H = 0, S = 0, V = 64`
    - `500` `H = 0, S = 0, V = 54`
    - `600` `H = 0, S = 0, V = 44`
    - `700` `H = 0, S = 0, V = 34`
    - `800` `H = 0, S = 0, V = 24`
    - `900` `H = 0, S = 0, V = 10`
