# World history plot
# -*- coding: utf-8 -*-

import helper

history_table = [
    ["<b>Event</b>","<b>Date</b>","<b>Era</b>","<b>Reference</b>"],
    ["Big Bang","13.7 Bya","Solar System",""],
    ["Formation of Milky Way","12.6 Bya (various values posited)","Solar System",""],
    ["Formation of the Sun","4.6 Bya","Solar System"],
    ["Formation of Earth","4.6 billion years ago","Solar System"], # https://www.britannica.com/science/geologic-history-of-Earth/The-pregeologic-period
    ["Hypothesized creation of the Moon in giant impact event","4.5 billion years ago","Earth","Canup and Asphaug"], # https://www.nature.com/articles/35089010
    ["Surface water known to exist","4.4 billion years ago","Earth"], # http://geoscience.wisc.edu/geoscience/people/faculty/john-valley/a-cool-early-earth/
    ["Oldest known rocks","4.28 billion years ago","Earth"], # https://www.britannica.com/science/geologic-history-of-Earth/The-pregeologic-period
    ["Unconfirmed evidence of life","4.1 billion years ago","Life","Bell et al."], # https://www.pnas.org/content/112/47/14518
    ["Earliest known evidence of life","3.7 billion years ago","Life","Ohtomo et al."], # https://www.nature.com/articles/ngeo2025
    ["Vaalbara, possibly the earliest supercontinent","3.6-2.7 billion years ago","Earth","Wit"], # https://onlinelibrary.wiley.com/doi/abs/10.1046/j.1365-3121.1998.00199.x
    ["Blue-green algae known to exist","3.5 billion years ago","Life"], # https://www.britannica.com/science/geologic-history-of-Earth/Development-of-the-atmosphere-and-oceans
    ["Earliest known land life","3.22 billion years ago","Life"], # https://www.livescience.com/63199-oldest-life-on-land.html
    ["Possible formation of Ur (incompatible with Vaalbara hypothesis)","3 billion years ago","Earth","Zubritsky"], # https://endeavors.unc.edu/spr97/ur.html
    ["Earliest fungi","2.4 billion years ago","Life","Bengtson"], # https://www.nature.com/articles/s41559-017-0141
    ["Great Oxygenation Event","2.4 to 2.0 billion years ago","Life","Lyons et al."], # https://www.nature.com/articles/nature13068
    ["Formation of Columbia supercontinent","2100 to 1800 million years ago","Earth","Zhao et al."], # https://www.sciencedirect.com/science/article/abs/pii/S0012825202000739?via%3Dihub
    ["Earliest known eukaryotes, oxygen-breathing organisms","1.4 billion years ago","Life"], # https://www.britannica.com/science/geologic-history-of-Earth/Development-of-the-atmosphere-and-oceans
    ["Formation of Rodinia supercontinent","1300 to 900 million years ago", "Earth","Li et al. (2008)"], # https://www.sciencedirect.com/science/article/abs/pii/S0301926807001635?via%3Dihub
    ["Origin of Sexual Reproduction","1.2 billion years ago","Life","Butterfield"], # https://bioone.org/journals/paleobiology/volume-26/issue-3/0094-8373(2000)026%3C0386%3ABPNGNS%3E2.0.CO%3B2/Bangiomorpha-pubescens-n-gen-n-sp--implications-for-the/10.1666/0094-8373(2000)026%3C0386:BPNGNS%3E2.0.CO;2.short
    
    ["Earliest animals","850-650 million years ago","Animals","Cunningham et al."], # https://onlinelibrary.wiley.com/doi/full/10.1002/bies.201600120
    ["Snowball Earth","720-635 million years ago","Earth","Hoffman et al."], # https://advances.sciencemag.org/content/3/11/e1600983
    ["First known animals with soft parts, e.g. jellyfish and worms","650 million years ago","Animals"], # https://www.britannica.com/science/geologic-history-of-Earth/Development-of-the-atmosphere-and-oceans
    ["Formation of Pannotia supercontinent","650 to 500 million years ago","Earth","Scotese"], # http://mr.crossref.org/iPage?doi=10.1144%2FSP326.4
    ["Cambrian Explosion: most modern phyla of animals appear","542-488 million years ago","Animals"], # https://burgess-shale.rom.on.ca/en/science/origin/04-cambrian-explosion.php
    # For the following, see the mass_extinction plot.
    ["Oldest known land plants","473-471 million years ago","Animals","Rubenstein et al."], # https://nph.onlinelibrary.wiley.com/doi/full/10.1111/j.1469-8137.2010.03433.x
    ["Ordovician-Silurian extinction events","450-440 million years ago","Animals"],
    ["Oldest known trees","393-372 million years ago","Normile","Animals"], # https://www.sciencemag.org/news/2017/10/world-s-first-trees-grew-splitting-their-guts#
    ["Late Devonian extinction","375-360 million years ago","Animals"],
    ["Existence of Pangaea supercontinent","299-180 million years ago","Earth"], # https://www.britannica.com/place/Pangea
    ["Permian-Triassic extinction event","252 million years ago","Animals"],
    ["Oldest known dinosaurs","231.4 million years ago","Animals"], # https://zookeys.pensoft.net/articles.php?id=2415
    ["First mammals","210 million years ago","Animals"], # https://www.nationalgeographic.com/science/prehistoric-world/rise-mammals/
    ["Triassic-Jurassic extinction event","201.3 million years ago","Animals"],
    
    ["Cretaceous-Paleogene extinction event","66 million years ago","Animals"],
    ["First primates","55-50 million years ago","Animals"], # https://www2.palomar.edu/anthro/earlyprimates/early_2.htm
    ["First hominids","20-15 million years ago","Hominids"], # http://www.timetree.org/search/pairwise/Hominidae/Hylobatidae
    ["Evolution of human bipedalism in <i>Danuvius guggenmosi</i>. Bipedalism is much more energy efficient than walking on four legs.","12 million years ago","Hominids"], # https://en.wikipedia.org/wiki/Danuvius_guggenmosi
    ["Earliest evidence of Australopithecus","4.2 million years ago","Hominids","Haile-Selassie"], # https://royalsocietypublishing.org/doi/10.1098/rstb.2010.0064
    ["Oldest known stone tools","3.3 million years ago","Hominids","Harmand et al."], # https://www.nature.com/articles/nature14464
    ["Earliest of genus Homo","2.8 million years ago","Hominids"], # https://www.bbc.com/news/science-environment-31718336
    ["Controlled fire","1 million years ago","Hominids","Berna et al."], # https://www.pnas.org/content/109/20/E1215
    
    ["Neanderthals","315 kya (earliest date of split from modern humans) to 40 kya (extinction). This should appear on both the Homo Sapiens and the Homonids timeline.","Homo Sapiens"], # https://en.wikipedia.org/wiki/Neanderthal
    ["Homo sapiens","350,000 to 260,000 years ago. This should appear on both the Homo Sapiens and the Homonids timeline.","Homo Sapiens","Schlebusch"], # https://science.sciencemag.org/content/358/6363/652
    ["Behavioral modernity: language, abstract thinking, social norms, big game hunting, symbolism.","50,000 years ago","Homo Sapiens","Bar-Yosef"], # https://www.annualreviews.org/doi/10.1146/annurev.anthro.31.040402.085416
    ["Permanent homo sapiens settlement of Europe (Cro-Magnon)","From 48 kya","Homo Sapiens"],
    ["Clovis culture in the Americans. This was once believed to be the oldest human settlement of the Americas, but settlement is now believed to have occurred earlier.","11,000 BC","Homo Sapiens"],
    
    ["Younger Dryas, a miniature ice age.","10900-9700 BC","Neolithic"],
    ["Agriculture in the Near East. Should be on the Homo Sapiens timeline as well.","9500 BC","Neolithic"], # https://www.journals.uchicago.edu/doi/10.1086/659307
    ["Göbekli Tepe settled, earliest known temple and major settlement. Should be on the Homo Sapiens timeline as well.","9500 BC","Neolithic"],
    ["Most large animals domesticated","8000 BC","Neolithic"], # https://en.wikipedia.org/wiki/Neolithic
    ["Copper smelting observed at Belovode","5000 BC","Neolithic"],
    
    ["Start of Bronze Age","By 3000 BC","Bronze Age Timeline"], # https://www.nature.com/articles/nature14507.
    ["Start of Iron Age","1200 BC","Bronze Age Timeline"], # https://www.bu.edu/anep/Ir.html
    ["Axial Age: Development of universal empires, religions, and philosophies","800-200 BC","Bronze Age Timeline"],
    ["Approximate date that papermaking started in China","100 BC","Bronze Age Timeline"],
    ["Fall of Western Roman Empire","AD 476","Bronze Age Timeline"],
    ["Black Death","AD 1347-1351","Bronze Age Timeline"],
    ["Columbus' Voyage","AD 1492","Bronze Age Timeline"],
    ["European Enlightenment","AD 1637-1789 (dates vary)","Bronze Age Timeline"],
    
    ["James Watt steam engine released commercially. It was much more versatile and efficient than previous steam engines and played a major role in the Industrial Revolution.","AD 1776","Industrial"],
    ["Commercial Trains in Widespread Use","1820s","Industrial"],
    ["Bessemer Process of steelmaking announced. This made steel cheap and mass-produced and greatly expanded railroads.","1856","Industrial"],
    ["First coal-fired power plant and arguably the first electric power plant.","AD 1882","Industrial"],
    ["Bakelite, first synthetic plastic, patented","1909","Industrial"],
    ["Kitty Hawk","1903","Industrial"],
    ["Bailley Solar PV design","1908","Industrial"], # https://www.ensolar.energy/a-history-overview-of-solar-panels/
    ["Henry Ford mass production of cars begins","1913","Industrial"], # https://en.wikipedia.org/wiki/Car
    ["World War I","AD 1914-1918","Industrial"],
    ["Great Depression","1929-39 (approximate)","Industrial"],
    ["World War II","AD 1939-1945","Industrial"],
    
    ["Calder Hall, first full-scale commercial nuclear power plant","1956","Atomic"],
    ["Ivy Mike, the first full-scale thermonuclear weapon, tested","1952","Atomic"],
    ["Construction begins on Interstate Highway System","1956","Atomic"],
    ["Sputnik I, the first artificial satellite, launched","AD 1957","Atomic"],
    ["TIROS, the first weather satellite, is launched","1960","Atomic"],
    ["Peak of decolonization","AD 1960s","Atomic"],
    ["Apollo 8, which captured the Earthrise photograph","1968","Atomic"],
    ["Apollo 11, first human landing on the Moon","1969","Atomic"],
    ["First Earth Day","1970","Atomic"],
    ["OPEC Oil Embargo","1973-74","Atomic"],
    ["Three Mile Island nuclear disaster hampers development of the industry","1979","Atomic"],
    ["Chernobyl nuclear disaster further hampers development of the industry","1986","Atomic"],
    ["Montreal Protocol signed, which banned most ozone-depleting substances","1987","Atomic"],
    
    ["Release of World Wide Web, the first Internet browser and a key event in making the Internet available to the public","1990","Information"],
    ["Breakup of Soviet Union","AD 1991","Information"],
    ["Rio de Janerio Earth Summit addressed climate change and other environmental challenges","1992","Information"],
    ["Global Position System fully operational","1995","Information"],
    ["Kyoto Protocol signed. The Protocol limited greenhouse gas emissions among signatories.","1997","Information"],
    ["iPhone, first commercially successful smartphone, released","2007","Information"],
    ["Global Financial Crisis","2008-09","Information"],
    ["Paris Agreement further limits greenhouse gas emissions.","2015","Information"],
    ["COVID-19 Pandemic","2020","Information"],
    ["Human population about 7.8 billion","2020","Information"],
    
    ["Humans on Mars","2033","Future","Reedy"],
    ["Brain-Computer Interfaces Widespread","2040","Future","Li and Zhao"],
    ["Designer Babies","2040-60","Future","Kimball"],
    ["Artificial General Intelligence","2060","Future","AI Multiple"],
    ["Fusion power is commercialized under the ITER timeline","2060s","Future"],
    ["Space colonization via O'Neill Cylinders","2074","Future","O'Neill"],
    ["Peak of human population at about 11 billion, median estimate","2100","Future","UN"],
    
    ["Under the worst case scenario (RCP 8.5, high end of range), global temperatures have increased by 12.6 &deg;C","2300","Far Future","IPCC"], # See https://www.ipcc.ch/site/assets/uploads/2018/02/WG1AR5_Chapter12_FINAL.pdf, Table 12.2
    ["If CO<sub>2</sub> emissions stop now, then 80% of excess CO<sub>2</sub> has been absorbed.","AD 3000","Far Future","Frölicher et al."], # https://www.princeton.edu/news/2013/11/24/even-if-emissions-stop-carbon-dioxide-could-warm-earth-centuries
    ["Sahara could turn green again","AD 12,000-13,000","Far Future","Coffey"], # https://www.livescience.com/will-sahara-desert-turn-green.html
    ["Absent the effects of climate change, the next ice age is expected","AD 50,000","Far Future","Nature"], # https://www.nature.com/scitable/knowledge/library/what-happens-after-global-warming-25887608/
    ["Niagara Falls will have eroded away","50,000 years from now","Far Future","Niagara Parks"], # https://www.niagaraparks.com/visit-niagara-parks/plan-your-visit/niagara-falls-geology-facts-figures/
    ["If CO<sub>2</sub> emissions stop now, then the world will have returned to preindustrial CO<sub>2</sub> concentrations.","AD 100,000","Far Future","Nature"], # https://www.nature.com/scitable/knowledge/library/what-happens-after-global-warming-25887608/
    ["South Dakota Badlands will have eroded","500,000 years from now","Far Future","Department of the Interior"], # https://www.doi.gov/blog/10-things-you-didnt-know-about-badlands-national-park
    ["An asteroid of size 1 km or greater has a 50% chance of having impacts Earth by now. The result of such an impact could be catastrophic for civilization.","AD 600,000","Far Future","MIT"], # https://news.mit.edu/2003/asteroid-0910
    
    ["East African Rift will create a new ocean and split the African continent","5-10 million years from now","Earth","Chow"], # https://www.nbcnews.com/science/environment/african-continent-very-slowly-peeling-apart-scientists-say-new-ocean-n1234128
    ["Hawaiian Islands will sink. New islands will have been formed.","80 million years from now","Earth","Perlman"], # https://www.sfgate.com/news/article/Kiss-that-Hawaiian-timeshare-goodbye-Islands-2468202.php
    ["Formation of Pangaea Ultima, the last supercontinent. It is likely to result in a mass extinction, due to loss of land and subduction of CO<sub>2</sub> in the atmosphere. Due to mantle cooling, place tectonics will slow. This and loss of CO<sub>2</sub> are likely to result in a mass extinction, from which complex life will not recover.","250 million years from now.","Earth"], # http://www.scotese.com/newpage11.htm
    ["Weathering increases, plate tectonics cease, carbon dioxide levels fall to the point where C<sub>3</sub> synthesis is impossible and most plants die.","500-600 million years from now","Animals","O'Malley-James et al."], # https://arxiv.org/abs/1210.5721
    ["End of solar eclipses","600 million years from now.","Earth","Mathewson"], # https://sunearthday.nasa.gov/2006/faq.php
    ["Most land is barren dessert","500-800 million years from now","Earth","Ward and Brownlee"], # https://www.ohsd.net/cms/lib09/WA01919452/Centricity/Domain/675/Rare%20Earth%20Book.pdf, allegedly
    ["C<sub>4</sub> photosynthesis becomes impossible, all plants and animals die out.","800-900 million years from now.","Animals","Ward"], # https://www.amazon.com/Life-Death-Planet-Earth-Astrobiology/dp/0805075127
    ["Moist greenhouse: runaway evaporation of the oceans commences.","1.1 billion years from now.","Earth","O'Malley-James et al."], # https://arxiv.org/abs/1210.5721
    ["Eukaryotic life dies out.","1.3 billion years from now.","Life","Franck et al."], # https://hal.archives-ouvertes.fr/hal-00297823/file/bgd-2-1665-2005.pdf
    ["Lower estimate for extinction of prokaryotic life","1.6 billion years from now.","Life","Franck et al."], # https://hal.archives-ouvertes.fr/hal-00297823/file/bgd-2-1665-2005.pdf
    ["Upper limit for survival of oceans.","2 billion years from now.","Life","Li et al. (2009)"], # https://www.pnas.org/content/106/24/9576
    ["Outer core freezes, magnetic field shuts down, charged particles from the Sun deplete the atmosphere.","2.3 billion years from now","Earth"], # https://agupubs.onlinelibrary.wiley.com/doi/abs/10.1029/92GL02485 and other sources
    ["All life on Earth is extinct.","2.8 billion years from now.","Life","Luhmann et al."], # https://arxiv.org/abs/1210.5721
    ["Surface rock on Earth starts melting.","3.5-4.5 billion years from now.","Earth","Kasting"], # https://www.sciencedirect.com/science/article/abs/pii/0019103588901169?via%3Dihub
    ["Earth has probably fallen into the red giant Sun and is destroyed. :(","7.59 billion years from now.","Earth"] # https://arxiv.org/abs/0801.4031
]

