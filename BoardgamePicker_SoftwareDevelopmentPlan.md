# Boardgame Picker
CCC-2021 T1A3 - Terminal Application - Karl Alberto

# Software Development Plan

## Purpose and Scope

### Problem Overview

This application is designed to give users suggestions for tabletop games to play, and features options for users to choose between single-player, two-player, and more than two player (party) games.

The last 18 months (as of development, July 2021) has seen more and more people take an interest in indoor activities out of necessity. And as a form of leisure away from TV screens, computer monitors, phones and tablets; board games, card games and other tabletop games have seen a massive boost in popularity.

The influence of video games over the last few decades has also bled into tabletop game development and the sheer variety of game types and genres now available makes it hard to dive into the hobby sometimes.

Even those well versed in tabletop games are sometimes so spoilt for choice these days that analysis-paralysis sets in when trying to decide on a game to play.

This application aims to ease that issue. The current list of games available is curated from a personal selection of popular titles, but there is scope to expand on this list in the future.

### Target Audience

Users of this app are either individuals looking for a game to spend their leisure time on (the single player option); or the "host" of a game night introducing another player (or players) to a game that the other parties may be interested in playing. Ideally, the host will have experience with most of the titles offered (or tabletop game conventions in general) as this helps in smoother set up of the titles, and delivers a more accurate representation of the average game duration.

### Application Use

The app works by asking the user questions that will filter down and help come up with suggestions for possible games to play. As mentioned previously, games can cater for different numbers of player groups. This feature will be open for further expansion in the future (for specific numbers of players, rather than the current range offered).

Questions will be gated and multiple choice for ease of use, so the application has less possible sources for user error.


## Features

### **Core Features**

### Branching

Users will be able to choose between 3 different options for the number of people playing: single-player, two-player, or party games. This will lock out certain game and genre options in the subsequent questions, narrowing down the list of games to be displayed in the end.

### Multiple Choice

The options offered by the app will be multiple choice. As mentioned in sections prior, this will help guide users in making the correct syntactic options. Any incorrect inputs will trigger a loop until the user chooses an available option.

### Restart/Exit

At the end of the questions segment, users wil be given a list of games that will suit the requirements of the user. Afterwards, they will be given the option to exit the application, or to restart and go through the process again (for a different result).

### **Additional Features**

Some possible additional features to be implemented after core set runs (with no errors):

* "Back Button"/Redo Last - to allow users to go back to the previous question.
* Confirm Choice - prompt to ask users if choice is final (Y/N or True/False) to allow for `boolean` implementation.
* User added games - to give users the ability to add a tabletop game not currently included in the database; also allowing them to assign number of players, game duration, and genre.





