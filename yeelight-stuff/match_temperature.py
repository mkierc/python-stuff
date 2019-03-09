import math

from my_lamps import bed_lamp


def convert_kelvin_to_rgb(colour_temperature):
    """
    Converts from K to RGB, algorithm courtesy of
    http://www.tannerhelland.com/4435/convert-temperature-rgb-algorithm-code/
    """
    # range check
    if colour_temperature < 1000:
        colour_temperature = 1000
    elif colour_temperature > 40000:
        colour_temperature = 40000

    tmp_internal = colour_temperature / 100.0

    # red
    if tmp_internal <= 66:
        red = 255
    else:
        tmp_red = 329.698727446 * math.pow(tmp_internal - 60, -0.1332047592)
        if tmp_red < 0:
            red = 0
        elif tmp_red > 255:
            red = 255
        else:
            red = tmp_red

    # green
    if tmp_internal <= 66:
        tmp_green = 99.4708025861 * math.log(tmp_internal) - 161.1195681661
        if tmp_green < 0:
            green = 0
        elif tmp_green > 255:
            green = 255
        else:
            green = tmp_green
    else:
        tmp_green = 288.1221695283 * math.pow(tmp_internal - 60, -0.0755148492)
        if tmp_green < 0:
            green = 0
        elif tmp_green > 255:
            green = 255
        else:
            green = tmp_green

    # blue
    if tmp_internal >= 66:
        blue = 255
    elif tmp_internal <= 19:
        blue = 0
    else:
        tmp_blue = 138.5177312231 * math.log(tmp_internal - 10) - 305.0447927307
        if tmp_blue < 0:
            blue = 0
        elif tmp_blue > 255:
            blue = 255
        else:
            blue = tmp_blue

    return red, green, blue


def main():

    props = bed_lamp.get_properties()
    # bed_lamp.set_brightness(50)
    print(props)

    # print(hex(int(props['rgb'])))
    #
    # # bed_lamp.set_color_temp(2440)
    # # bed_lamp.set_rgb(256,120,120)
    #
    # R, G, B = convert_kelvin_to_rgb(2440)
    # R, G, B = int(R), int(G), int(B)
    #
    # r_range = [x for x in range(R, 0, -R // 9)]
    # g_range = [x for x in range(G, 0, -G // 9)]
    # b_range = [x for x in range(B, 256, (256 - B) // 9)]
    #
    # # transitions = [HSVTransition(hue, 100, duration=00) for hue in range(0, 359, 40)]
    # # trans = [RGBTransition(r, g, b, duration=50) for r, g, b in zip(r_range, g_range, b_range)]
    #
    # # for r,g,b in  zip(r_range, g_range, b_range):
    # #     bed_lamp.set_rgb(R,B,b)
    # #     sleep(1)
    #
    #
    # # bed_lamp.set_color_temp(2440)
    #
    # flow = Flow(
    #     count=2,
    #     transitions=transitions.christmas()
    # )
    #
    # bed_lamp.start_flow(flow)
    #
    # # bed_lamp.set_rgb(R,G,B)
    #
    # print(r_range)
    # print(g_range)
    # print(b_range)


if __name__ == "__main__":
    main()
