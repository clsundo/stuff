import random
import os

#fichier = "/home/vins_kds_23/doc/CODE/python/projects/distrolist.txt"
neos = ["AIX", "Alpine", "Anarchy", "Android", "Antergos", "antiX", "AOSC",
"Apricity", "ArcoLinux", "ArchBox", "ARCHlabs", "ArchStrike",
"XFerience", "ArchMerge", "Arch", "Artix", "Arya", "Bedrock", "Bitrig",
"BlackArch", "BLAG", "BlankOn", "BlueLight", "bonsai", "BSD",
"BunsenLabs", "Calculate", "Carbs", "CentOS", "Chakra", "ChaletOS",
"Chapeau", "Chrom", "Cleanjaro", "ClearOS", "Clear_Linux", "Clover",
"Condres", "Container_Linux", "CRUX", "Cucumber", "Debian", "Deepin",
"DesaOS", "Devuan", "DracOS", "DragonFly", "Drauger", "Elementary",
"EndeavourOS", "Endless", "EuroLinux", "Exherbo", "Fedora", "Feren", "FreeBSD",
"FreeMiNT", "Frugalware", "Funtoo", "GalliumOS", "Gentoo", "Pentoo",
"gNewSense", "GNU", "GoboLinux", "Grombyang", "Guix", "Haiku", "Huayra",
"Hyperbola", "janus", "Kali", "KaOS", "KDE_neon", "Kibojoe", "Kogaion",
"Korora", "KSLinux", "Kubuntu", "LEDE", "LFS", "Linux_Lite",
"LMDE", "Lubuntu", "Lunar", "macos", "Mageia", "MagpieOS", "Mandriva",
"Manjaro", "Maui", "Mer", "Minix", "LinuxMint", "MX_Linux", "Namib",
"Neptune", "NetBSD", "Netrunner", "Nitrux", "NixOS", "Nurunner",
"NuTyX", "OBRevenge", "OpenBSD", "OpenIndiana", "OpenMandriva",
"OpenWrt", "osmc", "Oracle", "PacBSD", "Parabola", "Pardus", "Parrot",
"Parsix", "TrueOS", "PCLinuxOS", "Peppermint", "popos", "Porteus",
"PostMarketOS", "Proxmox", "Puppy", "PureOS", "Qubes", "Radix", "Raspbian",
"Reborn_OS", "Redstar", "Redcore", "Redhat", "Refracted_Devuan", "Regata",
"Rosa", "sabotage", "Sabayon", "Sailfish", "SalentOS", "Scientific", "Septor",
"SharkLinux", "Siduction", "Slackware", "SliTaz", "SmartOS", "Solus",
"Source_Mage", "Sparky", "Star", "SteamOS", "SunOS", "openSUSE_Leap",
"openSUSE_Tumbleweed", "openSUSE", "SwagArch", "Tails", "Trisquel",
"Ubuntu-Budgie", "Ubuntu-GNOME", "Ubuntu-MATE", "Ubuntu-Studio", "Ubuntu",
"Void", "Obarun", "windows10", "Windows7", "Xubuntu", "Zorin", "IRIX"]


bashCommand = ""
x = random.choice(neos)
print(x)
bashCommand = f"neofetch --ascii_distro {x}"
os.system(bashCommand)
print(x)