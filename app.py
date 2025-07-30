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
        "B1: Work safely and effectively, maintaining a safe working environment.",
        "B2: Take ownership of work and follow through to completion.",
        "B3: Demonstrate a positive and respectful attitude.",
        "B4: Show initiative and be proactive when solving problems.",
        "B5: Work collaboratively with others and adapt to change.",

        # Knowledge
        "K1: Health and Safety, Legislation, Codes of Practice and Policies, Risk Assessments",
        "K2: Environmental and sustainable good practice – including government sustainability and zero carbon targets",
        "K3: Environmental controls and compliance with regulations",
        "K4: Situations where special care should be taken and the importance of complying with rules (e.g. heritage, environmental or planning designations)",
        "K5: Maintenance for tools, equipment and machinery",
        "K6: Maintaining records in business setting",
        "K7: Effective and timely communication in the workplace",
        "K8: Identifying plants and their limitations",
        "K9: Plant pests and diseases ",
        "K10: Invasive Species – Importance of controlling them, impacts and legislation and actions to be taken",
        "K11: Biosecurity and phytosanitary measures",
        "K12: Plant pests and diseases – control measures and actions if notable by government",
        "K13: Plant biology and implications for plant health and growth",
        "K14: Environmental conditions on plant growth and how it affects plant care",
        "K15: Soil Science",
        "K16: Soil management practices, when and why to cultivate and methods to use",
        "K17: Clearing sites and controlling weeds – removal and control",
        "K18: Pruning",
        "K19: Planting for shrubs and trees and planting practice",
        "K20: Maintaining turf",
        "K21: Types of turf – characteristics and installation methods",
        "K22: Maintaining or protecting hard landscape features",
        "K23: Business policies, vision and values – workers' contributions and implications of actions on business",
        "K24: Importance and benefits of green space and the types of quality standards",
        "K25: Propagation techniques – Environment preparation and aftercare",
        "K26: Techniques of establishing ornamental turf and species-rich meadows",
        "K27: Turf Maintenance activities – purpose, importance and features",
        "K28: Plant Selection – combinations, microclimate, soil, purpose, etc.",
        "K29: Maintaining soft landscapes",
        "K30: Reasons for pruning and pruning techniques – timing and species suitability",
        "K31: Stock types and techniques for planting trees – planting herbaceous plants and seasonal displays",

        # Skills
        "S1: Work safely and adhere to relevant safety, environmental, and biosecurity legislation and guidelines",
        "S2: Communicate effectively with colleagues, clients, and the public",
        "S3: Interpret and follow verbal and written work instructions from supervisors and colleagues",
        "S4: Carry out risk assessments and implement control measures",
        "S5: Select, use, maintain, and store tools, equipment, and machinery safely and correctly",
        "S6: Use powered tools and pedestrian controlled equipment",
        "S7: Use and maintain ride-on equipment",
        "S8: Use appropriate personal protective equipment (PPE)",
        "S9: Carry out basic servicing and maintenance of tools and equipment",
        "S10: Maintain work records and report issues",
        "S11: Identify plants correctly and understand their requirements",
        "S12: Recognise and report plant health problems",
        "S13: Apply basic plant protection measures",
        "S14: Carry out planting and establishment of plants",
        "S15: Carry out pruning and training of plants",
        "S16: Carry out turf maintenance operations",
        "S17: Carry out soil cultivation and improvement",
        "S18: Carry out basic landscape maintenance",
        "S19: Carry out propagation techniques",
        "S20: Work effectively both individually and as part of a team",
        "S21: Follow business procedures and policies",
        "S22: Demonstrate environmental awareness in all work practices"

    ]),

       "L2 Landscape Operative": sorted([
        # Behaviours
        "B1: Work safely and effectively, maintaining a safe working environment.",
        "B2: Take ownership of work and follow through to completion.",
        "B3: Demonstrate a positive and respectful attitude.",
        "B4: Show initiative and be proactive when solving problems.",
        "B5: Work collaboratively with others and adapt to change.",

        # Knowledge
        "K1: Health and Safety, Legislation, Codes of Practice and Policies, Risk Assessments",
        "K2: Environmental and sustainable good practice – including government sustainability and zero carbon targets",
        "K3: Environmental controls and compliance with regulations",
        "K4: Situations where special care should be taken and the importance of complying with rules (e.g. heritage, environmental or planning designations)",
        "K5: Maintenance for tools, equipment and machinery",
        "K6: Maintaining records in business setting",
        "K7: Effective and timely communication in the workplace",
        "K8: Identifying plants and their limitations",
        "K9: Plant pests and diseases",
        "K10: Invasive Species – Importance of controlling them, impacts and legislation and actions to be taken",
        "K11: Biosecurity and phytosanitary measures",
        "K12: Plant pests and diseases – control measures and actions if notable by government",
        "K13: Plant biology and implications for plant health and growth",
        "K14: Environmental conditions on plant growth and how it affects plant care",
        "K15: Soil Science",
        "K16: Soil management practices, when & why to cultivate and methods to use",
        "K17: Clearing sites and controlling weeds – removal and control",
        "K18: Pruning",
        "K19: Planting for shrubs and trees and planting practice",
        "K20: Maintaining turf",
        "K21: Types of turf – characteristics and installation methods",
        "K22: Maintaining or protecting hard landscape features",
        "K23: Business policies, vision and values – workers' contributions and implications of actions on business",
        "K24: Importance and benefits of green space and the types of quality standards",
        "K32: Identifying pipework and cables above or below ground and any other potential hazards ",
        "K33: Safety and practical considerations when using abrasive wheels",
        "K34: Landscaping materials - application, uses, maintenance implications, environmental impact, benefits and disadvantages",
        "K35: Indicators that structures require repair and techniques for correcting common problems and the importance",
        "K36: Techniques for paving - setting levels, sub bases, laying bases, finishing",
        "K37: Techniques for constructing vertical landscape features including foundations, fences, brick laying and walls.",
        "K38: Purpose of drainage systems including installation",
        "K39: Techniques for constructing horizontal landscape features (excluding paving)",

        # Skills
        "S1: Work safely and adhere to relevant safety, environmental, and biosecurity legislation and guidelines",
        "S2: Communicate effectively with colleagues, clients, and the public",
        "S3: Interpret and follow verbal and written work instructions from supervisors and colleagues",
        "S4: Carry out risk assessments and implement control measures",
        "S5: Select, use, maintain, and store tools, equipment, and machinery safely and correctly",
        "S6: Use powered tools and pedestrian controlled equipment",
        "S7: Use and maintain ride-on equipment",
        "S8: Use appropriate personal protective equipment (PPE)",
        "S9: Carry out basic servicing and maintenance of tools and equipment",
        "S10: Maintain work records and report issues",
        "S11: Identify plants correctly and understand their requirements",
        "S12: Recognise and report plant health problems",
        "S13: Apply basic plant protection measures",
        "S14: Carry out planting and establishment of plants",
        "S15: Carry out pruning and training of plants",
        "S24: Setting out using string lines and levels",
        "S25: - Abrasive wheels – hand cutting or bench cutting",
        "S26: Repair constructed landscape features (simple and noncomplex)",
        "S27: Construct paved feature",
        "S28: Construct vertical landscape features ",
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
        "K3: Health and safety, standards and codes of practice",
        "K4: Risk assessments ",
        "K5: How to carry out processing of tree work arisings ",
        "K6: Understanding of the use of MEWPS",
        "K7: Key principles of electrical safety, including risk assessments ",
        "K8: Current codes of practice including environmental and wildlife legislation in relation to arboriculture ",
        "K9: Principles and understanding of legislation relating to trees including Tree Preservation Orders and Conservation Areas",
        "K10: The procedures and specific instructions for dealing with incidents and emergencies",
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
