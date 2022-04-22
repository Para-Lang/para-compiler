#define ExeName "Para"
#define ExeProjectSetupName "Para Project Setup Tool"
#define ExeVersion "0.1.dev7"
#define ExePublisher "Luna-Klatzer"
#define ExeURL "https://github.com/Para-Lang/Para/"
#define ExeExeCompilerName "para.exe"
#define ExeExeProjectSetupName "paraproj.exe"
#define ExeAssocExt1 ".para"
#define ExeAssocName1 ExeName + " Source File"
#define ExeAssocExt2 ".ph"
#define ExeAssocName2 ExeName + " Header File"
#define ExeAssocExt3 ".parah"
#define ExeAssocName3 ExeName + " Header File"
#define ExeAssocKey1 StringChange(ExeAssocName1, " ", "") + ExeAssocExt1
#define ExeAssocKey2 StringChange(ExeAssocName2, " ", "") + ExeAssocExt2
#define ExeAssocKey3 StringChange(ExeAssocName3, " ", "") + ExeAssocExt3

[Setup]
AppId={{5B1968C6-36C6-4E50-B6B8-B62051E67B0F}
AppName={#ExeName}
AppVersion={#ExeVersion}
AppVerName={#ExeName} Compiler v{#ExeVersion}
AppPublisher={#ExePublisher}
AppPublisherURL={#ExeURL}
AppSupportURL={#ExeURL}
AppUpdatesURL={#ExeURL}
DefaultDirName={autopf}\{#ExeName}
ChangesAssociations=yes
ChangesEnvironment=yes
DirExistsWarning=yes
DisableProgramGroupPage=yes
LicenseFile=LICENSE
PrivilegesRequired=admin
OutputBaseFilename=para
SetupIconFile=img/para.ico
Compression=lzma
UsePreviousAppDir=no
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; Flags: unchecked
Name: "addtopath"; Description: "Add Para compiler to the Windows Path"; Flags: unchecked

[Files]
Source: ".\dist\para\bin\{#ExeExeCompilerName}"; DestDir: "{app}\bin\"; Flags: ignoreversion
Source: ".\dist\para\bin\{#ExeExeProjectSetupName}"; DestDir: "{app}\bin\"; Flags: ignoreversion
Source: ".\dist\para\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Registry]
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt1}\OpenWithProgids"; ValueType: string; ValueName: "{#ExeAssocKey1}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#ExeAssocKey1}"; ValueType: string; ValueName: ""; ValueData: "{#ExeAssocName1}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt2}\OpenWithProgids"; ValueType: string; ValueName: "{#ExeAssocKey2}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#ExeAssocKey2}"; ValueType: string; ValueName: ""; ValueData: "{#ExeAssocName2}"; Flags: uninsdeletekey
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt3}\OpenWithProgids"; ValueType: string; ValueName: "{#ExeAssocKey3}"; ValueData: ""; Flags: uninsdeletevalue
Root: HKA; Subkey: "Software\Classes\{#ExeAssocKey3}"; ValueType: string; ValueName: ""; ValueData: "{#ExeAssocName3}"; Flags: uninsdeletekey

Root: HKA; Subkey: "Software\Classes\{#ExeAssocKey1}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\bin\{#ExeExeCompilerName},0"
Root: HKA; Subkey: "Software\Classes\{#ExeAssocKey1}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\bin\{#ExeExeCompilerName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt2}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\bin\{#ExeExeCompilerName},0"
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt2}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\bin\{#ExeExeCompilerName}"" ""%1"""
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt3}\DefaultIcon"; ValueType: string; ValueName: ""; ValueData: "{app}\bin\{#ExeExeCompilerName},0"
Root: HKA; Subkey: "Software\Classes\{#ExeAssocExt3}\shell\open\command"; ValueType: string; ValueName: ""; ValueData: """{app}\bin\{#ExeExeCompilerName}"" ""%1"""

Root: HKA; Subkey: "Software\Classes\Applications\{#ExeExeCompilerName}\SupportedTypes"; ValueType: string; ValueName: ".myp"; ValueData: ""
Root: HKLM; Subkey: "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"; \
    ValueType: expandsz; ValueName: "Path"; ValueData: "{olddata};{app}\bin"; \
    Check: NeedsAddPath('{app}\bin'); Tasks: addtopath

[Icons]
Name: "{autoprograms}\{#ExeName}"; Filename: "{app}\bin\{#ExeExeCompilerName}"
Name: "{autodesktop}\{#ExeName}"; Filename: "{app}\bin\{#ExeExeCompilerName}"; Tasks: desktopicon
Name: "{autoprograms}\{#ExeProjectSetupName}"; Filename: "{app}\bin\{#ExeExeProjectSetupName}"
Name: "{autodesktop}\{#ExeProjectSetupName}"; Filename: "{app}\bin\{#ExeExeProjectSetupName}"; Tasks: desktopicon

[Code]
function NeedsAddPath(Param: string): boolean;
var
  OrigPath: string;
begin
  if not RegQueryStringValue(HKEY_LOCAL_MACHINE,
    'SYSTEM\CurrentControlSet\Control\Session Manager\Environment',
    'Path', OrigPath)
  then begin
    Result := True;
    exit;
  end;
  { look for the path with leading and trailing semicolon }
  { Pos() returns 0 if not found }
  Result := Pos(';' + Param + ';', ';' + OrigPath + ';') = 0;
end;