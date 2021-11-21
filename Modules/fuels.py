# Comparison of transportation fuels

import pandas as pd
import helper

# Things we want to know about each fuel. Quantitative figures:
# - Combustion Efficiency
# - Gravimetry Density
# - Volumetric Density

# Probably more qualitative figures
# - Pollution at the point of combustion
# - Cost of engine
# - Safety
# - Current market position

# From 'dana' unless otherwise noted
combustion_efficiency = { # Percentages
    "Methane":54.1,
    "Compressed Natural Gas":54.1, # Assuming the same as for the other CH4.
    "Methanol":54.,
    "Dimethyl Ether":50.,
    "Ammonia":53.,
    "Aqueous Ammonium Hydroxide Urea":50.,
    "Aqueous Ammonium Hydroxide Ammonium Nitrate":47.,
    "Aqueous Urea Ammonium Nitrate":48.,
    "Gasoline":30., # internal combustion engine, 'carfuel',
    "Ethanol":30., # Same as gasoline
    "Diesel":43.5, # icct_diesel, based on statement of 43-44% efficiency.
    "Liquid Hydrogen":55., # hydrogenics. Assuming same efficiency for both kinds of H2
    "Compressed Hydrogen":55., # hydrogenics. Assuming same efficiency for both kinds of H2
    "Lithium Ion Battery":60.5, # fueleconomy_ev
    "Propane":35., # propane_efficiency. Based on eyeballing Figure 3.
    "Butane": 35., # See above, assuming the same as propane.
    "Jet Fuel":0 # Only a placeholder value for coding purposes because I could not find a good real value.
}

# From 'dana' unless otherwise noted
# Units are MJ/kg
gravimetric_density = {
    "Methane":55.5,
    "Compressed Natural Gas":55.5, # Assuming the same as for liquified
    "Methanol":23.7,
    "Dimethyl Ether":31.7,
    "Ammonia":22.5,
#    "Aqueous Ammonium Hydroxide Urea":9.2,
#    "Aqueous Ammonium Hydroxide Ammonium Nitrate":3.7,
#    "Aqueous Urea Ammonium Nitrate":3.3,
    "Liquid Hydrogen":131, # https://hypertextbook.com/facts/2005/MichelleFung.shtml. Average of values. Use this for liquid or compressed.
    "Compressed Hydrogen":131, # https://hypertextbook.com/facts/2005/MichelleFung.shtml. Average of values. Use this for liquid or compressed.
    "Gasoline":45.7, # https://hypertextbook.com/facts/2003/ArthurGolnik.shtml. Going with the first one.
    "Diesel": 35., # Roughly. https://hypertextbook.com/facts/2006/TatyanaNektalova.shtml
    "Ethanol": 29.7, # https://hypertextbook.com/facts/2005/JennyHua.shtml
    "Propane": 49.6, # https://hypertextbook.com/facts/2004/NicoleWeathers.shtml
    "Butane": 49.1, # https://hypertextbook.com/facts/2004/NicoleWeathers.shtml
    "Jet Fuel":43.5, # https://hypertextbook.com/facts/2003/EvelynGofman.shtml, second entry
    "Lithium Ion Battery": 0.25 * 3.6 # iclodean. 250 Wh/kg.
}

# MJ/liter
volumetric_density = {
    "Gasoline":8.76 * 3.6, # https://hypertextbook.com/facts/2003/ArthurGolnik.shtml
    "Diesel": 9.7*3.6, # https://hypertextbook.com/facts/2006/TatyanaNektalova.shtml
    "Methanol":15.912*3.6, # https://hypertextbook.com/facts/2005/JennyHua.shtml
    "Propane":25.3, # https://hypertextbook.com/facts/2004/NicoleWeathers.shtml
    "Butane": 27.7, # https://hypertextbook.com/facts/2004/NicoleWeathers.shtml
    "Jet Fuel": 35., # Roughly the median of several entries. # https://hypertextbook.com/facts/2003/EvelynGofman.shtml
    "Dimethyl Ether":19.188, # toolbox
    "Ethanol": 21.248, # toolbox
    "Liquid Hydrogen":8.49, # toolbox
    "Methane": 48.6, # Liquified. toolbox
    "Compressed Natural Gas": 8.76 * 3.6 * 0.375, # eia_density. Taking the gasoline value above and multiplying by 0.375.
    "Compressed Hydrogen":0.05* 8.76 * 3.6, # eia_density. Taking the gasoline value above and multiplying by 0.05
    "Lithium Ion Battery": 0.25 * 3.6 * 4./3., # battery_density. Applying a 4/3 ratio from volumetric to gravimetric based on this source and the above gravimetric figure.
    "Ammonia":15.6 # ammonia_density
}

# Pressure for fuel storage, in bars.
# From http://cdn.intechopen.com/pdfs/40233/intech-ammonia_as_a_hydrogen_source_for_fuel_cells_a_review.pdf unless otherwise noted.
pressure = {
    "Ammonia":10.,
    "Hydrogen":14., # Metal Hydride
    "Gasoline":1.,
    "LPG":14., # Mixture of propane and butane, though from the source it looks like propane
    "Compressed Natural Gas":250.,
    "Methanol":1.
}

keys = volumetric_density.keys()
# This block of code seems to be borked now.
#df_fuels = pd.DataFrame()
#df_fuels["Fuel"] = keys
#df_fuels["Gravimetric Density (MJ/kg)"] = [gravimetric_density[keys[i]] for i in range(len(keys))]
#df_fuels["Volumetric Density (MJ/liter)"] = [volumetric_density[keys[i]] for i in range(len(keys))]
#df_fuels["Post-Combustion Gravimetric Density (MJ/kg)"] = [gravimetric_density[keys[i]]*combustion_efficiency[keys[i]]/100. for i in range(len(keys))]
#df_fuels["Post-Combustion Volumetric Density (MJ/liter)"] = [volumetric_density[keys[i]]*combustion_efficiency[keys[i]]/100. for i in range(len(keys))]
#df_fuels.to_csv("/Users/michaelgoff/Desktop/Urban Cruise Ship/site/HTML/fuel_density.csv",index=False)

fuels_im = {
    "filename":"fuel_density.jpg",
    "status":"Done",
    "details":"Show gravimetric and volumetric density for various fuels. We will do this in two ways: one showing the energy density of the fuels themselves, and another showing the density of useful energy after combustion (in other words, multiplying fuel density by combustion efficiency). Split it up into several plots if this is too much to do in one. Data is <a href=\"/fuel_density.csv\">here</a>. Make the post-combustion efficiency a darker color and sort by those values, as that is the more relevant figure for the user. In the case of jet fuel, there are some zeros to indicate that I was not able to find a good figure to use for jet efficiency.",
    "references":["dana","hypertextbook","carfuel","icct_diesel","hydrogenics","fueleconomy_ev","propane_efficiency","iclodean","toolbox","eia_density","battery_density","ammonia_density"],
    "source_file":"fuels.py"
}
helper.save_image(fuels_im)




