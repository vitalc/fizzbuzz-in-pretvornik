print "Pozdravljen v pretvorniku."
number = int(raw_input("vnesi stevilo m: "))
while True:
    v_enote = raw_input("vnesi zeljeno pretvorbo (cm, km, milje, navticne milje): ")

    if v_enote == "cm":
        print number*100.0
    elif v_enote == "km":
        print number / 1000.0
    elif v_enote == "milje":
        print number * 0.000621371192
    elif v_enote == "navticne milje":
        print number * 0.000539956803
    else:
        print "napacna izbira enote"

    nova = raw_input("hoces novo pretvorbo? (da/ne)".lower())
    if nova == "ne":
        break

print "konec"

