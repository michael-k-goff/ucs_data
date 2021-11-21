# This is for testing stuff. Nothing permanent should go here.

# Value of solar PV land when used as such.

lcoe = 0.10 # Seems high but we'll go with it.
land_use = 140 # Square meters per kW.

production = 10**6 / land_use # kW per square kilometer
production = production * 0.3 * 8760 # Convert power to energy with 30% capacity
production = production * lcoe # Financial value
print(production)