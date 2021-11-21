# Plots for all the environmental ethics stuff.

import helper

ee_table = [
    ["<b>Ethical System</b>","<b>Main Concern</b>","<b>Major Advocates</b>"],
    ["Anthropocentrism","Well-being of humans","Murdy"],
    ["Weak Anthropocentrism","Well-being of humans and their ethical values","Hargrove"],
    ["Ecocentrism","Nature, including organisms and ecosystems","Leopold"],
    ["Biocentrism","Well-being of organisms","Schweitzer, Taylor"],
    ["Sentiocentrism","Well-being of conscious (sentient) organisms","Singer"],
    ["Theocentrism","Valuation of nature as God's creation","Hoffman and Sandelands"],
    ["Biotic Ethics","Extended existence of life","Mautner"],
    ["Environmental Pluralism","Multiple values are considered","Norton (via Afeissa)"]
]

helper.save_image({
    "filename":"environmental_ethics.jpg",
    "status":"Done",
    "details":"A review of several major systems of environmental ethics. This is meant to cover some important systems but not necessarily everything.",
    "table":ee_table,
    "references":["anthropocentrism","weak_anthropocentrism","ecocentrism","biocentrism1","biocentrism2","sentiocentrism","theocentrism","afeissa","mautner"],
    "source_file":"ethics.py"
})

env_table = [
    ["<b>Environmental Tradition</b>","<b>Main Concern</b>","<b>Value System</b>"],
    ["Mainline Environmentalism","Pollution, global warming","Anthopocentrism"],
    ["Nature Conservation","Preserving habitats","Ecocentrism"],
    ["Animal Advocacy","Well-being of individual organisms","Biocentrism or Sentiocentrism"]
]

helper.save_image({
    "filename":"environmentalism.jpg",
    "status":"Done",
    "details":"Three major approaches to environmentalism, at least according to this paper.",
    "table":env_table,
    "references":["three_env"],
    "source_file":"ethics.py"
})

######################################### Precautionary Principle

helper.save_image({
    "filename":"precautionary.jpg",
    "status":"Done",
    "details":"A basic graphical exposition of the precautionary principle. There are four planks as defined by the source: : taking preventive action in the face of uncertainty; shifting the burden of proof to the proponents of an activity; exploring a wide range of alternatives to possibly harmful actions; and increasing public participation in decision making. I don't know the best way to turn this bit of text into a graphic, but I'd like a graphic because otherwise there won't be any in the discussion of the precautionary principle.",
    "references":["precautionary"],
    "source_file":"ethics.py"
})

######################################### Climate change and discount rates

discount_table = [
    ["<b>Study</b>","<b>Discount Rate</b>","<b>Carbon Price per ton CO<sub>2</sub></b>"],
    ["Archer, Kite, Lusk, 2020","0%","$37,000 - 2,750,000"],
    ["Stern","1.4%","$85"],
    ["Nordhaus","3%","$9-10"]
]

# co2_zero_discount

helper.save_image({
    "filename":"c_price_discount.jpg",
    "status":"Done",
    "details":"We have a separate carbon pricing image, and the two might eventually be merged. But the purpose of this one is to show how the carbon price is responsive to the discount rate in particular. The discount rate is the main variable that governs the price.",
    "references":["co2_zero_discount","stern_review","scc_nordhaus_old"],
    "table":discount_table,
    "source_file":"ethics.py"
})

######################################### Population ethics: better to focus on average well-being or aggregate well-being?

pop_ethics_table = [
    ["<b>Ethical view</b>","<b>Description</b>","<b>Major advocates</b>"],
    ["Average Utility / Well-Being (Averagism)","Average well-being across people is the morally relevant value.","Hardin"],
    ["Aggregate Well-Being (Totalism)","Sum of total well-being across people is relevant","Tännsjö"]
]

