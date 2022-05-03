# **Software operation CLI on Wedge 100BF-32**

Each software operation command starts with `tna` prefix. From RARE/freeRtr CLI:


``` linenums="0"
FREERTR#tna-?
  tna-bfshell              - Start bfshell
  tna-cleanup              - Permanently remove unused packages
  tna-install-experimental - Install the latest commit of freerouter on top of the latest RARE development version
  tna-install-git          - Install the version from a specific Git commit
  tna-install-latest       - Install the latest RARE development version
  tna-install-release      - Install the specified release
  tna-list-available       - List all available releases
  tna-list-installed       - List all currently installed releases
  tna-list-long-installed  - List all currently installed releases with non-abbreviated Git tags
  tna-list-profiles        - List the available p4 profiles
  tna-set-profile          - Set the p4 profile and restart the data-plane processes
  tna-switch-to-generation - Select the RARE profile generation to activate and restart freerouter
  tna-uninstall-generation - Delete the specified generation, use tna-cleanup to permanently remove packages
  tna-update-release       - Install the latest update of the specified release
```

