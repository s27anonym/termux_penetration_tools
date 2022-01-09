import time
import os

os.system("apt-get install git")
os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Termux_Framework")

print("""
Aracımız termux için geliştirilmiştir Sızma testlerinde kullanılan 30 önemli aracı bir araya toplayıp termux kullnıcılarının hizmetine veriyoruz 

Exodia

""")



print("\033[93m 1.Nmap")
print("2.MetaSploit")
print("3.xerxes")
print("4.Sqlmap")
print("5.Zaafiyet.Analizi")
print("6.Exploit_Search")
print("7.Port_Tarama")
print("8.WpScan")
print("9.armitage")
print("10.recon-ng")
print("11.skipfish")
print("12.uniscan-gui")
print("13.WAPITI")
print("14.RAPIDSCAN")
print("15.WAES")
print("16.wireshark")
print("17.websploit")
print("18.hashcat")
print("19.Sn1per")
print("20.Yuki-Chan-The-Auto-Pentest")
print("21.TheHarvester")
print("22.maltego")
print("23.medusa")
print("24.w3af")
print("25.sqlninja")
print("26.beef-xss")
print("27.Ettercap")
print("28.vega")
print("29.CMSScan")
print("30.setoolkit")

pn = input("seç krdş birini: ")


if pn == "1":
    os.system("git clone https://github.com/nmap/nmap.git")

if pn == "2":
    os.system("apt update && apt install wget ncurses-utils -y;wget -O metasploit.sh https://raw.githubusercontent.com/remo7777/Termux-Metasploit/master/metasploit-installer.sh;bash metasploit.sh;")

if pn == "3":
    os.system("git clone https://github.com/zanyarjamal/xerxes")

if pn == "4":
    os.system("git clone https://github.com/sqlmapproject/sqlmap.git")

if pn == "5":
    os.system("https://github.com/s27anonym/zaafiyet.analizi.git")

if pn == "6":
    os.system("git clone https://github.com/s27anonym/Exploit_Search.git")

if pn == "7":
    os.system("git clone https://github.com/s27anonym/port_tarama.git")

if pn == "8":
    os.system("git clone https://github.com/wpscanteam/wpscan.git")

if pn == "9":
    os.system("git clone https://github.com/rsmudge/armitage.git")

if pn == "10":
    os.system("git clone https://github.com/lanmaster53/recon-ng.git")

if pn == "11":
    os.system("apt-get install skipfish")

if pn == "12":
    os.system("git clone https://github.com/poerschke/Uniscan.git")

if pn == "13":
    os.system("git clone https://github.com/pcdunyasitv/WAPITI.git")

if pn == "14":
    os.system("git clone https://github.com/pcdunyasitv/RAPIDSCAN.git")

if pn == "15":
    os.system("git clone https://github.com/Shiva108/WAES.git")

if pn == "16":
    os.system("git clone https://github.com/wireshark/wireshark.git")

if pn == "17":
    os.system("git clone https://github.com/websploit/websploit.git")

if pn == "18":
    os.system("git clone https://github.com/hashcat/hashcat.git")

if pn == "19":
    os.system("git clone https://github.com/1N3/Sn1per.git")

if pn == "20":
    os.system("git clone https://github.com/Yukinoshita47/Yuki-Chan-The-Auto-Pentest.git")

if pn == "21":
    os.system("git clone https://github.com/laramies/theHarvester.git")

if pn == "22":
    os.system("git clone https://github.com/paterva/maltego-trx.git")

if pn == "23":
    os.system("git clone https://github.com/pymedusa/Medusa.git")

if pn == "24":
    os.system("git clone https://github.com/andresriancho/w3af.git")

if pn == "25":
    os.system("git clone https://github.com/xxgrunge/sqlninja.git")

if pn == "26":
    os.system("git clone https://github.com/beefproject/beef.git")

if pn == "27":
    os.system("git clone https://github.com/bettercap/bettercap.git")

if pn == "28":
    os.system("git clone https://github.com/vega/vega.git")

if pn == "29":
    os.system("git clone https://github.com/ajinabraham/CMSScan.git")

if pn == "30":
    os.system("git clone https://github.com/trustedsec/social-engineer-toolkit.git")


else:
    print(
        "sanırım bi yerde yanlışlık yaptınız lütfen tekrar deneyiniz ;)")
