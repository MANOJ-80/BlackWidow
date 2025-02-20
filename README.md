# BlackWidow - Like a hawk watching over targets 
 For a fast and powerful scan



## Overview
BlackWidow is an automated reconnaissance tool designed for bug bounty hunters and penetration testers. It streamlines the reconnaissance process by executing various scanning tools in parallel using Python's `asyncio`. 

## Features
- **Automated Subdomain Enumeration** (Subfinder, Amass)
- **Live Host Discovery** (httprobe)
- **Port Scanning** (Nmap, Masscan)
- **Web Technology & WAF Detection** (WhatWeb, WafW00f)
- **Directory Enumeration** (Gobuster, Feroxbuster)
- **Vulnerability Scanning** (SQLMap, Nuclei)
- **Exploitation Scans** (XSStrike, FFUF)
- **Post-Exploitation Analysis** (WaybackURLs, GF Patterns)
- **Asynchronous Execution** for faster scanning
- **Organized Output** stored in structured files

## Installation
### Prerequisites
Make sure you have the following tools installed on your system:
- `subfinder`
- `amass`
- `httprobe`
- `nmap`
- `masscan`
- `whatweb`
- `wafw00f`
- `gobuster`
- `feroxbuster`
- `sqlmap`
- `nuclei`
- `xsstrike`
- `ffuf`
- `waybackurls`
- `gf`

### Clone the Repository
```bash
git clone https://github.com/MANOJ-80/BlackWidow.git
cd BlackWidow
```

### Install Python Dependencies
```bash
pip install -r requirements.txt
```

## Usage
### Running ReconX
```bash
python recon_automation.py -d example.com
```

### Command Line Arguments
| Argument | Description |
|----------|-------------|
| `-d` | Target domain (required) |
| `-o` | Output directory (default: `recon_results/`) |
| `--fast` | Run in fast mode (limited scans) |
| `--full` | Run all recon modules |

## Output Structure
All results are saved in the `recon_results/` directory:
```
recon_results/
  ├── subdomains.txt
  ├── amass_output.txt
  ├── live_hosts.txt
  ├── nmap_scan.txt
  ├── masscan_output.txt
  ├── whatweb_output.txt
  ├── wafw00f_output.txt
  ├── gobuster_output.txt
  ├── feroxbuster_output.txt
  ├── sqlmap_output.txt
  ├── nuclei_output.txt
  ├── xsstrike_output.txt
  ├── ffuf_output.txt
  ├── wayback_output.txt
  ├── xss_output.txt
  ├── sqli_output.txt
```

## Contributing
Feel free to submit issues or pull requests to improve the tool. Contributions are always welcome!

## License
This project is licensed under the MIT License.

## Disclaimer
This tool is for educational and ethical hacking purposes only. The author is not responsible for any misuse or illegal activities conducted with this tool.