helper.save_image({
    "filename":"pop_ethics.jpg",
    "status":"Done",
    "details":"A review of some basic ethical positions on population size.",
    "references":["hardin","repugnant"],
    "table":pop_ethics_table,
    "source_file":"ethics.py"
})

######################################### Population ethics: person-affecting views

pav_table = [
    ["<b>Viewpoint</b>","<b>Weight for hypothetical future people</b>"],
    ["Strict Person-Affecting View","None"],
    ["Moderate PAV","Some but not full"],
    ["Wide, or Impersonal","Full, or no distinction between hypothetical and real people"],
    ["Asymmetric PAV","Creating a person with a bad life is bad, and creating a person with a good life is neutral"]
]

helper.save_image({
    "filename":"pav.jpg",
    "status":"Done",
    "details":"A review of major person-affecting views. This is basically the question of what kind of moral weight should be assigned to a hypothetical future person, as opposed to a person who exists or will certainly exist. It bears on the ethics of having children.",
    "references":["beckstead"],
    "table":pav_table,
    "source_file":"ethics.py"
})

######################################### Instrumental vs. intrinsic value in conservation

cons_table = [
    ["<b>Value System</b>","<b>Description</b>","<b>Example Advocates</b>"],
    ["Instrumental","Conservation is valued mainly for human uses","Hampicke"],
    ["Intrinsic","Conservation is valued mainly for nature's sake","Wilson"],
    ["Both","","Callicott, Miller et al."]
]

helper.save_image({
    "filename":"conservation_ethics.jpg",
    "status":"Done",
    "details":"",
    "references":["conservation1","conservation2","conservation3","conservation5"],
    "table":cons_table,
    "source_file":"ethics.py"
})

######################################### Zoos and conservation

helper.save_image({
    "filename":"zoo_conservation.jpg",
    "status":"Done",
    "details":"Some facts about zoos and conservation. About one in seven endangered vertebrates are in a zoo somewhere. Zoos could provide sufficient captive breeding space for up to 800 of 7368 vertebrates that are identified by the 2013 IUCN as endangered (this is less than the 1/7 current accomodated because, just because an endangered vertebrate is in a zoo somewhere, doesn't mean there is enough captive breeding space that would maintain enough genetic diversity). Finally, 16 of 145 historically studied captive breeding programs",
    "references":["zoo_ethics"],
    "source_file":"ethics.py"
})

######################################### Current COSPAR standards for planetary protection

cospar_table = [
    ["<b>Grouping</b>","<b>Description</b>","<b>Example missions covered</b>","<b>Regulations</b>"],
    ["Category I","No interest to the origins or development of life","Metamorphosed asteroids, Io, Sun, Mercury","None"],
    ["Category II","Destination of interest to life, but remote chance of contamination","Moon, Venus, comets, carbonaceous asteroids, gas giants, Titan, Triton, Kuiper Belt objects (including Pluto/Charon), Ceres","Documentation"],
    ["Category III","Fly-by's and orbiters with significant chance of contamination","Mars, Europa, Enceladus","Documentation, spacecraft assembled in cleanroom, possible bioburden reduction"],
    ["Category IV","Probes and landers with significant chance of contamination","Mars, Europa, Enceladus","Extensive documentation, trajectory biasing, cleanrooms, bioburden reduction, possible partial sterilization of the direct contact hardware and a bioshield for that hardware as appropriate"],
    ["Category V, unrestricted","Earth-return missions from destinations not of interest for life","","Same restrictions as previous categories for outbound phase"],
    ["Category V, restricted","Earth-return missions from destinations of interest for life","","Strict containment procedures for all unsterilized material"]
]

helper.save_image({
    "filename":"cospar.jpg",
    "status":"Done",
    "details":"This is a summary of current regulations that the Committee on Space Research (COSPAR) imposes for planetary protection. It is part of the Planetary Protection section under Conservation Ethics. It may eventually be moved to the space site, though for now I think planetary protection is very much a conservation topic and should be covered with other conservation topics.",
    "references":["cospar"],
    "table":cospar_table,
    "source_file":"ethics.py"
})

