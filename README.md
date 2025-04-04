# Re-imagen

This is the repository for the *Re-imagen* framework for generating coherent background activity in synthetic disk images, which was presented at [DFRWS APAC 2024](https://dfrws.org/conferences/dfrws-apac-2024/).

We provide intermediate and final results of the disk image generation process for two examples described in our [paper](https://www.sciencedirect.com/science/article/pii/S266628172400129X):

> Voigt, L. L., Freiling, F., & Hargreaves, C. J. (2024). Re-imagen: Generating coherent background activity in synthetic scenario-based forensic datasets using large language models. Forensic Science International: Digital Investigation, 50, 301805.

Also, this repository contains research code for the prototype implementation of core components of the Re-imagen framework, as introduced in our paper.

## Demonstration - Examples

In the [Demonstration-Examples](https://github.com/lenavoigt/re-imagen/tree/main/Demonstration-Examples) directory, we provide intermediate and final results of the disk image generation process for two examples we introduced to demonstrate our approach. Full disk images for both examples will be shared upon request.

### Example 1 - Maximilian

- 3-day simulation for the GPT-4o-generated persona "Maximilian", based on a GPT-4o-generated Activity Description Script
- GPT-4o-generated activity:
    - Time: 07:10 on May 31, 2024 to 18:10 on June 2, 2024
    - Activity types (details generated by GPT-4o):
        - Computer on/off (time),
        - Google searches (time, search term)
- System details:
    - OS: Windows 10 Home
    - Default Browser: Mozilla Firefox 
- Examples of relevant files for observing activity related to the GPT-4o output: Mozilla Firefox places.sqlite

### Example 2 - Catherine

- 1-day simulation for the GPT-4o-generated persona "Catherine", based on a GPT-4o-generated Activity Description Script
- GPT-4o-generated activity:
    - Time: 22:52 to 23:58 on June 1, 2024
    - Activity types (details generated by GPT-4o):
        - Computer on/off (time),
        - Google searches (time, search term) including browsing to one to three search results,
        - Text document creation (time, document name, document content)
- System details:
    - OS: Windows 10 Home
    - Default Browser: Mozilla Firefox 
- Examples of relevant files for observing activity related to the GPT-4o output: Mozilla Firefox places.sqlite, Users/Catherine/Documents/workshop_outline.txt, Users/Catherine/Documents/recipe_notes.txt


## Re-imagen - Research Code

In the [Prototype](https://github.com/lenavoigt/re-imagen/tree/main/Prototype) directory, we provide the prototype implementation of [Re-imagen](https://github.com/lenavoigt/re-imagen/tree/main/Prototype/re-imagen) created to demonstrate our approach as well as some enhancements to [pyautoqemu](https://wiwi-gitlab.uni-muenster.de/itsecurity/pyautoqemu), the VM control automation tool used in our demonstration.

---

We'd like to thank Katharina de Rentiis for implementing the OCR functionality for pyautoqemu!
