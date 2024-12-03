# 1. **Install `virtualenv` or `venv` (if not already installed)**
- Open a terminal and run:
```bash
  pip install virtualenv
```

# Activete Virtual Envioment 

```bash
 flask_venv\Scripts\activate
  ```


### If error indicates that PowerShell's script execution policy is blocking the activation of your virtual environment. Here's how to fix it:

### Solution: Change PowerShell Execution Policy

1. **Open PowerShell as Administrator**:
   - Search for "PowerShell" in the Start menu.
   - Right-click on "Windows PowerShell" and select **Run as Administrator**.

2. **Check Current Execution Policy**:
   Run this command to see the current policy:
   ```powershell
   Get-ExecutionPolicy
   ```

3. **Set the Execution Policy to Allow Scripts**:
   To enable script execution, run:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned
   ```
   - Press `Y` to confirm.

   **Explanation**:
   - `RemoteSigned` allows locally created scripts to run but requires scripts from the internet to be signed.

4. **Reactivate the Virtual Environment**:
   Now, try activating the virtual environment again:
   ```powershell
   .\flask_venv\Scripts\Activate.ps1
   ```

---

### Important:
- After completing your work, you can reset the execution policy to its original state for security:
  ```powershell
  Set-ExecutionPolicy -ExecutionPolicy Restricted
  ```

### To deactivate your virtual environment, follow these simple steps:

### Command to Deactivate:
- Just type:
  ```bash
  deactivate
  ```

This works on all platforms (Windows, macOS, Linux) and exits the virtual environment, returning you to the global Python environment.

### After Deactivation:
- The terminal prompt will no longer show the virtual environment name, confirming you're back to your system's default Python environment.