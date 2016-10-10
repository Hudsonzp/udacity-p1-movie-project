```                                        __                  
   _____              .__        
  /     \   _______  _|__| ____  
 /  \ /  \ /  _ \  \/ /  |/ __ \ 
/    Y    (  <_> )   /|  \  ___/ 
\____|__  /\____/ \_/ |__|\___  >
        \/                    \/ 
__________                   __               __   
\______   \_______  ____    |__| ____   _____/  |_ 
 |     ___/\_  __ \/  _ \   |  |/ __ \_/ ___\   __\
 |    |     |  | \(  <_> )  |  \  ___/\  \___|  |  
 |____|     |__|   \____/\__|  |\___  >\___  >__|  
                        \______|    \/     \/      

```

## Description

This application is fairly simple.  It takes a list of movies and then it calls a file provided from
Udacity to display the movies on a grid.  You can then click on a movie within the grid to pull
it's associated trailer.  

TLDR: It's a basic movie trailer website for my favorite movies.

## The Files

* media.py - creates the reusable movie class.
* entertainment_center.py - uses the movie class to set the movies used for the page and then calls the 
open movies page from the fresh_tomatoes.py file from Udacity.
* fresh_tomatoes.py - contains css, html, and some python code to structure the movie page and start it up.

## Running

To run the application, open up a terminal with all the files in the proper folder. Then start
the entertainment_center.py file to get it started.  The browser should open with the movie
website grid on the page. 

#### Specific Steps:

Terminal:
1. Open up your terminal (windows powershell)
2. Navigate to the appropriate folder making sure all project files are stored in the same place.
3. Type 'python entertainment_center.py'
4. A browser should start with the movies displayed!

Python IDLE:
1. Open the entertainment_center.py file (Making sure all project files in same place)
2. Once the file is opened, click Run > Run Module
3. A browser should start with the movies displayed!




## Testing:
Currently, there are no tests to run with this project other than checking for standard python errors or by making
sure the site runs.
