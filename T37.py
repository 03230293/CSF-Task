month=input()
if month in ["January", "February", "March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
elif month in ["September","october", "November"]:
    print("Fall")
elif month=="December":
    print("Winter")
else:
    print("Invalid month")