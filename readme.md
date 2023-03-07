Endless Universe Expedition 

![Ghost](https://github.com/yusufutkug/EUE/blob/main/image/Ghost.png)
### Table of Contents 
1. Game Description 

    a. Brief explanation

    b. How to play 
2. Class Diagram 

    a. Classes 
    
    b. Relation between classes 
3. Use Case Diagram
4. Collaboration Diagrams

### 1.Game Description

**a. Brief explanation:**  
At the beginning of the game, the player is asked to choose a hero among 2 different options. The aim of the game is to be able to make the best possible score by killing enemies and defending themselves from enemies's attack. 

**b.How to Play:**:
In the game, there are 2 types of heroes with different kinds of attack and defense mechanisms. Heroes and their features are given in the following table:
| Name of the Hero | Attack | Defense |
| --- | --- | --- | 
| Tank | Laser | Life |
| Ghost | Clone | Invisibility | 

Heroes can use these skills by pressing Q for defense skill and pressing E on the keyboard to get the attack skill.

These heroes are fighting against 3 different enemies with different attributes such as damage and health. Just like heroes, enemies can attack to the heroes with bullets. According to their types, damage they can give to the heroes and how hard it is to kill them changes.  

Heroes are confronted by enemies not as individuals but as armies. There exist different kinds of armies which include different types of enemies. If heroes succeed in killing all the enemies in the current army, the later and more powerful army comes into the game. 

To help heroes win this mutual attack which has been done by firing bullets at each other, they are given some additional opportunities to improve their skills. These are drops and items. In the game, there are 2 drops and 2 items which are listed below with their features. Drops are sliding through the screen and heroes can collect them and benefit from their features by catching them. Items can be bought by pressing 1,2 on the keyboard; however, to be able to do so the player must have a certain amount of coin in its wallet. And these coins can be earned by killing enemies.

|  | Type1 | Type2  |  
| --- | --- | ---  |
| Drop | Health | PowerUp |
| Item | Speed of Shooting | Shooting Power |

**a.Classes:**
In the figure given below, you can see the representations of classes and the relations between them.

![Class Diagram ](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/class%20_diag.png)

**b.Relation between classes:** 

***Objects- Sprite/Groups:***  In the game, there is an upper class called objects which sprite and groups inherit from.

***Sprite-army/enemy/drops/bullets/drop/hero/wallet/items/skills:***  all the given classes inherit from the sprite class. This means that classes like army, enemy, etc. are also types of sprite objects with additional method and attributes 

***Game-Groups:*** We constructed 8 group in the game hence there is an aggregation relationship between game and the groups classes with cardinality one to 8.

***Army- Enemy:***  Armies are composed of several different types of enemies. One army can have many enemies hence relationship among them is composition with cardinality one to many.

***Army-Game:*** As all enemies are being killed, different kinds of armies are created in the game. Since game has armies, the relationship among them is aggregation with cardinality one to many.

***Enemy- Enemy1/Enemy2/Boss:*** Later ones are the subclasses of the Enemy class so there is an inheritance relationship among them.

***Enemy-Bullet:*** Since in the game bullets are created in the enemy class, the relationship among them is aggregation with one to many since one enemy can create many numbers of bullets.

***Enemy-Drop:*** When enemy dies, randomly one drop is created; however, this doesn’t occur every time an enemy die it happens randomly. After one enemy die there can be only one drop that have been created hence relationship among them is association with cardinality one to one. 

***Bullet-Hero:*** Heroes are creating many bullets to attack enemies. Since in the game we play with one hero, and it can create many bullets relationship among them is aggregation with cardinality one to many

***Drop-Hero:*** Heroes can collect several drops and become more powerful hence there is an association relationship among them with cardinality one to many.

***Game-Drop:*** Game has many drops inside it hence there is an aggregation relationship among them with cardinality one to many.

***Drop-Health/PowerUp:*** the later ones are subclasses of the drop class hence there is an inheritance relationship among them.

***Hero-Enemy:***  Heroes and enemies are killing each other with bullets. One hero can kill many enemies and enemies can kill the hero of the game. So, relationship among them is association and cardinality of it is one to many. 

***Hero-Wallet:*** Heroes can use wallet to buy items hence there is an association relationship among them with cardinality one to one.

***Hero-Items:*** Heroes can buy items if they have enough coin in their wallets. So, there is an association relationship among them with cardinality one to many since heroes can buy many numbers of items.

***Hero- Skill:***  Both types of hero have an attack and a defense skill. So, relationship among them is association with cardinality one to two. 

***Game-Hero:*** Game has a hero, so relationship among them is aggregation with cardinality one to one.

***Hero-Ghost/Tank:*** Ghost and Tank are the subclasses of the hero hence there is an inheritance relationship among them. 

***Wallet-Items:*** items are being bought thanks to wallet and the coins in the wallet many items can be bought so, relationship among them is association with cardinality one to many.

***Wallet-Game:***  Game has a wallet so, relationship among them is aggregation with cardinality one to one. 

***Items- Speed of Shooting/Shooting power:*** Speed of Shooting and Shooting power are the subclasses of the item class hence relationship among them is inheritance.

***Game- items:*** Since game has two types of items, relationship among them is aggregation with cardinality one to two.

***Game- Skills:*** Since game has two types of skills which are attack and defense skills respectively, relationship among them is aggregation with cardinality one to two.

***Skills- attack skill/defense skill:*** Attack skill and defense skill are the subclasses of the skill class hence there is an inheritance relationship among them.





### 3. Use Case Diagram 

In the figure below one can see the use case diagram.

![Use Case ](https://github.com/BUIE201-Spring2022/project-part-2-group-4/blob/main/useCase.png.jpeg)

In the use case diagram, there exists one external agent which is the player of the game, and one internal agent which is the computer itself. This diagram shows how these agents can control the game.

Here are the controls the external agent (player) has on the game:

***Start:*** Clicking run in the game python file. 

***Pick hero:*** At the beginning, player chooses a hero buy clicking left and right buttons in the keyboard.

***Fire:*** Hero is firing bullets to enemies in the control of the player by left clicking on the mouse. 

***Pause:*** Player can pause the game by clicking escape button.

***Use skills:*** Player can choose to use one of its skills by using Q,E buttons from keyboard . 

***Buy item:*** Player uses 1,2 buttons from keyboard to buy item. 

***Move hero:*** Player can move by moving the mouse. 

***Quit:*** Player can quit the game by clicking the quit button at pause or play again sections.

***Resume***  After pausing the game player can continue playing by pressing the escape button again.

***Play again*** After life of the hero finishes, game ask user if it wants to play the game from the beginning. Player can chose this by clicking on the play again button.

***Play*** Player can start the game by clicking on the play button.


And here are the controls the internal agent (computer) has on the game:

***time.tick():*** Our external agent which is computer, keeps track of time to make sure that certain events happen at the necessary time interval.

### 4.Collaboration Diagrams:



***1.Use skill:*** 

In the game, to be able to use the skills heroes are using Q and E buttons from the keyboard. These keyboard events are being checked in the handle_events() function which is defined in the game class. If the player press those buttons we go to the skills class to use its key_check() function. In this function we check if skills are in cooldown, if not we call the trigger functions which is again in the skills class. (being in cooldown means necessary time to use the skill didn’t pass). These events happen for the both subclasses of the skill class hence polymorphism due to subclasses also shown in the collaboration diagram given below. 


![Use skill](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/use%20skill.jpeg)

***2.Buy item:*** 

In the game, to be able to get items, hero must use 1,2 buttons from the keyboard. These keyboard events are being checked in the handle_events() function which is defined in the game class. If the player presses those buttons we go to the item class to use the trigger function in it. Inside the trigger function another function called update_wallet is called to decrease the amount of coin hero has after buying an item. After that, since we can no longer use the same item after being bought we call the kill() function (we can use this function since item class inherits from the sprites class) to get rid of the current item and create a new item object afterwards which costs more. These events happen for the both subclasses of the item class hence polymorphism due to subclasses also shown in the collaboration diagram given below. 


![buy item](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/buy_item.jpeg)

***3.Pick hero:*** 

Below one can see the collaboration diagram of the pick hero use case. In the game; when entry_screen comes to the screen, player must decide between two heroes. To pick one of them player can use left and right buttons in the keyboard. After checking if those buttons are being used or not, if they are used we go to the hero class and use the kill() function to get rid of the hero which is in the current screen. After that, according to the button that have been pressed we go to the tank or ghost class to create the new hero object. 

![pick hero](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/pick_hero%20(1).png)

***4.Move hero:***

Below collaboration diagram of the move hero use case is given.Player can move the hero with mouse movement. When player uses the mouse move() function of the game is called which changes the rect center of the hero according to the get_pos() function of the pygame.  

![Move Hero](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/move%20hero.jpeg)

***5.Quit:***

Below collaboration of the quit is given. In the game, player can choose to quit the game at to places. First is when we are inside the pause() function in the game.  When player presses the pause 2 button are being shown in the screen one is for quiting and other is to resume. If coordinates of the mouse coincides with the quit button we exit the game with sys.exit. Second quitting option is when the game is inside the play_again() function. When hero looses, quitting and playing again options are coming to the screen. If the coordinates of the mouse coincides with the quit button again we exit the game with sys.exit.

![Quit collab](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/quit%20(1).png)

***6.Pause:***

Below collaboration of the pause use case is given. Player can pause the game by pressing the escape button. This is checked in the handle_events() functions which  is in the game class. If escape is pressed game calls the pause function which is in itself  

![Pause collab](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/Pause%20(1).png)

***7.Resume:*** 

Below collaboration of the resume use case is given. If game is inside the pause function and the player presses the escape button game continues.   

![resume](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/Resume%20(1).png)

***8.Start:***

Below collaboration of the start use case is given. As we start the game by running the code, game first goes to the entry_screen() function which is in itself. in this functions by using pygame module’s functions like render(), get_rect(), etc. necessary text like the game’s name, top score, etc. are coming to the screen. Also game updates the background with update_background() function and after that it goes to the hero class to use the hero’s draw_hero() function to blit the hero’s image to the entry screen.

![start](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/Start%20(2).png)

***9.Play again:***

Below collaboration of the play again use case is given. When player loses the game, two option comes into the screen which are whether to quit the game or play again If coordinates of the mouse coincide with the play again button, game starts from the beginning. To be able to start the game again, game calls the self.__init__() function to reset every changes end after that it calls the entry screen to start with hero selection. 

![play again](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/play_again.png)

***10.Play:*** 

Below collaboration of the play use case is given. When the game is in the entry_screen() function, if player presses enter key from the keyboard, game starts. As the game starts, game goes to the hero class to call the move() function to be able to get the mouse movement and move the hero according to it. After that it calls the run function which in itself calls the update_background() function. After updating the background game calls the run_logic() function to update all_sprites(). While updating the army, it first goes to the army class to call the creating_army() function which goes to the game by calling the HereIsX() function which returns an enemy objects and hence we can go to the enemy class to create a new enemy object. 

![play](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/play.jpeg)

***11.Fire:***

Below collaboration of the fire use case is given. In the game, player fire bullets by mouse clicking. If player click mouse fire() function of the hero class is called. Then HereIsX() function of the game is called to get the necessary objects as return. And finally with the help of these objects, hero goes to the bullet class and creates bullet objects. 

![fire](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/fire.png)

***12.Time.tick:***

When the game starts with run function, it starts recording the time with the pygame module’s function clock.tick(). With taking this time as a parameter game calls the run_logic() function inside the run. This function goes to all_sprite group and update everything in the game that are changing with time. Since by calling the same update function we get different outputs, update functions are shown as polymorphism in the collaboration diagram.

For example, it goes to the army’s update function and controls if at the given time enemies are alive or not, if not enemies are removed. Also if all enemies are dead, it choses the next army with select_army() function in the army and creates army according to it.  

Bullet’s update is also being made with given time. Since bullet class inherit from sprite class it uses its spritecollide() function to look if enemies or heroes are colliding with the bullets, if so it changes the health of the enemy with change_health() function which takes the bullet’s damage as a parameter. If bullet collide with one of enemies its own health change too with the change_health() function which is in the bullet class. At last, if in the given time health of the bullet is smaller then zero or its coordinates are out of the screen it kills itself by calling kill() function.

 At hero’s update function, it is first checked that if in the given time hero’s health is below 0 or not, if so hero kills itself by calling kill() function. Firing bullets is also subject to time since pressing mouse and passing the given time both necessary conditions for hero’s fire function. If this condition holds, hero goes to the game and call its HereIsX() function which returns bullet object and hence hero can go to the bullet class and create a new bullet. And lastly, hero’s attack and defense skills can be used only if a certain time passed after the usage of the previous skill. So they are being control in the time.tick also.

Finally, enemies are being updated according to the time. If in the given time enemies collide with a hero’s bullet, the score end coins are increasing. But to be able to change them since enemies do not have a direct communication with the game, first it goes to the army class and call HereIsX() function and get a game object and change score and coins by calling change_score() and update_wallet() functions which are in game and wallet class respectively. At the same manner, drops are created, hero’s and enemy’s health being changed as it is shown in the below collaboration diagram for the time.tick.


![time.tick](https://github.com/BUIE201-Spring2022/project-part-3-group-4/blob/main/time.tick.jpeg)
