# Installation

tbd. 

# Preparation of a Simulation Run


## Initial Configuration of the target VM

tbd.

## Required files

tbd.


s. notion

## Templates 

As required by *pyautoqemu*, templates of the GUI elements that should be interacted with during VM control automation have to be provided. 

While we provide the templates we used for the prototype implementation, to run the prototype code, the templates in the shared/templates directory need to be replaced with screenshots of the respective GUI elements of the VM configured for an example run.

In particular, to run our prototype, we used the following templates:
- win_menu.png:  Windows Menu button
- win_menu_onoff.png: On/off button within the Windows Menu
- win_menu_shutdown.png: Shutdown button within the on/off menu
- firefox_desktop.png: Firefox icon, desktop shortcut
- firefox_go_back.png: Button within Firefox to navigate to the previously visited website
- firefox_google_new_search.png: Button within Google search bar in Firefox to conduct a new (consecutive) search
- firefox_close_active_tab.png: Button within Firefox to clase an active tab
- firefox_new_tab.png: Button within Firefox to open a new tab
- google_surf_failure.png: Failure indicator for a google search (e.g. Google searchbar that is still visible, when we should have navigated to a search result)

Note: During our experiments we observed, that (when using pyautoqemu) GUI interaction via mouse clicks is rather unrobust. Therefore, whenever possible, interaction via the keyboard should be preferred.

# How to run Re-imagen - an example

tbd. 

# Potential for Improvement

This code we provide is research code for a prototype and we acknowledge that there is potential for improvement. To give some examples:

- Integration with a VM control automation tool (e.g. [ForTrace++](https://gitlab.com/DW0lf/fortrace)) that is actively maintained and, e.g., provides more functionality to check whether actions were successful/lead to the expected result, to avoid hardcoded sleep times, or to handle unexpected results (e.g., popups). 
- Support of further activities and system types