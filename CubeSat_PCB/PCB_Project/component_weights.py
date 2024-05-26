# Creating a dictionary to store the weights of each component
# Note: Weights are assumed based on typical component weights if specific data is unavailable
component_weights = {
    "04024D105KAT2A": 0.0001,
    "CL05B104KP5VPNC": 0.00001,
    "CRCW040291K0JNED": 0.000008,
    "CRCW0402511KFKED": 0.000008,
    "GRM155R60G106ME01D": 0.00001,
    "C0402C103K4REC7867": 0.000005,
    "GRM155R6YA225KE11D": 0.00001,
    "GRM185C80J475ME11D": 0.000015,
    "C0603C160K3GAC7867": 0.000005,
    "CGA3E2C0G1H050C080AD": 0.000008,
    "LQM2MPN1R0NG0L": 0.00003,
    "BLM15PE300SH1D": 0.00001,
    "RP73PF1E10KBTD": 0.00001,
    "CRCW02014K70FKED": 0.000005,
    "1909763-1": 0.001,
    "C0402C470J4GAC7867": 0.000005,
    "AMK212BBJ476MD-T": 0.00002,
    "AISC-0603F-4R7J-T": 0.00003,
    "GRM158R61A226ME15D": 0.000015,
    "201701-MC01": 0.002,
    "ABLS-25.000MHZ-K4F-T": 0.0015,
    "B520C-13-F": 0.0002,
    "S2B-PH-SM4-TB": 0.001,
    "SR0402JR-7W10RP": 0.000005,
    "NPPN061BFLD-RC": 0.0003,
    "NPPN101BFCN-RC": 0.0003,
    "581-M09-213L462": 0.0015,
    "B4B-PH-SM4-TB": 0.0008,
    "DM3CS-SF": 0.0005,
    "NEO-M9N-00B": 0.002,
    "TPS631000DRLR": 0.0003,
    "430182043816": 0.001,
    "BME280": 0.0003,
    "BQ27427YZFR": 0.0003,
    "LSM9DS1TR": 0.0003,
    "STM32F411CEU6": 0.002,
    "TCA9406DCUR": 0.0003,
    "TPS62745DSSR": 0.0003
}

# Calculating the total weight
total_weight = sum(component_weights.values())
print(total_weight)

# Updated quantities for each component
component_quantities = {
    "04024D105KAT2A": 5,
    "CL05B104KP5VPNC": 12,
    "CRCW040291K0JNED": 1,
    "CRCW0402511KFKED": 1,
    "GRM155R60G106ME01D": 4,
    "C0402C103K4REC7867": 1,
    "GRM155R6YA225KE11D": 1,
    "GRM185C80J475ME11D": 2,
    "C0603C160K3GAC7867": 2,
    "CGA3E2C0G1H050C080AD": 2,
    "LQM2MPN1R0NG0L": 1,
    "BLM15PE300SH1D": 1,
    "RP73PF1E10KBTD": 9,
    "CRCW02014K70FKED": 2,
    "1909763-1": 1,
    "C0402C470J4GAC7867": 2,
    "AMK212BBJ476MD-T": 1,
    "AISC-0603F-4R7J-T": 1,
    "GRM158R61A226ME15D": 1,
    "201701-MC01": 1,
    "ABLS-25.000MHZ-K4F-T": 1,
    "B520C-13-F": 1,
    "S2B-PH-SM4-TB": 1,
    "SR0402JR-7W10RP": 1,
    "NPPN061BFLD-RC": 1,
    "NPPN101BFCN-RC": 2,
    "581-M09-213L462": 1,
    "B4B-PH-SM4-TB": 3,
    "DM3CS-SF": 1,
    "NEO-M9N-00B": 1,
    "TPS631000DRLR": 1,
    "430182043816": 1,
    "BME280": 1,
    "BQ27427YZFR": 1,
    "LSM9DS1TR": 1,
    "STM32F411CEU6": 1,
    "TCA9406DCUR": 1,
    "TPS62745DSSR": 1
}

# Calculating the total weight based on quantities
total_weight_with_quantities = sum(component_quantities[part] * component_weights[part] for part in component_quantities)
print("Total Component weight {:.1f} grams".format(total_weight_with_quantities*1000))
