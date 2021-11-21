# Figures for the communications sections in cities.

import helper

#################################### Rates of adoption of various IT

it_rate_table = [
    ["<b>Tool and Setting</b>","<b>Adoption Rate</b>"],
    ["Cell phones in the US, 2020","97%"],
    ["Smartphones in the US, 2020","85%"],
    ["Smartphones in the US, 2011","35%"],
    ["Desktop or Labtop in the US, 2021","77%"],
    ["Tablet computer in the US, 2021","53%"],
    ["Cell phones worldwide, 2021","62.07%"],
    ["Smartphones worldwide, 2021","48.33%"]
]

helper.save_image({
    "filename":"it_rates.jpg",
    "status":"Done",
    "details":"Some figures on rates of adoption of various communication devices. US figures are from the Pew Research Center, world figures from Bankmycell.",
    "table":it_rate_table,
    "references":["pew_it","bankmycell"],
    "source_file":"cities_comm.py"
})

##################################### Smartphone usage time

smartphone_use_table = [
    ["<b>Region</b>","<b>Daily smartphone usage time</b>"],
    ["World","3 hours, 15 minutes"],
    ["US","5 hours, 24 minutes"]
]

helper.save_image({
    "filename":"smartphone_use.jpg",
    "status":"Done",
    "table":smartphone_use_table,
    "details":"Some figures on the amount of smartphone use worldwide. Another figure to put in here, though not to portray with a bar, is that the world average is 58 smartphone checks per day.",
    "references":["kommando"],
    "source_file":"cities_comm.py"
})

##################################### Some digital divide stats

digital_divide_table = [
    ["<b>Metric</b>","<b>Percentage</b>"],
    ["Urban Americans with broadband access, 2019","98%"], # https://www.pewtrusts.org/en/trust/archive/summer-2019/americas-digital-divide
    ["Rural Americans with broadband access, 2019","73%"], # https://www.pewtrusts.org/en/trust/archive/summer-2019/americas-digital-divide
    ["Urban American adults with Interet access, 2021","95%"], # https://www.pewresearch.org/fact-tank/2021/04/02/7-of-americans-dont-use-the-internet-who-are-they/
    ["Suburban American adults with Interet access, 2021","94%"], # https://www.pewresearch.org/fact-tank/2021/04/02/7-of-americans-dont-use-the-internet-who-are-they/
    ["Rural American adults with Interet access, 2021","90%"] # https://www.pewresearch.org/fact-tank/2021/04/02/7-of-americans-dont-use-the-internet-who-are-they/
]

helper.save_image({
    "filename":"digital_divide.jpg",
    "status":"Done",
    "details":"Some figures on the digital divide. Keep them as two separate bar plots (in one image): access to broadband, and Internet access. First two numbers from Winslow, next three from Perrin and Atske.",
    "references":["pew_divide","pew_broadband"],
    "table":digital_divide_table,
    "source_file":"cities_comm.py"
})