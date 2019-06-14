<img src="https://raw.githubusercontent.com/mgp25/EvilUSB/master/assets/evil.png" width=300>
 
 # EvilUSB
 
 Quick utility to craft executables for pentesting and managing reverse shells.
 
 <img src="https://raw.githubusercontent.com/mgp25/EvilUSB/master/assets/screen1.png" width=500>
 <img src="https://raw.githubusercontent.com/mgp25/EvilUSB/master/assets/screen2.png" width=500>
 
 ### Instructions
 
 ```
 usage: usb.py [-h] [-b BAT] [-i ICON] [-o OUTPUT] [-t TARGET] [-l] [-p PORT]

EvilUSB: Quick utility to craft executables for pentesting and managing
reverse shells.

optional arguments:
  -h, --help            show this help message and exit
  -b BAT, --bat BAT     Path to bat file
  -i ICON, --icon ICON  Path to icon file (.ico)
  -o OUTPUT, --output OUTPUT
                        Path to exe output
  -t TARGET, --target TARGET
                        Set 32 or 64 for platform architecture (Default 32)
  -l, --listen          Listen for incoming connections
  -p PORT, --port PORT  Listening port (Default 4444)
  ```
  
### Constributions
  
Feel free to propose your modifications. It would be a great idea to have an option to send automatic payloads to Windows targets in order to escalate privileges or gain persistence.

### Note

The reverse manager shell was based on Wang Yihang's [project](https://github.com/WangYihang/Reverse-Shell-Manager).

Thanks to [jbelamor](https://github.com/jbelamor) for the ideas and tips. This project was based on one of his.
