
import streamlit as st
import yfinance as yf
import pandas as pd
import io

# -----------------------------
# Config
st.set_page_config(page_title="ASX Emerging Companies Stock Data Downloader", layout="wide", page_icon="📈")
st.title("📈 Combined Stock Data - Closing Price, MA20 & MA50 (Last 180 Days)")

# -----------------------------
# ASX Ticker List (from your screenshot)
tickers = [
     "IFT",	 "REH",	 "JBH",	 "QUB",	 "NXT",	 "TNE",	 "RHC",	 "CEN",	 "HVN",	 "APE",	 "SEK",	 "MCY",	 "TPG",	 "CDA",
     "ALX",	 "360",	 "EDV",	 "WOR",	 "AZJ",	 "BEN",	 "A2M",	 "AGL",	 "SDF",	 "CWY",	 "DOW",	 "ANN",	 "VNT",	 "BRG",
     "BOQ",	 "EBO",	 "TWE",	 "BFL",	 "AUB",	 "TUA",	 "TLX",	 "MTS",	 "SPK",	 "CNU",	 "FBU",	 "LOV",	 "MSB",	 "FLT",
     "SUL",	 "DRO",	 "NHF",	 "ASB",	 "MND",	 "RWC",	 "RYM",	 "NWH",	 "VGN",	 "DBI",	 "SNZ",	 "GNE",	 "GYG",	 "DMP",
     "FRW",	 "GDG",	 "NCK",	 "SLX",	 "ARB",	 "NEU",	 "PMV",	 "MP1",	 "TAH",	 "JDO",	 "EVT",	 "REG",	 "MGH",	 "4DX",
     "SRG",	 "BGA",	 "CBO",	 "DDR",	 "MAQ",	 "EOS",	 "NEC",	 "WEB",	 "SNL",	 "IEL",	 "RDX",	 "MAD",	 "GNC",	 "AIZ",
     "ELD",	 "IRE",	 "DTL",	 "OCL",	 "TPW",	 "SDR",	 "GNP",	 "SSM",	 "ABB",	 "CKF",	 "BGP",	 "SLC",	 "MMS",	 "WBT",
     "CU6",	 "NAN",	 "SIQ",	 "AOV",	 "TEA",	 "RUL",	 "SGLLV",  "ELS",	 "CAT",	 "SGR",	 "KLS",	 "HSN",	 "HGH",	 "IPH",
     "IDX",	 "PWH",	 "PYC",	 "BVS",	 "C79",	 "ING",	 "RIC",	 "SKC",	 "AVR",	 "CVL",	 "AAC",	 "ASG",	 "FCL",	 "MYR",
     "SYL",	 "MYS",	 "GTK",	 "BAP",	 "PNV",	 "GWA",	 "OML",	 "PFP",	 "EHL",	 "SXE",	 "SHV",	 "TRA",	 "JIN",	 "IMR",
     "HLS",	 "IMM",	 "UNI",	 "LYL",	 "NXL",	 "AYA",	 "BLX",	 "TWR",	 "DUR",	 "CUV",	 "AX1",	 "SHA",	 "OCA",	 "GEM",
     "SPZ",	 "ACL",	 "EOL",	 "THL",	 "KSC",	 "IPG",	 "IGL",	 "QOR",	 "EBR",	 "MPW",	 "AIH",	 "RAC",	 "LGI",	 "VGL",
     "SKS",	 "SKT",	 "PPS",	 "APX",	 "MYG",	 "KGN",	 "AMA",	 "AD8",	 "KSL",	 "PGC",	 "CGS",	 "BRN",	 "AGI",	 "AGIE",
     "NVX",	 "CVW",	 "ACF",	 "KPG",	 "SST",	 "RDY",	 "HLO",	 "AFP",	 "EIQ",	 "3DA",	 "SKO",	 "ADH",	 "XRF",	 "WJL",
     "SM1",	 "PBH",	 "BBN",	 "PWR",	 "DXB",	 "WRK",	 "SXL",	 "SLD",	 "IMB",	 "SFC",	 "MVF",	 "CMA",	 "ONE",	 "FWD",
     "ACE",	 "BBT",	 "DUG",	 "ATA",	 "RIV",	 "LAU",	 "OCC",	 "ARX",	 "MYX",	 "SGI",	 "BET",	 "BOT",	 "CTT",	 "MTO",
     "CEH",	 "NYR",	 "TTX",	 "SSG",	 "ERD",	 "CUP",	 "AVH",	 "EPI",	 "CLX",	 "NZM",	 "LDX",	 "AQZ",	 "KOV",	 "PEB",
     "WAT",	 "RCT",	 "RCE",	 "SEA",	 "IKE",	 "3PL",	 "SPL",	 "ANG",	 "EMV",	 "ALC",	 "AHX",	 "KMD",	 "BBL",	 "MHJ",
     "JYC",	 "DAI",	 "EWC",	 "IFN",	 "SOM",	 "ART",	 "ACW",	 "HPG",	 "AAL",	 "AHC",	 "CYC",	 "PAR",	 "VLS",	 "SND",
     "VVA",	 "AIM",	 "NOL",	 "FDV",	 "MCA",	 "CCR",	 "BWN",	 "BUB",	 "YOJ",	 "EVO",	 "ECL",	 "NDO",	 "BB1",	 "MXI",
     "PLY",	 "A1N",	 "SHJ",	 "VNL",	 "GLB",	 "AV1",	 "SDI",	 "VFY",	 "HNG",	 "EDU",	 "ALA",	 "TWD",	 "M7T",	 "NZK",
     "AL3",	 "ABY",	 "FLC",	 "BIO",	 "COV",	 "ARA",	 "ILA",	 "ITS",	 "LIS",	 "ATG",	 "IMU",	 "LTP",	 "FLN",	 "TRJ",
     "KYP",	 "AXE",	 "IOD",	 "OIL",	 "PIQ",	 "BPG",	 "RFG",	 "EXP",	 "ROC",	 "VEE",	 "EGL",	 "BXN",	 "NVU",	 "DBF",
     "ATH",	 "SKK",	 "EZZ",	 "CMP",	 "PHX",	 "ATP",	 "COS",	 "RAD",	 "AHL",	 "PTX",	 "PPE",	 "CYP",	 "ESK",	 "SHG",
     "SEG",	 "HIT",	 "LBL",	 "CYG",	 "JAN",	 "VR1",	 "VBC",	 "TPC",	 "ATX",	 "LRK",	 "FFI",	 "RKN",	 "BOL",	 "SMN",
     "SHO",	 "STP",	 "CC5",	 "SPG",	 "MX1",	 "RNT",	 "IRI",	 "PPL",	 "DCC",	 "EGG",	 "ECT",	 "BMT",	 "MAP",	 "NUZ",
     "SHM",	 "ABV",	 "PCK",	 "SIX",	 "NXD",	 "RHY",	 "UBN",	 "GTN",	 "MVP",	 "DSK",	 "SNT",	 "FRM",	 "CTE",	 "CSX",
     "WWG",	 "DOC",	 "IIQ",	 "AR9",	 "ENP",	 "SWP",	 "DUB",	 "RWL",	 "EYE",	 "SIO",	 "EMD",	 "AI1",	 "ADO",	 "CCX",
     "HMD",	 "NSB",	 "IPD",	 "AMS",	 "BDX",	 "NXN",	 "AQN",	 "FLX",	 "RTH",	 "DVL",	 "CPV",	 "SNS",	 "MPP",	 "3DP",
     "CVB",	 "MBH",	 "VRS",	 "1AI",	 "GTI",	 "NTD",	 "FTI",	 "KPO",	 "RKT",	 "VIT",	 "MFD",	 "GSS",	 "VHL",	 "CHL",
     "GUM",	 "KLV",	 "AVE",	 "LGP",	 "CCG",	 "5GN",	 "FRX",	 "ASH",	 "AGN",	 "DEM",	 "SEN",	 "BLG",	 "CNQ",	 "TCO",
     "BBC",	 "NOU",	 "ASV",	 "XRG",	 "RMY",	 "S66",	 "KME",	 "EVZ",	 "AVG",	 "HCT",	 "AT1",	 "MCP",	 "ZGL",	 "XF1",
     "CCE",	 "MOV",	 "OLL",	 "VMT",	 "CQT",	 "TAL",	 "FBR",	 "VPR",	 "HCL",	 "STG",	 "DTZ",	 "GAP",	 "W2V",	 "A3D",
     "AMX",	 "CBL",	 "NC6",	 "CLU",	 "ASP",	 "OEC",	 "TRI",	 "ATV",	 "NOX",	 "DEL",	 "ICE",	 "IDT",	 "IME",	 "STH",
     "EPX",	 "AHF",	 "RHT",	 "CXZ",	 "NUC",	 "AAP",	 "HTG",	 "EAX",	 "NTI",	 "EXT",	 "AVA",	 "LPE",	 "IS3",	 "PKP",
     "NOV",	 "TRP",	 "CLG",	 "4DS",	 "PAB",	 "EMB",	 "ICR",	 "RNV",	 "JCS",	 "JAT",	 "TNY",	 "AKG",	 "BPP",	 "JNS",
     "AFL",	 "OVT",	 "MXO",	 "ADR",	 "FRE",	 "CCO",	 "DTI",	 "CYB",	 "SKN",	 "FOS",	 "OSL",	 "RPM",	 "IG6",	 "MEM",
     "CAN",	 "5GG",	 "ODA",	 "AHE",	 "DWG",	 "RCL",	 "AJL",	 "FMR",	 "CMB",	 "BCC",	 "AUA",	 "AMO",	 "SP8",	 "CF1",
     "1CG",	 "AEI",	 "IVG",	 "CML",	 "TR8",	 "1AD",	 "IGN",	 "AD1",	 "EPN",	 "SP3",	 "TZL",	 "STV",	 "IBX",	 "ENL",
     "IMC",	 "TRU",	 "WOA",	 "CHM",	 "BSA",	 "SPX",	 "14D",	 "UNT",	 "PET",	 "FCT",	 "PFT",	 "SPA",	 "SOP",	 "DXN",
     "AVD",	 "WNX",	 "EGY",	 "SFG",	 "T3D",	 "ECS",	 "BEO",	 "RLG",	 "X2M",	 "VFX",	 "HIQ",	 "IXC",	 "REM",	 "MNC",
     "PER",	 "GLE",	 "CDE",	 "PRO",	 "BIT",	 "HMI",	 "IVX",	 "NVQ",	 "AER",	 "ZLD",	 "AUK",	 "SIS",	 "OMG",	 "SOC",
     "VBS",	 "NOR",	 "WHK",	 "PTL",	 "PKY",	 "IFG",	 "XGL",	 "8CO",	 "NGS",	 "XPN",	 "ACR",	 "IRX",	 "ADS",	 "H2G",
     "PKD",	 "RFT",	 "OSX",	 "KNO",	 "ZMM",	 "HYD",	 "OLI",	 "DDT",	 "GLH",	 "RGT",	 "EXL",	 "ANR",	 "SRH",	 "ERG",
     "HT8",	 "HFY",	 "TML",	 "BP8",	 "LVE",	 "AN1",	 "CGO",	 "PFM",	 "BGE",	 "CT1",	 "TD1",	 "OLH",	 "OAK",	 "CTQ",
     "HPC",	 "TFL",	 "CYQ",	 "MSG",	 "BMH",	 "1TT",	 "MSI",

]

