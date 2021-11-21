# These are calculations related to distributed electricity

import helper

# Some of these are copied from production_overview.py from the parent folder
distributed_lcoe = [
    {"type":"Distributed Solar - Small","lcoe_low":16.0,"lcoe_high":26.7, "source":"https://www.lazard.com/media/450784/lazards-levelized-cost-of-energy-version-120-vfinal.pdf"}, # Was Solar PV - Rooftop Residential
    {"type":"Distributed Solar - Large","lcoe_low":8.1,"lcoe_high":17.0, "source":"https://www.lazard.com/media/450784/lazards-levelized-cost-of-energy-version-120-vfinal.pdf"}, # Was Solar PV - Rooftop C&I.
    {"type":"Community Solar","lcoe_low":7.3,"lcoe_high":14.5, "source":"https://www.lazard.com/media/450784/lazards-levelized-cost-of-energy-version-120-vfinal.pdf"}, # Was Solar PV - Community
    {"type":"Fuel Cell","lcoe_low":10.3,"lcoe_high":15.2, "source":"https://www.lazard.com/media/450784/lazards-levelized-cost-of-energy-version-120-vfinal.pdf"},
    {"type":"Distributed Solar - Small","lcoe_low":7.2,"lcoe_high":11.6,"source":"https://www.ise.fraunhofer.de/content/dam/ise/en/documents/publications/studies/EN2018_Fraunhofer-ISE_LCOE_Renewable_Energy_Technologies.pdf"},
    {"type":"Distributed Solar - Large","lcoe_low":4.9,"lcoe_high":8.3,"source":"https://www.ise.fraunhofer.de/content/dam/ise/en/documents/publications/studies/EN2018_Fraunhofer-ISE_LCOE_Renewable_Energy_Technologies.pdf"},
    {"type":"Diesel Generator","lcoe_low":16.4,"lcoe_high":21.0,"source":"https://res.mdpi.com/energies/energies-11-00687/article_deploy/energies-11-00687-v3.pdf?filename=&attachment=1"},
    {"type":"Community Solar","lcoe":65.8,"source":"https://www.mdpi.com/2071-1050/9/6/910/htm"}, # Currency is RMB. Multiply by 0.15 for USD. Was Solar Microgrid
    {"type":"Wind Microgrid","lcoe":70.4,"source":"https://www.mdpi.com/2071-1050/9/6/910/htm"}, # Currency is RMB. Multiply by 0.15 for USD
    {"type":"Biomass Microgrid","lcoe":88.5,"source":"https://www.mdpi.com/2071-1050/9/6/910/htm"}, # Currency is RMB. Multiply by 0.15 for USD
    {"type":"Fuell Cell","lcoe_low":6.5,"lcoe_high":12.7,"source":"https://www.oecd-nea.org/ndd/pubs/2015/7057-proj-costs-electricity-2015.pdf"}, # 30/ton carbon pricing, no heat credit. Solid Oxide Fuel Cells
    {"type":"Fuel Cell","lcoe_low":8.1,"lcoe_high":16.8,"source":"https://www.oecd-nea.org/ndd/pubs/2015/7057-proj-costs-electricity-2015.pdf"}, # Molten Carbonate Fuel Cells
#    {"category":"Hydro","type":"Small Hydro","lcoe_low":2.3,"lcoe_high":10.6,"source":"irena_hydro"},
    {"type":"PV+Battery Microgrid","lcoe":30,"source":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3201095"},
    {"type":"Micro Hydro","lcoe":16,"source":"https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3201095"},
    {"type":"Micro-reactors: first of a kind","lcoe_low":11,"lcoe_high":41,"source":"https://www.nei.org/CorporateSite/media/filefolder/resources/reports-and-briefs/Report-Cost-Competitiveness-of-Micro-Reactors-for-Remote-Markets.pdf"},
    {"type":"Micro-reactors: after learning-by-doing","lcoe_low":9,"lcoe_high":33,"source":"https://www.nei.org/CorporateSite/media/filefolder/resources/reports-and-briefs/Report-Cost-Competitiveness-of-Micro-Reactors-for-Remote-Markets.pdf"}
]

# From production overview, since some of those currencies are not current USD.
source_currency_converters = {
    "http://www.co2crc.com.au/wp-content/uploads/2016/04/LCOE_Report_final_web.pdf":0.75,
    "https://www.ise.fraunhofer.de/content/dam/ise/en/documents/publications/studies/EN2018_Fraunhofer-ISE_LCOE_Renewable_Energy_Technologies.pdf":1.15,
    "https://www.bicc.de/uploads/tx_bicctools/MENA_Select-Electricity_Planning_for_Sustainable_Development_in_the_MENA_Region-main.pdf":1.15,
    "https://www.mdpi.com/2071-1050/9/6/910/htm":0.15,
    "https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/665197/TEA_Project_1_Vol_1_-_Comprehensive_Analysis_and_Assessment_SMRs.pdf":1.4,
    "https://www.euro-fusion.org/fileadmin/user_upload/Archive/wp-content/uploads/2015/02/Bustreo_Fusion-Economics.pdf":1.4,
    "https://www.ise.fraunhofer.de/content/dam/ise/de/documents/publications/studies/cpv-report-ise-nrel.pdf":1.2,
    "https://onlinelibrary.wiley.com/doi/full/10.1002/aenm.201802521":0.15,
    "https://architecture.mit.edu/sites/architecture.mit.edu/files/attachments/lecture/SolarUpdraftTower_Project.pdf":1.5,
    "https://ore.catapult.org.uk/analysisinsight/an-introduction-to-airborne-wind/":1.3,
    "https://cordis.europa.eu/project/rcn/96067/reporting/en":1.4,
    "https://www.sciencedirect.com/science/article/pii/S1364032116304282":1.3,
    "https://www.q-cells.eu/uploads/tx_abdownloads/files/12_6DO.13.2_Breyer2011_HybPV-FossilPlants_paper_PVSEC_preprint_01.pdf":1.12
}

for i in range(len(distributed_lcoe)):
    s = distributed_lcoe[i]["source"]
    if s in source_currency_converters:
        val = source_currency_converters[s]
        if "lcoe" in distributed_lcoe[i]:
            distributed_lcoe[i]["lcoe"] *= val
        if "lcoe_low" in distributed_lcoe[i]:
            distributed_lcoe[i]["lcoe_low"] *= val
        if "lcoe_high" in distributed_lcoe[i]:
            distributed_lcoe[i]["lcoe_high"] *= val
    if "lcoe" not in distributed_lcoe[i]:
        distributed_lcoe[i]["lcoe"] = "---"
    if "lcoe_low" not in distributed_lcoe[i]:
        distributed_lcoe[i]["lcoe_low"] = "---"
    if "lcoe_high" not in distributed_lcoe[i]:
        distributed_lcoe[i]["lcoe_high"] = "---"

distributed_table = [["<b>Source</b>","<b>LCOE (single value if given)</b>","<b>LCOE (low end of range)</b>","<b>LCOE (high end of range)</b>"]] + [[distributed_lcoe[i]["type"], distributed_lcoe[i]["lcoe"], distributed_lcoe[i]["lcoe_low"], distributed_lcoe[i]["lcoe_high"]] for i in range(len(distributed_lcoe))]
            
helper.save_image({
    "filename":"distributed_lcoe.jpg",
    "status":"Done",
    "details":"Show levelized cost of electricity for various distributed energy options. There are fewer and less reliable numbers than there are for centralized grid options. Actual costs probably vary more because conditions under which microgrid or off-grid power is used are much more heterogenous. A key message is that distributed options are generally more expensive than centralized options, which is why we generally use large power grids. More figures may be added later (I could not find even one good distributed geothermal figure, which I would like to have), but it is a low priority. Model this image after the other LCOE figures as much as reasonable. All LCOE values are cents/kWh.",
    "table":distributed_table,
    "references":["lazard","fraunhofer","diesel_lcoe","mayor","lcoe2015","indonesia_lcoe","microreactor"],
    "source_file":"distributed_electricity.py"
})