# Future stuff
# Designer babies: 2040-60: https://gizmodo.com/when-will-we-have-designer-babies-1820230299
# AGI: 2060: https://research.aimultiple.com/artificial-general-intelligence-singularity-timing/
# BCI: 2040: https://academic.oup.com/nsr/article/7/2/480/5586180
# Humans on Mars: 2033: https://futurism.com/when-will-the-first-human-space-colony-be-established
# Space colonization: 2074 (1974 article says 100 years). https://space.nss.org/the-colonization-of-space-gerard-k-o-neill-physics-today-1974/
# Peak of human population: 2100

helper.save_image({
    "filename":"earth_timeline.jpg",
    "status":"Done",
    "table":history_table,
    "details":"A few changes to be made. Look at the chart closely, as some events have been added, removed, or renamed. Some general comments. The projection lines were good; I would be careful about having them intersect text. Maybe add the lines but break them for text. For every timeline exceppt the Near Future, the first event on one timeline should also appear on the previous timeline. The words for time lengths (e.g. 'billions' on the first one) should be closer to the actual numbers. For the events with date ranges, like the world wars, either portray them as ranges on the image or indicate that the shown date is the starting date. A note about eras:<br><br>Rename \"Evolution of Animals Timeline\" to \"Animals Timeline\". The end date of this timeline should go to the likely extinction of animals, about 900 million years from now.<br><br>To be clearer on the name, and also a bit more accurate, Chalcolithic (Copper Age) has been renamed Bronze Age. The period corresponds more closely with the Bronze Age anyway. The dates on the Bronze Age should be 3500 BC to AD 1760 (this includes the Iron Age and subsequent eras, which don't have their own timeline). It should be noted that the dates of the Bronze Age vary considerably by region; I am choosing a start date corresponding with the Near East Bronze Age, which is the earliest widely accepted time that it started.<br><br>I am choosing the invention of the James Watt steam engine as the start of the Industrial Revolution. Dates range from the invention of the Newcomen steam engine (1712) to the commercialization of railroads (1820s).<br><br>There are more recent events, so let's go back to splitting the recent era into Atomic (~1945-1990) and Information (~1990 to present)<br><br>For the near future material, emphasize that these are predictions from practioners in the field, not necessarily our predictions.",
    "references":[],
    "source_file":"world_history.py"
})

