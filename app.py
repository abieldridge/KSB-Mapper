import streamlit as st
import difflib

# Title
st.title("Apprenticeship KSB Matcher")

# Filtered apprenticeship standards
apprenticeship_standards = [
    "L2 Horticulture Operative",
    "L2 Arborist",
    "L2 Landscape Operative"
]


# KSBs for selected standards
ksb_data = {
    "L2 Horticulture Operative": sorted([
        # Behaviours
        "B1: Puts safety first for themselves and others.",
        "B2: Respectful of others including customer care.",
        "B3: Sources solutions and seeks to continuously improve and develop.",
        "B4: Takes pride in and ownership of work.",
        "B5: Team focused and works effectively with colleagues and others.",

        # Knowledge
        "K1: Importance and application of health and safety legislation, codes of practice and policies including risk assessment, manual handling, use and storage of pesticides and hazards associated with horticultural environment",
        "K2: Concepts of good environmental and sustainable good practice, including a basic understanding of how to contribute to government-led sustainability and zero carbon targets",
        "K3: Environmental controls and compliance with regulations including pollution control, waste reduction, management and recycling",
        "K4: Situations where special care should be taken including where heritage, environmental or planning designations may be present. The importance of complying with rules in place to protect the site",
        "K5: Maintenance, operational requirements, pre start checks and legislation for tools, equipment and machinery including operator competence requirements",
        "K6: The importance of maintaining records in a business setting",
        "K7: Techniques for communicating with technical and non-technical audiences and the importance of effective communication in the workplace with colleagues, customers and the public. The value of effective and timely communication in customer care",
        "K8: Methods to identify plants and their limitations including the importance and role of scientific names and terminology",
        "K9: Main introduction routes for plant pests and diseases ",
        "K10: The importance of controlling invasive species including identification features, environmental impacts and legislation and actions that should be taken if present (includes invasive plants, pests and diseases)",
        "K11: Biosecurity and phytosanitary measures and why they are important",
        "K12: Sources of information on plant pests and diseases, their control measures and actions required if listed as notifiable by Government",
        "K13: Plant biology and implications for plant health and growth, including plant structures and their adaptations, lifecycles, germination, photosynthesis, respiration, transpiration and requirements",
        "K14: Impact of environmental conditions on plant growth and how this affects plant care",
        "K15: Soil science including soil formation, characteristics, texture and components, biological processes and their impact on plant growth",
        "K16: Soil management practices, when and why to cultivate and when to use other methods. Techniques to achieve tilth, levelling, aeration, drainage, level, pH, nutrient levels. Implications of site types, end use and finish to include fertilisers, soil amelioration, mulches",
        "K17:  Techniques for clearing sites and controlling weeds including identification and reasons for removal, techniques for control (including chemical) and situations for use",
        "K18:  Impact of pruning on the plant and the importance of placing pruning cuts correctly",
        "K19: Planting techniques for shrubs and trees (using a simple tree pit including support and protection), storage and handling of containerised and bare root plant material and impact of poor storage and planting practice",
        "K20: Techniques and tools for maintaining turf including quality standards",
        "K21: Types of turf, their characteristics and methods for installing",
        "K22: Reasons for maintaining or protecting hard landscape features, maintenance specifications and maintenance techniques including suitability to different situations",
        "K23: Role of business policies, vision and values. Workers’ contribution to earning profit and or awareness of implications of actions on business (for example work rate). How project management informs a team to achieve objectives",
        "K24:  The importance and benefits of green-space and the types of quality standards appropriate to different businesses and horticultural sites",
        "K25: Propagation techniques including environment, preparation and aftercare. Components of growing media, purpose, sustainability implications and formulation",
        "K26: Techniques of establishing ornamental turf and species rich meadows",
        "K27: Purpose, importance and features of turf maintenance activities to achieve quality standards and how they are presented in turf maintenance specifications",
        "K28: Factors influencing plant selection including planting combinations, microclimate, soil, purpose, aesthetics",
        "K29: Techniques for maintaining soft landscapes",
        "K30: Reasons for pruning and pruning techniques including timing and species suitability",
        "K31: Stock types and techniques for planting trees (other than simple tree pits). Techniques for planting herbaceous plants and those for seasonal display",

        # Skills
        "S1: Apply health and safety processes and procedures including risk assessments and or construction design management (CDM), manual handling, legislative requirements and organisational policies. Follow safe systems of work and safety information in line with employer requirements or site context (for example clearing their route before transporting materials).",
        "S2: Apply environmental mitigation measures including storage and disposal of waste, for example sorting materials for recycling or composting, acting in compliance with legal requirements, organisational policies and pollution controls.",
        "S3: Select, undertake a pre start check, set up, clean, store and safely operate tools, equipment and machinery (including pedestrian controlled and handheld) in line with current legislation and business policies.",
        "S4: Communicate with technical (for example supervisors or managers) and non-technical audiences (for example clients or the public) using language appropriate to the audience.",
        "S5: Identify plants commonly grown in the UK by scientific names including genus species and or cultivar",
        "S6: Maintain the correct phytosanitary and bio-security procedures for the site, in accordance with legal requirements",
        "S7:  Identify and report symptoms and or signs of commonly found UK plant pests, pathogens and disorders",
        "S8: Maintain plant health for example providing for basic needs such as water, nutrition (either organic or inorganic), light",
        "S9: Cultivate, improve and preserve soils by mechanical methods and or by hand including amelioration and mulching (these might be imported or natural).",
        "S10: Clear unwanted vegetation, selecting techniques to be used (for example weeding)",
        "S11: Identify plants correctly and understand their requirements",
        "S12: Plant shrubs and a tree using a simple tree pit.",
        "S13: Install turf for situation",
        "S14: Mow turf using pedestrian controlled powered driven mower",
        "S15: Maintain or protect hard surfaces, features or structures for example painting, re-gravelling, removing weeds from paving, drain clearance, cleaning",
        "S16: Use digital tools and techniques for research, collaboration, continuous professional development and resolution of problems",
        "S17: Propagate plants by cuttings and seed sowing (this might be indoors or outdoors). Including selection of suitable growing media and or soil",
        "S18: Provide aftercare to recently installed turf and maintain established turf or species rich meadows including irrigation, maintenance, monitoring health and protection from use",
        "S19: Identify if plants are suitable to site, purpose and aesthetics",
        "S20: Maintain soft landscapes for example - staking or support, division, seasonal clearance, and re-planting.",
        "S21: Monitor and control plant pests, pathogens, and disorders using basic control methods (including application of chemicals or organic equivalents",
        "S22: Plant herbaceous and seasonal planting (for example bedding, herbs or bulbs)"
        "S23: Prune plants to achieve healthy growth and form (including natural habit and formal or trained form)"

    ]),

       "L2 Landscape Operative": sorted([
        # Behaviours
        "B1: Puts safety first for themselves and others.",
        "B2: Respectful of others including customer care.",
        "B3: Sources solutions and seeks to continuously improve and develop.",
        "B4: Takes pride in and ownership of work.",
        "B5: Team focused and works effectively with colleagues and others.",

        # Knowledge
        "K1: Importance and application of health and safety legislation, codes of practice and policies including risk assessment, manual handling, use and storage of pesticides and hazards associated with horticultural environment",
        "K2: Concepts of good environmental and sustainable good practice, including a basic understanding of how to contribute to government-led sustainability and zero carbon targets",
        "K3: Environmental controls and compliance with regulations including pollution control, waste reduction, management and recycling",
        "K4: Situations where special care should be taken including where heritage, environmental or planning designations may be present. The importance of complying with rules in place to protect the site",
        "K5: Maintenance, operational requirements, pre start checks and legislation for tools, equipment and machinery including operator competence requirements",
        "K6: The importance of maintaining records in a business setting",
        "K7: Techniques for communicating with technical and non-technical audiences and the importance of effective communication in the workplace with colleagues, customers and the public. The value of effective and timely communication in customer care",
        "K8: Methods to identify plants and their limitations including the importance and role of scientific names and terminology",
        "K9: Main introduction routes for plant pests and diseases ",
        "K10: The importance of controlling invasive species including identification features, environmental impacts and legislation and actions that should be taken if present (includes invasive plants, pests and diseases)",
        "K11: Biosecurity and phytosanitary measures and why they are important",
        "K12: Sources of information on plant pests and diseases, their control measures and actions required if listed as notifiable by Government",
        "K13: Plant biology and implications for plant health and growth, including plant structures and their adaptations, lifecycles, germination, photosynthesis, respiration, transpiration and requirements",
        "K14: Impact of environmental conditions on plant growth and how this affects plant care",
        "K15: Soil science including soil formation, characteristics, texture and components, biological processes and their impact on plant growth",
        "K16: Soil management practices, when and why to cultivate and when to use other methods. Techniques to achieve tilth, levelling, aeration, drainage, level, pH, nutrient levels. Implications of site types, end use and finish to include fertilisers, soil amelioration, mulches",
        "K17:  Techniques for clearing sites and controlling weeds including identification and reasons for removal, techniques for control (including chemical) and situations for use",
        "K18:  Impact of pruning on the plant and the importance of placing pruning cuts correctly",
        "K19: Planting techniques for shrubs and trees (using a simple tree pit including support and protection), storage and handling of containerised and bare root plant material and impact of poor storage and planting practice",
        "K20: Techniques and tools for maintaining turf including quality standards",
        "K21: Types of turf, their characteristics and methods for installing",
        "K22: Reasons for maintaining or protecting hard landscape features, maintenance specifications and maintenance techniques including suitability to different situations",
        "K23: Role of business policies, vision and values. Workers’ contribution to earning profit and or awareness of implications of actions on business (for example work rate). How project management informs a team to achieve objectives",
        "K24:  The importance and benefits of green-space and the types of quality standards appropriate to different businesses and horticultural sites",
        "K32: Importance of identification of services, utilities and site hazards. Techniques and tools for measuring and setting out sites for landscape construction. The principles in defining site levels using manual or electrical equipment",
        "K33: Safety and practical considerations when using abrasive wheels",
        "K34: Landscaping materials, their application, uses, maintenance implications, environmental impact, benefits and disadvantages",
        "K35: Indicators that constructed structures require repair and techniques for correcting common problems. Importance of repairs for longevity and aesthetics",
        "K36:  Techniques for paving, including setting levels, sub bases, laying bases, finishing",
        "K37: Techniques for constructing vertical landscape features including foundations, fences, brick laying and walls.",
        "K38: Purpose of drainage systems including installation",
        "K39: Techniques for constructing horizontal landscape features (excluding paving)",

        # Skills
        "S1: Apply health and safety processes and procedures including risk assessments and or construction design management (CDM), manual handling, legislative requirements and organisational policies. Follow safe systems of work and safety information in line with employer requirements or site context (for example clearing their route before transporting materials).",
        "S2: Apply environmental mitigation measures including storage and disposal of waste, for example sorting materials for recycling or composting, acting in compliance with legal requirements, organisational policies and pollution controls.",
        "S3: Select, undertake a pre start check, set up, clean, store and safely operate tools, equipment and machinery (including pedestrian controlled and handheld) in line with current legislation and business policies.",
        "S4: Communicate with technical (for example supervisors or managers) and non-technical audiences (for example clients or the public) using language appropriate to the audience.",
        "S5: Identify plants commonly grown in the UK by scientific names including genus species and or cultivar",
        "S6: Maintain the correct phytosanitary and bio-security procedures for the site, in accordance with legal requirements",
        "S7:  Identify and report symptoms and or signs of commonly found UK plant pests, pathogens and disorders",
        "S8: Maintain plant health for example providing for basic needs such as water, nutrition (either organic or inorganic), light",
        "S9: Cultivate, improve and preserve soils by mechanical methods and or by hand including amelioration and mulching (these might be imported or natural).",
        "S10: Clear unwanted vegetation, selecting techniques to be used (for example weeding)",
        "S11: Identify plants correctly and understand their requirements",
        "S12: Plant shrubs and a tree using a simple tree pit.",
        "S13: Install turf for situation",
        "S14: Mow turf using pedestrian controlled powered driven mower",
        "S15: Maintain or protect hard surfaces, features or structures for example painting, re-gravelling, removing weeds from paving, drain clearance, cleaning",
        "S16: Use digital tools and techniques for research, collaboration, continuous professional development and resolution of problems",
        "S24: Measure and set out an uncomplicated site in preparation for landscape construction activities",
        "S25: Use free hand cutting and or bench cutting of hard landscape materials using abrasive wheels",
        "S26: Repair constructed landscape features (simple and noncomplex) for example re-grouting, re-sanding, damaged fencing",
        "S27: Construct paved feature for example path, patio or shed base. Including setting levels, sub bases, laying bases, finishing",
        "S28: Construct vertical landscape features including fences, ornamental vertical features, and walls",
        "S29: Install drainage in landscaping ",
        "S30: Construct horizontal landscape features(excluding paving)"

    ]),
    
       "L2 Arborist": sorted([
        # Behaviours
        "B1: Has a safety mind-set to protect self, colleagues, and others",
        "B2: Works effectively within a team/crew",
        "B3: Presents a professional manner in appearance, language, and behaviour",
        "B4: Takes responsibility for completing their tasks to show they can be relied upon ",
        "B5: Ensures they are mindful of environmental and sustainability factors at all times whilst carrying out their work",

        # Knowledge
        "K1: Arb equipment and their use and maintenance requirements ",
        "K2: PPE requirements for arboricultural operations",
        "K3: Principles and understanding of Health and safety legislation (Health & Safety at Work Act), standards (BS3998), and codes of practice (ICOP) in relation to arboricultural works",
        "K4: Practicalities of onsite risk assessments, with knowledge of putting in place control measures to maintain a safe working site ",
        "K5: How to carry out processing of tree work arisings ",
        "K6: Understanding of the use of MEWPS within the arboricultural sector",
        "K7: Key principles of electrical safety for working near power line(s), including how to read and adhere to risk assessments ",
        "K8: Principles and understanding of current codes of practice including environmental and wildlife legislation in relation to arboricultural works. ",
        "K9: Principles and understanding of legislation relating to trees including Tree Preservation Orders and Conservation Areas including the Town and Country Planning Act 1990",
        "K10: The procedures and specific instructions for dealing with incidents and emergencies, for example, aerial rescues",
        "K11: The principles of tree planting and establishment ",
        "K12: How to identify trees and the value of using their common names",
        "K13: The risks and impacts of tree decay fungi ",
        "K14: The principles and techniques of formative pruning for young trees",
        "K15: Principles and techniques of target pruning for mature trees ",
        "K16: Procedures for setting out workplace signage (highway & non highway) and assist with traffic control ",
        "K17: How to identify and manage pests, diseases, and disorders of trees",
        "K18: The benefits of trees for people, air quality, nature, the environment, ecosystem services ",
        "K19: - Different communication techniques to use, for example, tone of voice, listening, etc ",

        # Skills
        "S1: Recognise health and safety needs onsite and work safely",
        "S2: Complete site-specific risk assessments and emergency action plans ",
        "S3: Select appropriate equipment for tree work operations ",
        "S4: Set out workplace signage (highway & non highway) and assists with traffic control ",
        "S5: Process tree work arisings using appropriate machinery ",
        "S6: Maintain and take appropriate care of tools, equipment and other onsite factors (such as customer or public buildings etc.) ",
        "S7: Recognise a variety of tree species using common names ",
        "S8: Carry out a range of formative pruning operations ",
        "S9: Carry out branch removal up to 200mm diameter with hand tools (target pruning for final cut)",
        "S10: Fell and process small trees up to 380mm diameter ",
        "S11: Support aerial tree workers with transfer of equipment for aerial tree work operations ",
        "S12: Perform an aerial rescue of colleague from a rope and harness ",
        "S13: Work safely at height in the tree under supervision ",
        "S14: Communicate technical information about arboricultural operations to fellow team members, clients and other stakeholders as required ",
 ])
}

# UI elements
selected_standard = st.selectbox("Select your apprenticeship standard:", apprenticeship_standards)
reflection = st.text_area("Describe what you learned:")

# Matching function
def match_ksbs(reflection, ksb_list):
    matches = []
    for ksb in ksb_list:
        ksb_text = ksb.split(": ", 1)[1]
        similarity = difflib.SequenceMatcher(None, reflection.lower(), ksb_text.lower()).ratio()
        if similarity > 0.2:
            matches.append((ksb, similarity))
    matches.sort(key=lambda x: x[1], reverse=True)
    return [m[0] for m in matches[:5]] if matches else ["No relevant KSBs found."]

# Button to trigger matching
if st.button("Find Relevant KSBs"):
    if reflection.strip():
        ksb_list = ksb_data.get(selected_standard, [])
        matched_ksbs = match_ksbs(reflection, ksb_list)
        st.subheader("Suggested KSBs:")
        for ksb in matched_ksbs:
            st.write(f"- {ksb}")
    else:
        st.warning("Please enter a reflection to get KSB suggestions.")
