# Light Fixture Prototype

This Raspberry Pi Pico prototype using Python was designed to simulate a light fixture in a greenhouse for farmers’ crops. As various geographical locations do not provide the optimal amount of light for crops to prosper, supplemental lighting is required. This lighting is often in a red to blue ratio, creating a pink colour unpleasant for greenhouse workers. The objective of this light fixture is to add white light for workers to use when they are present. 

![](https://github.com/JuliaLWang8/Light-Fixture-Prototype/blob/main/Circuit.jpg?raw=true)

The design utilizes 2 push buttons acting as a mode switch and a white light switch. The first button alternates between 3 modes each time it is pressed: off, plant-only, and plant-and-worker modes. When the mode is off, no LEDs light up. When the mode is plant-only, the red (pink) LEDs light up. Similarly, both red lights are active in the plant-and-worker mode. However, upon switching to this mode, pushing the second button acts as an on/off light switch for the green LED (white light). 

![](https://github.com/JuliaLWang8/Light-Fixture-Prototype/blob/main/circuit.png?raw=true)

## Case Design
The case was designed using Fusion360 for 3D CAD, see BreadboardDesign.pdf for more

 Case with lid | Case with breadboard
:-------------------------:|:-------------------------:
![](https://github.com/JuliaLWang8/Light-Fixture-Prototype/blob/main/CaseWithLid.png?raw=true) | ![](https://github.com/JuliaLWang8/Light-Fixture-Prototype/blob/main/CaseWithBreadboard.png?raw=true)