history_table2 = [
    ["<b>Event</b>","<b>Date</b>","<b>Era</b>","<b>Reference</b>"],
    ["Invention of the Wheel","3500 BC (exact date debated)","Bronze Age","Cité de l'Economie et de la Monnaie"], # https://www.citeco.fr/10000-years-history-economics/the-origins/invention-of-the-wheel
    ["First known humans in Americas","31000 BC (actively debated)","Homo Sapiens","Somerville et al."], # https://www.cambridge.org/core/journals/latin-american-antiquity/article/new-ams-radiocarbon-ages-from-the-preceramic-levels-of-coxcatlan-cave-puebla-mexico-a-pleistocene-occupation-of-the-tehuacan-valley/F4C32FB10E73D660CB7D9B44E2C29A72
    ["Telescope invented","AD 1608","Bronze Age","Library of Congress"], # https://www.loc.gov/collections/finding-our-place-in-the-cosmos-with-carl-sagan/articles-and-essays/modeling-the-cosmos/galileo-and-the-telescope
    ["Heliocentric Model (publication of De Revolutionibus)","AD 1543","Bronze Age",""],
    ["Fukushima Nuclear Disaster","AD 2011","Information",""],
    ["Lucens Nuclear Disaster","AD 1969","Atomic",""], # https://en.wikipedia.org/wiki/Lucens_reactor
    ["SL-1 Nuclear Meltdown","AD 1961","Atomic",""], # https://en.wikipedia.org/wiki/SL-1
    ["Kyshtym Nuclaer Disaster","AD 1957","Atomic",""], # https://en.wikipedia.org/wiki/Kyshtym_disaster
    ["Windscale fire","AD 1957","Atomic",""], # https://en.wikipedia.org/wiki/Windscale_fire
    ["Metal bearings patented","AD 1794","Industrial",""], # http://resources.hartfordtechnologies.com/blog/the-history-of-ball-bearings
    ["First oil well (Edwin Drake's)","AD 1859","Industrial",""],
    ["First ocean-going ironclad (Gloire)","AD 1859","Industrial",""], # https://en.wikipedia.org/wiki/French_ironclad_Gloire
    ["First ISO standard on containerization","AD 1968","Atomic",""],
    ["First commercial airline","AD 1914","Industrial",""], # https://en.wikipedia.org/wiki/Airline
    ["Federal Aid Highway Act creates the Interstate Highway System","AD 1956","Atomic",""],
    ["First industrial robot, Unimate, enters production","AD 1961","Atomic","Norman"], # https://www.historyofinformation.com/detail.php?entryid=4071
    ["First 24/7 use of unmanned air vehicles in a major conflict","AD 1991","Information","Consortiq"], # https://consortiq.com/short-history-unmanned-aerial-vehicles-uavs/
    ["First practical helicopter","AD 1923","Industrial",""], # https://en.wikipedia.org/wiki/Autogyro
    ["First power grid","AD 1879","Industrial","Edison Tech Center"], # https://edisontechcenter.org/HistElectPowTrans.html
    ["Edison patents electric map","AD 1879","Industrial",""], # https://en.wikipedia.org/wiki/Incandescent_light_bulb
    ["First commercial LED","AD 1962","Atomic",""], # https://en.wikipedia.org/wiki/Light-emitting_diode
    ["First mobile phone","AD 1973","Atomic",""], # https://en.wikipedia.org/wiki/Mobile_phone
    ["First dinosaur fossils found","AD 1819","Industrial",""], # https://wonderopolis.org/wonder/who-discovered-the-first-dinosaur-bone
    ["Walden Published","AD 1854","Industrial",""],
    ["On the Origin of Species Published","AD 1859","Industrial",""],
    ["Sierra Club founded","AD 1892","Industrial",""],
    ["Yellowstone National Park created, first national park in the US","AD 1872","Industrial",""],
    ["The Jungle published. Pure Food and Drug Act passed the same year.","AD 1906","Industrial",""]
]

helper.save_image({
    "filename":"timeline_update.jpg",
    "status":"Not Done",
    "table":history_table2,
    "details":"More revisions to the timeline. I am making a separate entry and table here because the previous one was getting unwieldy. Add these events to the timelines depending on what will fit.",
    "references":[],
    "source_file":"world_history.py"
})