import os
import urllib.request
pmc1192 = "https://api.papermc.io/v2/projects/paper/versions/1.19.2/builds/258/downloads/paper-1.19.2-258.jar"
pmc1182 = "https://api.papermc.io/v2/projects/paper/versions/1.18.2/builds/388/downloads/paper-1.18.2-388.jar"
pmc1171 = "https://api.papermc.io/v2/projects/paper/versions/1.17.1/builds/411/downloads/paper-1.17.1-411.jar"
pmc1165 = "https://api.papermc.io/v2/projects/paper/versions/1.16.5/builds/794/downloads/paper-1.16.5-794.jar"
pmc1152 =  "https://api.papermc.io/v2/projects/paper/versions/1.15.2/builds/393/downloads/paper-1.15.2-393.jar"
pmc1144 = "https://api.papermc.io/v2/projects/paper/versions/1.14.4/builds/245/downloads/paper-1.14.4-245.jar"
pmc1132 = "https://api.papermc.io/v2/projects/paper/versions/1.13.2/builds/657/downloads/paper-1.13.2-657.jar"
pmc1122 = "https://api.papermc.io/v2/projects/paper/versions/1.12.2/builds/1620/downloads/paper-1.12.2-1620.jar"
vmc1193 = "https://piston-data.mojang.com/v1/objects/c9df48efed58511cdd0213c56b9013a7b5c9ac1f/server.jar"
vmc1182 = "https://launcher.mojang.com/v1/objects/c8f83c5655308435b3dcf03c06d9fe8740a77469/server.jar"
vmc1171 = "https://launcher.mojang.com/v1/objects/a16d67e5807f57fc4e550299cf20226194497dc2/server.jar"
vmc1165 = "https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"
vmc1152 = "https://launcher.mojang.com/v1/objects/bb2b6b1aefcd70dfd1892149ac3a215f6c636b07/server.jar"
vmc1144 = "https://launcher.mojang.com/v1/objects/3dc3d84a581f14691199cf6831b71ed1296a9fdf/server.jar"
vmc1132 = "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
vmc1122 = "https://launcher.mojang.com/v1/objects/3737db93722a9e39eeada7c27e7aca28b144ffa7/server.jar"
tp = "./"
df = "server.jar"
def download(v,dir,filename):
    print("Downloading")
    try:
        urllib.request.urlretrieve(v,dir + filename)
    except:
        print("Failed to download")
    if os.path.isfile("./server.jar"):
        print("Done downloading!")
    else:
        print("Failed to download")
        exit()
def start(x,xmx):
    os.system(f"java -Xmx{xmx}G -jar {x}")
def elua():
    file = open("./elua.txt","w")
    et = file.write("elua = true")
    file.close()