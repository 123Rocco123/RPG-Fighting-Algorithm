# RPG Video Game Algorithm
This repository contains the code of an Algorithm that I'm creating that will be able to be implamented in RPG video games, as well as table top games such as Dungeons and Dragons (DnD). 

The goal of this repository is to develop an algorithm to the point where it will be able to be used as a framework for video game developers to use for their games to quickly create an artificial intelligence for their games.

Currently, the repository contains code on how to creating your character, storing skill points for different categories, a damage system for the player and enemies. Although, much of this code is still subject to change.

## Goals to Complete:
1) Make sure that there aren't errors in the code.
2) Add more comments, to help with the understanding of the code.
3) Add new features to the algorithm.
4) Allowing the player to be able to use all of his / her skills before being killed by the horde.
   - Meaning, that rather than being based on a 2 strikes system it will be more like an RPG game. 
5) Make it so that if a player chooses to pick up a new weapon, then they have to give up the one that they have right now.
   - Make it so that lower level weapons have a skill roof, where they won't be able to be re-fined past a certain level. 

## Goals Completed:
1) Finalize the "structure" surrounding the algorithm.
   - This means "character creation" functions, dictionaries storing the information and skill points, and etc. This is so as to make the developemnt of the algorithm much faster and easier. 
2) Finalize the structure in the algorithm specifying the player's character's archetype, and how it's to affect other variables of the player.
3) Complete the Algorithm inside of the algorithm class determining what is to occur. 
   - This means finalizing the algorithm by utilizing all of the functions created. 
4) Code simplification
   - Meaning that the code shouldn't have much or any repetions. For any current repetitions of the code, they're to be inserted into functions so as to make it more modular and easier to deal with. 
   - This means making the two "intelligence" functions slot into one another. 
5) Leveling up System.
   - The leveling up system has been added to the algorithm as well.
6) Creating a difficulty system
   - Implamentation of the difficulty system has also been done.
7) Item drop function.
   - A function used to determine the rarity of the item thats dropped when a horde is defeated, and how that item scales with the level of the player.
   - The item also includes a "refining" method which improves the item.
