# Start Minecraft Server
if you want to download server,you can use download function
```
n.download(n.pmc1192,n.tp,n.df)
```
##### pmc1192 = paper server (1.19.2)
##### pmc1182 = paper server (1.18.2)
##### pmc1171 = paper server (1.17.1)
##### pmc1165 = paper server (1.16.5)
##### pmc1152 = paper server (1.15.2)
##### pmc1144 = paper server (1.14.4)
##### pmc1132 = paper server (1.13.2)
##### pmc1122 = paper server (1.12.2)
##### vmc1193 = vanilla server (1.19.3)
##### vmc1182 = vanilla server (1.18.2)
##### vmc1171 = vanilla server (1.17.1)
##### vmc1165 = vanilla server (1.16.5)
##### vmc1152 = vanilla server (1.15.2)
##### vmc1144 = vanilla server (1.14.4)
##### vmc1132 = vanilla server (1.13.2)
##### vmc1122 = vanilla server (1.12.2)

## n.tp
n.tp is the path of the module file
## n.df
n.df is the name of the server(server.jar)
# start the server
```
n.start(n.df,1)#start minecraft server
```
##### n.dh is the name of the server(server.jar)
##### 1 is the memory used by the server (GB)
# elua
Accept the elua
```
n.elua()
```
# example
```
import n#import module
n.download(n.pmc1192,n.tp,n.df)#download papermc 1.19.2 minecraft server and download in this directory and file name is server.jar
n.start(n.df,1)#start minecraft server
n.elua()#accept elua
n.start(n.df,1)#restart minecraft server
```
# License
License is GPL-2.0