######################################### Neuron Count

neuron_table = [
    ["<b>Organism</b>","<b>Approximate number of neurons</b>","<b>Source</b>"],
    ["Sponge","0","Sherwood et al."],
    ["Tardigrade","200","Martin et al."],
    ["Caenorhabditis elegans (roundworm)","302","White et al."],
    ["Jellyfish","5600","Bode et al."],
    ["Sea slug","18,000","Cash and Carew"],
    ["Lobster","100,000","The Lobster Institute"],
    ["Ant (depends on species)","250,000","Tefl"],
    ["Cockroach","1 million","anthropology.net"],
    ["Adult Zebrafish","10 million","Hinsch and Zupanc"],
    ["Frog","16 million","neurocomputing.org"],
    ["Bats (depends on species)","35-275 million","Herculano‐Houzel et al. 2020"],
    ["Shrews (depends on species)","36-261 million","Hofman and Falk, Herculano-Houzel December 2006"],
    ["House mouse","71 million","Herculano-Houzel et al. August 2006"],
    ["Red junglefowl (closest wild relative to domestic chickens)","221 million","Olkowicz et al."],
    ["Birds (depends on species)","221-3136 million","Olkowicz et al."],
    ["Guinea pig","240 million","Herculano-Houzel et al. August 2006"],
    ["Gray squirrel","453.66 million","Herculano-Houzel 2011"],
    ["European rabbit","494.2 million","Herculano-Houzel 2011"],
    ["Octopus","500 million","University of Washington"],
    ["Cat","760 million","Ananthanarayanan et al."],
    ["Dog (depends on species or breed)","1.16-4.39 billion","Salajková"],
    ["Monkeys and apes (depends on species)","1.468-33.4 billion","Herculano-Houzel December 2006, Herculano-Houzel and Kaas"],
    ["Raccoon","2.148 billion","Jardim-Messeder et al."],
    ["Pig","2.22 billion","Kazu et al."],
    ["Antelope (depends on species)","2.72-4.91 billion","Kazu et al."],
    ["Lion","4.667 billion","Jardim-Messeder et al."],
    ["Brown bear","9.586 billion","Jardim-Messeder et al."],
    ["Human","86.1 billion","Azevedo et al."],
    ["African elephant","257 billion","Herculano-Houzel 2014"]
]

helper.save_image({
    "filename":"neuron.jpg",
    "status":"Not Done",
    "details":"Neuron count for select animals. Under some models of gradual sentiocentrism, the moral weight that an animals deserves is proportional to the total number of neurons, which in turn are a crude measure of sentience. All this is listed on <a href=\"https://en.wikipedia.org/wiki/List_of_animals_by_number_of_neurons\">Wikipedia</a>, including a bunch of animals that are not included.",
    "references":["neuron_sponge","neuron_tardigrade","neuron_roundworm","neuron_jellyfish","neuron_seaslug","neuron_lobster","neuron_ant","neuron_cockroach", "neuron_zebrafish","neuron_frog","neuron_bat","neuron_shrew1","neuron_mouse","neuron_junglefowl","neuron_octopus","neuron_cat","neuron_dog1","neuron_monkey", "neuron_raccoon","neuron_pig","neuron_human","neuron_elephant"],
    "table":neuron_table,
    "source_file":"ethics.py"
})

######################################### Captive animals

captive_table = [
    ["<b>Category Kept</b>","<b>Number, millions</b>"],
    ["For food, cattle","1400"],
    ["For food, pigs","1000"],
    ["For food, sheep and goats","2000"],
    ["For food, chickens","17,300"],
    ["Companion animals (mostly dogs and cats)","1000"],
    ["Working animals","400"],
    ["Laboratory animals","<100"],
    ["Captive wild animals (e.g. zoos, circuses)","10-100"],
    ["<b>Category Killed per Year","<b>Number, millions</b>"],
    ["For food, cattle","300"],
    ["For food, pigs","1400"],
    ["For food, sheep and goats","1000"],
    ["For food, chickens","50,300"],
    ["For food, rabbits","1200"],
    ["Finfish in aquaculture","10,000-100,000"],
    ["Laboratory animals","100"]
]

