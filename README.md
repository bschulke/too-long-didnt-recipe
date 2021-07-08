# too-long-didnt-recipe
For everyone who hates the long stories people add to their recipe articles.

By [@bschulke](https://github.com/bschulke) and [@aibhleog](https://github.com/aibhleog)

## Previously on our show, we:
* scrape units from ofThing and make new column
  * each line ofThing, separate by spaces and capture first word if matches list (put empty string if no line)
  * added the unit (or empty string) to new units column 
  * cut out unit word from ofThing column
  * (also checked for "." at end of units and removed it, too)

## Action items // to do:

* **NEXT TIME**: need to account for subsections in the STEPS part and/or the INGREDIENTS
  * see if there are special tags for these subheader titles?
* test on multiple BonAppetit recipes


### Stretch goals:
* saving file info -- first time run prompt user to specify location/path if not inside repo?
* user input?
* ADD A RECIPE SCALING OPTION (like "double this recipe" or "halve this recipe")


### SUPER Stretch goals:
* make this a basic HTML website, where you input the URL of the recipe and it will output the ingredients and steps on the website.
  * consider caching recipes that have been run?
  * give option to save recipe to file
* what if we made this into a mobile app that can be used as a plugin on a web browser?
* test on other non-BonAppetit recipe websites!

### Thoughts:
For this script version, we need to think about how it will work out of the box for any user.
