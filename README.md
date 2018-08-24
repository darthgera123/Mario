#MARIO

###SSAD ASSIGNMENT

The game has been made in 3 sleepless nights and is the first version of it. This doesnt follow the conventional level generator approach but rather randomly generates enemy in positions and obstacles and is in endless mode. However completing certain missions gets you extra points. Each coin is worth 10 poinst while each each enemy kill is worth 30 points.Also jumping on each surface provides a **different height**.Also sound has been added.Survival Mode doesnt have a Boss.There is a smart enemy with a different head which turns around.
Extra Missions include -
+ Killed 5 enemies
+ 50 coins
+ Total Score over 500 
###List of characters

Symbol|Name|Use
---|---|---
'#'|Grass|Base
'?'|Spring|Extra Jump
'!'|Head of Enemy|Provides extra jump
'8'|Pipe|Nothing Special
'x'|Part of Bridge|Nothing Special
'$'|Coins|adds points

###Libraries used
Numpy
Colorama

###Controls
w - jump
a - left
d - right

###Code Review
In the following game, we have 4 classes. Screen is the base where all drawings are made. Board has all the obstacles. Player has all the attributes of player while Enemy class is for the following enemies.Jump is implemented as a function of iterations.There are 3 basic obstacles - Pipe,Bridge,Pit. Bridge has a spirng in the form of '?' which provides extra jump.The level ahead is generated randomly. Also clouds are made for the scenery. 
The sound.py file has the code for running the sound effects.