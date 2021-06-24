# too-long-didnt-recipe
For everyone who hates the long stories people add to their recipe articles.

By [@bschulke](https://github.com/bschulke) and [@aibhleog](https://github.com/aibhleog)

## Previously on our show, we:
* wrote the recipe output to a file (included URL)
* prettified the recipe output
* added print statements that showed script progress


## Action items // to do:

* **NEXT TIME**: need to account for subsections in the STEPS part and/or the INGREDIENTS
  * see if there are special tags for these subheader titles?
* check for operating system when first run, add key to flag if Unix or Windows - **homework for Bryn**
  * once OS is determined, switch driver
  * also change file extensions (the "/")
* scrape units from ofThing and make new column
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
