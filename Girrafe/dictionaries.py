monthConversion = {
    "Jan":"January",
    "Feb":"February",
    "Mar":"March",
    "Apr":"April",
    "May":"May",
    "Jun":"June",
    1:"January",
}
print(monthConversion["Jan"])
print(monthConversion.get("Jun"))
print(monthConversion.get("Luv","Not a valid key"))