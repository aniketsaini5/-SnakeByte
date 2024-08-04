[Setup]
AppName=Snake Byte
AppVersion=1.1.0
DefaultDirName={pf}\SnakeByte 
DefaultGroupName=Snake Game  
OutputBaseFilename=SnakeByte
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\Snake.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "bdj.jpg"; DestDir: "{app}"; Flags: ignoreversion
Source: "end.wav"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.ico"; DestDir: "{app}"; Flags: ignoreversion
Source: "start.wav"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Snake Game"; Filename: "{app}\Snake.exe"
Name: "{userdesktop}\Snake Game"; Filename: "{app}\Snake.exe"

[Run]
Filename: "{app}\Snake.exe"; Description: "Launch Snake Game"; Flags: nowait postinstall skipifsilent
