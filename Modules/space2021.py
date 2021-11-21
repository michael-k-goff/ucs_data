# 2021 space calculations.

# See 2020 space launch figures for tonnages. http://www.spacelaunchreport.com/log2020.html

# Treating EEO as LEO, MEO as GTO, FTO as LEO
tonnage = {
    "LEO":15.6+0.227+15.6+5.015+7.5+15.6+2+7.259+15.6+5.015+7.2+5.55+15.6+7.4+22+0.186+6+16.5+1.4+12.5+15.6+0.442+15.41+2.4+7.4+2.63+15.192+15.44+3.05+0.1+0.877+15.6+0.23+7.42+15.6+7.2+15.6+15.6+0.081+0.5+0.05+0.7+12.5+0.925+0.046+1.192+15.6+1.19+12.5+0.15+5.31+3.22+3.562,
    "GTO":6.976+9.236+4.6+1.415+6.168+4.6+4.311+5.55+4.39+9.804+0.94+4.311+7+1.41,
    "Earth Escape":1.8+1.35+5+4.082+8.2
}

falcon_heavy_energy = 28050044.6304 # See paper for details

max_payload = {
    "LEO":54400,
    "GTO":22200,
    "Earth Escape":13600
}

energy = {}

for key in max_payload:
    energy[key] = falcon_heavy_energy / max_payload[key]
    
total_energy = sum([
    tonnage[key]*energy[key] for key in tonnage
])

# Some emissions figures

us_emissions = 4432.2
space_emissions = 0.019305
us_population = 328200000

print(space_emissions / us_emissions * us_population)