helper.save_image({
    "filename":"captive.jpg",
    "status":"Done",
    "details":"Statistics on number of captive animals kills per year and a census. Only vertebrates are counted.",
    "references":["four_activities"],
    "table":captive_table,
    "source_file":"ethics.py"
})

######################################### Predation

predation_table = [
    ["<b>View</b>","<b>Advocates</b>"],
    ["It would be right hypothetically to prevent predation if it would prevent suffering, but this would actually increase suffering.","Singer, Clark"],
    ["Non-human predators are not moral agenda, predation is not a violation of animal rights, and there is no obligation to intervene.","Regan"],
    ["Interfering with predation would be a violation of nature.","Kapembwa"],
    ["We should try to reduce predation if this can be done without increasing overall suffering.","Sapontzis, Cowen"],
    ["We should reprogram predators to cease predation, or sterlize them.","Pearce"],
    ["Causing extinction of carnivores would be instrumentally good, if this doesn't cause ecological upheaval.","McMahan"],
    ["Predators should be preserved, as they are an important part of the ecology.","Fraser"],
    ["Predators are also important to conserve.","Hargrove"],
    ["Predation is a 'sad good' that should be respected, is an important natural process and driver of evolution.","Rolston"]
]

helper.save_image({
    "filename":"predation.jpg",
    "status":"Done",
    "details":"A set of views that environmental ethicists and other philosophers have advanced on the predation problem.",
    "references":["singer","wild_things","mcmahan","regan","kapembwa","sapontzis","policing_nature","pearce_pred","fraser","hargrove","rolston"],
    "table":predation_table,
    "source_file":"ethics.py"
})

######################################### Meat eating: philosophical positions and justifications

meat_table = [
    ["<b>Position</b>","<b>Explanation</b>"],
    ["Veganism","Avoid all animal products"],
    ["Vegetarianism","Avoid meat, not necessarily non-meat animal products like eggs or milk"],
    ["Animal welfarists","Not necessarily any dietary restriction, concerned about animal welfare"],
    ["Meat eaters","No restriction"]
]

helper.save_image({
    "filename":"meat_ethics.jpg",
    "status":"Done",
    "details":"A brief review of the major ethical stances toward meat eating, according to this paper. It is not meant to be comprehensive.",
    "table":meat_table,
    "references":["meat_facts"],
    "source_file":"ethics.py"
})

######################################### Meat eating: animals killed for various diets

meat_table2 = [
    ["<b>Food source</b>","<b>Animals killed over 70 for the average Polish meat/animal product consumption</b>"],
    ["Beef","15 cattle"],
    ["Pork","49 pigs"],
    ["Poultry","2450 chickens"],
    ["Fish (carp)","3220 fish"],
    ["Eggs","140 chickens"],
    ["Milk","2.5 cattle"]
]

helper.save_image({
    "filename":"meat_ethics2.jpg",
    "status":"Done",
    "details":"How many animals are killed if the average Pole gets all meat or animal products from a single species. We have a similar plot on the Meat and Animal Products page, but I made some of my own guesses for that plot, and for this one I think the author understands the issue better, though it's not as comprehensive. This may or may not replace the older plot. These figures include male chicks, bred for eggs, that are killed after birth and calves that are killed after a dairy cow is inseminated. Note that the animals is stated in the second column. The paper itself does not claim that all farm animals should carry the same moral weight, so unless it's the same animal, then these numbers are not comparable (even if they are the same animal, we also have to think about years of life lost, which is also not included here).",
    "table":meat_table2,
    "references":["meat_facts"],
    "source_file":"ethics.py"
})