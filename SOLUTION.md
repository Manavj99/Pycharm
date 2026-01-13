# Fixing PowerShell Execution Policy Error

## Why the Error Occurs

Windows PowerShell has a security feature called **Execution Policy** that prevents unauthorized scripts from running. When you try to activate a Python virtual environment using `Activate.ps1`, PowerShell blocks it because:
- The default policy is `Restricted` (blocks all scripts)
- Your `CurrentUser` policy is `Undefined`, which defaults to `Restricted`
- This is a security measure to prevent malicious scripts from running

## Solutions (Choose One)

### Solution 1: Use Relative Path (Recommended)
Instead of:
```powershell
& c:/Users/Manav/Desktop/Class/.venv/Scripts/Activate.ps1
```

Use:
```powershell
.\.venv\Scripts\Activate.ps1
```

### Solution 2: Bypass for One Command
```powershell
powershell -ExecutionPolicy Bypass -File .\.venv\Scripts\Activate.ps1
```

### Solution 3: Use the Helper Script
Run:
```powershell
.\activate_venv.ps1
```

### Solution 4: Use Command Prompt Instead
Open Command Prompt (cmd) instead of PowerShell:
```cmd
.venv\Scripts\activate.bat
```

### Solution 5: Set Execution Policy (If Permitted)
If you have admin rights and no group policy is blocking it:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Note:** This may not work if your system administrator has set group policies.

### Solution 6: Use PowerShell Core (pwsh)
If you have PowerShell 7+ installed:
```powershell
pwsh
.\.venv\Scripts\Activate.ps1
```

## Quick Reference

**In PowerShell (if you get the error):**
```powershell
# Try this first
.\.venv\Scripts\Activate.ps1

# If that doesn't work, use:
powershell -ExecutionPolicy Bypass -File .\.venv\Scripts\Activate.ps1
```

**Or simply use Command Prompt:**
```cmd
.venv\Scripts\activate.bat
```
