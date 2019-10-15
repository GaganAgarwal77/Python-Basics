birth_date= int(input("Enter your birth date(1-31): "))
birth_month= input("Enter your birth month: ").lower()
if birth_date <1 or birth_date >31:
    print("Invalid Input")
else:
    if birth_month == "july":
       if birth_date <23:
        print("Your Zodiac Sign is Cancer.")
       else:
           print("Your Zodiac Sign is Leo.")
    if birth_month == "june":
       if birth_date <21:
        print("Your Zodiac Sign is Gemini.")
       elif birth_date > 30:
           print("Invalid Input")
       else:
           print("Your Zodiac Sign is Cancer.")
    if birth_month == "august":
       if birth_date <23:
        print("Your Zodiac Sign is Leo.")
       else:
           print("Your Zodiac Sign is Virgo.")
    if birth_month == "september":
       if birth_date <23:
        print("Your Zodiac Sign is Virgo.")
       elif birth_date > 30:
           print("Invalid Input")
       else:
           print("Your Zodiac Sign is Libra.")
    if birth_month == "october":
       if birth_date <23:
        print("Your Zodiac Sign is Libra.")
       else:
           print("Your Zodiac Sign is Scorpio.")
    if birth_month == "november":
       if birth_date <22:
        print("Your Zodiac Sign is Scorpio.")
       elif birth_date > 30:
           print("Invalid Input")
       else:
           print("Your Zodiac Sign is Sagittarius.")
    if birth_month == "december":
       if birth_date <22:
        print("Your Zodiac Sign is Sagittarius.")
       else:
           print("Your Zodiac Sign is Capricorn.")
    if birth_month == "january":
       if birth_date <20:
        print("Your Zodiac Sign is Capricorn.")
       else:
           print("Your Zodiac Sign is Aquarius.")
    if birth_month == "february":
       if birth_date <19:
        print("Your Zodiac Sign is Aquarius.")
       elif birth_date > 29:
           print("Invalid Input")
       else:
           print("Your Zodiac Sign is Pisces.")
    if birth_month == "march":
       if birth_date <21:
        print("Your Zodiac Sign is Pisces.")
       else:
           print("Your Zodiac Sign is Aries.")
    if birth_month == "april":
        if birth_date <20:
            print("Your Zodiac Sign is Aries.")
        elif birth_date > 30:
            print("Invalid Input")
        else:
           print("Your Zodiac Sign is Taurus.")
    if birth_month == "may":
       if birth_date <21:
        print("Your Zodiac Sign is Taurus.")
       else:
           print("Your Zodiac Sign is Gemini.")
