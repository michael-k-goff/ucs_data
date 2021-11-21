# Information technology

import helper

streaming_energy_table = [
    ["<b>Scenario</b>","<b>Data Center</b>","<b>Data Transmission</b>","<b>Device</b>","<b>Total</b>"],
    ["Smartphone video on mobile default resolution",0.23, 8.35, 0.56, 9.14],
    ["Tablet with standard definition",0.64, 8.37, 1.39, 10.4],
    ["Laptop with standard definition",0.64, 8.37, 10.19, 19.2],
    ["Average Viewing",1.71, 8.2, 25.7, 35.61],
    ["50-inch LED television at 4K (ultrahigh definition) resolution",6.42, 8.69, 55.56, 70.67],
    ["Boiling a Kettle","","","",34],
    ["Driving 1 kilometer (about 0.6 miles)","","","",185]
]

helper.save_image({
    "filename":"streaming_emissions.jpg",
    "status":"Done",
    "details":"Emissions associated with one hour of video streaming from Netflix. All figures assume the world average electricity mix. For the four devices (smartphone, tablet, laptop, and TV), I assume local data is from high-powered WiFi. Energy from 4G or low-powered WiFi is a bit less; hence the Average Viewing value has lower emissions for Data Trasmission than the individual devices. This analysis was done by George Kamiya. I am pulling numbers from the IEA website, but the original analysis was on Carbon Brief. The kettle and driving values are included for the sake of comparison. The driving scenario assumes an average internal combustion car, and the kettle scenario assumes, like the streaming scenarios, the world average electricity mix. Only direct energy usage, and not embodied emissions of devices or equipment, is considered.",
    "table":streaming_energy_table,
    "references":["iea_streaming","cb_streaming"],
    "source_file":"it.py"
})

##################################################

bitcoin_energy_table = [
    ["<b>System</b>","<b>Annual Energy Consumption, TWh</b>"],
    ["Bitcoin (estimated by Digiconomist)",79.060],
    ["Ethereum (estimated by Digiconomist)",26],
    ["Bitcoin (estimated by the University of Cambridge)",128.84],
    ["Banks (servers, branches, ATMs, estimated by Zodhya)",139],
    ["Banks (servers, branches, ATMS, estimated by Domingas)",97]
]

helper.save_image({
    "filename":"bitcoin_energy.jpg",
    "status":"Done",
    "details":"Energy consumption of bitcoin vs. some aspects of banks. Of course, this is not a fair comparison for many reasons, not the least of which is that banks serve far more people. Eventually I would like to expand this plot to compare Bitcoin, Etherium, other cryptocurrencies, banks, and gold on the basis of energy per dollar of market capitalization and energy per dollar transacted. But that's a bigger project than I am ready for now. By way of comparison, world electricity consumption is something like 27,000 TWh and primary energy consumption is about six times that (don't put that on the graph, as it will bust the axes).",
    "table":bitcoin_energy_table,
    "references":["bitcoin_energy1","bitcoin_energy2","etherium_energy","bank_energy1","bank_energy2"],
    "source_file":"it.py"
})

##################################################

ml_energy_table = [
    ["<b>Energy User</b>","<b>Annual Consumption</b>"],
    ["Model Training","1.752 TWh"],
    ["Model Inference","8.8-17.5 TWh"]
]

helper.save_image({
    "filename":"ml_energy.jpg",
    "status":"Done",
    "details":"Energy consumption for machine learning models. The training figure is the upper bound for the main source. Inference is the application of a model in the real world. The article says that inference requires 80-90% of lifetime energy, so that's where the inference numbers come from.",
    "table":ml_energy_table,
    "references":["ml_energy"],
    "source_file":"it.py"
})

training_table = [
    ["<b>Energy User</b>","<b>CO<sub>2</sub> emissions (kg)</b>","<b>Explanation</b>"],
    ["Transformer (base)",26,"A lightweight encoder-decoder architecture typically used for machine translation."],
    ["Transformer (big)",192,"Similar to the base transformer but larger"],
    ["ELMo",262,"An NLP model described by Peters et al. in 2018."],
    ["BERT (base)",1438,"An NLP model descibed by Devin et al. in 2019."],
    ["Transformer with neural architecture search",626155,"A tranformer that automates the finding of model architecture. One of the most expensive NLP models as of the writing of the paper."],
    ["Round trip air travel, New York to San Francisco",1984],
    ["Average person, one year",11023],
    ["Average American, one year",36156],
    ["Lifetime emissions of a car",126000,"Included embodied energy and fuel."]
]

for i in range(1,len(training_table)):
    training_table[i][1] /= 2.20462

helper.save_image({
    "filename":"ml_energy2.jpg",
    "status":"Done",
    "details":"Some estimates of the CO<sub>2</sub> emissions required to train natural language processing models, compared with some better-known figures. Most figures from Strubell et al., with the papers describing ELMo and BERT included.",
    "table":training_table,
    "references":["strubell","elmo","bert"],
    "source_file":"it.py"
})

parameter_table = [
    ["<b>Model</b>","<b>Developer</b>","<b>Number of Parameters</b>","<b>Date</b>"],
    ["ELMo (large)","Allen Institute for Artificial Intelligence","93.6 million","2018"],
    ["BERT-large","Google","350 million","2018"],
    ["GPT-2 XL","OpenAI","1.5 billion","2019"],
    ["Grover","Allen Institute","1.5 billion","2019"],
    ["GPT-3","OpenAI","175 billion","2020"]
]

helper.save_image({
    "filename":"model_size.jpg",
    "status":"Done",
    "table":parameter_table,
    "details":"Sizes of some major deep learning models. The number of parameters is a reasonably good proxy for the energy consumption of training the model. Most of these figures are from the Allen Institute, with GPT-3 described by OpenAI (Brown et al.) and the number of parameters of ELMo given by Peters et al. This chart is just meant to portray language models, but similar trends can be observed in computer vision.",
    "references":["greenai","gpt3","elmo2"],
    "source_file":"it.py"
})