# Add ".AX" to each ticker for Yahoo Finance
tickers = [ticker + ".AX" for ticker in tickers]

# Combined DataFrame
all_data = []

# -----------------------------
# Fetch and process data
with st.spinner("Fetching data, please wait..."):
    for ticker in tickers:
        try:
            data = yf.download(ticker, period="180d", progress=False)
            if data.empty or 'Close' not in data.columns:
                continue
            
            # Create a new DataFrame with just the 'Close' column
            data_cleaned = pd.DataFrame()
            data_cleaned['Close'] = data['Close']
            data_cleaned['MA20'] = data_cleaned['Close'].rolling(window=20).mean()
            data_cleaned['MA50'] = data_cleaned['Close'].rolling(window=50).mean()
            data_cleaned['Ticker'] = ticker.replace(".AX", "")
            data_cleaned.reset_index(inplace=True)
            all_data.append(data_cleaned)

        except Exception as e:
            st.warning(f"Failed to fetch data for {ticker}: {e}")

# Combine all into one CSV
if all_data:
    combined_df = pd.concat(all_data, ignore_index=True)
    csv_buffer = io.StringIO()
    combined_df.to_csv(csv_buffer, index=False)
    st.download_button(
        label="📥 Download Combined CSV for All Stocks",
        data=csv_buffer.getvalue(),
        file_name="combined_asx_data.csv",
        mime="text/csv"
    )
else:
    st.error("No data was fetched. Please try again later or check ticker symbols.")





