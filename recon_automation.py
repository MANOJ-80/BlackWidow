import asyncio
import os

domain = "example.com"  # Change this to your target domain
output_dir = "recon_results"
os.makedirs(output_dir, exist_ok=True)

def output_file(name):
    return os.path.join(output_dir, name)

commands = {
    "subfinder": f"subfinder -d {domain} -o {output_file('subdomains.txt')}",
    "amass": f"amass enum -d {domain} -o {output_file('amass_output.txt')}",
    "httprobe": f"cat {output_file('subdomains.txt')} | httprobe > {output_file('live_hosts.txt')}",
    "nmap": f"nmap -p- -T4 -A -v {domain} -oN {output_file('nmap_scan.txt')}",
    "masscan": f"masscan -p1-65535,U:1-65535 --rate=1000 -oL {output_file('masscan_output.txt')} --output-format text {domain}",
    "whatweb": f"whatweb {domain} > {output_file('whatweb_output.txt')}",
    "wafw00f": f"wafw00f {domain} > {output_file('wafw00f_output.txt')}",
    "gobuster": f"gobuster dir -u http://{domain} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o {output_file('gobuster_output.txt')}",
    "feroxbuster": f"feroxbuster -u http://{domain} -o {output_file('feroxbuster_output.txt')}",
    "sqlmap": f"sqlmap -u http://{domain}/index.php?id=1 --batch --dbs --output={output_file('sqlmap_output.txt')}",
    "nuclei": f"nuclei -target {domain} -o {output_file('nuclei_output.txt')}",
    "xsstrike": f"xsstrike -u http://{domain} > {output_file('xsstrike_output.txt')}",
    "ffuf": f"ffuf -u http://{domain}/FUZZ -w /usr/share/wordlists/rockyou.txt -o {output_file('ffuf_output.txt')}",
    "waybackurls": f"waybackurls {domain} > {output_file('wayback_output.txt')}",
    "gf_xss": f"gf xss {output_file('wayback_output.txt')} > {output_file('xss_output.txt')}",
    "gf_sqli": f"gf sqli {output_file('wayback_output.txt')} > {output_file('sqli_output.txt')}"
}

async def run_command(name, command):
    print(f"[+] Running {name}...")
    process = await asyncio.create_subprocess_shell(command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    if stdout:
        print(f"[OUTPUT {name}]:\n{stdout.decode()}")
    if stderr:
        print(f"[ERROR {name}]:\n{stderr.decode()}")

async def main():
    tasks = [run_command(name, cmd) for name, cmd in commands.items()]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())
